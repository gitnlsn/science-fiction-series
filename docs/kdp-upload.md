# Uploading to KDP

What the build produces, and what each field on the KDP form wants. Run
`make release` first: it builds everything and preflights it.

    dist/<slug>/<slug>.epub            -> Kindle eBook, "Manuscript"
    dist/<slug>/<slug>-interior.pdf    -> Paperback, "Manuscript"
    dist/<slug>/<slug>-cover.pdf       -> Paperback, "Book Cover" (upload a PDF)

## Before you upload the cover

Set `cover_guides: false` in `book.yaml` and rebuild. The guides are trim
lines and a barcode keep-clear box — production aids, not artwork. `make check`
fails loudly while they are on.

## Paperback setup, matched to book.yaml

| KDP field | Comes from | Notes |
|---|---|---|
| Trim size | `print.trim` | Changing it changes the cover width; rebuild both files |
| Bleed | `print.bleed` | "No bleed" unless art runs to the page edge |
| Paper type | `print.paper` | Drives spine width: cream 0.0025 in/page, white 0.002252 |
| Interior | `print.interior` | `bw` keeps printing costs low and requires grayscale art |
| Cover finish | — | Matte suits illustrated non-fiction; gloss pops more on a thumbnail |

Hard limits the checker enforces: 24 pages minimum, 828 maximum, an even page
count, embedded fonts, 300 dpi images, and grayscale images in a
black-and-white interior.

## eBook setup

- **Manuscript**: the EPUB. KDP converts it; it is not a fixed-layout book.
- **Cover**: KDP wants a separate 1600×2560 JPEG for the eBook. The build
  makes one at `dist/<slug>/epub/img/cover.jpg` from
  `illustrations/masters/<epub.cover>`. With no such file it typesets the
  cover from `shared/print/cover.typ` instead, using the same front panel as
  the printed wrap — a finished cover for a text-only edition, not a stand-in.
- **Keywords**: the 7 in `kdp.keywords`. They also become `dc:subject` in the
  EPUB, so the two never drift apart.
- **Description**: `kdp.description`. KDP accepts limited HTML; plain
  paragraphs are safest.
- **ISBN**: leave `isbn` blank to take the free KDP identifier. A paperback
  gets a free KDP ISBN; eBooks get an ASIN and need none. Buy your own only if
  you want the same ISBN across other distributors.

## Series

Fill in `series.name` and `series.number`. They go into the EPUB as
`belongs-to-collection` / `group-position`, print on the title page and cover,
and are what you type into KDP's series fields.

## Then check it in Kindle Previewer

Amazon's own renderer catches things epubcheck cannot (bad page breaks, images
that swamp a phone screen). Free, Mac and Windows:
<https://kdp.amazon.com/help?topicId=G202131170>. Open the EPUB, then look at
a phone, a tablet and an e-ink profile.

## Proof the paperback

Order a printed proof before pressing publish. Screen and paper disagree about
gutter, margin and how dark an illustration reads at 300 dpi on cream stock.

---

## Conteúdo gerado por IA — o que a KDP exige

Este livro foi escrito com contribuição intensa de IA, e isso muda três campos
do formulário. Nenhum deles é opcional.

### 1. Autoria: um humano ou um pseudônimo

O campo de autor recebe **o seu nome ou um pseudônimo seu**. Não se credita
"Claude", "Anthropic" nem "inteligência artificial" como autor ou coautor — para
a plataforma e para a lei, quem publica é o responsável pelo conteúdo, pela
qualidade e pela veracidade dele.

**Se o nome no livro for de outra pessoa real**, essa pessoa passa a ser a
responsável legal pelo que está publicado, e precisa concordar com isso de forma
explícita. Um pseudônimo evita a questão inteira e é aceito sem restrição. É o
caminho recomendado se a intenção é apenas não usar o próprio nome.

O campo `author:` em `book.yaml` traz o pseudônimo **Íris Gradim**, e é dele que
saem a capa, a folha de rosto, a página de créditos e os metadados do EPUB. O
mesmo nome está em `back/01-sobre-a-autora.md`; trocar um sem trocar o outro
publica o livro com dois autores.

### 2. A declaração de IA: marcar "sim"

Na configuração do livro existe a seção **"Conteúdo gerado por inteligência
artificial (IA)"**. A resposta aqui é **sim**, e é preciso indicar que o texto
foi gerado por IA — e também a capa e as ilustrações, se elas forem geradas.

A regra da plataforma é ampla de propósito: se a IA produziu o rascunho ou os
blocos de texto iniciais, aquilo conta como conteúdo gerado por IA **mesmo que
tenha havido edição humana pesada depois**. Omitir isso viola os termos de
serviço e pode custar a conta.

Essa marcação é de controle interno da plataforma: o leitor não vê aviso de IA na
página de vendas. **Este livro conta ao leitor de todo modo, em "Antes de
começar"**, e essa é uma escolha editorial e não uma exigência — feita porque o
capítulo 4 pede que o leitor pergunte quem fez o que ele está lendo.

### 3. Direitos: "detenho os direitos autorais e de publicação"

No formulário, selecionar **"Eu detenho os direitos autorais e os direitos de
publicação necessários"**. Não selecionar domínio público — essa opção é para
obras históricas.

Vale entender a nuance jurídica, que corre em paralelo às regras da plataforma:
na legislação americana e na de vários outros países, **texto puramente gerado
por máquina não recebe proteção de direito autoral**. O que é protegível é a
contribuição criativa humana — a estrutura da obra, o que foi reescrito, as
decisões editoriais, o material original acrescentado. Na prática isso significa
que a obra é comercializável e que a proteção sobre o texto bruto é mais fraca do
que a de um livro escrito à mão.

Para este projeto isso tem uma consequência prática: **a parte humana do livro é
também a parte protegível.** As cenas de abertura dos capítulos, as decisões de
estrutura e as escolhas de registro não são apenas o que faz o livro ser bom —
são o que faz dele uma obra sua.

### 4. Qualidade: a exigência que derruba livros declarados

Declarar corretamente não basta. A plataforma bloqueia livro gerado por IA que
tenha informação falsa, formatação ruim ou aparência de spam, e alucinação de IA
em citação, número ou data é exatamente o tipo de defeito que caracteriza isso.

Este repositório tem três travas para isso, e todas devem estar limpas antes de
publicar:

    make marcadores  # nenhuma citação, número ou data sem verificação
    make fios        # nenhuma promessa sem pagamento
    make check       # preflight de formato e de imagem

E a checagem que nenhuma ferramenta faz: ler o PDF inteiro, em papel se possível,
uma vez, antes de subir.

## Decisão sobre a capa — 1ª edição

**Esta edição sai sem arte de capa.** A capa é tipográfica: título, subtítulo,
autora e lombada, compostas pelo `shared/print/cover.typ`, sem imagem. A capa
do eBook sai do mesmo arquivo e do mesmo painel, de modo que as duas não podem
divergir.

Isso é uma escolha e não uma pendência. Não gerar `illustrations/masters/cover.png`
não bloqueia o build nem a submissão: a KDP exige uma capa full-wrap com sangria
e a nossa atende. Se uma edição futura quiser arte, é só colocar o arquivo com
esse nome e reconstruir.

`cover_guides` fica em `false` para a versão de envio. Só volte a `true` para
conferir margens de sangria e a área do código de barras.

## Ficção, especificamente

Alguns campos do formulário se comportam de outro jeito quando o livro é um
romance:

- **Categorias** — a KDP dá três. As de ficção são profundas e específicas
  (Ficção > Ficção Científica > Distopia), e uma categoria específica com pouca
  concorrência vende mais que uma genérica. As três de `book.yaml` são um ponto
  de partida.
- **Aviso de ficção** — a página de créditos já traz "Esta é uma obra de ficção.
  Nomes, personagens, empresas, instituições e acontecimentos são produto da
  imaginação do autor ou usados de forma fictícia." Vem do `colophon:` em
  `book.yaml`. Não remova: é o que separa o livro de uma alegação sobre pessoas
  reais.
- **Sinopse** — escreva depois que a Parte I estiver em `draft`. Uma sinopse
  escrita antes do romance descreve o romance que você planejou.
- **Idade e conteúdo** — a KDP pergunta se há conteúdo adulto. Uma distopia
  administrativa em geral não tem, mas responda pelo livro que existir.
