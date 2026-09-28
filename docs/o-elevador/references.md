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
para ser encontrado por ela. [[?autor: qual das três — decide o livro]]

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
[[?fato: dose típica por hora no cinturão externo, de fonte primária (NASA/ESA), antes de pôr um número na prosa]]

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
[[?fato: fonte forense ou médica sobre corpos no vácuo antes de detalhar na prosa]]

### Para refazer os cálculos

    GM=3.986004418e14; R=6378.137e3; w=7.2921159e-5
    r=R+h; g=GM/r**2; c=w**2*r; liquida=g-c
    v=w*r; eps=v*v/2-GM/r; a=-GM/(2*eps); e=sqrt(1+2*eps*(r*v)**2/GM**2)
    rp=a*(1-e)   # abaixo de R+100 km: queima na atmosfera

## Ficção científica de referência

As obras com que este livro conversa, e o que cada uma empresta.

- **Arthur C. Clarke, *The Fountains of Paradise* (1979):** o romance clássico do
  elevador espacial. Serve para conhecer, e para não repetir.
