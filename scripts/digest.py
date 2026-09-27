#!/usr/bin/env python3
"""A compact map of the whole novel, for reading one chapter against the rest.

    scripts/digest.py <book-slug>              the map, plus the reports
    scripts/digest.py <book-slug> --fios       just threads, seeds and payoffs
    scripts/digest.py <book-slug> --elenco     who is on the page, and when
    scripts/digest.py <book-slug> --tempo      story order against reading order
    scripts/digest.py <book-slug> --capitulo 09

Reviewing a chapter for continuity means holding the other thirty-nine in mind,
and reading thirty-nine chapters to review one is not affordable. The front
matter already carries the brief -- pov, when, where, premise, turn, threads,
seeds, pays, cast -- for every chapter, so the map is generated from it rather
than written by hand, and cannot drift out of date the way a hand-kept summary
would.

Read the map first, then the target chapter in full. See the skill
`revisar-capitulo` for what to do with it.
"""

from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FM = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.S)
MARKER = re.compile(r"\[\[\?(.+?)\]\]", re.S)
XREF = re.compile(r"\{\{cap:([a-z0-9-]+)\}\}")
REGISTRO = re.compile(r"^::: *\{\.registro\}", re.M)
# A leading sortable date in `when:` -- "2039-04-11 — três dias depois".
WHEN_KEY = re.compile(r"^\s*(\d{4}(?:-\d{2}){0,2})")


def one_line(value, width: int = 96) -> str:
    """Front matter wraps across lines; a map is only readable one line deep."""
    if isinstance(value, list):
        value = ", ".join(str(v) for v in value)
    text = " ".join(str(value or "").split())
    return text if len(text) <= width else text[: width - 1] + "…"


def words(body: str) -> int:
    body = re.sub(r"```.*?```", "", body, flags=re.S)
    body = re.sub(r"[#>*_`\[\]()]", " ", body)
    return len(body.split())


class Chapter:
    def __init__(self, path: Path, order: int) -> None:
        text = path.read_text(encoding="utf-8")
        m = FM.match(text)
        self.path = path
        self.order = order
        self.slug = re.sub(r"^\d+-", "", path.stem)
        self.num = path.stem.split("-")[0]
        self.meta = (yaml.safe_load(m.group(1)) if m else {}) or {}
        body = FM.sub("", text)
        self.words = words(body)
        self.refs = [s for s in XREF.findall(body) if s != self.slug]
        self.markers = MARKER.findall(body)
        self.registros = len(REGISTRO.findall(body))
        self.incoming: list[str] = []

    def get(self, key: str) -> str:
        return one_line(self.meta.get(key))

    def list_of(self, key: str) -> list[str]:
        value = self.meta.get(key) or []
        if isinstance(value, str):
            value = [v.strip() for v in value.split(",") if v.strip()]
        return [str(v) for v in value]

    @property
    def title(self) -> str:
        return str(self.meta.get("title") or self.slug)

    @property
    def part(self) -> str:
        return str(self.meta.get("part") or "?")

    @property
    def povs(self) -> list[str]:
        # A chapter carries one point of view, with one declared exception --
        # the parade, where three of them share a chapter in sections. Read it
        # as a list so the reports do not quietly lose the other two.
        return self.list_of("pov") or ["—"]

    @property
    def pov(self) -> str:
        return " / ".join(self.povs)

    @property
    def status(self) -> str:
        return str(self.meta.get("status") or "outline")

    @property
    def when_key(self) -> str | None:
        if m := WHEN_KEY.match(str(self.meta.get("when") or "")):
            return m.group(1)
        return None


def load(book: Path) -> list[Chapter]:
    chapters = [Chapter(p, i) for i, p
                in enumerate(sorted((book / "chapters").glob("*.md")))]
    by_slug = {c.slug: c for c in chapters}
    for c in chapters:
        for target in c.refs:
            if target in by_slug:
                by_slug[target].incoming.append(c.num)
    return chapters


def print_map(chapters: list[Chapter]) -> None:
    part = None
    for c in chapters:
        if c.part != part:
            part = c.part
            print(f"\n{part}")
        flags = []
        if c.registros:
            flags.append(f"registro×{c.registros}")
        if c.markers:
            flags.append(f"marcadores×{len(c.markers)}")
        tail = f"  [{', '.join(flags)}]" if flags else ""
        print(f"\n  {c.num} {c.title}   ({c.status}, {c.words} palavras){tail}")
        print(f"      pov......: {c.pov}")
        print(f"      quando...: {c.get('when')}")
        print(f"      onde.....: {c.get('where')}")
        print(f"      premissa.: {c.get('premise')}")
        print(f"      virada...: {c.get('turn')}")
        print(f"      fios.....: {c.get('threads') or '—'}")
        print(f"      planta...: {c.get('seeds') or '—'}")
        print(f"      paga.....: {c.get('pays') or '—'}")
        print(f"      elenco...: {c.get('cast') or '—'}")
        print(f"      remete a.: {', '.join(c.refs) if c.refs else '—'}")
        print(f"      citado em: {', '.join(c.incoming) if c.incoming else '—'}")


def print_fios(chapters: list[Chapter]) -> None:
    """Where the novel fails to hold together mechanically.

    These are candidates, never verdicts. A thread can be alive in a chapter
    that never declares it, and a long silence can be the point. The list says
    where to look; the reading says whether anything is wrong.
    """
    print("\n\nfios, promessas e pagamentos")

    threads: dict[str, list[Chapter]] = defaultdict(list)
    for c in chapters:
        for thread in c.list_of("threads"):
            threads[thread].append(c)
    for thread, group in sorted(threads.items()):
        caps = ", ".join(g.num for g in group)
        first, last = group[0], group[-1]
        print(f"  {thread:<26} {len(group):>2} cap.  {first.num}→{last.num}  [{caps}]")

    planted = {}
    for c in chapters:
        for seed in c.list_of("seeds"):
            planted.setdefault(seed, c)
    paid: dict[str, list[Chapter]] = defaultdict(list)
    for c in chapters:
        for seed in c.list_of("pays"):
            paid[seed].append(c)

    print(f"\n  {len(planted)} promessa(s) plantada(s), "
          f"{len(set(paid) & set(planted))} paga(s)")
    for seed, c in sorted(planted.items(), key=lambda x: x[1].order):
        payers = paid.get(seed) or []
        where = ", ".join(p.num for p in payers) if payers else "—— não paga"
        print(f"      {seed:<26} {c.num} → {where}")
    orphan = sorted(set(paid) - set(planted))
    if orphan:
        print("\n  pagamentos sem promessa (o leitor lê isso como trapaça):")
        for seed in orphan:
            print(f"      {seed}  em {', '.join(p.num for p in paid[seed])}")

    heavy = [c for c in chapters if c.registros > 1]
    if heavy:
        print("\n  mais de um registro (CLAUDE.md: no máximo um por capítulo):")
        for c in heavy:
            print(f"      {c.num} {c.title}  ×{c.registros}")
    used = sum(1 for c in chapters if c.registros)
    print(f"\n  registros: {used} de {len(chapters)} capítulos")


def print_elenco(chapters: list[Chapter]) -> None:
    print("\n\nponto de vista")
    per_pov: dict[str, list[Chapter]] = defaultdict(list)
    for c in chapters:
        for p in c.povs:
            per_pov[p].append(c)
    total_words = sum(c.words for c in chapters) or 1
    for pov, group in sorted(per_pov.items(), key=lambda x: -len(x[1])):
        # A shared chapter splits its words between the points of view in it,
        # so the shares still add up to the book.
        w = sum(c.words // len(c.povs) for c in group)
        share = 100 * w / total_words
        caps = ", ".join(g.num for g in group)
        print(f"  {pov:<22} {len(group):>2} cap.  {w:>6} palavras  {share:>4.0f}%")
        print(f"      {caps}")

    print("\nelenco")
    per_cast: dict[str, list[Chapter]] = defaultdict(list)
    for c in chapters:
        for name in c.list_of("cast"):
            per_cast[name].append(c)
    for name, group in sorted(per_cast.items(), key=lambda x: x[1][0].order):
        spans = [g.order for g in group]
        gaps = [b - a for a, b in zip(spans, spans[1:])]
        tail = f"   sumiu por {max(gaps)} capítulos" if max(gaps, default=0) > 8 else ""
        print(f"  {name:<22} {len(group):>2} cap.  "
              f"{group[0].num}→{group[-1].num}{tail}")


def print_tempo(chapters: list[Chapter]) -> None:
    """Story order against reading order.

    Out-of-order chapters are a technique, not an error, so this reports and
    never fails. What it is really for is the chapter whose `when:` was written
    without looking at its neighbours -- a scene set before an event the
    previous chapter already showed.
    """
    print("\n\nordem da história")
    dated = [c for c in chapters if c.when_key]
    undated = [c for c in chapters if not c.when_key]
    if not dated:
        print("  nenhum capítulo tem uma data ordenável em `when:`.")
        print("  Escreva `when: 2039-04-11 — três dias depois` e este relatório")
        print("  passa a comparar a ordem da história com a ordem da leitura.")
        return
    for c in sorted(dated, key=lambda x: (x.when_key or "", x.order)):
        print(f"  {c.when_key}  cap. {c.num}  {c.title}")
    inversions = [(a, b) for a, b in zip(dated, dated[1:])
                  if (a.when_key or "") > (b.when_key or "")]
    if inversions:
        print(f"\n  {len(inversions)} salto(s) para trás na ordem de leitura:")
        for a, b in inversions:
            print(f"      {a.num} ({a.when_key}) → {b.num} ({b.when_key})")
        print("      (analepse é técnica, não erro — confira se foi intencional)")
    if undated:
        print(f"\n  sem data ordenável: {', '.join(c.num for c in undated)}")


def print_chapter(chapters: list[Chapter], key: str) -> None:
    key = key.lower()
    matches = [c for c in chapters if c.num == key.zfill(2) or key in c.slug]
    if not matches:
        sys.exit(f"!! nenhum capítulo casa com {key!r}")
    for c in matches:
        print_map([c])
        print("\n  vizinhos de leitura:")
        for s in chapters[max(0, c.order - 2):c.order + 3]:
            if s is c:
                continue
            print(f"      {s.num} {s.title}  ({s.pov}, {s.get('when')})")
            print(f"          {s.get('premise')}")
        shared = [s for s in chapters if s is not c
                  and set(s.list_of("threads")) & set(c.list_of("threads"))]
        if shared:
            print("\n  no mesmo fio:")
            for s in shared:
                print(f"      {s.num} {s.title}  "
                      f"[{', '.join(sorted(set(s.list_of('threads')) & set(c.list_of('threads'))))}]")
        owed = [s for s in chapters if set(s.list_of("pays")) & set(c.list_of("seeds"))]
        if owed:
            print("\n  capítulos que cobram o que este planta:")
            for s in owed:
                print(f"      {s.num} {s.title}")


def main() -> None:
    args = sys.argv[1:]
    if not args:
        sys.exit(__doc__)
    book = ROOT / "books" / args[0]
    if not book.is_dir():
        sys.exit(f"!! no such book: {args[0]}")
    chapters = load(book)
    if not chapters:
        sys.exit("!! no chapters")

    if "--capitulo" in args:
        print_chapter(chapters, args[args.index("--capitulo") + 1])
    elif "--fios" in args:
        print_fios(chapters)
    elif "--elenco" in args:
        print_elenco(chapters)
    elif "--tempo" in args:
        print_tempo(chapters)
    else:
        print_map(chapters)
        print_fios(chapters)
        print_elenco(chapters)
        print_tempo(chapters)


if __name__ == "__main__":
    main()
