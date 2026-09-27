# Arte — prompts para o Gemini

**Estado:** as quatro aberturas de parte estão prontas e no livro. **A capa não
terá arte, por decisão do autor**: é tipográfica, gerada pelo build a partir do
`shared/print/cover.typ`, com as cores do bloco `cover:` de `book.yaml`
(ardósia `#2c3a45`, título `#eef1f2`, fio `#9fb8c8`). O prompt de capa abaixo
fica só como registro. Os originais do Gemini estão em
`illustrations/originais/`; as versões `-v1` foram recusadas (III tinha uma
mulher sem cabeça atrás do balcão; IV tinha botas masculinas e de marca). Os
masters foram ampliados a 200% com Lanczos e tiveram o papel clareado para
branco (`-level 0%,90%`); III também perdeu a moldura desenhada.

Cinco imagens: a capa e as quatro aberturas de parte. As aberturas **abrem sem
epígrafe** (decisão do autor), então a imagem é a única coisa na página além do
título da parte.

## Onde salvar

Salvar em `books/depois-de-mim/illustrations/masters/` com estes nomes exatos.
O build casa pelo nome e gera o resto (escala de cinza e 300 dpi para o miolo,
RGB reduzido para o EPUB):

| Arquivo | O que é | Formato pedido ao Gemini |
|---|---|---|
| `cover.png` | capa (frente) | retrato 1600 × 2560 px (1 : 1,6), colorida |
| `01-arco-1.jpg` | abertura da Parte I — O despertar | retrato 4 : 5, pelo menos 2000 × 2500 px |
| `02-arco-2.jpg` | abertura da Parte II — O pertencimento | idem |
| `03-arco-3.jpg` | abertura da Parte III — O motivo | idem |
| `04-arco-4.jpg` | abertura da Parte IV — A escolha | idem |

Depois de salvar: `make BOOK=depois-de-mim` e `make check BOOK=depois-de-mim`.

**Capa impressa:** o `shared/print/cover.typ` ainda monta a capa de papel com
cores chapadas. Quando `cover.png` existir, é preciso adaptar a frente da
capa impressa para usar a imagem, com sangria de 0,125 pol. Hoje só o EPUB usa
`cover.png`.

## Regras para todas as imagens

Estão no fim de cada prompt, em inglês, porque o Gemini obedece melhor assim:

- **Sem texto, letras, números legíveis, logotipos ou marca d'água.** O título e o
  nome da autora são compostos pelo build.
- **Nenhuma cidade real, marco reconhecível, bandeira ou marca.** A cidade do
  livro não tem nome nem país.
- **Não é cyberpunk:** sem neon, sem chuva roxa, sem letreiros. O futuro do livro
  é verde, úmido, calmo, feito contra o calor e a água.
- **As quatro aberturas são uma série:** mesma técnica, mesmo papel, mesmo traço.

---

## Capa

```
A quiet literary science-fiction book cover illustration, portrait 1600x2560.
Close-up of two hands resting together on a wool blanket: a young woman's
right hand, smooth and unmarked, completely without scars, holding a very old
woman's hand — thin, translucent skin, many age spots, blue veins, a loose
gold wedding ring stuck on the knuckle. Soft natural daylight from a large
floor-to-ceiling window behind them. Through the window, slightly out of
focus: a future city built against heat and rain — buildings with meadow-green
living roofs, wide open rain gutters running diagonally down the facades like
streams, pale milky covered walkways bridging between buildings at the tenth
floor, heavy straight rain falling. Muted palette: rain-grey, soft blue, warm
skin tones, a little moss green. Painterly, delicate, realistic lighting,
intimate, melancholic but tender, lots of calm negative space in the top third
for a title and at the bottom for an author name.
No text, no letters, no numbers, no logo, no watermark, no border, no frame.
No recognizable real city, landmark, flag or brand. Not cyberpunk: no neon,
no signs, no purple glow, no flying cars.
```

## Parte I — O despertar

Imagem-chave: as mãos. Helena acorda e olha as mãos, que são dela e não têm a
cicatriz.

```
Fine graphite and ink illustration on white paper, black and white only,
portrait 4:5. Two open hands of a young woman, palms up, seen from her own
point of view as if she is looking down at them for the first time. The skin
is perfectly smooth, like new, with no scars, no lines. Above, the suggestion
of a seamless curved ceiling that glows softly from within, with one single
barely-visible hairline seam. Very generous white space, quiet, clinical,
tender. Delicate hatching, precise architectural line quality.
No text, no letters, no numbers, no watermark, no border. No color.
```

## Parte II — O pertencimento

Imagem-chave: a cidade que anda em cima. Uma pessoa atravessa uma passarela sem
olhar para cima.

```
Fine graphite and ink illustration on white paper, black and white only,
portrait 4:5, same style as a series of architectural drawings. A future city
seen from slightly above: a thin pale covered walkway spanning about forty
metres between two buildings with no visible supports, no cables, no pillars.
Many small people walk on it; one woman in a wide-brimmed hat walks in the
middle, not looking up. Below, the street is empty and flooding on purpose
with rain; round cistern openings in the pavement. Buildings with living
meadow roofs and wide diagonal rain gutters on the facades. Calm, orderly,
airy, lots of white space. Delicate hatching, precise line.
No text, no letters, no numbers, no signs, no watermark, no border. No color.
No recognizable real city or landmark. Not cyberpunk.
```

## Parte III — O motivo

Imagem-chave: os catorze minutos. O relógio da sorveteria, das onze às onze e
catorze, e um sorvete de flocos que uma menina de seis anos tomou sem saber.

```
Fine graphite and ink illustration on white paper, black and white only,
portrait 4:5, same style as the series. An old-fashioned round analogue wall
clock with hands pointing to 11:14, on a plain wall above a long ice-cream
shop counter. On the counter, a small glass cup of chocolate-chip ice cream,
half eaten, a spoon resting in it, melting. Beside it, a child's small hand on
the counter edge, and two loose uneven braids just entering the frame. An
adult's hands folded tightly nearby, not eating. Morning light. Still,
suspended, heartbreaking but quiet. Delicate hatching, lots of white space.
No text, no letters, no numerals on the clock face (use simple tick marks),
no brand names, no watermark, no border. No color.
```

## Parte IV — A escolha

Imagem-chave: o sapato em pé, com a ponta para dentro. Ao lado das botas de obra
de Helena, no corredor de casa.

```
Fine graphite and ink illustration on white paper, black and white only,
portrait 4:5, same style as the series. The floor of a quiet apartment hallway
next to a front door. A pair of muddy work boots standing side by side, and
right next to them one single small child's canvas shoe with a velcro strap,
old and worn, standing upright, carefully aligned, its toe pointing inward,
into the home, away from the door. Soft late-evening light across the floor.
Tender, hopeful, very still. Delicate hatching, lots of white space.
No text, no letters, no numbers, no brand, no watermark, no border. No color.
```

## Se o Gemini errar

- **Se aparecer texto**, repetir o pedido acrescentando no começo: *"Absolutely no
  text or lettering of any kind."*
- **Se a capa ficar cyberpunk**, acrescentar: *"Style reference: quiet European
  literary fiction covers, soft daylight, like a watercolour."*
- **Se as quatro aberturas não combinarem**, gerar a da Parte I primeiro e anexar
  essa imagem às outras três como referência de estilo: *"Match exactly the style,
  paper and line of the attached image."*
