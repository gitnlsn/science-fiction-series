#!/usr/bin/env python3
"""Scaffold another book in the series.

    scripts/new-book.py <slug> [--title "..."] [--from <slug>]

Copies the book.yaml, part openers and back matter of the newest existing book
(or --from) so a series shares its typography by construction, and creates
docs/<slug>/ from the blank templates in docs/_modelo/. Leaves an empty
manuscript to write into.

book.yaml is edited as text, not round-tripped through YAML, so its comments
survive -- they are the only record of why a setting is what it is.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--title")
    ap.add_argument("--from", dest="source", help="book slug to inherit settings from")
    args = ap.parse_args()

    dest = ROOT / "books" / args.slug
    docs = ROOT / "docs" / args.slug
    for path in (dest, docs):
        if path.exists():
            sys.exit(f"!! {path.relative_to(ROOT)} already exists")

    books = sorted(p for p in (ROOT / "books").iterdir() if (p / "book.yaml").exists())
    source = ROOT / "books" / args.source if args.source else (books[-1] if books else None)
    if source is None:
        sys.exit("!! no existing book to inherit from")

    text = (source / "book.yaml").read_text(encoding="utf-8")
    yaml.safe_load(text)  # fail early on an invalid source book.yaml
    title = args.title or args.slug.replace("-", " ").title()
    number = max((yaml.safe_load((b / "book.yaml").read_text()).get("series") or {})
                 .get("number") or 0 for b in books) + 1

    # Replace only the value on each line and keep any trailing comment.
    def set_value(text: str, key: str, value: str, indent: str = "") -> str:
        pat = re.compile(rf"^({indent}{key}:\s*)(\S.*?)?(\s+#.*)?$", re.M)
        if not pat.search(text):
            sys.exit(f"!! {source.name}/book.yaml has no `{key}:` line")
        return pat.sub(lambda m: f"{m.group(1)}{value}{m.group(3) or ''}", text, count=1)

    text = set_value(text, "slug", args.slug)
    text = set_value(text, "title", title)
    text = set_value(text, "isbn", '""')
    text = set_value(text, "number", str(number), indent="  ")

    for sub in ("front", "chapters", "back", "parts", "illustrations/masters"):
        (dest / sub).mkdir(parents=True)
    (dest / "book.yaml").write_text(text, encoding="utf-8")
    (dest / "chapters" / ".gitkeep").touch()
    (dest / "illustrations" / "masters" / ".gitkeep").touch()
    for sub in ("parts", "back"):
        for md in sorted((source / sub).glob("*.md")):
            shutil.copy(md, dest / sub / md.name)

    templates = ROOT / "docs" / "_modelo"
    docs.mkdir(parents=True)
    for md in sorted(templates.glob("*.md")):
        body = md.read_text(encoding="utf-8")
        body = body.replace("<slug>", args.slug).replace("<título>", title)
        body = body.replace("Livro N da série", f"Livro {number} da série")
        (docs / md.name).write_text(body, encoding="utf-8")

    print(f"-> books/{args.slug} and docs/{args.slug} created "
          f"(book {number}; settings from {source.name})\n"
          f"   the part openers were copied from {source.name}: rename them to "
          f"match docs/{args.slug}/outline.md\n"
          f"   then: make BOOK={args.slug}")


if __name__ == "__main__":
    main()
