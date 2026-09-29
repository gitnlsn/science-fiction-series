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

Pesquisado em 2026-09-28. Os números marcados *(calculado)* saem de física
básica: GM da Terra = 3,986 × 10¹⁴ m³/s², raio equatorial de 6.378 km e
rotação sideral de 7,292 × 10⁻⁵ rad/s. Não saem de fonte, e se refazem com o
script no fim desta seção.

### O elevador: medidas [core]

- **Órbita geoestacionária a 35.786 km** acima do Equador. O cabo sai do chão
  no Equador e passa bem além da GEO, até um **contrapeso a cerca de 100.000
  km**, que o mantém esticado.
- **O material:** o cabo precisa de cerca de **dez vezes a resistência da melhor
  fibra de carbono** fabricada hoje (estimativa do ISEC). Os candidatos são
  nanotubos de carbono (100 a 200 GPa teóricos) e grafeno (~130 GPa). O cabo
  **afina** da GEO para baixo. Hoje o nanotubo mais longo fabricado tem 0,5 m, e
  o grafeno chega a 1 km a 2 m por minuto. **A fabricação é a invenção do livro;
  a física não é.**
- **Os escaladores** vão à velocidade de trem rápido: especificações citam
  **83 m/s (300 km/h)**, e **quatro a cinco dias, ou até sete, até a GEO**.
  *(calculado)* A 300 km/h, chega-se aos 20.000 km em **2,8 dias** e à GEO em
  **5,0**. A 200 km/h, em 4,2 e 7,5 dias.
- Quem sobe vai **mais devagar que o trecho de cabo acima**, porque a
  velocidade do cabo aumenta com a altura.

Fontes: https://en.wikipedia.org/wiki/Space_elevator ·
https://www.isec.org/faq ·
https://users.wpi.edu/~paravind/Publications/PKASpace%20Elevators.pdf ·
https://www.sciencedirect.com/science/article/abs/pii/S0094576523001704

### A gravidade ao longo do cabo [core] *(calculado)*

| Altitude | Gravidade líquida (gravidade menos centrífuga) |
|---|---|
| 0 km | 99,6% de g |
| 1.000 km | 74% |
| 5.000 km | 31% |
| 10.000 km | 14% |
| **20.000 km** | **4,4% de g** (0,43 m/s²) |
| 35.786 km (GEO) | zero |
| 50.000 km | −1,8% (a "queda" é para fora) |
| 100.000 km | −5,4% |

**O que isso dá ao livro:** a 20.000 km, onde está o corpo, ainda existe um
"embaixo", fraco, de 4%. Uma pessoa de 70 kg pesa uns 3 kg. As coisas caem
devagar, mas caem **para a Terra**. Acima da GEO, caem **para fora**.

### O que acontece com uma coisa solta do cabo [core] *(calculado)*

Solto do cabo, um objeto sai com a velocidade do cabo naquele ponto, que é
menor que a orbital abaixo da GEO:

| Solto a | Velocidade do cabo | Velocidade orbital ali | Destino |
|---|---|---|---|
| 10.000 km | 1,19 km/s | 4,93 | cai na atmosfera e queima |
| **20.000 km** | **1,92 km/s** | **3,89** | **cai na atmosfera e queima** |
| 30.000 km | 2,65 km/s | 3,31 | órbita elíptica, com o ponto baixo a ~10.800 km |
| 35.786 km | 3,07 km/s | 3,07 | fica parado, em órbita geoestacionária |
| 40.000 km | 3,38 km/s | 2,93 | órbita elíptica que sobe até ~86.000 km |
| 50.000 km | — | — | escapa da Terra |

**O que isso dá ao livro, e é o motor do mistério:** a 20.000 km, **para fazer
um corpo sumir, basta soltá-lo**. Ele cai, entra na atmosfera e queima, sem
deixar nada. Se o corpo do mentor **está preso no cabo**, alguém quis que ele
fosse encontrado, ou quem o matou foi interrompido, ou **ele mesmo se prendeu**,
para ser encontrado por ela. **Decidido: ele se prendeu sozinho** (ver `outline.md`).

### Se o cabo romper [core]

- **Rompido abaixo de ~25.000 km:** a parte de baixo desce e **se estende ao longo
  do Equador, a leste da âncora**. A parte de cima, desequilibrada, sobe para uma
  órbita mais alta.
- Na atmosfera, a maior parte do cabo se parte por forças aerodinâmicas e desce
  devagar, **mas formam-se grandes laços**, alguns fora da atmosfera, e **alguns
  pedaços chegam ao chão em alta velocidade**. O risco é para tudo o que está no
  plano equatorial, no espaço e em terra.
- Enquanto a parte de baixo se enrola na Terra, a tensão no resto aumenta, e as
  seções de cima **se partem e são lançadas**, em trajetórias muito sensíveis às
  condições iniciais.

**O que isso dá ao livro:** uma catástrofe real, mas não o fim do mundo, e **de
escala certa para um mistério**. A 20.000 km, o corpo está dentro da faixa em que
uma ruptura faz o cabo cair sobre o Equador.
Fontes: https://en.wikipedia.org/wiki/Space_elevator_safety ·
https://www.researchgate.net/publication/251231502_Dynamics_of_Space_Elevator_After_Tether_Rupture

### O para-sol em L1 — por que o mundo depende do elevador [core]

- **Roger Angel (2006)** propôs um para-sol espacial feito de **trilhões de discos
  refrativos**, transparentes, que desviam a luz em vez de bloqueá-la. Ficariam
  perto do **ponto de Lagrange L1**, entre a Terra e o Sol, a cerca de 1,5 milhão
  de km, e **bloqueariam 1,8% do fluxo solar**, o bastante para compensar o
  aquecimento global.
- A massa total seria de cerca de **20 milhões de toneladas**, construída ao longo
  de **25 anos** por menos de 0,5% do PIB mundial no período.
- **Lançar a partir do elevador:** uma carga que sobe além da GEO e é solta na
  ponta do cabo ganha velocidade suficiente para **escapar da Terra**. Soltar
  depois de ~2.000 km dá órbita baixa, e na GEO dá geoestacionária. Com um cabo de
  144.000 km, a ponta chega a 10,93 km/s. *(calculado, ver a tabela acima)*
  Solto a 50.000 km, já escapa.

**O que isso dá ao livro:** o elevador é **a única maneira barata** de subir 20
milhões de toneladas. **Parar o elevador é parar o para-sol**, e o calor mata no
Equador, onde fica a Âncora. **Não parar é arriscar que o cabo caia sobre o
Equador.** As duas escolhas cobram da mesma gente. É o dilema do livro, e é o
que faz de Álvaro uma figura trágica e não um vilão.
**Os números reais por trás da decisão de 2110:**

- **1,7 a 1,8% menos luz** (~23 W/m² da constante solar de 1.367 W/m²) compensa o
  aquecimento de equilíbrio de **uma duplicação do CO₂** (Bala, Duffy e Taylor).
- **Roteiros reais:** missões precursoras nas próximas duas décadas, fase
  operacional inicial por volta de 2040, implantação completa por volta de 2080.
- **Termination shock:** se uma geoengenharia solar que mascara muito
  aquecimento para de repente, a temperatura sobe rápido, mais depressa do que a
  sociedade consegue se adaptar, e a alta depende de quanto resfriamento havia.
  Um estudo de 2018 (Parker e Irvine, *Earth's Future*) diz que o risco foi
  superestimado e que sistemas com reserva são resistentes. [care]

Fontes: https://www.pnas.org/doi/10.1073/pnas.0608163103 ·
https://www.sciencedirect.com/science/article/pii/S0273117726004503 (roteiro para um para-sol planetário) ·
https://agupubs.onlinelibrary.wiley.com/doi/10.1002/2017EF000735 ·
https://www.carbonbrief.org/explainer-six-ideas-to-limit-global-warming-with-solar-geoengineering

A decisão do livro está em `bible.md`, *O para-sol*: dois terços pronto em
2110, reposição de 5% ao ano (invenção) e um ano parado custando ~0,1 °C.

Fontes: https://en.wikipedia.org/wiki/Space_sunshade ·
https://www.researchgate.net/publication/6710728_Feasibility_of_cooling_the_Earth_with_a_cloud_of_small_spcecraft_near_the_inner_Lagrange_point_L1 ·
https://en.wikipedia.org/wiki/Roger_Angel ·
https://arxiv.org/pdf/2008.05244 (Peet, *The Orbital Mechanics of Space Elevator Launch Systems*)

### A âncora no mar [core]

A maior parte dos projetos põe a âncora **numa plataforma no oceano**, no
Pacífico equatorial, longe das rotas aéreas e marítimas: a LiftPort fala em 650
km de qualquer rota. **A plataforma é móvel**, um navio ou plataforma que se
desloca para tirar a fita do caminho de satélites e detritos quando os
rastreadores avisam. O Equador também tem menos furacões e raios.
Fontes: https://www.esa.int/ESA_Multimedia/Images/2002/10/Space_Elevator_platform_in_the_Pacific ·
https://www.isec.org/2015-study (ISEC, *Design Considerations of a Space Elevator Earth Port*) ·
https://science.howstuffworks.com/space-elevator.htm

**O que isso dá ao livro, se for adotado:** a Âncora seria **uma cidade flutuante,
longe de tudo**, o que explica sem esforço por que o país não tem nome. E é **um
círculo fechado**: pouca gente, todos com credencial, ninguém chega nem sai sem
registro. É a situação clássica do mistério de suspeitos limitados.

### O calor que mata — temperatura de bulbo úmido [core] [care]

- A **temperatura de bulbo úmido** combina calor e umidade e mede se o corpo
  ainda consegue se resfriar suando. **35 °C** foi por muito tempo o limite
  teórico de sobrevivência.
- **Pesquisas recentes com pessoas** acharam limites **menores**: de cerca de 25,8
  a 34,1 °C para adultos jovens e de 21,9 a 33,7 °C para idosos, conforme as
  condições. [care] É um debate em aberto; não cravar um número sem fonte.

Fontes: https://iopscience.iop.org/article/10.1088/1748-9326/ace83c ·
https://www.pnas.org/doi/10.1073/pnas.2305427120 ·
https://www.nature.com/articles/s41467-023-43121-5

**O que isso dá ao livro:** a onda de calor de *O que ele deixou* pode ser
precisa. Na Âncora, no Equador, sobre o mar quente, é o bulbo úmido que mata, e
os velhos morrem primeiro. É o que o para-sol existe para impedir.

### A radiação: o cinturão externo de Van Allen [core] [care]

O cinturão interno fica mais ou menos entre 1.000 e 12.000 km, conforme a
fonte. O **externo** vai de cerca de **13.000–20.000 km até 40.000–60.000 km**,
e as fontes divergem sobre os limites. **Os 20.000 km ficam dentro ou na borda
do cinturão externo.** [care] Os limites variam com a fonte e com a atividade
solar, então o livro não deve cravar um número de dose sem fonte primária.

**O que isso dá ao livro:** quem trabalha ali tem **blindagem** e **dosímetro**,
e o dosímetro do traje do morto registra a dose ao longo do tempo. É **um
relógio forense**: diz quanto tempo ele passou fora, e onde.

Fontes: https://en.wikipedia.org/wiki/Van_Allen_radiation_belt ·
https://sci.esa.int/web/cluster/-/52831-earth-plasmasphere-and-the-van-allen-belts
**Conferido (2026-09-28):**
- No cinturão externo, **atrás de 4 mm de alumínio, a dose fica em torno de 4,2
  mSv por hora ou mais**. Uma conta a partir de dados de satélite dá ~6 mSv/h sem
  blindagem. [care] As fontes são secundárias e os números variam muito com a
  blindagem e a atividade solar: **a prosa não crava número de dose**, fala em
  verde, amarelo e limite.
- **O limite de carreira da NASA desde 2022 é de 600 mSv**, universal para
  qualquer idade e sexo, calibrado para menos de 3% de risco de morte por câncer.
  **O que isso dá ao livro:** a Operadora tem um limite de carreira parecido
  (invenção), e trinta anos de cabo, com três mil noites no Posto, passam dele. É a
  carta médica de Otávio (`a-dose-limite`).
Fontes: https://spacemath.gsfc.nasa.gov/earth/10Page119.pdf ·
https://www.nationalacademies.org/read/26155/chapter/5 ·
https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf

### Um corpo no vácuo [core] [care]

- **Exposto ao vácuo**, sem oxigênio, não há decomposição aeróbica. O corpo
  **congela** (na sombra) ou **seca por liofilização**, com a água sublimando
  (ao sol), e fica preservado por tempo indefinido.
- **Dentro de um traje pressurizado**, as bactérias do próprio corpo ainda fazem
  a decomposição normal, primeiro aeróbica e depois anaeróbica.

**O que isso dá ao livro:** saber **se o traje estava íntegro ou furado** muda
tudo: a hora da morte, o estado do corpo, e se o furo veio antes ou depois.
Fontes de divulgação, não científicas [care]:
https://www.scienceabc.com/nature/universe/if-you-die-in-space-does-your-body-decompose
**Conferido (2026-09-28), a exposição ao vácuo:**
- Com despressurização rápida, **a pessoa perde a consciência em 10 a 15 segundos**
  (a umidade da língua e dos olhos ferve; em 1966, o técnico da NASA Jim LeBlanc
  lembrou da saliva fervendo antes de apagar). O coração para por "vapor lock",
  e a letalidade sobe muito depois de **~90 segundos**. O corpo incha, mas não
  explode.
- **O que isso obriga o livro a fazer:** Otávio **não poderia** ter se amarrado com
  um rasgo grande. **O rasgo é pequeno, um vazamento lento**: o traje perde pressão
  aos poucos, a reserva compensa por alguns minutos, e ele tem **minutos, não
  segundos**, para se amarrar. É o que torna possível o `corpo-preso`, e o leitor
  de fair play deve receber isso em *Três quilos*.
- Depois de o traje despressurizar todo, o corpo fica exposto ao vácuo dentro do
  traje, congela na sombra e seca aos poucos, e **não se decompõe**. Seis dias
  depois está preservado.
Fontes: https://www.nasa.gov/wp-content/uploads/2026/08/ebullism-cliff-2023.pdf ·
https://link.springer.com/chapter/10.1007/978-94-010-3464-7_2 ·
https://ntrs.nasa.gov/citations/19920013110

### Para refazer os cálculos

    GM=3.986004418e14; R=6378.137e3; w=7.2921159e-5
    r=R+h; g=GM/r**2; c=w**2*r; liquida=g-c
    v=w*r; eps=v*v/2-GM/r; a=-GM/(2*eps); e=sqrt(1+2*eps*(r*v)**2/GM**2)
    rp=a*(1-e)   # abaixo de R+100 km: queima na atmosfera

## Ficção científica de referência

As obras com que este livro conversa, e o que cada uma empresta.

- **Arthur C. Clarke, *The Fountains of Paradise* (1979):** o romance clássico do
  elevador espacial. Serve para conhecer, e para não repetir.
  **Terceira dívida em "Sobre a autora":** as pesquisas de bulbo úmido com pessoas
  (PNAS 2023 e outras, acima, em *O calor que mata*), de onde sai dona Celeste. O texto não
  nomeia os estudos.
  **Edição brasileira, citada em "Sobre a autora":** *As fontes do paraíso* (Editora
  Aleph, 1ª ed. 2015, nova ed. 2022, tradução de Susana L. de Alexandria). Ganhou o
  Hugo e o Nebula.
  Fonte: https://aleph.com.br/products/as-fontes-do-paraiso
- **Kim Stanley Robinson, *Red Mars* (1992):** o elevador de Marte é sabotado e o
  cabo, de 35.000 km e 6 bilhões de toneladas, se enrola duas vezes em volta do
  equador marciano. **É a queda de cabo mais famosa da ficção. *A volta a mais* não
  pode repeti-la**, e não repete: aqui o cabo não cai, e o livro é sobre impedir.
- **Kim Stanley Robinson, *The Ministry for the Future* (2020):** abre com uma
  onda de calor na Índia, com o bulbo úmido acima do limite, que mata 20
  milhões. **A onda de calor de *O que ele deixou* tem de ser pequena, de perto,
  pelos olhos de Iara: uma pessoa, não uma estatística**, para não ecoar essa
  abertura.
- **Isaac Asimov, *The Caves of Steel* (1954):** o romance que tirou o detetive de
  ficção científica da revista barata; um mistério de regras claras num mundo
  novo.
- **Mur Lafferty, *Six Wakes* (2017)** e **Mary Robinette Kowal, *The Spare Man*
  (2022):** assassinatos em espaço fechado (uma nave, um cruzeiro espacial), com
  suspeitos limitados. São a referência para o círculo fechado da Âncora e do
  cabo.
Fontes: https://en.wikipedia.org/wiki/Space_elevators_in_fiction ·
https://en.wikipedia.org/wiki/The_Ministry_for_the_Future ·
https://fivebooks.com/best-books/best-sci-fi-mysteries-mary-robinette-kowal/
