#!/usr/bin/env python3
"""The novel's structural gate: setups without payoffs, payoffs without setups.

    scripts/check-threads.py <book-slug>
    scripts/check-threads.py <book-slug> --strict   # unpaid seeds also fail

Every chapter declares, in its front matter, what it plants and what it
collects:

    seeds: [porta-do-porao, o-nome-de-vera]
    pays:  [cartao-de-acesso]

A reader does not forgive either failure. A payoff that was never set up reads
as the author cheating; a setup that never pays reads as the author forgetting.
Both are invisible while drafting one chapter and obvious across forty, which
is exactly the kind of error worth spending a script on.

What fails the build:

  - a `pays:` whose seed is planted in no chapter at all
  - a `pays:` whose seed is planted LATER in reading order than the payoff
  - a seed planted and never paid, once every chapter has reached `final`
    (or immediately, with --strict)

Threads are reported, never gated: a thread that goes quiet for six chapters
may be suspense or may be a dropped ball, and only reading decides.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
# How many chapters a thread may go unmentioned before the report says so.
# Not a rule -- a number that makes the gap visible enough to judge.
QUIET = 6


class Chapter:
    def __init__(self, path: Path, order: int) -> None:
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        self.path = path
        self.order = order
        self.num = path.stem.split("-")[0]
        try:
            self.meta = yaml.safe_load(m.group(1)) if m else {}
        except yaml.YAMLError as exc:
            sys.exit(f"!! {path.name}: front matter is not valid YAML\n   {exc}")
        self.meta = self.meta or {}

    def list_of(self, key: str) -> list[str]:
        value = self.meta.get(key) or []
        if isinstance(value, str):
            value = [v.strip() for v in value.split(",") if v.strip()]
        return [str(v) for v in value]

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.path.stem)

    @property
    def status(self) -> str:
        return str(self.meta.get("status") or "outline")


def main() -> None:
    args = sys.argv[1:]
    strict = "--strict" in args
    args = [a for a in args if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    book = ROOT / "books" / args[0]
    if not book.is_dir():
        sys.exit(f"!! no such book: {args[0]}")

    chapters = [Chapter(p, i) for i, p
                in enumerate(sorted((book / "chapters").glob("*.md")))]
    if not chapters:
        sys.exit("!! no chapters")

    planted: dict[str, Chapter] = {}
    for c in chapters:
        for seed in c.list_of("seeds"):
            # First plant wins: a seed re-declared later is a reminder, not a
            # second setup, and the reader met it the first time.
            planted.setdefault(seed, c)

    failures: list[str] = []

    # --- payoffs with nothing behind them ---------------------------------
    for c in chapters:
        for seed in c.list_of("pays"):
            source = planted.get(seed)
            if source is None:
                failures.append(
                    f"[FAIL] {c.num} {c.title}: paga \"{seed}\", que nenhum "
                    f"capítulo planta")
            elif source.order > c.order:
                failures.append(
                    f"[FAIL] {c.num} {c.title}: paga \"{seed}\", plantado depois, "
                    f"em {source.num} {source.title}")
            elif source.order == c.order:
                failures.append(
                    f"[FAIL] {c.num} {c.title}: planta e paga \"{seed}\" no mesmo "
                    f"capítulo — isso não é uma promessa, é uma coincidência")

    # --- setups nobody collects -------------------------------------------
    paid = {seed for c in chapters for seed in c.list_of("pays")}
    unpaid = [(seed, c) for seed, c in planted.items() if seed not in paid]
    sealed = all(c.status == "final" for c in chapters)
    if unpaid:
        blocking = strict or sealed
        flag = "FAIL" if blocking else "todo"
        print(f"\n{len(unpaid)} promessa(s) sem pagamento:")
        for seed, c in sorted(unpaid, key=lambda x: x[1].order):
            print(f"  [{flag}] {seed}  (plantado em {c.num} {c.title})")
        if blocking:
            failures.append(f"{len(unpaid)} promessa(s) sem pagamento")
        else:
            print("       (ainda não bloqueia: o livro não está todo em `final`)")

    # --- threads, reported only -------------------------------------------
    threads: dict[str, list[Chapter]] = defaultdict(list)
    for c in chapters:
        for thread in c.list_of("threads"):
            threads[thread].append(c)
    if threads:
        print("\nfios")
        for thread, group in sorted(threads.items()):
            spans = [c.order for c in group]
            gaps = [b - a for a, b in zip(spans, spans[1:])]
            worst = max(gaps, default=0)
            tail = ""
            if worst > QUIET:
                where = spans[gaps.index(worst)]
                after = next(c for c in chapters if c.order == where)
                tail = f"   silêncio de {worst} capítulos depois de {after.num}"
            caps = ", ".join(c.num for c in group)
            print(f"  {thread:<28} {len(group):>2} cap.  [{caps}]{tail}")

    if failures:
        print()
        for line in failures:
            if line.startswith("[FAIL]"):
                print(line)
        print(f"\n{sum(1 for f in failures if f.startswith('[FAIL]'))} falha(s) "
              f"estrutural(is).")
        sys.exit(1)

    print(f"\n{len(planted)} promessa(s), {len(paid)} paga(s), "
          f"{len(threads)} fio(s). Nada quebrado.")


if __name__ == "__main__":
    main()
