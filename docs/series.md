# A série

Três romances de ficção científica, **mundos separados**. Os três livros
dividem um nome de série e nada mais: nenhum personagem, tecnologia, data ou
acontecimento passa de um livro para outro. Cada `docs/<slug>/bible.md` é um
cânone independente.

## A ordem — decidido

Ordem de leitura e de publicação: **o gancho mais forte primeiro.**

| # | Livro (título de trabalho) | Pasta | Gênero |
|---|---|---|---|
| 1 | *Depois de mim* | `depois-de-mim` | ficção científica emocional; o futuro visto por quem veio de 2031 |
| 2 | *A volta a mais* | `a-volta-a-mais` | mistério com coração + ficção científica hard; lugar sem nome |
| 3 | *O que é do mar* | `o-que-e-do-mar` | solarpunk / hopepunk; clima e comunidade |

`series.number` em cada `book.yaml` segue esta tabela.

## O que os três têm em comum — decidido

- **A forma:** uma protagonista, quatro arcos, 4 partes × 4–5 capítulos.
- **As regras de *O futuro na página*** (`CLAUDE.md`).
- **O pseudônimo:** Íris Gradim, o mesmo de *Manual da Vida* e *Quarenta dias úteis*.
- **O tamanho:** o que a história pedir. A KDP exige só de 24 a 828 páginas no impresso; *Depois de mim* tem ~43.000 palavras e 186 páginas.
- **O tom:** a série sai do território de *Quarenta dias úteis*. É ficção
  científica movida por emoção e, no fim, esperançosa — é o que os leitores do
  gênero estão procurando agora.

## A decidir pelo autor

Nada em aberto.

## O nome — decidido (2026-10-03)

**What Remains** em inglês, **O que fica** em português. É o que os três livros têm em
comum: Helena fica até o fim, Iara guarda a volta a mais, Joana fica na água.

## Publicação — decidido (2026-10-03)

**Por enquanto, só as edições em inglês vão para a KDP**, como a série *What Remains*
(1 *After Me*, 2 *The Extra Turn*, 3 *What Belongs to the Sea*), com a amazon.com como
loja principal. As edições em português ficam prontas e saem depois, como série
própria (*O que fica*): na KDP, uma série reúne livros de uma língua só. `make
release-en` constrói e confere só as três em inglês.
