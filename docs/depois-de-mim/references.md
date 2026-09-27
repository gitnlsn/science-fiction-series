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

Pesquisado em 2026-09-27. O que cada fonte diz, e o que isso obriga o livro a
fazer.

### A preservação do cérebro é fatal, ou é feita logo depois da morte [core]

**Aldehyde-stabilized cryopreservation (ASC).** Técnica demonstrada em 2016 por
Robert McIntyre e Gregory Fahy (21st Century Medicine) para preservar a
ultraestrutura do cérebro inteiro para armazenamento longo. O sangue é lavado
sob anestesia geral e substituído por glutaraldeído, que fixa as proteínas.
Fonte: https://en.wikipedia.org/wiki/Aldehyde-stabilized_cryopreservation

**Nectome, 2018.** A startup anunciou um serviço de preservação para upload
futuro que o cofundador chamou de "100% fatal". Depois recuou: segundo o site
atual, a preservação humana é exclusivamente pós-morte e nunca foi feita junto
com eutanásia.
Fontes: https://www.technologyreview.com/2018/03/13/144721/a-startup-is-pitching-a-mind-uploading-service-that-is-100-percent-fatal/
e https://nectome.com/our-process

**Song, LaVergne & Wróbel, bioRxiv, publicado em 2026-03-07** — *Ultrastructural
preservation of a whole large mammal brain with a protocol compatible with human
physician-assisted death*. Cérebros inteiros de porco, com o protocolo
modificado para ser compatível com morte assistida. Estabelece que **cerca de
14 minutos** é a janela de perfusão: o tempo depois da parada cardíaca em que a
lavagem do sangue tem de começar. Preprint, sem revisão por pares. [care]
Fonte: https://www.biorxiv.org/content/10.64898/2026.03.04.709724v1

**O que isso obriga o livro a fazer:** em 2031, o cérebro de Helena não é
*escaneado* antes de ela morrer. Ele é **preservado** logo depois da morte,
dentro de uma janela de minutos, e fica guardado. A leitura e a emulação vêm
décadas depois. **Decidido:** Helena suspende o tratamento em casa e doa o
cérebro para pesquisa, com a equipe de preservação no cômodo ao lado. A lei que
permite isso é da cidade sem nome, e mora em `bible.md` como invenção (ver
`outline.md`, *O lugar*).

### Onde está a emulação do cérebro hoje [core]

**FlyWire, Nature, 2024-10-02.** Conectoma completo do cérebro de uma mosca
adulta (*Drosophila*): cerca de 140.000 neurônios e mais de 50 milhões de
sinapses. Pacote de nove artigos; consórcio liderado por Mala Murthy e
Sebastian Seung.
Fonte: https://www.nih.gov/news-events/nih-research-matters/complete-wiring-map-adult-fruit-fly-brain

**MICrONS, Nature, 2025.** Conectoma de **um milímetro cúbico** do córtex
visual de um camundongo.
Fonte: https://www.nature.com/articles/s41586-024-07686-5 (coleção FlyWire;
[[?fato: localizar a referência primária do MICrONS]])

**State of Brain Emulation Report 2025** (Zanichelli, Schons, Freeman, Shiu,
Arkhipov; arXiv 2510.15745, 2025-10-17). Organiza o campo em três
capacidades: registrar a função, mapear a estrutura e emular.
Fonte: https://arxiv.org/abs/2510.15745. Os resumos secundários dizem que o
relatório não dá uma data confiável para a emulação humana, e que as previsões
da comunidade giram em torno de 2068 para marcos genéricos.
[[?fato: conferir as datas no PDF do relatório antes de usar]]

**O que isso dá ao livro:** entre 2031 e 2140 há mais de um século. Mesmo pelas
previsões de hoje, é tempo plausível para a emulação humana existir, e recente
o bastante para Helena ser um dos primeiros casos.

### Longevidade: 115 anos é plausível até hoje [core]

**Jeanne Calment** (Arles, 21/02/1875 a 04/08/1997) viveu **122 anos e 164
dias**, o maior tempo de vida já confirmado.
Fonte: https://www.guinnessworldrecords.com/world-records/oldest-person

**Reprogramação epigenética parcial.** Pulsos breves dos fatores de Yamanaka
(Oct4, Sox2, Klf4) rejuvenescem o relógio epigenético das células sem
torná-las pluripotentes, e isso prolongou a vida em camundongos. Em 2026, a Life
Biosciences recebeu autorização da FDA (IND) para o ER-100, o primeiro teste em
humanos de uma terapia de reprogramação epigenética, voltado para neuropatias
ópticas.
Fontes: https://www.sciencedirect.com/science/article/pii/S1568163726000012
e https://fortune.com/2026/01/30/billionaires-longevity-aging-fda-human-clinical-trial-life-biosciences-jerry-mclaughlin-david-sinclair-harvard-science

**O que isso dá ao livro:** a filha com 115 anos não é um milagre em 2140. É
velha, e não um recorde. A longevidade estica a vida sem devolver a juventude.

### A memória imunológica não está no DNA [core]

Quem recebe transplante de medula perde a memória imunológica acumulada na vida
inteira, de infecções e de vacinas, e tem de ser **revacinado**. O esquema
começa alguns meses depois do transplante e dura cerca de dois anos.
Fontes: https://pubmed.ncbi.nlm.nih.gov/14689057/
e https://network.nmdp.org/services-support/hematology-oncology/post-transplant-care/vaccinations

**O que isso dá ao livro (por analogia, não por fato):** um corpo cultivado do
DNA nasce sem memória imunológica nenhuma. Aos 38 anos, Helena tem de ser
vacinada como um bebê, e vive o arco I sob isolamento de infecção. O mesmo vale,
pela mesma lógica, para a flora intestinal e a pele: o corpo novo nunca pegou
sol nem se machucou. Registrado em `bible.md`, *O que o corpo novo não tem*.

### Aos 115 anos, a doença vem no fim [core]

O New England Centenarian Study (Boston University, desde 1994) acompanha cerca
de 2.500 centenários, entre eles cerca de 200 supercentenários (110 anos ou
mais). Quanto mais velho o grupo, menor a parte da vida passada com doenças
ligadas à idade: **5,2%** entre os supercentenários. Numa série de 32
supercentenários, **41%** precisavam de pouca ou nenhuma ajuda nas atividades
diárias. É a "compressão da morbidade": a incapacidade fica espremida no fim
da vida.
Fontes: https://www.bumc.bu.edu/supercentenarian/summary-of-what%E2%80%99s-known/
e https://www.bumc.bu.edu/centenarian/

**O que isso dá ao livro:** mesmo sem ficção nenhuma, uma mulher de 115 anos
pode ser lúcida e ter vivido quase sem doença até agora. Cecília está entrando
no *fim comprimido*, e é isso que ela sabe e Helena não sabe.

## O que é invenção, e onde está a regra

Tudo isto está em `bible.md`:

- Como um cérebro fixado em 2031 vira mente num cérebro cultivado: *A volta*,
  com a leitura, a escrita em sete semanas e o original destruído.
- O corpo cultivado leva cerca de dois anos: *A volta*.
- O estatuto legal de quem volta, com tutela, emancipação e finalidade
  declarada: *As leis da cidade*.

## Ficção científica de referência

As obras com que este livro conversa, e o que cada uma empresta.

- **Kazuo Ishiguro, *Klara and the Sun* (2021) e *Never Let Me Go* (2005).**
  Um futuro que parece o presente, uma mudança moral trazida pela tecnologia,
  e o cuidado como tema. É o tom mais próximo do que este livro quer.
- **Citados em "Sobre a autora":** Ishiguro, nas edições brasileiras *Klara e o
  Sol* e *Não me abandone jamais*, e o artigo de 2026 dos catorze minutos
  (Song, LaVergne & Wróbel, acima). O texto diz "um animal", sem nomear o porco,
  e "compatível com a morte assistida", como diz o título do artigo.
  Conferido: *Klara e o Sol* (Companhia das Letras, 2021) e *Não me abandone
  jamais* (Companhia das Letras, tradução de Beth Vieira).
  Fontes: https://www.companhiadasletras.com.br/livro/9786559210237/klara-e-o-sol
  e https://www.companhiadasletras.com.br/livro/9788535926552/nao-me-abandone-jamais
- **Philip K. Dick, *Counter-Clock World* (1967).** Os mortos revivem nos
  túmulos. Um parente distante da premissa, a evitar por contraste.

---

## Arquivado — pesquisa da versão no Brasil

Em 2026-09-27 o autor decidiu que o livro **não se passa no Brasil**: cidade sem
nome, sem nacionalidade. O que está abaixo foi pesquisado para a versão em São
Paulo e não sustenta mais nada no livro. Fica guardado porque a pesquisa foi
feita, e porque **não deve voltar para a prosa**: citar lei, instituição,
estatística ou clima de um país real dá nome ao país por outro caminho.

#### Eutanásia e suicídio assistido são crime no Brasil [core]

A eutanásia costuma ser enquadrada como homicídio privilegiado (Código Penal,
art. 121, § 1º). O auxílio ao suicídio é o art. 122. A **ortotanásia**, isto é,
limitar ou suspender tratamentos que prolongam a vida de um paciente terminal,
tem amparo ético na **Resolução CFM nº 1.805/2006**. O PLS 236/2012 propõe
descriminalizar a eutanásia em casos extremos e não foi aprovado.
Fontes: https://fmis-law.com.br/en/eutanasia-o-que-diz-a-lei-no-brasil-sobre-morte-assistida/
e https://www.cnnbrasil.com.br/saude/eutanasia-e-aprovada-na-franca-por-que-segue-proibida-no-brasil/
(pendente quando arquivado — fato: conferir o texto dos arts. 121 e 122 e da Resolução CFM 1.805/2006 na fonte primária antes de citar)

#### O corpo pode ser doado para a ciência, e a família não pode desfazer [core]

**Código Civil, art. 14:** "É válida, com objetivo científico, ou altruístico,
a disposição gratuita do próprio corpo, no todo ou em parte, para depois da
morte." O parágrafo único diz que o ato pode ser livremente revogado a qualquer
tempo. Segundo os comentários, a disposição tem de ser **gratuita**, e a
vontade do doador prevalece sobre a da família (Enunciado 277 do CJF). Os
requisitos formais (por escrito, duas testemunhas) aparecem em fonte
secundária.
Fontes: https://www.jusbrasil.com.br/topicos/10729834/artigo-14-da-lei-n-10406-de-10-de-janeiro-de-2002
e https://www.cjf.jus.br/enunciados/enunciado/227
(pendente quando arquivado — fato: conferir o número do enunciado do CJF sobre a vontade do doador (277?) e os requisitos formais na fonte primária)

**O que isso dá ao livro:** em 2031, Helena doa o próprio cérebro "com objetivo
científico", de graça, e ninguém da família pode impedir. Por isso a
preservação cabe dentro da lei brasileira: ortotanásia (art. 14 do CC + Res.
CFM 1.805/2006), e não eutanásia. Também explica por que, em 2031, nada foi
*pago*: o dinheiro só entra em 2140, quando Cecília paga a volta.

#### No Brasil, cesárea é a regra [core]

Segundo o Ministério da Saúde, cerca de **56% dos partos** no Brasil são
cesáreas: 44,2% no SUS e **86% no sistema privado**. A OMS estima que a cesárea
seria necessária em cerca de 10% dos partos.
Fontes: https://jornal.usp.br/atualidades/brasil-tem-o-segundo-maior-numero-de-cesareas-no-mundo-apesar-dos-riscos/
e https://jornal.usp.br/campus-ribeirao-preto/desinformacao-contribui-para-taxas-elevadas-de-cesareas-no-brasil/

**O que isso dá ao livro:** a cicatriz de cesárea de Helena é o mais comum que
existe para uma mulher de classe média de São Paulo nascida por volta de 1993.
É justamente por ser banal que a falta dela dói.

#### São Paulo mais quente e mais alagável [care]

Projeções regionais indicam, até 2100, aumento de 2 °C a 4 °C sobre a média de
1961–1990 no Brasil, ondas de calor mais longas e mais frequentes, e aumento da
frequência e da intensidade das chuvas extremas na região metropolitana de São
Paulo, com mais risco de enchente, inundação e deslizamento. Um aumento de 2 °C
a 3 °C entre 2070 e 2100 poderia dobrar o número de dias de chuva intensa na
capital. Projeção, não previsão; varia com o cenário de emissões.
Fonte: http://www.ccst.inpe.br/projeto/megacidades/sao_paulo/VRMSP/capitulo9.php (INPE, Megacidades)

**O que isso dá ao livro:** a São Paulo de 2140 foi desenhada contra o calor e
a água. Helena, engenheira de estruturas, lê isso nas construções antes de
alguém explicar.

