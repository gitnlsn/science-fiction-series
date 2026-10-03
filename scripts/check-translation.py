#!/usr/bin/env python3
"""Which translated chapters have fallen behind their source.

    scripts/check-translation.py <translation-slug>
    scripts/check-translation.py <translation-slug> --stamp FILE   # record source hash

A translation is a separate book whose chapters name the file they came from
and the hash of that file's body at the moment of translating:

    source: quarenta-dias-uteis/chapters/01-a-prova.md
    source_sha: 3f9a0c21be47

Only the body is hashed, so advancing `status:` or editing a planning note in
the source does not mark the translation stale; changing a sentence does.

What fails:
  - a translated chapter whose source body has changed since `source_sha`
  - a translated chapter whose `source` does not exist

What is reported and does not fail:
  - source chapters with no translation yet
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)


def split(path: Path) -> tuple[dict, str, str]:
    text = path.read_text(encoding="utf-8")
    if m := FM.match(text):
        return yaml.safe_load(m.group(1)) or {}, m.group(1), text[m.end():]
    return {}, "", text


def body_sha(path: Path) -> str:
    return hashlib.sha256(split(path)[2].strip().encode("utf-8")).hexdigest()[:12]


def stamp(path: Path) -> None:
    meta, raw, body = split(path)
    src = ROOT / "books" / meta["source"]
    sha = body_sha(src)
    if re.search(r"^source_sha:.*$", raw, re.M):
        raw = re.sub(r"^source_sha:.*$", f"source_sha: {sha}", raw, flags=re.M)
    else:
        raw = raw + f"\nsource_sha: {sha}"
    path.write_text(f"---\n{raw}\n---\n{body}", encoding="utf-8")
    print(f"-> {path.name}: source_sha {sha}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    book = ROOT / "books" / args[0]
    if "--stamp" in args:
        stamp(Path(args[args.index("--stamp") + 1]).resolve())
        return

    stale, missing, sources = [], [], set()
    translated = sorted((book / "chapters").glob("*.md"))
    for ch in translated:
        meta = split(ch)[0]
        src = ROOT / "books" / str(meta.get("source", ""))
        if not meta.get("source") or not src.is_file():
            missing.append(ch.name)
            continue
        sources.add(src.resolve())
        if body_sha(src) != str(meta.get("source_sha", "")):
            stale.append(ch.name)

    source_dirs = {p.parent for p in sources}
    untranslated = sorted(p.name for d in source_dirs for p in d.glob("*.md")
                          if p.resolve() not in sources)

    print(f"tradução: {len(translated)} capítulos, "
          f"{len(stale)} desatualizados, {len(untranslated)} sem tradução")
    for name in stale:
        print(f"  !! {name}: o original mudou desde a tradução")
    for name in missing:
        print(f"  !! {name}: `source` ausente ou inexistente")
    for name in untranslated:
        print(f"  .. {name}: ainda não traduzido")
    if stale or missing:
        sys.exit(1)


if __name__ == "__main__":
    main()
