# CLAUDE.md

Production repo for a **science fiction series of three novels** (the author's
third, fourth and fifth books). Each book lives in `books/<slug>/` and has its
own planning docs in `docs/<slug>/`. The Markdown manuscript builds to a
KDP-ready EPUB and a print-ready PDF, with the same toolchain as *Quarenta dias
úteis* (`../artificial-intelligence-a-dystopia`) and *Manual da Vida*.

## A série — decided

Reading order is **strongest hook first**, by the author's decision:

| # | Slug (working) | Working title | Premise | Year |
|---|---|---|---|---|
| 1 | `depois-de-mim` | **Depois de mim** (decided) | Helena, 38, scanned before dying in 2031, wakes in 2140 in a body grown from her DNA; her daughter, 115 and dying, brought her back for herself | 2140 |
| 2 | `o-elevador` | O elevador | on the world's space elevator, anchored near the equator in an unnamed country, a maintenance technician finds a body 20,000 km up the cable: her mentor. A mystery with a heart | [[?autor]] |
| 3 | `recife-submersa` | Recife submersa | a water engineer leads a community rebuilding flooded Recife on the water | 2090 |

- **Separate worlds.** The three books share a series label and nothing else:
  no shared characters, technology, timeline or events. **Never cross-reference
  one book from another**, and never copy an invention from one bible to the
  next. Each `docs/<slug>/bible.md` is its own canon.
- **The same shape for all three:** one protagonist, four arcs, **4 parts × 4–5
  chapters** (16–20 chapters). Each outline starts with 18 slots (5/4/4/5); the
  split is the author's to change.
- Each book's premise and four arcs are in `docs/<slug>/outline.md`. They are
  the chosen **starting point**; chapter titles do not exist yet. Do not invent
  them into the docs as if decided — propose in conversation, record once the
  author chooses. Open items are `[[?autor: …]]` so `make marcadores` asks.
- `docs/series.md` holds what belongs to the series rather than a book: the
  series name (open), the order, the shared form.

Each arc must **change the protagonist**: they leave each part a different
person than they entered it, and the change is recorded under *Protagonista*
in that book's `bible.md`. Four parts that are four episodes of the same
person are one arc told four times.

## O futuro na página

The author asked for *lots* of futuristic references. The failure mode of that
request is a catalogue: gadgets listed, named and dropped. The rule instead:

- **Every technology is used, not mentioned.** It is on the page because
  someone is doing something with it in this scene.
- **Describe the hardware** — shape, sound, weight, heat, what it smells like
  when it breaks. A name alone is not a reference.
- **Every technology has a limit, a cost and someone left out.** Plot lives in
  the limit.
- **Nobody in the future is amazed by the future.** Characters use it the way
  we use a lift. Wonder belongs to the reader, not the cast.
  **The one declared exception in the series is Helena** (book 1): she comes
  from 2031, so she *is* amazed, and the reader discovers 2140 through her.
  Everyone around her follows the rule — which is what makes her stand out.
- **Real science is checked.** Extrapolation is the genre; getting the present
  wrong is not. Anything the book asserts about real physics, biology or
  engineering goes in `docs/<slug>/references.md` or is marked `[[?fato: …]]`.
- **Invented technology is canon once written.** It goes in that book's
  `bible.md` the same session, or is marked `[[?mundo: …]]`.

## O mundo é canônico — docs/<slug>/bible.md

**A chapter may invent, but the invention is not real until it is written
down.** When a draft invents something, add it to `docs/<slug>/bible.md` in
the same session, or leave `[[?mundo: …]]` in the prose. `make marcadores` will not let
that chapter reach `revised` or `final` while the marker stands.

## Promessa e pagamento

Every chapter declares its setups and payoffs in front matter, as slugs:

    seeds: [porta-do-porao, o-nome-de-vera]
    pays:  [cartao-de-acesso]

`make fios` fails the build on a payoff whose seed is planted nowhere, or later
in reading order, or in the same chapter. Threads are reported, never gated.

## Ponto de vista, tempo e continuidade

`pov:`, `when:` and `where:` are the continuity record. Lead `when:` with a
sortable date so `make digest --tempo` can flag jumps backwards. `cast:` lists
who is on the page; `make digest --elenco` shows who has gone missing.

**Never write a chapter number into this file, into a skill, or into prose.**
Refer to chapters by title here, and by `{{cap:slug}}` in the manuscript.

## Diálogo — the whole series

Dialogue is set the Brazilian way, as in *Quarenta dias úteis*: each speech on
its own line, opening with a **travessão and a space** (`— `), never quotation
marks and never a hyphen.

    — As mãos eram minhas.

A line opening with `- `, `– ` or `-- ` is a Markdown list item and prints as a
bullet. `make marcadores` fails on it (`lint_dialogue` in
`scripts/check-claims.py`). Book 1's own voice rules (Helena in first person present, Cecília in
third person past, alternating) are in `docs/depois-de-mim/outline.md`.

## Language

Portuguese (pt-BR) is the primary edition of all three, as with the author's
first two books. Printed labels come from `labels:` in `book.yaml`.

## Structure and conventions

- `docs/<slug>/outline.md` is the single source for that book's chapter titles
  and numbering. `make outline BOOK=<slug>` creates missing chapter files and
  refreshes planning notes; it never touches a written body. **Don't run it
  while the slots still carry placeholder titles** — it would create 18 files
  named after placeholders.
- `docs/<slug>/bible.md` is that book's world. `docs/<slug>/timeline.md` is its
  chronology in story order, including the history between today and the
  book's present. `docs/<slug>/references.md` is what is real.
- `docs/_modelo/` holds the blank templates; `make new-book SLUG=…` copies them
  into a new `docs/<slug>/`. Nothing in `_modelo/` is read by the gates.
- Planning notes (`pov`, `when`, `where`, `premise`, `turn`, `threads`, `seeds`,
  `pays`, `cast`, `status`) live in chapter front matter; the build strips it.
  `status:` goes `outline` → `draft` → `revised` → `final`, by hand.
- Part openers live in `books/<slug>/parts/`; their `part:` string must match
  the `## PARTE …` heading in that book's outline exactly (`I — O DESPERTAR`).
  Rename both together.
- Chapter bodies: `##` for section heads (rarely), `---` for a scene break,
  never an `#` heading.
- Illustrations are part openers only, one master per part in
  `illustrations/masters/`, matched by the part's `illustration:` field. A
  placeholder is generated until the art exists.
- The build still supports the `::: {.registro}` block (a set-apart machine
  document) from *Quarenta dias úteis*. Useful for logs, transmissions and
  system output — whether any of the three uses it is undecided.
- Covers are typographic, from `shared/print/cover.typ`. Each book can set its
  own palette in `book.yaml` under `cover:` (`bg`, `ink`, `accent`, hex); the
  build passes them to both the print wrap and the eBook cover. *Depois de mim*
  has no cover artwork, by the author's decision.
- `dist/` is never committed.

## Commands

Every target takes `BOOK=<slug>`; the default is `depois-de-mim`.

    make                 # build the book (epub + interior + cover)
    make books           # build all three
    make check           # KDP preflight + both manuscript gates
    make fios            # setups without payoffs, payoffs without setups
    make marcadores      # unresolved [[?...]] markers (the book + docs/<slug>/ + docs/series.md)
    make digest          # whole-novel map: pov, time, threads, cast
    make stats           # word counts, pacing, POV balance
    make outline         # docs/<slug>/outline.md -> chapter files
    make watch           # rebuild the print PDF on every save

**`vale` is not a gate** (English linters, Portuguese manuscript — see
`.vale.ini`). Never report it as passing or failing.

## Template gotchas, already solved — do not "fix" them

Inherited from *Quarenta dias úteis*; the comments in
`shared/print/template.typ` explain each:

1. Recto breaks use `pagebreak(to: "odd")`. Do not reintroduce hand-computed
   page parity from `here().page()`.
2. Running heads and blank-page detection query elements; chapter numbers are
   passed as arguments. Do not convert either to `state`.
3. In the EPUB, a part opener's figure comes *after* the `<h1>`.
4. Only the vendored Libertinus faces are guaranteed to embed; KDP rejects a
   PDF with an unembedded font.

## A decidir pelo autor

Decided and recorded: the pen name is **Íris Gradim** for the whole series; there
is no length target (KDP needs only 24–828 pages in print; *Depois de mim* is
~43,000 words, 186 pages); *Depois de mim* gets **no new characters**.

Still open: the series name (`docs/series.md`), and each book's items under
*A decidir pelo autor* in its `docs/<slug>/outline.md`. When a book gets its real
title, rename `books/<slug>/`, `docs/<slug>/` and `slug:` in its `book.yaml`
together, and `BOOK ?=` in the Makefile if it is book 1.
