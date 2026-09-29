# Arte — prompts para o Gemini

**A capa é tipográfica, sem arte**, como a de *Depois de mim*, com paleta própria em
`book.yaml`: azul-noite `#151c26`, título `#eef0f3` e fio âmbar `#d98a3d`.

**As quatro aberturas de parte** seguem **o mesmo estilo de *Depois de mim***: grafite e
nanquim, traço preciso de desenho de arquiteto, muito branco. Assim a série parece uma
série na estante. Lições de *Depois de mim* que valem aqui: nenhum rosto; um detalhe
concreto da história em cada imagem; nada que pareça marca; tudo descrito em excesso.

**Onde salvar:** `books/a-volta-a-mais/illustrations/masters/`, com os nomes
`01-arco-1.jpeg` a `04-arco-4.jpeg`. O build casa pelo nome. Depois, os originais vão
para `illustrations/originais/` e os masters são ampliados a 200% e têm o papel clareado
para branco, como em *Depois de mim*.

---

## Parte I — Vinte mil (20.000 km, 4% de g)

A imagem: a fita, larga e chata, descendo do Posto até uma Terra pequena e terminando
num ponto **dentro** do disco. No meio, as duas voltas de corda que Otávio deixou, e uma
técnica com as mãos espalmadas na face da fita, olhando para baixo.

**Versão 2 (2026-09-28).** A primeira tentativa do Gemini saiu com quatro erros:
- a fita parecia um poste, e a figura a abraçava;
- a fita cortava a Terra ao meio, com o terminador em linha reta sobre ela;
- a Terra estava grande demais;
- a figura era um astronauta de desenho animado.

O prompt abaixo corrige os quatro.

```
Create a single illustration for the opening page of Part One of a literary
science fiction novel. Read every instruction carefully; the details matter
more than the drama.

FORMAT AND MEDIUM
- Portrait orientation, aspect ratio exactly 4:5, highest resolution possible.
- Black and white only. Pure graphite pencil and fine black ink on slightly
  warm off-white drawing paper, with a faint, even paper grain visible.
- The look of a patient, precise hand drawing by an architect or scientific
  illustrator: clean confident contour lines in ink, soft tonal shading in
  graphite, fine parallel hatching and light cross-hatching. No digital
  gloss, no airbrush, no photorealism, no comic, cartoon or manga style.

THE STORY MOMENT (for your understanding, do not write it anywhere)
In the future, a single space elevator rises from a floating city in the
equatorial ocean to far beyond orbit. It is not a tower, not a cable and not a
pole: it is a flat ribbon, one metre wide and thinner than a sheet of paper,
stretched tight between the Earth and a counterweight. Twenty thousand
kilometres up, a maintenance technician has found her dead mentor tied to the
ribbon. He tied himself there, dying, with two turns of rope around the
ribbon, to mark the exact spot where the ribbon is failing. The body is gone
now; the two turns of rope are still there. She has come back to them. The
image must feel like enormous height, silence, near-weightlessness, and one
small human mark on an immense thing.

VIEWPOINT AND COMPOSITION
- We are high up, looking almost straight DOWN along the ribbon toward the
  Earth far below.
- At the very top of the image, cut off by the top edge, the underside of a
  small space station clamped onto the ribbon: a fat white cylinder seen from
  below, with two flat rectangular solar panels spread out to the sides.
- From the station, the ribbon descends through the whole image, narrowing in
  perspective, and ENDS at a single tiny vanishing point INSIDE the Earth's
  disc, slightly below the disc's centre, where it is anchored in the ocean.
  The ribbon never passes in front of the Earth and never continues past it.
- In the upper-middle of the image, on the ribbon, the two turns of rope and
  the technician. This is the focal point, roughly on the upper third line.
- In the lower part of the image, small and far away, the Earth: a circle
  occupying roughly one third of the image width, with generous white space
  around it on all sides.
- Everything else is empty. Outer space is left as the white of the paper, with
  NO stars, the way an architectural drawing leaves the sky blank.

THE RIBBON — THE MOST IMPORTANT ELEMENT
- It is a WIDE, FLAT RIBBON, like a long strip of dark film seen almost
  face-on. Near the station it is about as wide as half a person's height, and
  clearly wider than the technician's shoulders. It is NOT a thin pole, NOT a
  rod, NOT a cable, NOT a rope, NOT a tube, NOT a tower, NOT a lattice. No
  rungs, no rails, no structure: just a broad, flat, matte, dark band,
  perfectly straight and tight.
- Hard sunlight comes from the right: the right edge and a thin strip of the
  face catch dull light, and the rest of the face is dark, rendered in dense
  smooth graphite, with the faint texture of woven fibres where it is close.

THE TWO TURNS OF ROPE
- Wrapped tightly around the ribbon, a short piece of thin, grey, braided rope
  makes exactly TWO full turns around it, pressed flat against the ribbon, side
  by side. There is NO KNOT: just the two tight turns, and one short cut end
  drifting loose a little way from the ribbon, frayed at the tip.
- The rope is clearly drawn and easy to see: it is the one small, human,
  handmade thing in the whole picture.

THE TECHNICIAN — A WORKER, NOT A CARTOON ASTRONAUT
- One adult technician in a slim, modern work spacesuit, white and grey, with
  reflective bands on the arms and legs and a small, compact life-support pack
  on the back (not a big bulky backpack). A tool holster and a hooked knife are
  strapped to one thigh, and a coil of grey rope to the other.
- Realistic adult proportions, drawn with the same precision as the rest.
- Both gloved hands rest FLAT on the ribbon's face, just ABOVE the two turns of
  rope, like someone steadying themselves against a wall. The technician does
  NOT hug the ribbon and does NOT wrap arms around it.
- The body floats close to the ribbon's face, legs relaxed and slightly
  drifting away from it, because at this height a person weighs almost
  nothing.
- The helmet is turned DOWN, looking at the rope. The visor is dark and
  reflective: NO FACE visible, only a faint reflection of the ribbon.
- A thin safety line runs from a ring at the waist of the suit up along the
  ribbon to the station above.
- The figure is small in the frame, about one eighth of the image height, so
  the immensity of the ribbon dominates.

THE EARTH
- Seen from 20,000 km: a complete sphere, small, low in the frame.
- About two thirds of the disc is lit: ocean, with a few fine-line clouds and
  a thin bright rim. About one third is in night, rendered in dense hatching.
- The boundary between day and night is a soft CURVED line crossing the disc
  at an angle. It is NOT a straight vertical line, and it does NOT follow or
  touch the ribbon.
- The ribbon's vanishing point sits on the lit ocean, just below the centre.

LIGHT AND MOOD
- Hard, unsoftened sunlight from the right, with no air to diffuse it: sharp
  shadows, very high contrast on the suit and the ribbon, the station's panels
  catching the light.
- The mood is vastness, silence, stillness, grief and attention: a person paying
  close attention to one small thing in the middle of something too big to see.

STRICTLY AVOID
- No thin pole, rod, cable, rope-tower, lattice mast, rails, rungs or elevator
  car. The elevator is a wide flat ribbon only.
- No cartoon astronaut, no bulky classic spacesuit backpack, no cute
  proportions.
- No face, eyes or skin anywhere.
- No knot in the rope around the ribbon: only two turns.
- The ribbon must not cut the Earth in half, and the day-night line must not be
  straight or vertical.
- No stars, no galaxies, no Moon, no spaceships, no rockets, no lens flares.
- No text, no letters, no numbers, no logos, no flags, no signature, no
  watermark, no border, no frame around the picture.
- No colour of any kind. No sepia tint beyond the natural warmth of the paper.
```

Pontos que não podem faltar:
- **A fita** tem metade da altura de uma pessoa, é chata "como uma tira de filme" e é
  vista quase de frente. **A técnica apoia as mãos espalmadas na face, como numa
  parede**, e não a abraça.
- **A fita termina num ponto dentro do disco da Terra**, um pouco abaixo do centro, e
  nunca passa na frente dela.
- **A Terra** ocupa um terço da largura, com dois terços iluminados. O terminador é
  **curvo e inclinado** e não encosta na fita.
- **A técnica é trabalhadora**, não astronauta: traje fino branco e cinza com faixas
  refletivas, mochila compacta, coldre de ferramenta, faca de gancho numa coxa e corda
  enrolada na outra, proporções adultas. Capacete para baixo, sem rosto.
- **A corda** dá duas voltas, sem nó, com uma ponta cortada e esgarçada.

Se ainda sair poste: *"The ribbon is as wide as a door, flat like a strip of film."*

## Revisão das quatro aberturas (2026-09-28)

- **Parte I** (a fita e a Terra): boa, mas a Terra mostrava a África e a Europa, e a fita
  terminava em terra firme. **Refazer mostrando o lado do Pacífico**, só oceano, com o fim
  da fita na água do Equador. A figura continua "astronauta", mas é aceitável.
- **Parte II** (o anel da âncora): **aprovada.** Cortar a moldura desenhada.
- **Parte III** (o nicho): linda, mas tinha **texto legível em inglês** ("modified
  bowline") e cabeçalhos legíveis na tabela. **Refazer só a escrita**, trocando por
  rabiscos. A nuca e a orelha aparecem; é aceitável, porque não há rosto.
- **Parte IV:** a trava (mãos num colar de metal) **foi trocada** por decisão do autor,
  porque dizia pouco a quem não leu o livro. **Nova imagem: o nó no mar, do enterro de
  *Terra*.** As mãos de Iara fecham o lais de guia com a volta a mais na corda cinza em
  volta do pano branco; ao fundo, o mar ao pôr do sol e a fita subindo da cidade no
  horizonte. É a imagem do título. Fecha a história da corda nas quatro aberturas: marca o
  lugar (I), o cabo canta no anel (II), o nó está desenhado no caderno (III), e o nó é
  amarrado uma última vez (IV).

## Estado final (2026-09-28): as quatro aprovadas e no livro

| Parte | Página | Imagem |
|---|---|---|
| I, Vinte mil | 9 | a fita larga descendo do Posto até a Terra, só oceano (lado do Pacífico); as duas voltas de corda; a figura de traje |
| II, A Âncora | 53 | o anel da âncora no fundo do Poço, a fita subindo, uma mão nua no metal molhado |
| III, A subida | 87 | o nicho: o caderno aberto com a tabela ilegível e o nó desenhado, a caneta flutuando, a corda no pulso, sem cabeça |
| IV, A Estação | 117 | o enterro: as mãos de Iara fechando o nó na corda cinza em volta do pano branco; o mar e a fita no horizonte |

**Tratamento:** os originais do Gemini estão em `illustrations/originais/`. Os masters foram
ampliados a 200% (Lanczos), com o papel clareado para branco (`-level 0%,90%`). A
**Parte II** perdeu a moldura desenhada e **foi completada com branco nas laterais até 4:5**,
para o título cair na mesma altura das outras. A Parte IV veio em PNG e virou JPEG. Preflight
da KDP: 9/9, todas as imagens a 300 dpi ou mais e em escala de cinza.
