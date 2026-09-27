#!/usr/bin/env python3
"""Add a chapter file, numbered after the last one.

    scripts/new-chapter.py <book-slug> "Título do Capítulo"

Prefer editing docs/<slug>/outline.md and running scaffold-outline.py -- the outline
is the source of truth for titles and numbering. This is for a chapter that
arrives while drafting, before the outline has caught up.
"""

from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def slugify(text: str) -> str:
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def main() -> None:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    book, title = sys.argv[1], sys.argv[2]
    chapters = ROOT / "books" / book / "chapters"
    if not chapters.is_dir():
        sys.exit(f"!! no such book: {book}")

    used = [int(m.group(1)) for p in chapters.glob("*.md")
            if (m := re.match(r"(\d+)", p.name))]
    n = max(used, default=0) + 1
    path = chapters / f"{n:02d}-{slugify(title)[:44].strip('-')}.md"
    path.write_text(
        "---\n"
        f"title: {title}\n"
        "part:\n"
        "pov:          # whose head this chapter is in, one name\n"
        "when:         # story time; lead with a sortable date if you have one\n"
        "where:\n"
        "premise:      # one sentence: what this chapter is for\n"
        "turn:         # what is different at the end than at the start\n"
        "threads: []   # plot threads this chapter moves\n"
        "seeds: []     # planted here, paid off later\n"
        "pays: []      # seeds this chapter collects on\n"
        "cast: []\n"
        "status: outline\n"
        "---\n\n",
        encoding="utf-8")
    print(f"-> {path.relative_to(ROOT)}")
    print(f"   add it to docs/{book}/outline.md too, or the next scaffold will not know it")


if __name__ == "__main__":
    main()
