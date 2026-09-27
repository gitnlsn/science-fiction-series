#!/usr/bin/env python3
"""Preflight the built files against what KDP actually rejects.

    scripts/check.py <slug>

Checks the EPUB with epubcheck, then the interior PDF for page size, even
page count, embedded fonts, image resolution and colour space. Exits non-zero
if anything would fail or look wrong in print, so it can gate a release.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
PASS, WARN, FAIL = "ok  ", "warn", "FAIL"
results: list[tuple[str, str]] = []


def record(level: str, msg: str) -> None:
    results.append((level, msg))
    print(f"  [{level}] {msg}")


def sh(cmd: list[str]) -> str:
    p = subprocess.run(cmd, capture_output=True, text=True)
    return p.stdout + p.stderr


def inches(value) -> float:
    s = str(value).strip()
    for unit, f in (("in", 1.0), ("mm", 1 / 25.4), ("cm", 1 / 2.54), ("pt", 1 / 72)):
        if s.endswith(unit):
            return float(s[: -len(unit)]) * f
    return float(s)


def check_epub(path: Path) -> None:
    print(f"\nEPUB  {path.name}")
    if not path.exists():
        record(FAIL, "not built")
        return
    out = sh(["epubcheck", str(path)])
    if "No errors or warnings detected" in out:
        record(PASS, "epubcheck clean")
    else:
        for line in out.splitlines():
            if line.startswith(("ERROR", "FATAL")):
                record(FAIL, line.strip()[:110])
            elif line.startswith("WARNING"):
                record(WARN, line.strip()[:110])
    mb = path.stat().st_size / 1e6
    # KDP charges a delivery fee per MB against the 70% royalty option.
    level = PASS if mb < 10 else WARN
    record(level, f"file size {mb:.1f} MB (delivery fee applies per MB at 70% royalty)")


def check_interior(path: Path, cfg: dict) -> None:
    print(f"\nPDF   {path.name}")
    if not path.exists():
        record(FAIL, "not built")
        return

    info = sh(["pdfinfo", str(path)])
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    size = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    w_in, h_in = float(size.group(1)) / 72, float(size.group(2)) / 72

    p = cfg.get("print", {})
    trim = p.get("trim", ["6in", "9in"])
    want_w, want_h = inches(trim[0]), inches(trim[1])
    if p.get("bleed"):
        want_w, want_h = want_w + 0.125, want_h + 0.25
    tol = 0.01
    if abs(w_in - want_w) < tol and abs(h_in - want_h) < tol:
        record(PASS, f"page size {w_in:.3f} x {h_in:.3f} in matches trim")
    else:
        record(FAIL, f"page size {w_in:.3f} x {h_in:.3f} in, expected "
                     f"{want_w:.3f} x {want_h:.3f} in")

    if pages % 2 == 0:
        record(PASS, f"{pages} pages (even, as KDP requires)")
    else:
        record(FAIL, f"{pages} pages -- KDP requires an even page count")
    if pages < 24:
        record(FAIL, f"{pages} pages -- KDP paperback minimum is 24")
    elif pages > 828:
        record(FAIL, f"{pages} pages -- exceeds the 828-page maximum")

    fonts = sh(["pdffonts", str(path)])
    rows = [r for r in fonts.splitlines()[2:] if r.strip()]
    not_embedded = [r.split()[0] for r in rows if len(r.split()) > 3
                    and r.split()[3].strip() == "no"]
    if not rows:
        record(WARN, "no fonts found in the PDF")
    elif not_embedded:
        record(FAIL, f"fonts not embedded: {', '.join(not_embedded)}")
    else:
        record(PASS, f"all {len(rows)} fonts embedded")

    out = sh(["pdfimages", "-list", str(path)])
    lows, colours, masks = [], [], []
    bw = str(p.get("interior", "bw")).lower() == "bw"
    for line in out.splitlines()[2:]:
        f = line.split()
        if len(f) < 15:
            continue
        try:
            page_no, kind, comp = f[0], f[2], int(f[6])
            x_ppi, y_ppi = int(f[12]), int(f[13])
        except (ValueError, IndexError):
            continue
        if kind == "smask":
            masks.append(f"p{page_no}")
            continue
        if min(x_ppi, y_ppi) < 300:
            lows.append(f"p{page_no}@{min(x_ppi, y_ppi)}dpi")
        # Component count, not the colour-space name: a grayscale PNG with an
        # ICC profile is listed as "icc" but still has one component.
        if bw and comp > 1:
            colours.append(f"p{page_no}:{f[5]}/{comp}comp")
    if lows:
        record(WARN, f"images under 300 dpi: {', '.join(lows[:8])}")
    else:
        record(PASS, "all images at 300 dpi or better")
    if colours:
        record(FAIL, f"colour images in a black-and-white interior: "
                     f"{', '.join(colours[:8])}")
    elif bw:
        record(PASS, "all images grayscale (black-and-white interior)")
    if masks:
        record(WARN, f"images carry transparency on {', '.join(sorted(set(masks))[:8])}"
                     " -- flatten against white for print")


def check_cover(path: Path, cfg: dict) -> None:
    print(f"\nCOVER {path.name}")
    if not path.exists():
        record(WARN, "not built")
        return
    info = sh(["pdfinfo", str(path)])
    pages = int(re.search(r"Pages:\s+(\d+)", info).group(1))
    size = re.search(r"Page size:\s+([\d.]+) x ([\d.]+) pts", info)
    w_in, h_in = float(size.group(1)) / 72, float(size.group(2)) / 72
    record(PASS if pages == 1 else FAIL,
           f"{pages} page(s) -- a wrap cover must be exactly 1")

    pc = ROOT / "dist" / cfg["slug"] / "pagecount.txt"
    p = cfg.get("print", {})
    trim = p.get("trim", ["6in", "9in"])
    per_page = 0.0025 if str(p.get("paper", "cream")).lower() == "cream" else 0.002252
    spine = int(pc.read_text().strip()) * per_page if pc.exists() else 0
    want_w = 2 * inches(trim[0]) + spine + 0.25
    want_h = inches(trim[1]) + 0.25
    if abs(w_in - want_w) < 0.02 and abs(h_in - want_h) < 0.02:
        record(PASS, f"{w_in:.3f} x {h_in:.3f} in incl. bleed, spine {spine:.4f} in")
    else:
        record(FAIL, f"{w_in:.3f} x {h_in:.3f} in, expected "
                     f"{want_w:.3f} x {want_h:.3f} in")
    if cfg.get("cover_guides", True):
        record(WARN, "production guides are ON -- set cover_guides: false "
                     "in book.yaml before uploading")


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    slug = sys.argv[1]
    cfg = yaml.safe_load((ROOT / "books" / slug / "book.yaml").read_text())
    d = ROOT / "dist" / slug
    print(f"Preflight: {cfg['title']}")
    check_epub(d / f"{slug}.epub")
    check_interior(d / f"{slug}-interior.pdf", cfg)
    check_cover(d / f"{slug}-cover.pdf", cfg)

    fails = sum(1 for lvl, _ in results if lvl == FAIL)
    warns = sum(1 for lvl, _ in results if lvl == WARN)
    print(f"\n{len(results) - fails - warns} passed, {warns} warnings, {fails} failures")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
