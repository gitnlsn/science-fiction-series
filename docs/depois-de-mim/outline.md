# Plano — Depois de mim

Livro 1 da série. Este arquivo é a **fonte única**
dos títulos e da numeração dos capítulos: `make outline BOOK=depois-de-mim` cria
ou atualiza os arquivos em `books/depois-de-mim/chapters/`, sem nunca tocar no
corpo já escrito.

**Não rodar `make outline` enquanto as vagas tiverem títulos provisórios** —
o scaffolder cria um arquivo por vaga.

---

## A premissa — escolhida

Helena, 38 anos, engenheira de estruturas com uma doença terminal, aceita
em 2031 ter o cérebro escaneado. Acorda em 2140 num corpo novo — e a
filha, que tinha seis anos quando ela morreu, hoje é mais velha que ela.

**Decidido:**

- **A filha tem 115 anos em 2140.** A tecnologia de longevidade a mantém viva
  e lúcida, mas visivelmente velha: uma mãe de 38 anos e uma filha de 115.
- **Quem trouxe Helena de volta foi a filha, para si mesma.** Está morrendo e
  pagou para ter a mãe de novo no fim da vida. Helena não voltou para viver a
  própria vida: voltou para cuidar. Não há vilão. É o que o arco III revela.
- **O corpo novo foi cultivado a partir do DNA dela**, aos 38 anos: o próprio
  rosto, sem cicatrizes e sem história.
- **Como Helena morre em 2031:** legalmente. Ela escolhe suspender o
  tratamento, o que a lei da cidade permite, e doa o próprio cérebro para
  pesquisa. Morre em casa, com a equipe de preservação esperando no cômodo ao
  lado, porque o cérebro tem de começar a ser preservado em cerca de 14
  minutos. A filha, de seis anos, está na casa nesse dia. O cérebro não é
  escaneado antes da morte: é **preservado** e fica guardado por décadas até
  ser lido. Ver `references.md`.
- **Onde:** **uma cidade sem nome**, como em *Quarenta dias úteis*. Helena
  morava nela em 2031, então cada rua que ela reconhece, ou não reconhece, é
  uma referência futurista que dói. Regras em *O lugar*, abaixo.
- **Tamanho:** o rascunho completo tem **~43.000 palavras** (186 páginas), e fica assim, por decisão do autor. O alvo de 60.000 foi abandonado: a KDP não exige mais.

- **Protagonista:** Helena, 38 — engenheira de estruturas, mãe de Cecília ("Ciça"), morta em 2031, acordada em 2140
- **Quando:** 2031 (a morte) e 2140 (o presente do livro)
- **Onde:** uma cidade sem nome

**A exceção declarada da série:** Helena vem de 2031, então ela é a única
personagem das três obras que *se espanta* com o futuro. O leitor descobre
2140 junto com ela — é isso que transforma as muitas referências
futuristas em enredo. Todo o resto do elenco segue a regra: ninguém no
futuro se espanta com o futuro.

## O lugar — decidido

**A cidade não tem nome, e nem o país.** Helena e Cecília não têm
nacionalidade dita. A mesma decisão de *Quarenta dias úteis*, com a mesma
regra dura: **sem nome não quer dizer vago.** A cidade tem bairros com nome,
ruas, linhas de transporte, o preço de um café e uma estação em que chove. Não
tem bandeira.

- Nenhum nome de país, de cidade real, de moeda, de instituição nacional, de
  feriado ou de lei real na prosa.
- **Nunca nomear um mês** quando o mês entrega um hemisfério. Calor, frio e
  chuva existem; agosto não. As datas ISO do front matter alimentam
  `make digest --tempo` e nunca são impressas.
- Ao tirar uma marca de lugar, varrer a classe inteira: datas, feriados,
  estações, clima, moeda, esportes, calendário escolar, formato de tomada.
- As leis da cidade (morrer, doar o corpo, o estatuto de quem volta) são
  **invenção**, registrada em `bible.md`, não fato conferido.

## Sem epígrafes — decidido

As quatro partes abrem sem epígrafe, por decisão do autor, ao contrário de
*Quarenta dias úteis*. Os arquivos em `books/depois-de-mim/parts/` ficam só com o
título da parte e a ilustração. **Não acrescentar.**

## A voz — decidido

Decidido em 2026-09-27, substituindo a decisão anterior de terceira pessoa em
todo o livro.

- **Pontos de vista alternados** entre Helena e a filha, cada capítulo preso a
  uma das duas (`pov:` no front matter).
- **Os capítulos de Helena: primeira pessoa, no presente.** Helena não tem
  passado neste mundo, só o agora.

      Acordo e olho as mãos. São minhas. Não têm a cicatriz.

- **Os capítulos de Cecília: terceira pessoa, no passado.** Cecília, aos 115, é
  quase toda passado, e a distância da terceira pessoa protege o segredo dela.

      Cecília recebeu a notícia à tarde, sentada, porque já não recebia nada
      em pé.

- A gramática e o tempo verbal dizem de quem é o capítulo antes do nome. **Nunca
  misturar:** um capítulo de Helena não escorrega para o passado, e um de
  Cecília nunca diz "eu" fora das falas.
- **Falas com travessão**, nos dois: `— Ciça.`
- Lembranças de 2031 nos capítulos de Helena vão no pretérito, que é o passado
  *dela*: "Em 2031 eu tinha uma cicatriz aqui."
- **O leitor sabe cedo.** Os capítulos da filha deixam o leitor ver o motivo
  dela desde o arco I; Helena não sabe. É ironia dramática: toda cena de
  carinho entre as duas dói porque o leitor sabe. O arco III é Helena
  descobrindo o que o leitor já sabe. Os capítulos da filha **nunca** escondem
  o motivo do leitor, e os de Helena nunca deixam que ela adivinhe antes da hora.

## Os quatro arcos — ponto de partida

Cada arco é uma parte, e cada parte muda a protagonista. O estado em que ela
entra e sai de cada arco fica em `bible.md`, em *Protagonista*.

| Parte | O arco | Capítulos |
|---|---|---|
| I — O despertar | perdida num mundo que ela não entende | 5 |
| II — O pertencimento | constrói uma vida, um trabalho, amigos; reaproxima-se da filha | 4 |
| III — O motivo | descobre por que foi trazida de volta — e não foi por ela | 4 |
| IV — A escolha | decide quem vai ser | 5 |

## A decidir pelo autor


---

## Formato de cada capítulo

Copiar o bloco abaixo por capítulo. `make outline` lê os campos em negrito;
`Fios`, `Planta`, `Paga` e `Elenco` são listas separadas por vírgula.

    ### 1. Título do capítulo
    - **POV** — quem conta
    - **Quando** — 2140-03-14 — manhã (a data ordenável vem primeiro)
    - **Onde** — lugar
    - **A ideia** — o capítulo em uma frase
    - **A virada** — o que muda até o fim dele
    - **Fios** — fio-um, fio-dois
    - **Planta** — semente-um
    - **Paga** — semente-plantada-antes
    - **Elenco** — nome-um, nome-dois

---

## PARTE I — O DESPERTAR

*Arco:* Helena perdida num mundo que não entende. A parte termina quando ela encontra a filha.

### 1. As mãos
- **POV** — Helena
- **Quando** — 2140-03-01 — manhã
- **Onde** — a clínica
- **A ideia** — Helena acorda num corpo sem história e sem a cicatriz; sem memória imunológica, fica em isolamento e é vacinada como um bebê; a última lembrança dela é o dia em que morreu, em 2031.
- **A virada** — Helena ouve: "Ela está viva. Tem cento e quinze anos."
- **Fios** — o-corpo, a-filha
- **Planta** — cicatriz, corpo-sem-historia, catorze-minutos, a-ultima-frase
- **Elenco** — helena, ravi

### 2. Cento e quinze
- **POV** — Cecília
- **Quando** — 2140-03-01 — tarde
- **Onde** — o apartamento de Cecília
- **A ideia** — Cecília, 115 anos, recebe a notícia de que a mãe acordou; o leitor fica sabendo por que ela trouxe a mãe de volta: está morrendo e quer ser cuidada pela mãe no fim; ninguém vivo a chama de Ciça.
- **A virada** — o leitor sabe o motivo, e Helena não
- **Fios** — a-filha, o-segredo
- **Planta** — cica, o-motivo
- **Elenco** — cecilia, ravi, irene, a-cuidadora

### 3. A cidade
- **POV** — Helena
- **Quando** — 2140-04-19 — dia inteiro
- **Onde** — a cidade
- **A ideia** — Depois das vacinas, Helena sai pela primeira vez; lê a cidade de 2140, construída contra o calor e a água, com olho de engenheira; vê de longe um prédio em que trabalhou em 2031.
- **A virada** — todo mundo que ela conhecia morreu, menos a Ciça
- **Fios** — o-corpo, a-cidade
- **Planta** — o-predio
- **Paga** — corpo-sem-historia
- **Elenco** — helena, ravi

### 4. O quarto
- **POV** — Cecília
- **Quando** — 2140-05-10 — noite
- **Onde** — o apartamento de Cecília
- **A ideia** — Cecília prepara um quarto para a mãe, assina o contrato com a clínica e tem medo de não ser reconhecida.
- **A virada** — decide não contar a Helena por que a trouxe de volta
- **Fios** — o-segredo
- **Planta** — o-contrato, o-sapato
- **Elenco** — cecilia

### 5. Ciça
- **POV** — Helena
- **Quando** — 2140-05-12 — tarde
- **Onde** — a clínica
- **A ideia** — O encontro: uma mãe de 38 anos diante de uma filha de 115; Helena reconhece um gesto de quando a filha tinha seis anos.
- **A virada** — Helena diz "Ciça", e vai para casa com ela
- **Fios** — a-filha
- **Paga** — cica
- **Elenco** — helena, cecilia, ravi

## PARTE II — O PERTENCIMENTO

*Arco:* Helena constrói uma vida. É a parte mais feliz, e cada cena de carinho dói porque o leitor sabe.

### 6. A neta
- **POV** — Cecília
- **Quando** — 2140-06-14 — almoço
- **Onde** — o apartamento de Cecília
- **A ideia** — Irene, a neta de 68 anos, chega hostil: a herança pagou a volta de Helena; Cecília olha a mãe e a neta, duas estranhas uma para a outra.
- **A virada** — Irene pergunta se Helena sabe por que foi trazida, e Helena não entende a pergunta
- **Fios** — a-familia, o-segredo
- **Planta** — irene-e-o-dinheiro
- **Elenco** — cecilia, helena, irene

### 7. O prédio
- **POV** — Helena
- **Quando** — 2140-07-22 — manhã
- **Onde** — o prédio de 2031
- **A ideia** — Helena encontra de perto o prédio de 2031, ainda de pé; em 2140 as máquinas projetam, mas o jeito como se construía em 2031 virou saber raro, e ela arranja trabalho no retrofit dessas estruturas.
- **A virada** — ela volta a ser útil
- **Fios** — a-cidade, o-trabalho
- **Paga** — o-predio
- **Elenco** — helena

### 8. A brincadeira
- **POV** — Cecília
- **Quando** — 2140-09-05 — noite
- **Onde** — o apartamento de Cecília
- **A ideia** — Mãe e filha refazem uma brincadeira de quando Cecília era criança; Cecília está feliz e esconde os sintomas.
- **A virada** — o leitor vê o pouco tempo que resta, e Helena não
- **Fios** — a-filha, o-segredo
- **Elenco** — cecilia, helena

### 9. Cinco anos
- **POV** — Helena
- **Quando** — 2140-10-18 — fim de tarde
- **Onde** — a obra e o apartamento
- **A ideia** — Helena assina um projeto de cinco anos e sente que pertence a 2140.
- **A virada** — Cecília desaba
- **Fios** — o-trabalho, a-filha
- **Planta** — projeto-de-cinco-anos
- **Elenco** — helena, cecilia

## PARTE III — O MOTIVO

*Arco:* Helena descobre o que o leitor já sabe.

### 10. O prognóstico
- **POV** — Cecília
- **Quando** — 2140-11-02 — madrugada
- **Onde** — o hospital
- **A ideia** — Cecília, internada, tem meses de vida; decide de novo não contar.
- **A virada** — pede aos médicos que não digam nada à mãe
- **Fios** — o-segredo
- **Elenco** — cecilia

### 11. O contrato
- **POV** — Helena
- **Quando** — 2140-11-20 — tarde
- **Onde** — a casa de Irene
- **A ideia** — Irene mostra o contrato a Helena: a volta dela está registrada como acompanhamento de fim de vida.
- **A virada** — Helena entende por que voltou
- **Fios** — o-segredo, a-familia
- **Paga** — o-motivo, o-contrato, irene-e-o-dinheiro
- **Elenco** — helena, irene

### 12. Catorze minutos
- **POV** — Cecília
- **Quando** — 2140-12-08 — noite
- **Onde** — o hospital, e a casa de 2031 na lembrança
- **A ideia** — A lembrança inteira de 2031: Cecília, seis anos, no quarto ao lado, com a equipe esperando; a raiz do motivo é que a mãe escolheu ir.
- **A virada** — o leitor entende o porquê do porquê
- **Fios** — o-segredo
- **Paga** — catorze-minutos
- **Elenco** — cecilia, helena

### 13. As duas versões
- **POV** — Helena
- **Quando** — 2141-01-10 — noite
- **Onde** — o apartamento de Cecília
- **A ideia** — O confronto: Helena conta a sua versão de 2031, por que escolheu ir; as duas histórias não batem.
- **A virada** — Helena sai de casa, e fica a pergunta de se ela volta
- **Fios** — a-filha, o-segredo
- **Paga** — a-ultima-frase
- **Elenco** — helena, cecilia

## PARTE IV — A ESCOLHA

*Arco:* Helena escolhe, e depois vive.

### 14. A carta
- **POV** — Cecília
- **Quando** — 2141-02-03 — manhã
- **Onde** — o apartamento de Cecília
- **A ideia** — Cecília liberta a mãe: documentos, independência e parte do patrimônio; e recusa ser preservada.
- **A virada** — Cecília diz: "Depois de mim, nada."
- **Fios** — a-filha, a-familia
- **Planta** — sem-preservacao
- **Paga** — o-sapato
- **Elenco** — cecilia, irene

### 15. A escolha
- **POV** — Helena
- **Quando** — 2141-02-03 — tarde, e dezessete dias depois
- **Onde** — a Tessel, a cidade, e depois o apartamento
- **A ideia** — Helena volta e escolhe ficar, sabendo de tudo.
- **A virada** — escolhe o papel em vez de receber o papel
- **Fios** — a-filha
- **Elenco** — helena, cecilia

### 16. O banho
- **POV** — Cecília
- **Quando** — 2141-05-30 — manhã
- **Onde** — o apartamento de Cecília
- **A ideia** — A inversão: Helena dá banho na filha como dava quando ela tinha seis anos; Cecília enfim pergunta pela cicatriz; é o último capítulo dela, e ela morre no fim.
- **A virada** — Cecília morre
- **Fios** — a-filha, o-corpo
- **Paga** — cicatriz
- **Elenco** — cecilia, helena

### 17. Depois
- **POV** — Helena
- **Quando** — 2141-05-30 — os catorze minutos
- **Onde** — o apartamento de Cecília
- **A ideia** — Os catorze minutos, sem equipe esperando, por escolha de Cecília; Helena atravessa os catorze minutos, e Irene está junto; as duas se reconciliam.
- **A virada** — o espelho de 2031 se fecha
- **Fios** — a-familia
- **Paga** — catorze-minutos, sem-preservacao, irene-e-o-dinheiro
- **Elenco** — helena, irene

### 18. A primeira cicatriz
- **POV** — Helena
- **Quando** — 2141-10-15 — dia
- **Onde** — a obra
- **A ideia** — Meses depois, Helena vive a própria vida e segue no projeto de cinco anos; um acidente na obra dá ao corpo novo a primeira cicatriz, a primeira coisa que é história dele.
- **A virada** — o livro termina em esperança
- **Fios** — o-corpo, o-trabalho
- **Paga** — cicatriz, projeto-de-cinco-anos
- **Elenco** — helena
