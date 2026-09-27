#!/usr/bin/env python3
"""Word counts, pacing, and where the point of view actually sits.

    scripts/stats.py <book-slug>

A novel's word count is a schedule, not a quality measure. What is worth
watching while drafting is the shape: chapters that have quietly become twice
their neighbours, a point of view that was meant to be shared and has taken
eighty per cent of the book, a part that runs long enough to sag.
"""

from __future__ import annotations

import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
REGISTRO = re.compile(r"^::: *\{\.registro\}", re.M)
STATUSES = ("outline", "draft", "revised", "final")


def words(text: str) -> int:
    text = FM.sub("", text)
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"[#>*_`\[\]()]", " ", text)
    return len(text.split())


def pov_list(meta: dict) -> list[str]:
    value = meta.get("pov") or []
    if isinstance(value, str):
        value = [v.strip() for v in value.split(",") if v.strip()]
    return [str(v) for v in value] or ["—"]


def meta_of(path: Path) -> dict:
    if m := FM.match(path.read_text(encoding="utf-8")):
        return yaml.safe_load(m.group(1)) or {}
    return {}


def bar(fraction: float, width: int = 32) -> str:
    return "#" * max(0, round(fraction * width))


def main() -> None:
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    book = ROOT / "books" / sys.argv[1]
    if not book.is_dir():
        sys.exit(f"!! no such book: {sys.argv[1]}")

    total = 0
    chapters: list[tuple[Path, int, dict]] = []
    for folder in ("front", "chapters", "back"):
        files = sorted((book / folder).glob("*.md"))
        if not files:
            continue
        print(f"\n{folder}/")
        for f in files:
            text = f.read_text(encoding="utf-8")
            n = words(text)
            total += n
            meta = meta_of(f)
            if folder == "chapters":
                chapters.append((f, n, meta))
            status = str(meta.get("status") or "—")
            reg = "  [registro]" if REGISTRO.search(text) else ""
            print(f"  {f.stem:<40} {n:>6,} palavras  {status:<8}{reg}")

    # ~300 words per 5.5x8.5 page at 11pt, ~250 words per minute read aloud.
    print(f"\n  {'total':<40} {total:>6,} palavras")
    print(f"  {'páginas impressas (estimativa)':<40} {round(total / 300):>6,}")
    minutes = round(total / 250)
    reading = f"{minutes // 60} h {minutes % 60:02d} min" if minutes >= 60 else f"{minutes} min"
    print(f"  {'tempo de leitura (estimativa)':<40} {reading:>6}")

    if not chapters:
        return

    counts = [n for _, n, _ in chapters]
    mean = sum(counts) / len(counts)
    print(f"\nritmo ({len(chapters)} capítulos)")
    print(f"  {'média':<40} {mean:>6,.0f} palavras")
    print(f"  {'mais curto':<40} {min(counts):>6,}")
    print(f"  {'mais longo':<40} {max(counts):>6,}")
    # A chapter at twice the mean is not wrong; it is a place to look. Long
    # chapters cluster where the plot got explained instead of dramatised.
    outliers = [(f, n) for f, n, _ in chapters if n > 1.6 * mean or n < 0.4 * mean]
    if outliers:
        print("\n  fora da média (não é erro — é onde olhar):")
        for f, n in outliers:
            print(f"      {f.stem:<40} {n:>6,}  {bar(n / max(counts))}")

    print("\nestado")
    by_status = Counter(str(m.get("status") or "outline") for _, _, m in chapters)
    for s in STATUSES:
        if by_status.get(s):
            n = by_status[s]
            done = sum(w for _, w, m in chapters if str(m.get("status")) == s)
            print(f"  {s:<12} {n:>3} cap.  {done:>7,} palavras  "
                  f"{bar(n / len(chapters))}")

    print("\nponto de vista")
    per_pov: dict[str, list[int]] = defaultdict(list)
    for _, n, m in chapters:
        # One point of view per chapter, with one declared exception -- the
        # parade shares a chapter between three of them. Split the words so the
        # shares still add up to the book.
        povs = pov_list(m)
        for p in povs:
            per_pov[p].append(n // len(povs))
    body = sum(counts) or 1
    for pov, group in sorted(per_pov.items(), key=lambda x: -sum(x[1])):
        share = sum(group) / body
        print(f"  {pov:<22} {len(group):>3} cap.  {sum(group):>7,} palavras  "
              f"{share:>4.0%}  {bar(share)}")

    print("\npor parte")
    per_part: dict[str, list[int]] = defaultdict(list)
    order: list[str] = []
    for _, n, m in chapters:
        part = str(m.get("part") or "?")
        if part not in per_part:
            order.append(part)
        per_part[part].append(n)
    for part in order:
        group = per_part[part]
        print(f"  {part[:36]:<38} {len(group):>2} cap.  {sum(group):>7,} palavras")

    if total < 7200:
        print("\n  nota: o mínimo de 24 páginas da KDP pede cerca de 7.200 palavras.")


if __name__ == "__main__":
    main()
