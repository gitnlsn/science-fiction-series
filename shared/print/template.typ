// KDP paperback interior template.
// Trim size, KDP margin rules, running heads, chapter openers.
//
// Two typst behaviours shaped this design, both learned the hard way:
//   * `here().page()` is the PHYSICAL page number, not the folio, and inside
//     a context placed right after a weak pagebreak it still reports the page
//     before the break. So page parity is never computed by hand -- recto
//     breaks use `pagebreak(to: "odd")`, which is correct by construction.
//   * `state` does not resolve as expected inside a header or a show rule.
//     Running heads and filler-page detection therefore query elements, and
//     chapter numbers are passed in explicitly.

// --- KDP inside (gutter) margin minimums, by interior page count ---------
#let kdp-gutter-min(pages) = {
  if pages <= 150 { 0.375in } else if pages <= 300 { 0.5in } else if pages <= 500 {
    0.625in
  } else if pages <= 700 { 0.75in } else { 0.875in }
}

// Marks the end of a piece, so the header/footer can tell a blank filler
// page (which must stay completely blank) from a page of running text.
#let _piece-end = [#metadata("piece-end")<piece-end>]

// --- Chapter with an optional opener illustration -------------------------
#let chapter(title, number: none, label: "Chapter", illustration: none, body) = {
  pagebreak(to: "odd", weak: true)
  if illustration != none {
    block(width: 100%, above: 0pt, below: 1.5em, align(center, image(
      illustration,
      width: 74%,
    )))
  }
  if number != none {
    block(width: 100%, above: 0pt, below: 0.85em, align(center, text(
      font: ("Libertinus Sans",),
      size: 8.5pt,
      tracking: 0.28em,
      fill: luma(35%),
    )[#upper[#label #number]]))
  }
  [#heading(level: 2, title)<cap>]
  body
  _piece-end
}

// --- Unnumbered opener, for front and back matter ------------------------
// `outlined: false` keeps a piece out of the table of contents -- the right
// setting for a dedication, an epigraph, or the contents page itself.
#let section(title, outlined: true, body) = {
  pagebreak(to: "odd", weak: true)
  heading(level: 2, outlined: outlined, title)
  body
  _piece-end
}

// Scene break. Pandoc's typst writer emits `#divider()` for a markdown
// `---`, so this is the function that name has to resolve to.
#let divider() = align(center, block(above: 1.3em, below: 1.3em, text(
  size: 1.05em,
  tracking: 0.55em,
  fill: luma(35%),
)[#sym.ast.op#sym.ast.op#sym.ast.op]))

// --- Abertura de parte ----------------------------------------------------
// Each part opens on a recto with its numeral and title, and then carries the
// hard data for the part -- the figures live here rather than scattered
// through the chapters, so the chapters can stay in the book's own voice.
// `body-inset` is passed in by the generated main.typ, because the build has
// to rasterize the opener art at exactly the width it prints at -- a single
// number in book.yaml drives both, so the two can never drift apart.
#let part-opener(numeral, title, illustration: none, body-inset: 0.3in, body) = {
  pagebreak(to: "odd", weak: true)
  set page(header: none, footer: none)
  // A part has to appear in the table of contents and in the PDF bookmarks.
  // The title block below is drawn by hand, so the heading that carries the
  // outline entry is placed out of the flow and hidden: it occupies no space
  // and still has a location for `outline` and for the bookmark tree.
  place(top, hide(heading(level: 1, outlined: true, bookmarked: true)[
    Parte #numeral — #title
  ]))
  // The opener art sets to the same measure as the part's body text below,
  // by construction rather than by a hand-tuned percentage: same inset, image
  // at full width. A trim or margin change moves both together.
  if illustration != none {
    v(0.55in)
    block(width: 100%, below: 1.4em, inset: (x: body-inset), image(illustration, width: 100%))
  } else {
    v(1.6in)
  }
  align(center)[
    #text(font: ("Libertinus Sans",), size: 9pt, tracking: 0.32em, fill: luma(40%))[
      #upper[Parte #numeral]
    ]
    #v(1.1em)
    #text(font: ("Libertinus Serif Display",), size: 22pt, weight: "semibold")[
      #title
    ]
  ]
  v(2.2em)
  // The body sets in the book's own voice, so a part can introduce its ideas
  // before its first scene. A `::: {.registro}` block inside styles
  // itself, which is how the data still arrives in the other register.
  block(width: 100%, inset: (x: body-inset))[
    #set par(justify: true, first-line-indent: 0pt, spacing: 0.95em)
    #body
  ]
  pagebreak(weak: false)
}

// --- O registro ------------------------------------------------------------
// The novel's second register. When the machine speaks in its own voice -- a
// log line, a transcript, a scheduling notice, a policy memorandum -- the book
// does not describe it, it reproduces it. The typography has to announce the
// switch before a word is read: a full hairline box (this is a document, not a
// paragraph), a sans face, ragged right against the book's justified measure,
// no paragraph indent, tight leading.
//
// A mono face would read better still, and is deliberately not used: only the
// vendored Libertinus faces are guaranteed to embed, and KDP rejects a PDF with
// an unembedded font. Vendor an OFL mono into shared/fonts and change `font`
// here if you want one -- nothing else in the build needs to know.
//
// `etiqueta` prints a tracked, uppercase caption above the rule -- the header a
// real document carries. Omit it and the block is just the box.
#let registro(body, etiqueta: none) = block(
  width: 100%,
  above: 1.7em,
  below: 1.7em,
  stroke: 0.5pt + luma(45%),
  inset: (x: 1em, top: 0.85em, bottom: 0.85em),
  breakable: true,
)[
  #set text(font: ("Libertinus Sans", "Helvetica Neue"), size: 9.5pt, fill: luma(12%))
  // Tight leading, generous paragraph spacing: each entry stands alone.
  #set par(justify: false, first-line-indent: 0pt, leading: 0.62em, spacing: 1.15em)
  #if etiqueta != none {
    block(below: 0.9em)[
      #set text(size: 7.5pt, tracking: 0.14em, fill: luma(35%))
      #upper(etiqueta)
    ]
  }
  #body
]

// --- Generated front-of-book pages ---------------------------------------
// Half title (recto), blank verso, title page (recto), copyright (verso).
#let front-pages(
  title: "",
  subtitle: none,
  author: "",
  publisher: none,
  copyright-year: none,
  rights: none,
  isbn: none,
  edition: none,
  series: none,
  colophon: "Set in Libertinus Serif.",
  sans: ("Libertinus Sans",),
  display: ("Libertinus Serif Display",),
) = {
  set page(header: none, footer: none)
  v(2.2in)
  align(center, text(font: display, size: 17pt, tracking: 0.04em)[#title])
  pagebreak(weak: false) // blank verso
  pagebreak(weak: false) // title page lands on a recto
  v(1.5in)
  align(center)[
    #text(font: display, size: 30pt, weight: "semibold")[#title]
    #if subtitle != none [
      #v(0.9em)
      #text(font: display, size: 14pt, style: "italic", fill: luma(25%))[#subtitle]
    ]
    #v(2.4em)
    #text(font: sans, size: 11.5pt, tracking: 0.16em)[#upper(author)]
    #if series != none [
      #v(3.2em)
      #text(font: sans, size: 8.5pt, tracking: 0.2em, fill: luma(40%))[
        #upper(series)
      ]
    ]
  ]
  pagebreak(weak: false)
  // Copyright page, on the verso of the title page.
  set text(size: 8.5pt)
  set par(justify: false, first-line-indent: 0pt, leading: 0.7em)
  v(1fr)
  align(left)[
    #title #if subtitle != none [-- #subtitle] \
    #if copyright-year != none [Copyright © #copyright-year #author \ ]
    #if rights != none [#rights \ ]
    #v(0.8em)
    #if publisher != none [#publisher \ ]
    #if isbn != none and isbn != "" [ISBN #isbn \ ]
    #if edition != none [#edition \ ]
    #v(0.8em)
    #colophon
  ]
}

// --- The book -------------------------------------------------------------
// Content arrives in three slots so that the roman -> arabic folio switch
// happens at the top level of this function, where `set` rules actually
// apply to everything that follows.
#let book(
  title: "",
  subtitle: none,
  author: "",
  publisher: none,
  copyright-year: none,
  rights: none,
  isbn: none,
  edition: none,
  series: none,
  colophon: "Set in Libertinus Serif.",
  trim: (6in, 9in),
  pages-estimate: 120,
  bleed: false,
  outer-margin: 0.625in,
  top-margin: 0.7in,
  bottom-margin: 0.75in,
  gutter-extra: 0.375in,
  serif: ("Libertinus Serif", "Georgia"),
  sans: ("Libertinus Sans", "Helvetica Neue"),
  display: ("Libertinus Serif Display", "Libertinus Serif"),
  font-size: 11pt,
  leading: 0.78em,
  lang: "en",
  region: "US",
  contents: true,
  contents-title: "Contents",
  front: [],
  main: [],
  back: [],
) = {
  let inside = kdp-gutter-min(pages-estimate) + gutter-extra
  let b = if bleed { 0.125in } else { 0pt }

  // Level-1 headings open a piece; `<piece-end>` closes one. A page whose
  // most recent marker is an end-marker on an EARLIER page carries nothing,
  // so it gets no running head and no folio.
  let last-page-of(elems, p) = {
    let prior = elems.filter(e => e.location().page() <= p)
    if prior.len() == 0 { 0 } else { prior.last().location().page() }
  }
  let page-kind(p) = {
    let heads = query(heading.where(level: 2))
    let h = last-page-of(heads, p)
    let e = last-page-of(query(<piece-end>), p)
    if e >= h and e > 0 and e < p { "blank" } else if h == p { "opener" } else { "text" }
  }
  let running-for(p) = {
    let prior = query(heading.where(level: 2)).filter(h => h.location().page() <= p)
    if prior.len() == 0 { none } else { prior.last().body }
  }

  set document(title: title, author: author)
  set page(
    width: trim.at(0) + b,
    height: trim.at(1) + 2 * b,
    margin: (
      inside: inside,
      outside: outer-margin + b,
      top: top-margin + b,
      bottom: bottom-margin + b,
    ),
    numbering: "i",
    header: context {
      let p = here().page()
      if page-kind(p) != "text" { return none }
      let running = running-for(p)
      if running == none { return none }
      set text(font: sans, size: 8pt, tracking: 0.08em, fill: luma(25%))
      if calc.even(p) { align(left, upper(title)) } else { align(right, upper(running)) }
    },
    footer: context {
      if page-kind(here().page()) == "blank" { return none }
      let pat = page.numbering
      if pat == none { return none }
      set align(center)
      set text(font: sans, size: 9pt)
      numbering(pat, ..counter(page).get())
    },
  )

  set text(
    font: serif,
    size: font-size,
    lang: lang,
    region: region,
    hyphenate: true,
    costs: (hyphenation: 60%, widow: 300%, orphan: 300%),
  )
  set par(
    justify: true,
    leading: leading,
    spacing: leading,
    first-line-indent: (amount: 1.3em, all: false),
    linebreaks: "optimized",
  )
  set heading(numbering: none)

  // Chapter and section opener title (level 2; level 1 belongs to parts)
  show heading.where(level: 2): it => {
    set align(center)
    set par(justify: false, first-line-indent: 0pt, leading: 0.5em)
    block(width: 100%, above: 0pt, below: 2.2em, text(
      font: display,
      size: 21pt,
      weight: "semibold",
      hyphenate: false,
    )[#it.body])
  }
  // Section head inside a chapter
  show heading.where(level: 3): it => {
    set par(justify: false, first-line-indent: 0pt)
    block(above: 1.8em, below: 0.8em, text(
      font: sans,
      size: 11pt,
      weight: "semibold",
      tracking: 0.02em,
    )[#it.body])
  }
  show heading.where(level: 4): it => {
    set par(justify: false, first-line-indent: 0pt)
    block(above: 1.4em, below: 0.6em, text(size: 11pt, style: "italic")[#it.body])
  }

  show quote.where(block: true): it => pad(x: 1.4em, y: 0.4em, emph(it.body))
  show raw.where(block: true): it => block(
    width: 100%,
    inset: (x: 0.8em, y: 0.7em),
    fill: luma(96%),
    radius: 2pt,
    text(font: ("Libertinus Mono", "Menlo"), size: 9pt, it),
  )
  show figure.caption: it => text(font: sans, size: 8.5pt, fill: luma(30%), it)

  // --- Table of contents ---------------------------------------------------
  // Parts are set apart: small caps, no leader, air above. Chapters are
  // numbered continuously across the whole book -- the number is derived by
  // position, the same way the chapter opener gets it, so the two can never
  // disagree.
  show outline.entry.where(level: 1): it => {
    block(above: 1.5em, below: 0.55em)[
      #text(font: sans, size: 8.5pt, tracking: 0.16em, weight: "semibold",
            fill: luma(25%))[#upper(it.element.body)]
    ]
  }
  show outline.entry.where(level: 2): it => context {
    let i = query(<cap>).position(h => h.location() == it.element.location())
    block(above: 0.35em, below: 0pt)[
      #link(it.element.location())[
        #box(width: 1.9em)[
          #if i != none {
            align(right, text(fill: luma(35%))[#(i + 1).])
          }
        ]
        #h(0.45em)
        #it.element.body
        #box(width: 1fr, inset: (x: 0.35em), repeat[.])
        #it.page()
      ]
    ]
  }

  // ---- front matter, roman folios ----
  front-pages(
    title: title,
    subtitle: subtitle,
    author: author,
    publisher: publisher,
    copyright-year: copyright-year,
    rights: rights,
    isbn: isbn,
    edition: edition,
    series: series,
    colophon: colophon,
    sans: sans,
    display: display,
  )
  front
  if contents {
    section(contents-title, outlined: false)[
      #outline(title: none, depth: 2, indent: 0pt)
    ]
  }

  // ---- main matter restarts at arabic 1 on a recto ----
  pagebreak(to: "odd", weak: true)
  counter(page).update(1)
  set page(numbering: "1")
  main
  back
}
