# Série de ficção científica — três romances

Manuscrito em Markdown; EPUB pronto para a KDP e PDF pronto para impressão do
outro lado. Mesma cadeia de ferramentas de *Quarenta dias úteis* e do
*Manual da Vida*.

    make deps                        # uma vez, no macOS
    make                             # constrói o livro 1
    make BOOK=a-volta-a-mais         # constrói outro livro
    make books                       # constrói os três
    make check BOOK=recife-submersa  # preflight contra o que a KDP recusa

| # | Livro (título de trabalho) | `BOOK=` |
|---|---|---|
| 1 | Depois de mim | `depois-de-mim` |
| 2 | A volta a mais | `a-volta-a-mais` |
| 3 | Recife submersa | `recife-submersa` |

## Layout

    books/<slug>/
      book.yaml              metadados, formato, número na série, anúncio na KDP
      front/                 o que vier antes             (fólios romanos)
      chapters/              o romance                    (fólios arábicos)
      parts/                 aberturas das 4 partes (os 4 arcos)
      back/                  o que vier depois
      illustrations/masters/ originais em alta, um por parte
    docs/
      series.md              o que é da série: nome, ordem, forma comum
      kdp-upload.md          o passo a passo do upload
      <slug>/
        outline.md           premissa, os 4 arcos, fonte única dos capítulos
        bible.md             o mundo daquele livro
        timeline.md          a cronologia, incluindo a história do futuro
        references.md        a ciência real, e onde foi conferida
      _modelo/               os quatro arquivos em branco, para um livro novo
    shared/                  template de impressão, capa, CSS do EPUB, fontes
    scripts/                 build, gates, digest, stats, scaffolders

Um quarto livro: `make new-book SLUG=<slug> TITLE="..."`.
