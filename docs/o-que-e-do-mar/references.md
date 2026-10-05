# Referências

O que é **real** neste livro. Tudo o que é inventado mora em `docs/bible.md`.

Ficção científica é lida por gente que confere. Toda ciência, engenharia ou
fato histórico que o livro afirma é conferido aqui — ou marcado `[[?fato: …]]`
na prosa, e `make marcadores` cobra. Extrapolar é o gênero; errar o presente
não é. O livro pode inventar um motor, mas não pode errar a gravidade de Marte.

Nunca reconstruir de memória um número, uma constante, um procedimento ou uma
citação.

---

## Como usar

- `[core]` marca o que sustenta a espinha do livro.
- `[care]` marca achado contestado, especulativo ou que não replicou. **Nunca
  usar um trabalho `[care]` sem a ressalva junto.**
- Cada entrada registra **o que a fonte diz de fato**, com localização.

Formato:

    ### Autor, *Título* (ano) [core]
    O que a fonte diz, na parte que o livro usa. Localização: cap./p./seção.
    Usado em: capítulo "Título".

---

## Direitos e permissões

Letra de música e texto protegido: não imprimir sem licença. Mesmas regras de
*Quarenta dias úteis* — ver o `docs/references.md` daquele livro.

## Ciência e tecnologia

### IPCC AR6 WG1, projeções de nível médio do mar global (2021) [core]
Faixa *provável* para 2100, relativa a 1995–2014: SSP2-4.5, 0,44–0,76 m; SSP5-8.5,
0,63–1,01 m. **Para 2090 (cap. 9, tab. 9.9), mediana (faixa provável):** SSP1-2.6 0,39 m
(0,30–0,54); SSP2-4.5 0,48 m (0,38–0,65); SSP3-7.0 0,56 m (0,46–0,74); SSP5-8.5 0,63 m
(0,52–0,83); SSP5-8.5 de baixa confiança (calotas) 0,71 m (0,52–1,30). Taxa 2080–2100: 5,2 /
7,7 / 10,4 / 12,1 mm/ano. De 2061 a 2090: ~15 cm (SSP1-2.6), ~22 (SSP2-4.5), ~32 (SSP5-8.5);
"um palmo" desde 2061 é a mediana do SSP2-4.5. Na costa somam-se a impressão regional
(costas tropicais um pouco acima da média) e o movimento do solo; em aterro sobre mangue a
subsidência (1–2 cm/ano) pode passar a subida do mar — é por isso que o chão do Baixo está
~1,3 m abaixo de onde foi aterrado (ver `bible.md`, *As cotas*). Os 13 cm da casa da Ilda levam
~17 anos a 7,7 mm/ano. Fonte: IPCC AR6 WG1, Box TS.4 Fig. 1 e Fig. 9.25
(ipcc.ch/report/ar6/wg1). **A prosa não dá número absoluto**; "um palmo" entre 2061 e
2090 (~20–25 cm) cabe na faixa alta. Uma cidade baixa alaga de vez pela soma de subida do
mar, subsidência do solo e marés extremas — não pela subida sozinha.
Usado em: *A maré grande*.

### Marés de sizígia e equinociais [core]
As maiores marés vêm um ou dois dias depois da lua nova ou cheia, e as maiores do ano
perto dos equinócios. Ressaca (sobre-elevação por vento e pressão) soma-se à maré
astronômica e pode atrasar o pico. Lua nova de 2090 calculada para ~30/03 (fase média;
conferir com efeméride antes do final). Usado em: *A maré grande*.
**Conferido (2026-10-05, Espenak, AstroPixels 2001–2100, com PyEphem):** lua nova
31/03/2090 03:49 UT = **00:49 em UTC−3** (com eclipse solar parcial); lua cheia 15/03/2090
23:43 UT; equinócio 20/03/2090 ~03:01 UT; lua nova 20/03/2091 03:47 UT = 00:47 local. Em
31/03/2090 a maré é de sizígia, mas **de apogeu** (~401.800 km): a maior de março foi
~16–17/03, a do ano ~23–25/09/2090 (lua nova no perigeu, com eclipse solar total). O livro
diz "maré de sizígia alta, perto do equinócio; a ressaca fez dela a pior". Outras fases:
lua cheia 13/05/2090 19:02 UT; lua nova 27/07/2090 01:20 UT (26/07 local); lua cheia
07/11/2090 09:06 UT; lua nova 17/06/2091 02:42 UT (16/06 local); lua cheia de perigeu em
01/06/2091. A maré semidiurna atrasa **~50 min por dia**; o livro ancora na preamar prevista
das 23h52 de 31/03/2090. astropixels.com/ephemeris/phasescat/phases2001.html

### EurOtop, *Manual on wave overtopping of sea defences* (2018) [core]
Galgamento medido em L/s por metro de muralha. Ordens de grandeza para pessoas e
estrutura: décimos de L/s/m são respingo; ~10 L/s/m já é perigoso para pedestre; dezenas
a centenas danificam o tardoz da muralha. A borda livre (crista menos nível da água)
manda no galgamento: com ondas de ~4 m, 40 cm de borda livre é quase nada.
Usado em: *A maré grande*.
**Conferido (2026-10-05).** Pessoas (2018, tab. 3.3): na crista, 0,3 L/s/m com Hm0 = 3 m;
1 com 2 m; 10–20 com 1 m; em muralha vertical com galgamento violento, **nenhum acesso**.
Propriedade (2007, tab. 3.4): **0,4 = dano a equipamento a 5–10 m da muralha**; 1 = elementos
de edificação; 10 = afunda barco pequeno; 50 = dano sério. Estrutura (2007, tab. 3.5):
crista e tardoz bem protegidos, sem dano até **50–200**. Não existe "0,4 = respingo". A fala
de Joana: "Quatro décimos, com onda desse tamanho, já é proibido ficar em cima. Com dez,
derruba um homem. Com cinquenta, cem, começa a estragar o que está atrás."
**Muralha vertical (2018, eq. 7.1):** q/√(g·Hm0³) = 0,047·exp[−(2,35·Rc/Hm0)^1,3]. Com a onda
no pé limitada pela profundidade (H ≈ 0,6–0,8·d):
- 31/03/2090: água parada +2,6, H ≈ 2 m, Rc = 1,6 → **~43 L/s/m** (o livro diz 42); com a crista
  de 5,00 (Rc = 2,4) → ~9 L/s/m, um quinto; com o dique de 6,00, Rc = 3,4.
- 21/03/2091: água parada +2,7, Rc = 1,5, H ≈ 1,4–1,5 m depois do recife → **~9–13 L/s/m** (o
  livro diz 11).
overtopping-manual.com; kennisbank-waterbouw.nl/DesignCodes/EurOtop.pdf

### Comportas de setor [core]
Portão em fatia de cilindro que gira num eixo e se deita no fundo do canal quando aberto
(o tipo da barreira do Tâmisa, em Londres, é uma variante rotativa). Projetado para carga
de um lado; carga dos dois lados com impacto de onda é condição fora de projeto.
Usado em: *A maré grande*.

### Destiladores solares de bacia (solar stills) [core]
Bacia rasa enegrecida com água salgada sob vidro inclinado; rendimento típico de 2–5
L/m²/dia em clima tropical com sol, muito menos em dia nublado. O livro usa ~3 L/m²/dia
(900 L em ~300 m²). Usado em: *Os que ficaram*, *Água doce*.
**Conferido (2026-10-05).** Bacia simples: eficiência 30–45%, **1–4 L/m²/dia** em bom sol
tropical, ~1–1,5 nublado; teto teórico ~9. 900 L em 300 m² = 3 L/m²/dia: alto, dentro da
faixa. Osmose reversa: 2,5–4 kWh/m³ em planta grande, ~4–10 em pequena com fotovoltaico — os
900 L/dia caberiam em ~1 kWp, mas pedem membrana, pré-filtragem e bomba de alta pressão, que o
Baixo não tem. ScienceDirect S0011916411002608; Joule 2024, S2542435124003738.

### Estabilidade de flutuantes [core]
Um flutuante volta à posição enquanto o metacentro fica acima do centro de gravidade; carga
alta e que se desloca (água solta, caixa que escorrega) reduz a altura metacêntrica. Lastro
baixo e boca larga aumentam a estabilidade. **Mas numa plataforma larga e rasa o que vira
não é a altura metacêntrica** (BM = B²/12T ≈ 12 m para 5 m de boca e 0,17 m de calado;
~50 t·m/rad de endireitamento para ~5 t): é a **falta de borda livre**. 500 L em ~30 m²
afundam ~1,6 cm. Uma caixa meio cheia tem superfície livre, que reduz a estabilidade. Usado em: *O estaleiro*, *A primeira jangada*.

### Casas anfíbias e flutuantes em postes-guia [core]
Casas sobre flutuadores presas a postes verticais por argolas que correm sobem e descem com a
água; existem na Holanda (ex.: Maasbommel, 2005). Usado em: *A primeira jangada* em diante.

### Subsidência de pôlderes e solos orgânicos drenados [core]
Solo turfoso ou de mangue drenado desce por oxidação e adensamento, da ordem de 1–2 cm/ano
em muitos casos; pôlderes exigem bombeamento perpétuo. Usado em: *A conta*.

### Efeito de borda de diques e perda de armazenamento [core]
Fechar uma área de inundação remove armazenamento e pode elevar o nível em áreas vizinhas
desprotegidas; extremidades de estruturas costeiras concentram escoamento. Usado em: *A conta*.

### Recifes de ostra e mangue como defesa costeira ("linhas de costa vivas") [core]
Recifes submersos e faixas de mangue reduzem a altura e a energia das ondas, mais quanto mais
largos e mais rasa a água; não reduzem a maré. Eficácia cai com água funda sobre o recife.
Ostras recrutam em qualquer substrato duro na zona entremarés em meses. Usado em: *O recife*,
*Mangue*, *A grande maré*.
**Conferido (2026-10-05).** Narayan et al., *PLoS ONE* 11(5): e0154735 (2016), 69 medições de
campo: recife de coral −70% na altura de onda (54–81), marisma −72%, **mangue −31%** (25–37);
sem medições de campo em recife de ostra. Ferrario et al., *Nat. Commun.* 5:3794 (2014):
recifes dissipam ~97% da energia; quebra-mar tropical US$ 19.791/m × restauração de recife US$
1.290/m. McIvor et al. (2012, TNC/Wetlands International): 100 m de mangue, −13–66%. Nenhum
dos três segura a maré nem a sobre-elevação lenta. Por isso o livro diz que o recife tira
mais, e "o mangue, atrás, tirava mais um tanto".

### Propágulos de mangue vermelho (*Rhizophora*) [core]
Viviparidade: o propágulo se desenvolve na árvore e cai pronto para fincar na lama. Plantio
manual por propágulos é prática comum de restauração. Usado em: *Mangue*.

### Institutas de Justiniano, 2.1.1 (533) [core]
"Por direito natural são comuns a todos: o ar, a água corrente, o mar e, por isso, as praias
do mar." Origem da doutrina do domínio público costeiro (*public trust*). A Lei da Orla de
Thalassa é inventada; a ideia é esta. Usado em: *O que é do mar*; *Sobre a autora*.


### Conferido na revisão de 2026-10-05 (o resto)

- **Ressaca numa costa sem ciclone:** sobre-elevação de 0,3 a 1,5 m por vento e pressão; o pico
  atrasa. **Perigeu e apogeu** mudam a sizígia em ~20%.
- **O datum legal da preamar:** a média se faz sobre uma época de 18,6 anos; uma série curta
  é corrigida contra um marégrafo de controle — é o que torna críveis o caderno do Nilo (dentro
  de 3 cm da torre) e os "17 dias" do levantamento oficial.
- **Flutuação:** tambor de 200 L dá ~0,2 m³; isopor de câmara fria, densidade ~15–30 kg/m³.
  Oitenta tambores dão ~16 t de empuxo, contra ~4,5 t de sessenta pessoas e ~5 t de deque e
  teto.
- **Água (Sphere):** 2,5–3 L por pessoa por dia só para beber; mais 3–6 para cozinhar.
- **Doença depois de enchente:** leptospirose e diarreia são as de livro-texto (958 casos de
  leptospirose em três meses nas enchentes do RS de 2024; PMC12030144). Botas e controle de
  rato são a prevenção.
- **Ostra do mangue** (*Crassostrea rhizophorae*): faixa entremarés; recruta em substrato duro
  em meses. **Coral** de água turva (*Siderastrea stellata*): recrutas de 1–2 mm com um ou
  dois meses, adultos crescem 6–8 mm por ano; colônias de 0,4–5 cm têm 1–10 anos.
- ***Rhizophora***: propágulos soltam no verão; plantio manual pega cerca de metade.
- **Estaca-prancha:** martelo vibratório crava duas a três estacas de 12 m por hora; 310 m
  são ~450 estacas, três semanas.
- **Estação de bombas:** 64 m³/s a ~5 m de altura são ~4–5 MW.
- **Estações:** a costa de Thalassa tem verão em janeiro e inverno em junho.
- **θάλασσα** = mar, em grego.

## Ficção científica de referência

As obras com que este livro conversa, e o que cada uma empresta.

- **Ursula K. Le Guin, *Os despossuídos*** — a comunidade sem dono que decide junto.
