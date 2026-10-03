#!/usr/bin/env python3
"""Print the front matter for a translated chapter, built from its source.

    scripts/translation-header.py <translation-slug> <source-chapter.md> "<English title>" > new.md

Copies the source front matter verbatim (the planning notes stay in the
language of the canon), replaces `title:` and `part:`, and adds `source:`,
`source_sha:` and `status: draft`. The English part string comes from the
translation's own `parts/` files, matched through their `source:` line. Rules:
docs/translation-en.md and docs/<source-slug>/translation-en.md.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def meta(path: Path) -> dict:
    m = FM.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(m.group(1)) if m else {}


def part_map(slug: str) -> dict[str, str]:
    out = {}
    for p in sorted((ROOT / "books" / slug / "parts").glob("*.md")):
        m = meta(p)
        if m.get("source"):
            out[meta(ROOT / "books" / m["source"]).get("part", "")] = m.get("part", "")
    return out


def main() -> None:
    slug, src, title = sys.argv[1], Path(sys.argv[2]).resolve(), sys.argv[3]
    parts = part_map(slug)
    text = src.read_text(encoding="utf-8")
    m = FM.match(text)
    raw, body = m.group(1), text[m.end():]
    sha = hashlib.sha256(body.strip().encode("utf-8")).hexdigest()[:12]
    out = []
    for line in raw.splitlines():
        if line.startswith("status:"):
            continue
        if line.startswith("title:"):
            line = f"title: {title}"
        elif line.startswith("part:"):
            part = line.split(":", 1)[1].strip()
            line = f"part: {parts.get(part, part)}"
        out.append(line)
    rel = src.relative_to(ROOT / "books")
    out += [f"source: {rel}", f"source_sha: {sha}", "status: draft"]
    print("---\n" + "\n".join(out) + "\n---")


if __name__ == "__main__":
    main()
