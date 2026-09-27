#!/usr/bin/env python3
"""Turn docs/<slug>/outline.md into chapter files.

    scripts/scaffold-outline.py <book-slug> [--outline docs/<book-slug>/outline.md]

The outline is the single source for chapter titles and numbering. This script
creates any missing chapter file and refreshes the planning notes in the front
matter of the ones that exist -- it never touches a body you have written.

The planning fields are the novel's, not an essay's: who is telling it, when
and where it happens, what turns, which threads it moves, what it plants and
what it pays off. `scripts/check-threads.py` reads the last two and is the
reason they are structured lists rather than prose.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)

# Outline heading -> front-matter field. Both languages, so the English
# edition can be outlined in its own words without a second scaffolder.
FIELDS = {
    "POV": "pov",
    "Quando": "when",
    "Onde": "where",
    "A ideia": "premise",
    "A virada": "turn",
    "Fios": "threads",
    "Planta": "seeds",
    "Paga": "pays",
    "Elenco": "cast",
    "Fontes": "sources",
    "When": "when",
    "Where": "where",
    "The idea": "premise",
    "The turn": "turn",
    "Threads": "threads",
    "Plants": "seeds",
    "Pays off": "pays",
    "Cast": "cast",
    "Sources": "sources",
}
# Fields the tooling reads as lists of slugs rather than as prose.
LIST_FIELDS = {"threads", "seeds", "pays", "cast"}


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def as_list(value: str) -> list[str]:
    """`porta-do-porao, o-nome-de-vera` -> two slugs.

    Written comma-separated in the outline because that is how a person writes
    it; stored as a YAML list because that is how check-threads.py reads it.
    """
    return [slugify(part) for part in value.split(",") if part.strip()]


def parse(outline: Path) -> list[dict]:
    part = None
    chapters: list[dict] = []
    for line in outline.read_text(encoding="utf-8").splitlines():
        if m := re.match(r"^##\s+(PARTE|PART)\s+(.+)$", line):
            part = m.group(2).strip()
        elif m := re.match(r"^###\s+(\d+)\.\s+(.+)$", line):
            chapters.append({"number": int(m.group(1)), "title": m.group(2).strip(),
                             "part": part})
        elif chapters and (m := re.match(r"^\*\((.+?)\)\*", line)):
            chapters[-1]["title_en"] = m.group(1).strip()
        elif chapters and (m := re.match(r"^-\s+\*\*(.+?)\*\*\s+[—-]\s+(.+)$", line)):
            if key := FIELDS.get(m.group(1).strip()):
                value = m.group(2).strip()
                chapters[-1][key] = as_list(value) if key in LIST_FIELDS else value
    return chapters


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--outline", help="default: docs/<slug>/outline.md, "
                    "or docs/outline.md in a single-book repo")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    if args.outline is None:
        per_book = f"docs/{args.slug}/outline.md"
        args.outline = per_book if (ROOT / per_book).exists() else "docs/outline.md"

    chapters = parse(ROOT / args.outline)
    if not chapters:
        raise SystemExit(f"!! no chapters found in {args.outline}")
    target = ROOT / "books" / args.slug / "chapters"
    target.mkdir(parents=True, exist_ok=True)

    created = updated = 0
    for ch in chapters:
        stem = f"{ch['number']:02d}-{slugify(ch['title'])[:44].strip('-')}"
        path = target / f"{stem}.md"
        # Planning notes live in the front matter, which the build strips, so
        # nothing here can leak into the book.
        meta = {
            "title": ch["title"],
            "part": ch.get("part"),
            "title_en": ch.get("title_en"),
            "pov": ch.get("pov"),
            "when": ch.get("when"),
            "where": ch.get("where"),
            "premise": ch.get("premise"),
            "turn": ch.get("turn"),
            "threads": ch.get("threads"),
            "seeds": ch.get("seeds"),
            "pays": ch.get("pays"),
            "cast": ch.get("cast"),
            "sources": ch.get("sources"),
            "status": "outline",
        }
        meta = {k: v for k, v in meta.items() if v is not None}

        body = ""
        if path.exists():
            text = path.read_text(encoding="utf-8")
            if m := FM.match(text):
                body = text[m.end():]
                try:
                    old = yaml.safe_load(m.group(1)) or {}
                except yaml.YAMLError as exc:
                    raise SystemExit(f"!! {path.name}: front matter is not valid "
                                     f"YAML\n   {exc}") from None
                # Never clobber a status you have advanced by hand.
                if old.get("status") not in (None, "outline"):
                    meta["status"] = old["status"]
                # Seeds and payoffs are commonly discovered while drafting, not
                # while outlining. Anything the file knows and the outline does
                # not is kept, merged, and left in the file's order.
                for key in LIST_FIELDS:
                    merged = list(dict.fromkeys(
                        list(meta.get(key) or []) + list(old.get(key) or [])))
                    if merged:
                        meta[key] = merged
            else:
                body = text
            updated += 1
        else:
            created += 1

        front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True,
                               default_flow_style=False, width=78)
        if not args.dry_run:
            path.write_text(f"---\n{front}---\n{body or ''}", encoding="utf-8")

    stale = sorted(p.name for p in target.glob("*.md")
                   if not any(p.name.startswith(f"{c['number']:02d}-") for c in chapters))
    print(f"-> {created} created, {updated} refreshed in books/{args.slug}/chapters")
    if stale:
        print(f"   not in the outline (left alone): {', '.join(stale)}")


if __name__ == "__main__":
    main()
