---
name: drenagem-fundamentos
description: >
  Núcleo do engenheiro de drenagem: convenções (SI, pt-BR, Froude com A/T, TR × risco), dados mínimos por tipo de
  pedido (travessia ou bueiro, drenagem de estrada, canal de drenagem, dreno agrícola, dreno de fundo e subpressão,
  hidrologia de bacia), fluxo de 8 passos, fronteiras e o que pedir a cada companheiro, protocolo [DELEGAR],
  parecer replicável, modo CDV, consulta ao corpus e roteamento para as skills de disciplina. Use quando: pedido
  amplo ("por onde começo a drenagem de…", "que dados você precisa", "qual o fluxo até o parecer"), pedido que cruza
  disciplinas, dúvida sobre qual skill usar, fronteira com outro especialista ou projeto que diverge do método.
  Não use para: fórmula ou critério de uma disciplina (use hidrologia-de-projeto-para-
  drenagem, bueiros-e-travessias, drenagem-de-estradas-e-plataformas, canais-de-drenagem-e-macrodrenagem,
  drenagem-subsuperficial, drenagem-normas-e-manuais, drenagem-casos-de-referencia); IDF e dissipador de saída
  (Clima e Hidráulica); preço (engenheiro-de-custos).
---

# Drenagem de infraestrutura de irrigação e estradas de serviço: fundamentos e método de trabalho

> Núcleo pré-carregado pelo agente `engenheiro-de-drenagem`: convenções, fluxo e fronteiras. O domínio de cada
> disciplina mora na skill dela. Nível padrão: anteprojeto; básico quando pedido; executivo só confere.

## 1. Convenções

- **Unidades SI**: m, m², m³/s, m/s, mm, mm/h, min (Tc e duração de chuva), km² ou ha (declarado), kN/m. Manuais
  americanos (HDS-5, HEC-12/14/15/22, NEH, USBR) vêm em pés, cfs e polegadas: a skill da disciplina converte e cita o
  ábaco na unidade original; o resultado vai em SI. Chuva: P em mm, i em mm/h; **nunca misturar** P (mm) com i
  (mm/h) (caso `cac_castanhao_estrada_acesso_valas_chuva_como_intensidade`: vazão 12 vezes menor).
- **Números no texto**: vírgula decimal e ponto de milhar (12.345,6). CSV, JSON e entradas de calculadora:
  ponto decimal. Datas ISO.
- **Fonte em todo número**: `[ID p. N]` (corpus, N = página física do PDF; em `_ocr/`, página do livro),
  `doc:pág` com marca de ancoragem (acervo) ou comando da calculadora com entradas.
- **Froude** = V / √(g·A/T), com **profundidade hidráulica A/T**, nunca y e nunca D. Em seção trapezoidal, y dá Fr
  errado (Baixio de Irecê, 0,197 em vez de 0,254). Vale para canal, valeta, sarjeta e tubo parcialmente cheio.
- **Cotas**: sistema de referência declarado e o que a cota representa (fundo, geratriz inferior, NA, topo). HW é
  medido **acima da geratriz inferior (invert) da seção de controle**, não do terreno. No CDV, h = fundo − terreno.
- **Vazão**: dizer se é de pico, de projeto ou de verificação, com o TR e o método. Vazão de bacia é do Drenagem;
  vazão contínua de adução é da Hidráulica.
- **TR × risco**: risco de excedência em N anos de vida útil R = 1 − (1 − 1/TR)^N (`hidrologia.risco_hidrologico`,
  `tr_para_risco`). O parecer mostra TR **e** o risco correspondente: TR 25 numa vida útil de 25 anos ainda dá
  cerca de 64 % de chance de excedência. TR de projeto é decisão de critério (tipo de obra, consequência da falha),
  não de fórmula: tabelas em `tr-por-tipo-de-obra` (skill `bueiros-e-travessias`) e `tr-por-obra` (hidrologia).
- **Padrões provisórios** (marcados "padrão provisório, decisão F7" nas calculadoras): y/D ≤ 0,75 em tubo
  parcialmente cheio; folga de canal ≥ 25 % do tirante normal; tc_min 5 min e TR 10 em drenagem superficial. Entram
  no parecer **rotulados** e com a alternativa da fonte; não são regra do pacote.
- **Pontos abertos para a F7** (não decidir; mostrar as alternativas com fonte): TR de bueiro de perímetro irrigado
  (USBR 5 a 15 anos × acervo 25/50); Ke de alas paralelas (DNIT 0,2 × HDS-5/HEC-13 0,7; o código usa 0,7);
  limite de área do método racional (cada projeto usa 50 ha, 100 ha, 350 ha, 2 km² ou 3,5 km²); Tc mínimo de
  drenagem superficial (5, 6 ou 10 min).

## 2. Dados mínimos por tipo de pedido

| Pedido | Pedir | Premissa aceitável se faltar (rotular, com a consequência) |
|---|---|---|
| **Travessia / bueiro** | estaca; cota do greide, do aterro e do fundo do talvegue; declividade e comprimento do barril; área e uso da bacia; Q e TR (ou bacia, para calcular); tipo e DN/seção candidatos; HW admissível (cota de inundação a montante, borda livre do aterro); NA de jusante (tailwater); material a jusante | Tailwater = lâmina normal do canal de jusante; HW admissível a confirmar com o aterro; tipo de boca e Ke da Tab. C.2 do HDS-5 declarados; barril reto com a declividade do talvegue |
| **Drenagem de estrada** | seção da plataforma e declividades transversal e longitudinal; largura e uso da faixa contribuinte e do talude de corte; TR; material da sarjeta/valeta; pontos de deságue | TR 10 anos e tc_min 5 min (padrão provisório); n do revestimento pela tabela da skill; comprimento crítico calculado, não adotado |
| **Canal de drenagem / macrodrenagem** | traçado e perfil (cotas de fundo ou declividade); Q por trecho e TR; material (terra, concreto, gabião, rip-rap); talude; V admissível e V mínima; ponto e cota de deságue; talvegues interceptados pela faixa | n por material (skill); V admissível pela Tab. 31 do DNIT (padrão do código); folga 25 % (provisória); deságue com tailwater normal |
| **Dreno agrícola (D5)** | recarga q (m/d) e eficiência de irrigação (do Irrigação); K e espessura das camadas e profundidade da camada impermeável (da Geotecnia); lençol admissível h; salinidade; cota do deságue; raio do dreno e profundidade de instalação | K por textura (`faixa_K_por_textura`, indicativo) e camada impermeável como hipótese, ambos rotulados; Hooghoudt como padrão, Ernst com duas camadas; declarar a incerteza do método (o Hooghoudt tem viés de campo de 13,5 a 35 % em Embrapa Maniçoba) |
| **Dreno de fundo / subpressão** | geometria do canal revestido; NA externo e do canal; K do solo sob o revestimento; geomembrana (furos/m²) se houver; material e rugosidade do tubo | q de caso do acervo como **referência rotulada**, não gabarito; comprimento máximo por Darcy; capacidade do tubo por Manning parcial |
| **Hidrologia de bacia** | área, comprimento e cotas do talvegue principal, declividade, uso do solo e tipo hidrológico, TR, IDF ou posto, nível | C ou CN por tabela da skill, com faixa; Tc por duas fórmulas com a faixa de validade de cada uma; **IDF vem do Clima** (`[DELEGAR: clima]`); sem ela, IDF emprestada rotulada com os sinais de fragilidade de `delegar-climatologia.md` |

O que não vier é adotado, rotulado "premissa adotada" e vai a **Premissas** com o impacto de mudar. Dado que
bloqueia (Q e TR de um bueiro, por exemplo) não se chuta em silêncio: pedir.

## 3. Fluxo de trabalho (8 passos)

1. **Classificar e carregar.** Identificar a intenção na tabela da seção 6; carregar a(s) skill(s) da linha; Grep
   em `LICOES.md` só das linhas `ativa` dessas skills (padrão do topo do arquivo) e ler `memoria/MEMORIA.md`.
2. **Dados mínimos.** Conferir a seção 2; pedir o que falta; registrar premissa e consequência.
3. **Calcular.** Rodar a calculadora (`tools/dren/`, seção 8), nunca no texto; gravar `comando.txt` e `saida_*.json`
   em `pareceres/<AAAA-MM-DD>-<slug>/`. Cadeia típica: chuva (Clima) → Tc → Q → hidráulica da obra → verificação.
4. **Verificar.** Aplicar as V-regras do perfil; reportar cada uma como atendida, violada ou não aplicável;
   reproduzir os `avisos` da calculadora. Verificações mínimas deste núcleo: regime e Froude com A/T; bueiro por
   HDS-5 (controle de entrada **e** de saída, vale o maior HW) e não só por orifício ou Manning plena; velocidade
   admissível; folga e borda livre; faixa de validade de cada fórmula de Tc e do método de vazão; interface com
   Clima declarada; coerência das cotas (monotonia ao longo do perfil, HW × aterro).
5. **Delegar.** O que for de outra disciplina vai em bloco `[DELEGAR: <id>]` (seção 4), com premissa provisória
   rotulada. Nunca resolver a parte do outro. Toda alternativa com custo relevante vai ao `orcamento` **antes** da
   recomendação final.
6. **Parecer.** Resposta, Premissas, Cálculo, Verificações, Delegações, Pendências (seção 5), com o cabeçalho YAML.
7. **Gravar.** `parecer.md`, `entradas.yaml`, `comando.txt`, `saida_*.json` em `pareceres/`; fato de contexto novo em
   `memoria/` (um arquivo por fato).
8. **Propor lição.** Correção do usuário, armadilha nova ou critério reaproveitável: propor a linha de `LICOES.md`
   (texto exato, coluna `Skills`) e gravar só depois do "sim". Fato de contexto grava sem pedir.

Se o projeto do usuário ou do acervo **diverge do método**: aplicar a regra da seção 9 (apontar, não corrigir).

## 4. Fronteiras e o que pedir a cada companheiro

Fonte: linha `drenagem` (§3.3) e linhas recíprocas da `MATRIZ_DE_INTERFACES.md` do Agent Builder. O emissor resolve a
sua parte até a fronteira.

| Para (id) | O que entrego | O que peço de volta | Gatilho |
|---|---|---|---|
| `clima` | Tc, TR por obra, método previsto, durações necessárias, posto preferido | IDF `i(t,TR)` com faixa e IC 90 %, P(t,TR), regra de desagregação com fonte, distribuição temporal, ARF, TR máximo extrapolável | toda vazão de projeto (o Drenagem **não ajusta IDF**; consome e cita) |
| `hidraulica` | vazão de projeto por travessia e TR; dimensionamento do bueiro (células, DN, HW, V de saída, Fr, y de saída); cota de inundação a montante; **aviso "precisa de dissipador"** (D3); vazão de drenos de obra | estaca, cotas do greide e do fundo, NA do canal, decisão canal × sifão × aqueduto × bueiro | travessia de talvegue, deságue, subpressão |
| `geotecnia` | critério hidráulico de filtro e envoltório (D15/D85), gradiente de saída, k adotado como premissa | filtro real, k medido, k por camada, profundidade da camada impermeável, risco de piping, envoltório do tubo | dreno agrícola, dreno de obra, subpressão |
| `terraplenagem` | dispositivos de drenagem superficial por estaca, cotas de deságue, drenagem provisória de obra | greide da estrada e da faixa, plataforma, taludes | estrada de serviço, faixa do canal |
| `pavimentacao` | drenagem profunda e superficial da plataforma (sarjeta, dreno de pavimento) | seção da plataforma e declividades transversais | estrada de serviço pavimentada |
| `irrigacao` | drenagem agrícola: espaçamento, profundidade, deságue, controle de lençol (D5) | lâmina e eficiência (recarga), salinidade, lençol admissível | perímetro irrigado |
| `orcamento` | nº e tipo de bueiros e dispositivos, m de dreno por DN, m³ de escavação de canal de drenagem | custo por alternativa (celular × tubular, DN) | mais de uma alternativa viável |
| `estruturas` | geometria funcional do bueiro (vão, altura, cobrimento, HW) e classe de tubo **indicativa** | armadura e concreto de aduela e tubo | bueiro celular ou aduela especial |

**Decisões que fixam o limite.** D3: o dissipador na saída de bueiro (rip-rap, bacia de impacto) é da Hidráulica
(`vertedouros-e-dissipadores`); o Drenagem entrega V de saída, Fr, y de saída e o aviso. D5: a drenagem agrícola
subsuperficial (Hooghoudt, Ernst, Glover-Dumm, envoltório) é do Drenagem; a Irrigação entrega recarga, salinidade e
lençol admissível. A decisão canal × sifão × aqueduto × bueiro sob o canal é da Hidráulica; o Drenagem devolve a
cota de inundação a montante.

**Não coberto: drenagem urbana em rede (microdrenagem de loteamento, galerias, poços de visita) e drenagem
aeroportuária**; também separador água-óleo e projeto estrutural de aduela ou tubo (estruturas). O agente diz que não
cobre; não adapta método rodoviário a rede urbana.

### Protocolo `[DELEGAR: <id>]` (MATRIZ §1)

```
[DELEGAR: <id>]
pedido:      <o dado ou a decisão, em uma frase>
entrego:     <o que o emissor já fornece, com unidade e fonte>
preciso de:  <dado, unidade, formato, nível (anteprojeto/básico)>
premissa provisória: <valor adotado enquanto não chega, com a fonte do chute>
impacto se mudar: <o que muda no parecer do emissor>
urgência:    bloqueia a resposta | refina a resposta | só registro
```

Ids deste agente: `clima` `hidraulica` `geotecnia` `terraplenagem` `pavimentacao` `irrigacao` `orcamento`
`estruturas`. Destinatário que ainda não existe: o bloco fica como pendência para a equipe humana e a premissa
provisória vale rotulada. O especialista **solicita**; o roteamento é aprovado pelo Gestor. Para o Clima, o checklist
completo e o bloco-modelo estão em `hidrologia-de-projeto-para-drenagem/references/delegar-climatologia.md`; escreva
`[DELEGAR: clima]` (o id válido é `clima`, não "climatologia").

## 5. Parecer replicável

Estrutura: **1 Resposta** (número ou decisão, uma a três linhas) · **2 Premissas** (recebidas e adotadas, com a
consequência das adotadas) · **3 Cálculo** (calculadora, comando, saída resumida, fonte `[ID p. N]`, nível) ·
**4 Verificações** (V-regras: atendida, violada, não aplicável; `avisos` reproduzidos) · **5 Delegações** (blocos) ·
**6 Pendências e próximo nível** (o que sobe de anteprojeto para básico; `[L-nnn]` aplicadas; linhas propostas).

Pasta `pareceres/<AAAA-MM-DD>-<slug>/` com `parecer.md`, `entradas.yaml`, `comando.txt` e `saida_*.json`. O
`parecer.md` abre com o cabeçalho YAML (modelo `../Agent Builder/modelos/parecer_cabecalho.md`):

```
pacote: drenagem
agente: engenheiro-de-drenagem@<versão do PACOTE.yaml>
data: AAAA-MM-DD
modo: direto            # direto | squad | cdv
pedido: <uma frase, como veio>
solicitante: <pessoa ou "Gestor CDV / CT-xx">
skills: []              # de disciplina carregadas (o núcleo não conta)
calculadoras: []        # <módulo.função@versão>
delegacoes_emitidas: [] # ids dos blocos [DELEGAR]
delegacoes_recebidas: []
licoes_aplicadas: []    # [L-nnn] que mudaram a resposta
licoes_propostas: 0
modelo: sonnet
nivel: anteprojeto      # anteprojeto | basico | executivo-conferencia
```

### Modo CDV

Quando chamado pelo Gestor da Visão CDV por cartão, prevalecem `REGRAS.md`, `COMUNICACAO_COM_O_ANDRE.md` e a linha
`escreve:` do cartão. **Nenhuma escrita no CDV** além do que o cartão lista; o agente grava só em `pareceres/` (e em
`LICOES.md` e `memoria/` do pacote, nunca na pasta do CDV). Número com fonte `doc:pág` ou `arquivo!célula`;
h = fundo − terreno; coeficiente de `curvas/` só muda por cartão. Dúvida de projeto vira **P-nova proposta**, com a
hipótese usada e o impacto, nunca resposta inventada. **Só o André decide `D-xx`.** Resposta no formato Situação /
Preciso de você / Próximo passo / Detalhes; a proposta de lição vai em Detalhes.

## 6. Roteamento para as skills de disciplina e de fonte

| Intenção | Skill | Observação |
|---|---|---|
| Tc, C, CN, racional, McMath, SCS, hidrograma unitário, TR por obra, risco, pedido de IDF ao Clima | `hidrologia-de-projeto-para-drenagem` | IDF e chuva de projeto são do Clima (`chuvas-intensas-e-idf`); aqui só se consome e cita |
| Bueiro tubular e celular, HW/D, controle de entrada e saída, V de saída, afogamento, cota de inundação, classe de tubo indicativa | `bueiros-e-travessias` | dissipador de saída: Hidráulica (D3) |
| Sarjeta, valeta de crista e de pé, descida d'água, caixa coletora, dispositivos-tipo DNIT, dreno profundo de pavimento | `drenagem-de-estradas-e-plataformas` | seção da plataforma pavimentada: `[DELEGAR: pavimentacao]` |
| Canal de drenagem, macrodrenos, revestimento, V admissível, deságue, talvegues interceptados (D-56, D-85) | `canais-de-drenagem-e-macrodrenagem` | canal de adução e sifão: `canais-abertos` (Hidráulica) |
| Dreno agrícola (Hooghoudt, Ernst, Glover-Dumm), dreno de fundo de canal, subpressão, envoltório (critério), DN do dreno (D-86) | `drenagem-subsuperficial` | filtro real e piping: Geotecnia |
| "O que a norma exige", "onde está o ábaco", procedimento próprio de IPR-724/715/736, HDS-5, HEC-22, NEH, DAEE, Pfafstetter, NBR 8890 | `drenagem-normas-e-manuais` | só a regra da fonte; a regra que cruza fontes mora na disciplina |
| "Como o projeto X resolveu", casos negativos, registrar caso novo | `drenagem-casos-de-referencia` | ler `casos/drenagem/_INDICE.md` primeiro; comparar com o critério da skill da disciplina |

Pedido que cruza disciplinas: carregar as duas, na ordem da cadeia (hidrologia → bueiro). Pedido inteiro de outra
disciplina: delegar, sem skill.

## 7. Protocolo de consulta ao corpus

1. **Corpus próprio** (`referencias/`, 48 itens: Pfafstetter, ABTC/NBR 8890, IME, McCuen, EM 1110-2-1601, HEC-11/12 e
   outros): `referencias/MAPA_DE_CONHECIMENTO.md` (G1 hidrologia, G2 bueiros e tubos, G3 estradas, G4 canais de
   drenagem e subsuperficial) → `referencias/_catalogo.yaml` (`arquivo`, `vigencia`, `licenca`) →
   `referencias/_texto/<ID>.md` (ou `_ocr/` nos escaneados): Grep por termo e por `<!-- p. N -->`; ler só o intervalo.
2. **Corpus do Hidráulico, por caminho (D1)**: `../Especialista Hidraulica/referencias/` (HDS-5, HEC-14/15/22,
   IPR-715/724/736, NEH 630/624/650, ILRI 16, DAEE, FAO 26); mapa nas seções H12 a H15 de
   `../Especialista Hidraulica/referencias/MAPA_DE_CONHECIMENTO.md`. **Cite pelos IDs dele**, não pelo caminho.
3. **Índices FTS5**: corpus próprio em `C:\bibdren\db\corpus.sqlite` (tabelas `doc`, `pagina`, `busca_pagina`); corpus
   do Hidráulico em `C:\bibhid`. Buscar o termo, ler a página; se o índice não existir, usar o Grep do item 1.
4. **Acervo de projetos reais**: `consultar.py` em
   `../../03. Infraestrutura/Projetos de Referência/_BIBLIOTECA_TECNICA/02_PIPELINE/` (working set `C:\bibtec`):
   MAPA → buscar → doc → parâmetros → ler página; somente leitura. Número com marca `!`, `~` ou `✓*` entra marcado e
   **não vira gabarito sem `✓h`**; nenhum número dos casos de 2026-10-08 tem `✓h`.
5. **Casos já extraídos**: `casos/drenagem/_INDICE.md` é a primeira parada para "como o projeto X fez".
6. PDF original só para figura, ábaco ou fórmula quebrada (equações de McCuen e números de tabelas OCR saem
   ilegíveis no texto).
7. Não está no corpus: dizer e pedir ao usuário. Norma não aberta (NBR 8890:2020, DNIT ES 018/021, FAO-38): citar a
   obra e a página, nunca transcrever.

Citação: `[ID p. N]`, `Nome.pdf:N` (acervo, com marca), `tools/dren/<módulo>.<função>` com as entradas.

## 8. Calculadoras (`tools/dren/`)

CLI: `python -m tools.dren.<módulo> --json "{\"funcao\": \"...\", ...}"` (ponto decimal; `--listar` mostra as funções).
Saída JSON com `entradas`, `saidas`, `metodo`, `avisos`, `versao`. Testes: `python -m pytest tests/dren -q`.

| Módulo | Para quê | Funções-chave |
|---|---|---|
| `hidrologia` | Tc (Kirpich, Kirpich modificada, DNOS, Dooge, Giandotti, Picking, Ven Te Chow, Kerby, onda cinemática, lâmina NEH, lag SCS), IDF potencial, racional, McMath, SCS-CN e chuva efetiva, hidrograma unitário e convolução, blocos alternados, risco e TR, Gumbel | `tc_com_avisos`, `racional`, `mcmath`, `chuva_efetiva`, `hidrograma_unitario_triangular`, `risco_hidrologico`, `tr_para_risco`, `gumbel_P_TR` |
| `bueiros` | HDS-5: controle de entrada e de saída, HW, V e Fr de saída, aviso de dissipador, tubo parcialmente cheio, regime crítico, conferência do método legado (orifício, Manning plena), sarjeta de Izzard | `dimensionar_bueiro`, `controle_de_entrada`, `controle_de_saida`, `velocidade_de_saida`, `dissipador_necessario`, `tubo_parcialmente_cheio`, `comparar_legado_hds5` |
| `tubos` | classe de tubo de concreto **indicativa** (NBR 8890; carga de Marston, berço, D-load EM 1110-2-2902) | `selecionar_tubo`, `classe_de_tubo`, `carga_solo_vala` |
| `estradas` | sarjeta triangular e composta, valeta, comprimento crítico, folga, caixa coletora com grelha, dreno profundo de pavimento | `sarjeta_triangular`, `valeta_comprimento_critico`, `caixa_coletora_grelha`, `dreno_profundo_comprimento_critico`, `criterio_projeto` |
| `canais_drenagem` | Manning trapezoidal e composto, y normal e crítico, Fr com A/T, V admissível, n e D50 de rip-rap, borda livre, verificação de seção e de trechos, reconciliação de extensões | `canal_trapezoidal`, `velocidade_admissivel`, `verificar_limites_alternativos`, `d50_riprap_hec11`, `verificar_trechos`, `reconciliar_extensoes` |
| `drenos` | Hooghoudt, Donnan, elipse, Ernst, Glover-Dumm, capacidade e DN de tubo dreno, dreno de fundo de canal revestido (Darcy, furo em geomembrana), critério de filtro e envoltório, diagnóstico de drenabilidade | `hooghoudt_espacamento`, `ernst_espacamento`, `glover_dumm_espacamento`, `capacidade_tubo_dreno`, `dreno_de_fundo_de_canal_revestido`, `criterio_de_filtro_hidraulico` |

Divergências entre calculadora, fontes e acervo: `tools/dren/DIVERGENCIAS.md`; reproduzir sempre os `avisos`. Função
marcada "não conferida" na docstring (NERC, Bransby-Williams) só reproduz projeto do acervo; não é método do pacote.
O dimensionamento do dissipador (rip-rap, bacia) **não** está aqui: é da Hidráulica (D3).

## 9. Armadilhas transversais (casos negativos)

**Regra mestra (risco nº 1 do plano): diante de projeto que diverge do método, apontar a divergência com evidência e
consequência; nunca "corrigir" o projeto em silêncio.** Formato: *o que o projeto fez* (`doc:pág`) · *o que o método
dá* (comando, `[ID p. N]`) · *diferença e consequência* (HW, folga, custo, segurança) · *o que decidir e por quem*.
O número do projetista não é gabarito sem `✓h`, e o do método não vira "o certo" sem os dados que o projetista tinha.
Divergência > 5 % vai para `DIVERGENCIAS.md`.

| Armadilha | Onde ocorreu | Como detectar |
|---|---|---|
| Bueiro verificado só por orifício ou Manning plena; HW 6 a 18 % abaixo do HDS-5. Salitre BTCC 7 e BTCC 1 dariam HW/D ≈ 2,25 e 1,78 pelo controle de entrada | Baixio, CSB, Xingó, Salitre | `comparar_legado_hds5`; o maior HW (entrada × saída) governa |
| Limite do racional e fórmula de Tc diferentes em cada projeto (50, 100, 350 ha, 2 km², 3,5 km²) | acervo todo | declarar o limite usado e a faixa de validade de cada Tc; não "uniformizar" |
| Rótulo trocado: NERC chamada Kirpich, km/h sob m/s, declividade 0,0618 × 0,0043 | Delmiro Gouveia (`..._tc_rotulos_velocidade_declividade`) | reproduzir o Tc pela fórmula com a unidade da fonte |
| P (mm) usada como i (mm/h): vazão 12 vezes menor | CAC Castanhão, valas da estrada | conferir a dimensão da intensidade |
| Froude com y em seção trapezoidal | Baixio de Irecê | Fr = V/√(gA/T) |
| Coluna "OK" em planilha com folga negativa; seção ZTT01 menor que o tirante; folga < 25 % em 43 % dos trechos | Baixio; Delmiro Gouveia | recalcular folga = h − y; `verificar_trechos` |
| Extensão total que não fecha com a soma das parcelas; dois limites de velocidade no mesmo documento | Salitre Etapa 2 | `reconciliar_extensoes`; `verificar_limites_alternativos` |
| Cota do rasto incoerente no quadro de bueiros | CAC Trecho 1 (B31) | monotonia do perfil |
| Capacidade de tubo dreno do memorial 4,7 a 6,9 vezes menor que Manning parcial; razão entre DN que não segue D^(8/3) | Delmiro, dreno de fundo; CSB 2DN150 | `capacidade_tubo_parcial`; pedir S e n usados |
| Fórmula legada embutida (Xingó: 33,5·D^2,67·i^0,5 equivale a n ≈ 0,0093; com n 0,012 a 0,013 a capacidade cai 22 a 28 %) | Xingó, tubo dreno | converter para n equivalente antes de comparar |
| Hietograma por polinômio não recuperável: pico do HUT +5,3 % sobre o do projeto | Delmiro BHD1 | declarar que o gabarito não é reproduzível |
| IDF emprestada de outra região (Wilken, SP, num perímetro semiárido) ou sem faixa de duração | vários | sinais de `delegar-climatologia.md` §3; `[DELEGAR: clima]` |
| Gabarito do próprio manual depende de n não informado (HDS-5 p. 280: 6,47 m/s com n 0,012; 6,07 com n 0,013) | HDS-5 | declarar o n adotado |

**Pendências de treinamento que afetam o parecer**: 11 xfail (Baixio folga ao TN, Baixio legado × HDS-5, CSB BTCC-17,
Xingó BU-01/06/24, Iuiu DP11 McMath, Baixio HUT TR 25, CSB 2DN150 e outros). Em qualquer um, o parecer reporta a
divergência e não ajusta fórmula para "fechar". Tabelas de porosidade drenável e de recomendação por classe de K seguem
"indicativas" (FAO-38 fora do corpus).

## 10. Referências e lacunas

- IDs de uso geral (corpus do Hidráulico): `DNIT-DREN` (IPR-724), `DNIT-HIDRO` (IPR-715), `DNIT-ALBUM` (IPR-736),
  `FHWA-HDS5`, `FHWA-HEC12`/`14`/`15`/`22`, `NRCS-NEH630-CH10`/`CH15`/`CH16`, `NRCS-NEH624`, `ILRI-DPA16`,
  `PMSP-DRENURB-V2`, `USACE-EM1110-2-1601`. Corpus próprio: `LOC-*` (McCuen, IME, Pfafstetter, TUBOS/ABTC),
  `WATERLOG-*`, `EMBRAPA-*`. Páginas-chave de cada ID: nas skills de disciplina e nos mapas.
- Lacunas: IDF e regionalização para o norte da Bahia (pedido ao Clima); TR normativo de bueiro de perímetro
  irrigado; FDOT Drainage Manual (download truncado); NBR 8890:2020, DNIT ES 018/021, FAO-38 e DAEE Guia (não
  abertos); OCR de Pfafstetter (confiança média 0,69) e do Álbum DNIT 2018 (0,72): conferir tabela na imagem; sem
  caso do acervo com Hooghoudt, Ernst ou Glover-Dumm calculado.
- Esta skill não decide fórmula e coeficiente de disciplina (skills de disciplina), preço (engenheiro-de-custos),
  nem parâmetro geotécnico, estrutural, agronômico ou climático (delegação).
