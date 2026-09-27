#!/usr/bin/env python3
"""Build KDP-ready files from a Markdown manuscript.

    scripts/build.py <slug> [--epub] [--print] [--cover] [--all]

Markdown is the single source. EPUB goes through pandoc; the print interior
goes through pandoc -> typst so page geometry, gutters and chapter openers are
under real typographic control. Illustrations are derived per target: grayscale
300 dpi for a KDP black-and-white interior, RGB and downsized for the EPUB.
"""

from __future__ import annotations

import argparse
import math
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SHARED = ROOT / "shared"
DIST = ROOT / "dist"
IMG_EXT = (".png", ".jpg", ".jpeg", ".tif", ".tiff", ".webp", ".svg")
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII"}
# ImageMagick has no default font on macOS, so placeholder art names one.
LABEL_FONT = SHARED / "fonts" / "LibertinusSerif-Regular.otf"


def run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if proc.returncode != 0:
        sys.exit(
            f"\n!! command failed: {' '.join(str(c) for c in cmd)}\n"
            f"{proc.stdout}\n{proc.stderr}"
        )
    return proc


def inches(value) -> float:
    """Parse '6in' / '152.4mm' / 6 into inches."""
    if isinstance(value, (int, float)):
        return float(value)
    s = str(value).strip()
    for unit, factor in (("in", 1.0), ("mm", 1 / 25.4), ("cm", 1 / 2.54), ("pt", 1 / 72)):
        if s.endswith(unit):
            return float(s[: -len(unit)]) * factor
    return float(s)


# --------------------------------------------------------------------------
# manuscript model
# --------------------------------------------------------------------------

@dataclass
class Piece:
    """One markdown file: a chapter, or a front/back matter section."""

    path: Path
    kind: str  # front | chapter | back
    title: str
    body: str
    illustration: Path | None = None
    meta: dict = field(default_factory=dict)

    @property
    def stem(self) -> str:
        return self.path.stem


FM_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def read_piece(path: Path, kind: str, masters: dict[str, Path]) -> Piece:
    text = path.read_text(encoding="utf-8")
    meta: dict = {}
    if m := FM_RE.match(text):
        meta = yaml.safe_load(m.group(1)) or {}
        text = text[m.end() :]

    title = meta.get("title")
    if not title:
        # Fall back to the first level-1 heading, and remove it from the body
        # so the template owns chapter-title typography.
        if h := re.search(r"^#\s+(.+?)\s*$", text, re.M):
            title = h.group(1)
            text = text[: h.start()] + text[h.end() :]
        else:
            title = path.stem.replace("-", " ").title()

    illo = None
    if kind == "part":
        key = meta.get("illustration", path.stem)
        if key is not False and key is not None:
            illo = masters.get(str(key))
            if illo is None:
                illo = Path("MISSING:" + str(key))

    return Piece(path, kind, str(title), text.strip() + "\n", illo, meta)


def load_book(slug: str):
    book_dir = ROOT / "books" / slug
    cfg = yaml.safe_load((book_dir / "book.yaml").read_text(encoding="utf-8"))

    masters_dir = book_dir / "illustrations" / "masters"
    masters = {
        p.stem: p
        for p in sorted(masters_dir.glob("*"))
        if p.suffix.lower() in IMG_EXT
    }

    pieces: list[Piece] = []
    for kind, folder in (("front", "front"), ("chapter", "chapters"), ("back", "back")):
        for md in sorted((book_dir / folder).glob("*.md")):
            pieces.append(read_piece(md, kind, masters))

    # Part openers, keyed by the same `part:` string the chapters carry. They
    # hold the book's hard data, so the chapters can stay in its own voice.
    parts: dict[str, Piece] = {}
    for md in sorted((book_dir / "parts").glob("*.md")):
        piece = read_piece(md, "part", masters)
        parts[str(piece.meta.get("part") or piece.title)] = piece
    return book_dir, cfg, pieces, parts


# --------------------------------------------------------------------------
# illustrations
# --------------------------------------------------------------------------

def placeholder(dest: Path, label: str, w: int, h: int, gray: bool) -> None:
    """Stand-in art so the book always builds while illustrations are pending."""
    dest.parent.mkdir(parents=True, exist_ok=True)
    run([
        "magick", "-size", f"{w}x{h}", "canvas:white",
        "-stroke", "#999999", "-strokewidth", "3", "-fill", "none",
        "-draw", f"rectangle 6,6 {w - 6},{h - 6}",
        "-draw", f"line 6,6 {w - 6},{h - 6}",
        "-draw", f"line {w - 6},6 6,{h - 6}",
        "-stroke", "none", "-fill", "#555555", "-gravity", "center",
        "-font", str(LABEL_FONT), "-pointsize", str(max(14, w // 18)),
        "-annotate", "+0+0", f"illustration\n{label}",
        # Flatten: transparency in a print interior is asking for trouble.
        "-background", "white", "-alpha", "remove", "-alpha", "off", "-strip",
        *(["-colorspace", "Gray"] if gray else []),
        str(dest),
    ])


def derive(master: Path | None, dest: Path, label: str, *, px: int, gray: bool,
           dpi: int | None) -> Path:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if master is None or str(master).startswith("MISSING:"):
        placeholder(dest, label, px, int(px * 1.25), gray)
        return dest
    if dest.exists() and dest.stat().st_mtime >= master.stat().st_mtime:
        return dest
    cmd = ["magick", str(master), "-strip"]
    if gray:
        cmd += ["-colorspace", "Gray", "-background", "white", "-alpha", "remove",
                "-alpha", "off"]
    else:
        cmd += ["-colorspace", "sRGB"]
    cmd += ["-resize", f"{px}x{px * 4}>"]
    if dpi:
        cmd += ["-units", "PixelsPerInch", "-density", str(dpi)]
    if dest.suffix.lower() in (".jpg", ".jpeg"):
        cmd += ["-quality", "88", "-background", "white", "-alpha", "remove"]
    cmd.append(str(dest))
    run(cmd)
    return dest


def text_width_in(cfg: dict, pages: int) -> float:
    p = cfg.get("print", {})
    trim_w = inches(p.get("trim", ["6in", "9in"])[0])
    gutter_min = kdp_gutter_min(pages)
    inside = gutter_min + inches(p.get("gutter_extra", "0.375in"))
    outside = inches(p.get("outer_margin", "0.625in"))
    return trim_w - inside - outside


def kdp_gutter_min(pages: int) -> float:
    if pages <= 150:
        return 0.375
    if pages <= 300:
        return 0.5
    if pages <= 500:
        return 0.625
    if pages <= 700:
        return 0.75
    return 0.875


IMG_MD_RE = re.compile(r"(!\[[^\]]*\]\()([^)\s]+)(\s*(?:\"[^\"]*\")?\))")
# The novel's set-apart registers. A `::: {.registro}` block is a machine
# record -- a log line, a transcript, a notice, a policy memorandum -- and it
# is typeset as a document that got slipped between the pages. The class name
# drives the typst function of the same name in shared/print/template.typ, so
# adding a second register is one entry here plus one function there.
REGISTERS = ("registro",)
REGISTER_OPEN = re.compile(
    r"^:::+\s*\{?\.(" + "|".join(REGISTERS) + r")\}?\s*$")
REF_RE = re.compile(r"\{\{cap:([a-z0-9-]+)\}\}")


def chapter_refs(pieces: list) -> dict[str, int]:
    """Map a chapter's slug to the number it will actually print with.

    Chapters are numbered by position, not by filename, so the printed numbers
    close up automatically when a chapter is removed. Prose therefore never
    hard-codes a number: it writes `{{cap:reversivel-ou-nao}}` and this map
    resolves it. Restructuring the book can no longer produce a wrong
    cross-reference, which it did three times before this existed.
    """
    refs, n = {}, 0
    for piece in pieces:
        if piece.kind != "chapter":
            continue
        n += 1
        refs[re.sub(r"^\d+-", "", piece.stem)] = n
    return refs


def resolve_refs(body: str, refs: dict[str, int], where: Path) -> str:
    def sub(m):
        slug = m.group(1)
        if slug not in refs:
            sys.exit(f"!! {where.name}: unknown chapter reference "
                     f"{{{{cap:{slug}}}}}\n   known: {', '.join(sorted(refs))}")
        return str(refs[slug])

    return REF_RE.sub(sub, body)
FENCE_CLOSE = re.compile(r"^:::+\s*$")


def register_blocks_to_typst(body: str) -> str:
    """Turn `::: {.registro}` divs into raw typst calls to `#registro[]`.

    The novel switches register when the machine speaks in its own voice, and
    that switch has to be visible on the page before a word of it is read.
    Pandoc's HTML writer keeps the div class, so the EPUB styles it from CSS;
    the typst writer drops the class, so print needs the block rewritten into a
    real function call.
    """
    out, depth, name = [], 0, ""
    for line in body.split("\n"):
        if depth == 0 and (m := REGISTER_OPEN.match(line)):
            name = m.group(1)
            out += ["```{=typst}", f"#{name}[", "```", ""]
            depth = 1
        elif depth == 1 and FENCE_CLOSE.match(line):
            out += ["", "```{=typst}", "]", "```"]
            depth = 0
        else:
            out.append(line)
    if depth:
        sys.exit(f"!! an unclosed ::: {{.{name}}} block")
    return "\n".join(out)


def rewrite_images(body: str, md_path: Path, resolver) -> str:
    """Point markdown image links at the derivative built for this target."""

    def sub(m):
        src = m.group(2)
        if src.startswith(("http://", "https://", "data:")):
            return m.group(0)
        new = resolver((md_path.parent / src).resolve())
        return f"{m.group(1)}{new}{m.group(3)}"

    return IMG_MD_RE.sub(sub, body)


# --------------------------------------------------------------------------
# EPUB
# --------------------------------------------------------------------------

def build_epub(book_dir: Path, cfg: dict, pieces: list[Piece],
               parts: dict[str, Piece]) -> Path:
    slug = cfg["slug"]
    work = DIST / slug / "epub"
    if work.exists():
        shutil.rmtree(work)
    (work / "img").mkdir(parents=True)

    ep = cfg.get("epub", {})
    fmt = "." + str(ep.get("illustration_format", "png")).lstrip(".")
    px = int(ep.get("illustration_max_px", 1400))

    def epub_derivative(master: Path | None, label: str) -> str:
        dest = work / "img" / (label + fmt)
        derive(master, dest, label, px=px, gray=False, dpi=None)
        return "img/" + dest.name

    # Cover
    cover_rel = None
    cover_master = book_dir / "illustrations" / "masters" / str(ep.get("cover", "cover.png"))
    cover_path = work / "img" / "cover.jpg"
    if cover_master.exists():
        run(["magick", str(cover_master), "-strip", "-colorspace", "sRGB",
             "-resize", "1600x2560^", "-gravity", "center", "-extent", "1600x2560",
             "-quality", "90", str(cover_path)])
    else:
        # No artwork: set the same typographic front panel the printed wrap
        # uses. This is the finished cover for a text-only edition, not a
        # stand-in, so it carries no placeholder mark.
        typeset_ebook_cover(cfg, work / "cover", cover_path)
    cover_rel = "img/cover.jpg"

    # Body markdown, one level-1 heading per piece so pandoc splits on chapters.
    refs = chapter_refs(pieces)
    chunks: list[str] = []
    seen_part = None
    for piece in pieces:
        body = resolve_refs(piece.body, refs, piece.path)
        body = rewrite_images(
            body, piece.path,
            lambda abs_src: epub_derivative(
                abs_src if abs_src.exists() else None, abs_src.stem),
        )
        head = ""
        if False:
            master = piece.illustration
            label = master.stem if not str(master).startswith("MISSING:") else \
                str(master).split(":", 1)[1]
            src = epub_derivative(
                None if str(master).startswith("MISSING:") else master, label)
            head = (f'<figure class="opener">'
                    f'<img src="{src}" alt="Illustration for {piece.title}"/>'
                    f'</figure>')
        # Part opener, once, before the first chapter of each part.
        pk = str(piece.meta.get("part") or "")
        if piece.kind == "chapter" and pk and pk != seen_part:
            seen_part = pk
            if op := parts.get(pk):
                fig = ""
                if op.illustration is not None:
                    miss = str(op.illustration).startswith("MISSING:")
                    lbl = (str(op.illustration).split(":", 1)[1] if miss
                           else op.illustration.stem)
                    src = epub_derivative(None if miss else op.illustration, lbl)
                    fig = (f'<figure class="opener"><img src="{src}" '
                           f'alt="Ilustração de abertura: {op.title}"/></figure>\n\n')
                chunks.append(f"# {op.title}\n\n{fig}{op.body}")

        # `{.unlisted}` keeps a piece (a dedication, say) out of the TOC.
        attr = "" if piece.meta.get("toc", True) else " {.unlisted}"
        # The opener figure has to come AFTER the heading: pandoc splits the
        # EPUB at level-1 headings, so anything before one lands in the
        # previous chapter's file.
        opener = f"{head}\n\n" if head else ""
        chunks.append(f"# {piece.title}{attr}\n\n{opener}{body}")

    md = work / "book.md"
    md.write_text("\n\n".join(chunks), encoding="utf-8")

    # EPUB metadata
    kdp = cfg.get("kdp", {})
    series = cfg.get("series") or {}
    meta = {
        "title": [{"type": "main", "text": cfg["title"]}]
        + ([{"type": "subtitle", "text": cfg["subtitle"]}] if cfg.get("subtitle") else []),
        "author": [cfg.get("author", "")],
        "lang": f"{cfg.get('language', 'en')}-{cfg.get('region', 'US')}",
        "date": str(cfg.get("copyright_year", "")),
        "rights": f"Copyright © {cfg.get('copyright_year','')} {cfg.get('author','')}. "
                  f"{cfg.get('rights','')}".strip(),
        "publisher": cfg.get("publisher") or cfg.get("author", ""),
        "description": (kdp.get("description") or "").strip(),
        "subject": kdp.get("keywords", []),
        # Both, or neither. `group-position` alone refines a collection that
        # was never written, and epubcheck rejects the package with RSC-005 --
        # which is a KDP rejection for a standalone book whose book.yaml still
        # carries a series number from the book it was scaffolded from.
        "belongs-to-collection": series.get("name") or None,
        "group-position": series.get("number") if series.get("name") else None,
        "cover-image": cover_rel,
        "css": "style.css",
        "toc-title": (cfg.get("labels") or {}).get("contents"),
    }
    if cfg.get("isbn"):
        meta["identifier"] = [{"scheme": "ISBN-13", "text": cfg["isbn"]}]
    meta = {k: v for k, v in meta.items() if v not in (None, "", [])}
    meta_path = work / "metadata.yaml"
    meta_path.write_text(yaml.safe_dump(meta, allow_unicode=True), encoding="utf-8")
    shutil.copy(SHARED / "epub" / "style.css", work / "style.css")

    out = DIST / slug / f"{slug}.epub"
    run([
        "pandoc",
        "--from=markdown+smart",
        "--to=epub3",
        f"--metadata-file={meta_path}",
        "--toc", "--toc-depth=2",
        "--split-level=1",
        "--epub-title-page=true",
        f"--resource-path={work}",
        "--output", str(out),
        str(md),
    ], cwd=work)
    return out


# --------------------------------------------------------------------------
# print interior
# --------------------------------------------------------------------------

def typ_str(value) -> str:
    if value is None:
        return "none"
    return '"' + str(value).replace("\\", "\\\\").replace('"', '\\"') + '"'


def typ_paragraphs(value) -> str:
    """A block of prose as a typst array of paragraphs, one string each.

    Blank lines separate paragraphs; every other newline is soft and becomes a
    space. `kdp.description` is a YAML literal block, so it keeps the line
    breaks of book.yaml, and a newline inside a typst string is a hard break.
    """
    blocks = [" ".join(block.split())
              for block in re.split(r"\n\s*\n", str(value or "").strip())]
    blocks = [block for block in blocks if block]
    return "(" + "".join(typ_str(block) + ", " for block in blocks) + ")"


HEADING_RE = re.compile(r"^(=+) ", re.M)


def pandoc_typst(body: str) -> str:
    """Markdown to a typst fragment, with heading levels pushed down one.

    Level 1 belongs to the parts, so a chapter is level 2 and the `##` heads
    inside a chapter body must land on level 3. Pandoc emits `==` for those,
    so every heading in a fragment gains one `=`.
    """
    proc = run(["pandoc", "--from=markdown+smart", "--to=typst", "--wrap=none"],
               input=body)
    return HEADING_RE.sub(lambda m: "=" + m.group(1) + " ", proc.stdout)


def build_print(book_dir: Path, cfg: dict, pieces: list[Piece],
                parts: dict[str, Piece], passes: int = 2) -> Path:
    slug = cfg["slug"]
    work = DIST / slug / "print"
    if work.exists():
        shutil.rmtree(work)
    (work / "img").mkdir(parents=True)

    p = cfg.get("print", {})
    gray = str(p.get("interior", "bw")).lower() == "bw"
    pages = 120  # first-pass estimate; refined below

    def print_derivative(master: Path | None, label: str, width_frac: float) -> str:
        px = int(math.ceil(width_frac * text_width_in(cfg, pages) * 300))
        dest = work / "img" / (label + ".png")
        derive(master, dest, label, px=px, gray=gray, dpi=300)
        return "img/" + dest.name

    illo_frac = float(p.get("illustration_width", 0.74))
    # The part opener sets its art to the same measure as the part's body text,
    # so it has to be rasterized at that width and not at the chapter's.
    part_inset = p.get("part_body_inset", "0.3in")
    part_illo_frac = (
        text_width_in(cfg, pages) - 2 * inches(part_inset)
    ) / text_width_in(cfg, pages)

    # Convert each piece once; typst fragments get included from main.typ.
    refs = chapter_refs(pieces)
    frags: list[tuple[Piece, str, str | None]] = []
    for i, piece in enumerate(pieces):
        body = rewrite_images(
            resolve_refs(piece.body, refs, piece.path), piece.path,
            lambda abs_src: print_derivative(
                abs_src if abs_src.exists() else None, abs_src.stem, 0.9),
        )
        name = f"{i:02d}-{piece.stem}.typ"
        # `include` evaluates a file in its own scope, so a fragment does not
        # inherit main.typ's imports. Every fragment imports the template
        # itself, or any template function it uses -- `registro` from a
        # register switch, `divider` from a markdown `---` -- is an unknown
        # variable at compile time.
        (work / name).write_text(
            '#import "template.typ": *\n\n'
            + pandoc_typst(register_blocks_to_typst(body)),
            encoding="utf-8")
        frags.append((piece, name, None))

    trim = p.get("trim", ["6in", "9in"])
    series = cfg.get("series") or {}
    labels = {"chapter": "Chapter", "contents": "Contents", "book": "Book",
              **(cfg.get("labels") or {})}
    series_line = (f"{series['name']} · {labels['book']} {series['number']}"
                   if series.get("name") else None)

    def piece_call(piece: Piece, name: str, illo: str | None, number: int | None) -> list[str]:
        if piece.kind == "chapter":
            args = [f"number: {number}", f"label: {typ_str(labels['chapter'])}"]
            if illo:
                args.append(f"illustration: {typ_str(illo)}")
            head = f"  #chapter({typ_str(piece.title)}, {', '.join(args)})["
        else:
            outlined = "true" if piece.meta.get("toc", True) else "false"
            head = f"  #section({typ_str(piece.title)}, outlined: {outlined})["
        return [head, f'    #include "{name}"', "  ]"]

    def main_typ(page_estimate: int) -> str:
        slots: dict[str, list[str]] = {"front": [], "main": [], "back": []}
        number = 0
        seen_part, part_i = None, 0
        for piece, name, illo in frags:
            slot = {"front": "front", "chapter": "main", "back": "back"}[piece.kind]
            pk = str(piece.meta.get("part") or "")
            if piece.kind == "chapter" and pk and pk != seen_part:
                seen_part = pk
                part_i += 1
                if pk in parts:
                    op = parts[pk]
                    art = None
                    if op.illustration is not None:
                        missing = str(op.illustration).startswith("MISSING:")
                        label = (str(op.illustration).split(":", 1)[1] if missing
                                 else op.illustration.stem)
                        art = print_derivative(
                            None if missing else op.illustration, label,
                            part_illo_frac)
                    slots["main"] += [
                        f"  #part-opener({typ_str(ROMAN.get(part_i, part_i))}, "
                        f"{typ_str(op.title)}, illustration: {typ_str(art)}, "
                        f"body-inset: {part_inset})[",
                        f'    #include "part-{part_i:02d}.typ"',
                        "  ]",
                    ]
            if piece.kind == "chapter":
                number += 1
            slots[slot] += piece_call(piece, name, illo, number)

        lines = [
            '#import "template.typ": *',
            "",
            "#book(",
            f"  title: {typ_str(cfg['title'])},",
            f"  subtitle: {typ_str(cfg.get('subtitle'))},",
            f"  author: {typ_str(cfg.get('author'))},",
            f"  publisher: {typ_str(cfg.get('publisher') or None)},",
            f"  copyright-year: {typ_str(cfg.get('copyright_year'))},",
            f"  rights: {typ_str(cfg.get('rights'))},",
            f"  isbn: {typ_str(cfg.get('isbn') or None)},",
            f"  edition: {typ_str(cfg.get('edition'))},",
            f"  series: {typ_str(series_line)},",
            f"  trim: ({trim[0]}, {trim[1]}),",
            f"  pages-estimate: {page_estimate},",
            f"  bleed: {str(bool(p.get('bleed', False))).lower()},",
            f"  outer-margin: {p.get('outer_margin', '0.625in')},",
            f"  top-margin: {p.get('top_margin', '0.7in')},",
            f"  bottom-margin: {p.get('bottom_margin', '0.75in')},",
            f"  gutter-extra: {p.get('gutter_extra', '0.375in')},",
            f"  font-size: {p.get('font_size', '11pt')},",
            f"  leading: {p.get('leading', '0.78em')},",
            f"  lang: {typ_str(cfg.get('language', 'en'))},",
            f"  region: {typ_str(cfg.get('region', 'US'))},",
            f"  contents-title: {typ_str(labels['contents'])},",
            f"  colophon: {typ_str(cfg.get('colophon') or 'Set in Libertinus Serif.')},",
        ]
        for slot in ("front", "main", "back"):
            if not slots[slot]:
                continue
            lines.append(f"  {slot}: [")
            lines += ["  " + ln for ln in slots[slot]]
            lines.append("  ],")
        lines += [")", ""]
        return "\n".join(lines) + "\n"

    # Part opener bodies as their own typst fragments, numbered by position.
    seen, i = None, 0
    for piece in pieces:
        pk = str(piece.meta.get("part") or "")
        if piece.kind != "chapter" or not pk or pk == seen:
            continue
        seen, i = pk, i + 1
        op = parts.get(pk)
        (work / f"part-{i:02d}.typ").write_text(
            '#import "template.typ": *\n\n'
            + (pandoc_typst(register_blocks_to_typst(
                resolve_refs(op.body, refs, op.path))) if op else ""),
            encoding="utf-8",
        )

    shutil.copy(SHARED / "print" / "template.typ", work / "template.typ")
    out = DIST / slug / f"{slug}-interior.pdf"

    for attempt in range(passes):
        (work / "main.typ").write_text(main_typ(pages), encoding="utf-8")
        run(["typst", "compile", "--root", str(ROOT),
             "--font-path", str(SHARED / "fonts"),
             str(work / "main.typ"), str(out)])
        actual = int(run(["qpdf", "--show-npages", str(out)]).stdout.strip())
        if kdp_gutter_min(actual) == kdp_gutter_min(pages):
            pages = actual
            break
        pages = actual  # gutter band changed: recompile with the right gutter

    # KDP interiors must have an even page count; pad with a real blank page.
    if pages % 2 == 1:
        blank_src = work / "blank.typ"
        blank_src.write_text(
            f"#set page(width: {trim[0]}, height: {trim[1]}, margin: 0pt)\n#box()\n",
            encoding="utf-8",
        )
        blank_pdf = work / "blank.pdf"
        run(["typst", "compile", "--root", str(ROOT), str(blank_src), str(blank_pdf)])
        padded = work / "padded.pdf"
        run(["qpdf", "--empty", "--pages", str(out), "1-z", str(blank_pdf), "1",
             "--", str(padded)])
        shutil.move(str(padded), str(out))
        pages += 1
    print(f"   interior: {pages} pages, "
          f"gutter {kdp_gutter_min(pages) + inches(p.get('gutter_extra', '0.375in')):.3f}in")
    (DIST / slug / "pagecount.txt").write_text(str(pages))
    return out


# --------------------------------------------------------------------------
# print cover
# --------------------------------------------------------------------------

def typeset_ebook_cover(cfg: dict, work: Path, dest: Path) -> None:
    """The eBook cover, typeset from the same template as the printed wrap.

    KDP wants 1600x2560. The typst page is 5.5 x 8.8in, which is that ratio
    exactly, so the rasterised page needs no cropping -- only a snap to the
    exact pixel box to absorb the rounding in the ppi.
    """
    work.mkdir(parents=True, exist_ok=True)
    shutil.copy(SHARED / "print" / "cover.typ", work / "cover.typ")
    series = cfg.get("series") or {}
    src = "\n".join([
        '#import "cover.typ": ebook-cover',
        "#show: ebook-cover.with(",
        f"  title: {typ_str(cfg['title'])},",
        f"  subtitle: {typ_str(cfg.get('subtitle'))},",
        f"  author: {typ_str(cfg.get('author'))},",
        f"  series: {typ_str(series.get('name') or None)},",
        ")",
        "",
    ]) + "\n"
    (work / "ebook.typ").write_text(src, encoding="utf-8")
    png = work / "ebook.png"
    run(["typst", "compile", "--root", str(ROOT), "--font-path", str(SHARED / "fonts"),
         "--format", "png", "--ppi", "290.909091",
         str(work / "ebook.typ"), str(png)])
    run(["magick", str(png), "-strip", "-colorspace", "sRGB",
         "-resize", "1600x2560!", "-quality", "90", str(dest)])


def build_cover(book_dir: Path, cfg: dict) -> Path:
    slug = cfg["slug"]
    pc_file = DIST / slug / "pagecount.txt"
    if not pc_file.exists():
        sys.exit("!! build the interior first -- the spine width depends on page count")
    pages = int(pc_file.read_text().strip())

    p = cfg.get("print", {})
    trim = p.get("trim", ["6in", "9in"])
    per_page = 0.0025 if str(p.get("paper", "cream")).lower() == "cream" else 0.002252
    spine = pages * per_page

    work = DIST / slug / "cover"
    work.mkdir(parents=True, exist_ok=True)
    shutil.copy(SHARED / "print" / "cover.typ", work / "cover.typ")
    series = cfg.get("series") or {}
    src = "\n".join([
        '#import "cover.typ": kdp-cover',
        "#show: kdp-cover.with(",
        f"  title: {typ_str(cfg['title'])},",
        f"  subtitle: {typ_str(cfg.get('subtitle'))},",
        f"  author: {typ_str(cfg.get('author'))},",
        f"  blurb: {typ_paragraphs(cfg.get('kdp', {}).get('description'))},",
        f"  series: {typ_str(series.get('name'))},",
        f"  trim: ({trim[0]}, {trim[1]}),",
        f"  spine: {spine:.4f}in,",
        f"  pages: {pages},",
        f"  guides: {str(bool(cfg.get('cover_guides', True))).lower()},",
        ")",
        "",
    ]) + "\n"
    (work / "main.typ").write_text(src, encoding="utf-8")
    out = DIST / slug / f"{slug}-cover.pdf"
    run(["typst", "compile", "--root", str(ROOT), "--font-path", str(SHARED / "fonts"),
         str(work / "main.typ"), str(out)])
    print(f"   cover: spine {spine:.4f}in for {pages} pages "
          f"({p.get('paper', 'cream')} paper)")
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("slug")
    ap.add_argument("--epub", action="store_true")
    ap.add_argument("--print", dest="print_", action="store_true")
    ap.add_argument("--cover", action="store_true")
    ap.add_argument("--all", action="store_true")
    args = ap.parse_args()
    if not (args.epub or args.print_ or args.cover):
        args.all = True

    book_dir, cfg, pieces, parts = load_book(args.slug)
    chapters = [x for x in pieces if x.kind == "chapter"]
    words = sum(len(x.body.split()) for x in pieces)
    print(f"-> {cfg['title']}: {len(chapters)} chapters, ~{words:,} words")
    (DIST / cfg["slug"]).mkdir(parents=True, exist_ok=True)

    if args.epub or args.all:
        print(f"   epub:  {build_epub(book_dir, cfg, pieces, parts).relative_to(ROOT)}")
    if args.print_ or args.all:
        print(f"   pdf:   {build_print(book_dir, cfg, pieces, parts).relative_to(ROOT)}")
    if args.cover or args.all:
        print(f"   cover: {build_cover(book_dir, cfg).relative_to(ROOT)}")


if __name__ == "__main__":
    main()
