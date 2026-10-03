# Translation contract — the English editions

The English editions of the three novels. Settled (by the author's delegation,
2026-10-03, following the precedent of *Forty Working Days*): **US English**;
the pen name **Íris Gradim**, pronoun **she**; and these titles:

| Portuguese | English | Slug |
|---|---|---|
| *Depois de mim* | ***After Me*** | `after-me` |
| *A volta a mais* | ***The Extra Turn*** | `the-extra-turn` |
| *O que é do mar* | ***What Belongs to the Sea*** | `what-belongs-to-the-sea` |

Each English edition is a **separate book** in `books/<english-slug>/`, not a
variant. **The Portuguese manuscript stays canon.** The bible, timeline, outline
and references of each book describe the novel and are not translated. When the
English and the Portuguese disagree about what happens, the Portuguese wins.
When they disagree about how to *say* it in English, the book's own
`docs/<source-slug>/translation-en.md` wins, then this file.

Every rule in `CLAUDE.md` binds the translation exactly as it binds the
Portuguese: no country, no month, no currency, no real institution; separate
worlds; the future used, not catalogued; nobody amazed except Helena. A
translation that is fluent and breaks one of those is a worse book.

## How a chapter is translated

- **Same filename as the source.** `books/<english-slug>/chapters/` mirrors the
  Portuguese `chapters/` file for file.
- **Front matter** comes from `scripts/translation-header.py`:

      python3 scripts/translation-header.py <english-slug> \
          books/<source-slug>/chapters/<file>.md "<English title>" > books/<english-slug>/chapters/<file>.md

  It copies the source front matter **verbatim, in Portuguese** (`pov`, `when`,
  `where`, `premise`, `turn`, `threads`, `seeds`, `pays`, `cast`), so `make
  fios` and `make digest` work on the English book; it replaces `title:` and
  `part:`, and adds `source:`, `source_sha:` and `status: draft`. Then append
  the English body.
- **`make traducao`** lists every English chapter whose Portuguese source body
  changed since it was translated. Re-translate the changed passage, then
  `python3 scripts/check-translation.py <english-slug> --stamp <file>`.
- **Front, back and part files** carry `source:` too (no hash needed).
- **Translate the chapter, not the sentence.** Keep the register: close, plain,
  specific. Keep the paragraph shapes and the rhythm of short lines. Break a
  long Portuguese chain of *e … e … e* only where English would really lose the
  reader. Never tidy a flat sentence; the flatness is often the point.
- **Nothing added, nothing explained.** Where the Portuguese leaves a gap, the
  English leaves the same gap. No clarifying clause, no gloss.
- **Recurring sentences are fixed.** A line a character repeats, or the
  narration returns to, must be the same English every time. Each book's
  contract lists them; when you meet a new one, add it there before using it.

## Form and typography

- **Dialogue takes US double quotation marks.** The Portuguese travessão is a
  typographic convention, not a voice. `— Ciça.` → `"Ciça."` Attributions move
  inside the normal English way: `— Não — disse ela.` → `"No," she said.`
- **Italics stay italics** (remembered words, messages, sayings, a word held up
  to look at); bold stays bold.
- **Scene breaks (`---`), `##` heads and any `::: {.registro}` block stay where
  they are.**
- **Numbers are spelled out in prose** where the Portuguese spells them out.
  Clock times in prose are spoken: *nine forty*, *ten past midnight*. **Metric
  stays metric** (kilometres → *kilometers*, US spelling); converting to miles
  or feet would place the book in one country. Decimals take a point in
  documents and displays: `2,9 kg` → `2.9 kg`.
- **Dates never appear in prose**, as in the Portuguese. Never introduce a
  month, a holiday, a school term, a sport or an institution that the
  Portuguese does not have. Seasons only where the Portuguese has them.
- **Honorifics.** *Dona* and *seu* are Brazilian on an English page and would
  fix a country by another route. *Dona Ilda* → **Mrs. Ilda**; *Seu Lauro* →
  **Mr. Lauro**. Use one exactly where the Portuguese does. Drop the Portuguese
  article before names (*o Davi* → Davi).
- **Personal names never change**, accents included (Helena, Cecília, Iara,
  Otávio, Joana, Taís…). Nicknames stay as they are (*Ciça*).
- **Invented place names that are proper names stay** (Thalassa). **Places named
  with ordinary Portuguese words are translated** into ordinary English words,
  so that no Portuguese street word sits on the page and points at a country
  (*rua dos Calafates* → *Caulkers Street*). Each book's contract fixes them.
- **Kinship words in speech:** *mãe* → Mom (address) / my mother; *vô*, *vó* →
  Grandpa, Grandma; *filha* as an endearment → sweetheart.

## Front and back matter

- *Antes de começar* → **Before You Begin**; *Sobre a autora* → **About the
  Author**. Translate them closely. "About the Author" keeps *She works under
  human direction*, and **never** mentions the person who directed the book.
- Book titles inside them: *Quarenta dias úteis* → *Forty Working Days*; the
  other books of the series by their English titles. Published translations
  cited by name keep the English edition's title (Clarke's *The Fountains of
  Paradise*, Le Guin's *The Dispossessed*, Ishiguro's *Klara and the Sun* and
  *Never Let Me Go*).
- **`book.yaml`:** translate `kdp.description`; replace `keywords` with seven
  English ones and `categories` with English BISAC-style paths
  (`Fiction > Science Fiction > General`, …). Everything else is set.

## What the translator does not do

- **Never edit the Portuguese.** A translation finds things: a contradiction, a
  month that slipped through, a line that only works in Portuguese. List them in
  the book's contract under *Found in the Portuguese*, and leave the
  Portuguese for the author.
- **Never translate the docs** (bible, outline, timeline, references).
