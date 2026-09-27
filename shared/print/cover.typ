// KDP full-wrap paperback cover: back cover + spine + front cover on one
// page, with 0.125in bleed on every outside edge.
//
//   width  = bleed + trim + spine + trim + bleed
//   height = bleed + trim height + bleed
//
// Spine width comes from the interior page count (0.0025in per page on cream
// stock, 0.002252in on white) and is computed by scripts/build.py, so this
// file only ever receives a finished measurement.
//
// This is a working starting point, not a finished jacket. Replace the flat
// fills with artwork when you have it; the geometry and safe areas stay right.

#let bleed = 0.125in

// The front panel, shared by the printed wrap and the eBook cover so the two
// can never drift apart. Everything that differs between them -- panel size,
// how far the title drops, how far the author sits off the foot -- arrives as
// an argument; nothing about the design does.
#let front-panel(
  title: "",
  subtitle: none,
  author: "",
  series: none,
  w: 5.5in,
  h: 8.5in,
  inset: 0.25in,
  top-drop: 1in,
  author-lift: 0.6in,
  side-trim: 0.625in,
  title-size: 34pt,
  subtitle-size: 13pt,
  author-size: 13pt,
  accent: rgb("#c8a44a"),
  serif: ("Libertinus Serif", "Georgia"),
  sans: ("Libertinus Sans",),
  display: ("Libertinus Serif Display", "Libertinus Serif"),
) = block(width: w, height: h)[
  #place(top + left, dx: inset, dy: top-drop, block(width: w - side-trim)[
    #align(center)[
      #if series != none [
        #text(font: sans, size: 8pt, tracking: 0.26em, fill: accent)[
          #upper(series)
        ]
        #v(2.2em)
      ]
      #text(font: display, size: title-size, weight: "semibold")[#title]
      #if subtitle != none [
        #v(1.1em)
        #line(length: 22%, stroke: 0.6pt + accent)
        #v(1.1em)
        #text(font: serif, size: subtitle-size, style: "italic")[#subtitle]
      ]
    ]
  ])
  #place(bottom + center, dy: -author-lift, text(
    font: sans,
    size: author-size,
    tracking: 0.18em,
  )[#upper(author)])
]

// The eBook cover: the same front panel on a single 1:1.6 page, which is the
// shape KDP asks for (1600 x 2560). No bleed and no trim, because nothing is
// cut -- so the panel gets the whole page and a slightly larger title.
#let ebook-cover(
  title: "",
  subtitle: none,
  author: "",
  series: none,
  bg: rgb("#1d2b2b"),
  ink: rgb("#f4f1ea"),
  accent: rgb("#c8a44a"),
  serif: ("Libertinus Serif", "Georgia"),
  sans: ("Libertinus Sans",),
  display: ("Libertinus Serif Display", "Libertinus Serif"),
  body,
) = {
  let w = 5.5in
  let h = 8.8in
  set page(width: w, height: h, margin: 0pt, fill: bg)
  set text(font: serif, fill: ink, hyphenate: false)
  front-panel(
    title: title, subtitle: subtitle, author: author, series: series,
    w: w, h: h, inset: 0.4in, top-drop: 1.5in, author-lift: 1in,
    side-trim: 0.8in, title-size: 40pt, subtitle-size: 15pt, author-size: 14pt,
    accent: accent, serif: serif, sans: sans, display: display,
  )
  body
}

#let kdp-cover(
  title: "",
  subtitle: none,
  author: "",
  blurb: "",
  series: none,
  trim: (6in, 9in),
  spine: 0.5in,
  pages: 0,
  guides: true,
  bg: rgb("#1d2b2b"),
  ink: rgb("#f4f1ea"),
  accent: rgb("#c8a44a"),
  serif: ("Libertinus Serif", "Georgia"),
  sans: ("Libertinus Sans",),
  display: ("Libertinus Serif Display", "Libertinus Serif"),
  body,
) = {
  let tw = trim.at(0)
  let th = trim.at(1)
  let full-w = 2 * tw + spine + 2 * bleed
  let full-h = th + 2 * bleed
  // KDP requires text and logos to stay 0.25in clear of trim edges, and the
  // spine only takes text at all once the book is 79+ pages.
  let safe = 0.25in + bleed

  set page(width: full-w, height: full-h, margin: 0pt, fill: bg)
  set text(font: serif, fill: ink, hyphenate: false)

  place(top + left, dx: 0pt, dy: 0pt, block(width: full-w, height: full-h)[
    // ---------------- back cover ----------------
    #place(top + left, dx: safe, dy: safe, block(
      width: tw - 2 * 0.25in - bleed,
      height: th - 2 * 0.25in,
    )[
      #if series != none [
        #text(font: sans, size: 8pt, tracking: 0.24em, fill: accent)[
          #upper(series)
        ]
        #v(1.4em)
      ]
      #set par(justify: false, leading: 0.72em, spacing: 1.45em)
      // The blurb arrives as one string per paragraph, because a newline
      // inside a typst string prints as a hard line break and not as a space:
      // handing over the whole description in one string reproduces the line
      // breaks of book.yaml on the printed cover.
      #let paragraphs = if type(blurb) == str { (blurb,) } else { blurb }
      #text(font: serif, size: 11pt)[
        #for p in paragraphs [#par(p)]
      ]
      #v(1fr)
      // The bottom-right 2 x 1.2in must stay free of text and artwork: KDP
      // prints the barcode there and it will cover whatever is underneath.
      // The area does not need to be white -- the background runs through, and
      // the barcode arrives on its own patch. So this rectangle is a guide and
      // is drawn only while guides are on; with them off it leaves no mark.
      #place(bottom + right, rect(
        width: 2in,
        height: 1.2in,
        fill: if guides { white } else { none },
        stroke: if guides { (paint: red, dash: "dashed", thickness: 0.5pt) } else { none },
      )[
        #if guides [
          #align(center + horizon, text(size: 7pt, fill: red, font: sans)[
            barcode area \ (keep clear)
          ])
        ]
      ])
    ])

    // ---------------- spine ----------------
    #place(top + left, dx: bleed + tw, dy: 0pt, block(
      width: spine,
      height: full-h,
      fill: bg.darken(12%),
    )[
      #if pages >= 79 [
        #place(center + horizon, rotate(90deg, reflow: false, block(width: th - 1in)[
          #align(center, text(font: display, size: 11pt, weight: "semibold")[
            #title
            #h(1.2em)
            #text(font: sans, size: 8.5pt, tracking: 0.1em, fill: accent)[
              #upper(author)
            ]
          ])
        ]))
      ]
    ])

    // ---------------- front cover ----------------
    #place(top + left, dx: bleed + tw + spine, dy: 0pt, front-panel(
      title: title, subtitle: subtitle, author: author, series: series,
      w: tw, h: full-h, inset: 0.25in, top-drop: safe + 0.6in,
      author-lift: safe + 0.3in, side-trim: 2 * 0.25in + bleed,
      accent: accent, serif: serif, sans: sans, display: display,
    ))

    // ---------------- production guides ----------------
    #if guides [
      #let g = (paint: rgb("#ff3b30"), thickness: 0.5pt, dash: "dashed")
      // trim lines
      #place(top + left, dx: bleed, line(angle: 90deg, length: full-h, stroke: g))
      #place(top + left, dx: bleed + tw, line(angle: 90deg, length: full-h, stroke: g))
      #place(top + left, dx: bleed + tw + spine, line(angle: 90deg, length: full-h, stroke: g))
      #place(top + left, dx: full-w - bleed, line(angle: 90deg, length: full-h, stroke: g))
      #place(top + left, dy: bleed, line(length: full-w, stroke: g))
      #place(top + left, dy: full-h - bleed, line(length: full-w, stroke: g))
      #place(top + left, dx: bleed + 0.06in, dy: bleed + 0.06in, text(
        size: 6pt,
        fill: rgb("#ff3b30"),
        font: sans,
      )[
        #pages pp · spine #calc.round(spine / 1in, digits: 4)in · full #calc.round(full-w / 1in, digits: 3)in × #calc.round(full-h / 1in, digits: 3)in · GUIDES ON — set cover_guides: false before upload
      ])
    ]
  ])

  body
}
