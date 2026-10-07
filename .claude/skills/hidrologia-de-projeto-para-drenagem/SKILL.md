---
name: hidrologia-de-projeto-para-drenagem
description: >
  Transforma chuva em vazão de projeto para drenagem de perímetro irrigado: tempo de concentração (Kirpich e sua
  faixa, Kirpich modificada DNIT, California Culverts, DNOS, Giandotti, Dooge, Kerby), método racional (C por uso
  do solo e TR, limite de área e divergências DNIT, DAEE, PMSP, acervo), McMath, SCS-CN (CN, Ia, hidrograma
  unitário triangular, blocos alternados), Gumbel, TR por obra, risco hidrológico, forma da IDF, o que pedir à
  Climatologia e a lacuna de chuva de projeto do semiárido baiano. Use quando: "vazão de projeto da bacia",
  "tempo de concentração", "Kirpich", "método racional", "coeficiente C", "McMath", "SCS", "número da curva CN",
  "hidrograma unitário", "hietograma", "Gumbel", "TR do bueiro", "risco na vida útil", "a IDF serve?",
  "racional vale até quantos hectares?". Não use para: dimensionar bueiro, canal, sarjeta ou descida d'água (use
  bueiros-e-drenagem-superficial); dreno de parcela (use drenagem-subsuperficial); amortecimento em reservatório
  e vertedouro (use reservatorios-e-pequenas-barragens, vertedouros-e-dissipadores); gerar IDF e séries
  (Climatologia); demanda de irrigação (Irrigação); preço (engenheiro-de-custos).
---

# Hidrologia de projeto para drenagem de perímetro irrigado

Convenções, V1-V12, delegação e parecer estão em `hidraulica-fundamentos` e no perfil do agente. Tabelas longas em `references/`: `tc-formulas.md`, `coeficiente-c-racional.md`, `cn-scs.md`, `tr-por-obra.md`, `delegar-climatologia.md`, `gabaritos-numericos.md`.

## 1. Escopo e fronteiras

**Entrega:** vazão de pico (e, quando preciso, hidrograma) por bacia, TR e método, com Tc, C ou CN, IDF e faixa de validade declarados.

**Decisão D7:** a Climatologia entrega a IDF e a chuva de projeto com incerteza. O hidráulico escolhe método e TR e calcula a vazão. Não gera IDF por conta própria.

**Fronteiras (um parágrafo, sem invadir):**
- A obra que usa a vazão (bueiro, HW/D, canal, sarjeta, descida): `bueiros-e-drenagem-superficial`. Esta skill entrega Q e termina.
- Dreno subsuperficial: `drenagem-subsuperficial` (recarga e K não são desta skill).
- Amortecimento em reservatório ou barragem: aqui só se menciona que a cheia pode ser laminada e que a duração da chuva de projeto deve então ser bem maior que Tc [PMSP-DRENURB-V2 p. 33]; o cálculo é de `reservatorios-e-pequenas-barragens`.
- Séries, IDF primária, ARF, tendência: Climatologia (`[DELEGAR: climatologia]`, ver `references/delegar-climatologia.md`).
- Grupo hidrológico do solo (Ksat) e uso do solo final: Geotecnia e projeto agronômico (`[DELEGAR: geotecnia]`).
- Simulação distribuída de bacia grande (HEC-HMS, propagação, calibração): consultoria (D2). Só se aponta quando indicado (seção 3.6).

**Nível de projeto:**
- Anteprojeto (padrão): racional ou McMath em bacia pequena, SCS-CN com HU triangular acima, Tc por duas fórmulas, IDF tabelada recebida da Climatologia, TR por obra com risco calculado. Margem de erro da vazão: sem valor no corpus; o DNIT mostra razão de 5 entre fórmulas de Tc em bacias < 2,5 km² [DNIT-HIDRO p. 85] e +28 % do racional sobre outro método em 10,5 km² [p. 131].
- Projeto básico: hietograma por blocos alternados com durações ≥ Tc, convolução com HU, ARC declarado e sensibilidade, calibração com vazão observada se houver.
- Executivo: conferir o que a projetista entregou (D2).

## 2. Dados mínimos específicos

Pedir antes de calcular; o que faltar vira premissa rotulada.

1. Bacia: área, comprimento do talvegue L, desnível H (ou S), declividade média, forma; delimitada em planta com divisor.
2. Uso e cobertura **final** (perímetro implantado), solo e grupo hidrológico (Ksat de Geotecnia), lençol raso ou camada restritiva.
3. TR de projeto e de verificação por obra (`references/tr-por-obra.md`) e vida útil.
4. IDF local com faixa de validade e incerteza, ou P(t, TR) tabelada (`references/delegar-climatologia.md`).
5. Para HU: duração de chuva de projeto, distribuição temporal, ARC. Se há reservatório a jusante, o volume.
6. Existência de vazão observada (posto, n de anos) na bacia ou em bacia semelhante.

## 3. Método por nível

### 3.1 Qual método por tamanho de bacia (divergências entre fontes)

| Fonte | Racional até | Acima |
|---|---|---|
| FHWA HDS-2 | < 200 acres (≈ 81 ha), "geralmente" [p. 90-91, 181]; HEC-22 repete 80 ha [p. 57] | Hidrograma unitário |
| NRCS EFH cap. 2 (gráfico) | método de pico válido de 1 a 2.000 acres (0,4 a 810 ha) [NRCS-NEH650-CH02 p. 11] | TR-55 ou TR-20 |
| DAEE-SP IT DPO 11 | 2 km² [DAEE-IT-DPO11 p. 1] | Não define o método |
| PMSP-V2 | < 3 km² ou tc < 1 h [PMSP-DRENURB-V2 p. 53] | — |
| ABDER | ≤ 4 km² (C de Peltier); 4 a 10 km² racional com coeficiente de retardo φ = 1/(100·A)^(1/n), n = 4, 5, 6 conforme a declividade; > 10 km² HU triangular [ABDER-APOSTILA p. 53-55, 59] | HUT |
| DNIT IPR-715 | Sem teto; "de preferência bacias pequenas", aplicável a maiores com fator de distribuição A^-0,10 [DNIT-HIDRO p. 129, 131]; para pontes e bueiros sem fluviometria indica o HU sintético [DNIT-HIDRO p. 57] | — |
| Acervo | Iuiu: 50 ha racional, 50 a 400 ha média de McMath e CN (ignora valor menor que o racional), > 400 ha CN [doc 1051:316]; Baixio: 100 ha; CSB: 350 ha (350 a 2.000 ha HUT de uma ordenada, > 2.000 ha 11 ordenadas) [doc 1341:46]; Xingó: A < 2 km² ou Tc < 1 h [doc 1419:26] | HUT |

**Regra do agente (decisão desta skill, não norma):** racional puro até 80 a 100 ha; de 100 ha a 2 km² racional com Cd = A^-0,10 e conferência por McMath ou SCS-CN; de 2 a 3,5 km² só com justificativa e comparação com HUT-SCS; acima de 3,5 km² ou Tc > 1 h, SCS-CN com HUT. Declarar o limite adotado e quais fontes o sustentam. Mostrar a vazão por dois métodos e adotar a maior com justificativa; diferença > 30 % entre métodos exige explicação.

### 3.2 Tempo de concentração

Tabela com fórmula, unidades, faixa e fonte: `references/tc-formulas.md` (Kirpich, California Culverts, Kirpich modificada, DNOS, Kerby, Giandotti, Dooge, SCS lag, Lag, método da velocidade). Pontos operativos:
- Kirpich e California são **a mesma fórmula** (0,95·(L³/H)^0,385 h) e foram calibradas em bacias de 0,004 a 0,45 km² (DNIT: < 0,8 km²) [FHWA-HDS2 p. 80; DNIT-HIDRO p. 88]. Fora disso dão Tc curto (vazão alta).
- Kirpich modificada do DNIT = 1,42·(L³/H)^0,385 h, isto é, Kirpich × 1,5, indicada para qualquer área e padrão quando não há dado observado [DNIT-HIDRO p. 90, 98]. DNOS com K = 4 é a outra indicada [DNIT-HIDRO p. 94]. Mostrar as duas e a razão.
- Giandotti é para bacia grande; Kerby só para o trecho de escoamento sobre o terreno (L ≤ 365 m).
- Perímetro plano (S < 0,5 %): várias fórmulas saem da faixa [NRCS-NEH650-CH02 p. 11]; usar método da velocidade com Manning e declarar.
- Tc mínimo 15 min [ABDER-APOSTILA p. 67]. Duração da chuva do racional = Tc [DNIT-HIDRO p. 127].
- Bacia com trechos de declividades muito diferentes: somar por parte [DNIT-HIDRO p. 98].

### 3.3 Método racional

Q[m³/s] = C·i·A/3,6 (A em km², i em mm/h) = C·i·A/360 (A em ha) [DNIT-HIDRO p. 127; FHWA-HDS2 p. 181]. No `_texto` do DNIT a equação sai com "6,3"; é 3,6 (o exemplo da p. 130 só fecha com 3,6: 0,1828 × 101,0 × 2,4/3,6 = 12,31 m³/s).

- i = IDF(t = Tc, TR). C por uso, solo, declividade e TR: `references/coeficiente-c-racional.md`. C ponderado por área.
- **Cd** (distribuição): Q × A^-0,10 (A em km²) para bacias > 1 km² [DNIT-HIDRO p. 131]; Burkli-Ziegler A^-0,15 (A em ha, urbano) [p. 132]. O CSB usa Cd = A^-0,10 desde 100 ha. Cd não está embutido na função `racional`: multiplicar C por Cd ou Q por Cd e dizer qual.
- C por TR: a forma C_T = 0,8·T^0,1·C10 é do acervo (CSB), a equação-fonte do PMSP está em imagem (a confirmar); o FHWA não endossa fator de frequência [FHWA-HEC22 p. 56-57]. Usar só em anteprojeto e rotular.
- Vários trechos ou sub-bacias: usar o maior tc para a bacia total e checar a condição crítica com o tc menor [FHWA-HDS2 p. 183-184].

### 3.4 McMath

Forma do acervo (Iuiu, CDV): Q[m³/s] = 0,0091·C·i·A^0,8·S^0,2, com i em mm/h, A em ha, S em m/m [doc 1051:317]. Origem: fórmula do USBR, em unidades inglesas, para estágio de planejamento de drenagem agrícola: Q = C·i·s^0,2·A^0,8 (cfs, pol/h, s em m por 1.000 m, acres), C de 0,20 a 0,75 [USBR-DRAINAGE p. 57-58]. **A constante 0,0091 é a conversão exata** (0,02832/25,4 × 2,471^0,8 × 1.000^0,2 = 0,00915, com S em m/m). Com S em m/km vale 0,0023 [EMBRAPA-DREN-SUP p. 5].
- S é a declividade do **canal principal** entre o ponto mais remoto e o ponto de concentração [USBR-DRAINAGE p. 57], não a do dreno projetado nem a média da bacia (a docstring da calculadora diz "média da bacia": conferir).
- C de McMath tem tabela própria (soma de vegetação, solo e topografia; `references/coeficiente-c-racional.md` 1.5). Não misturar com C do racional.
- Faixa: o corpus não dá limite de área. O Iuiu usa 50 a 400 ha (prática do acervo). Aviso da função fora de 50 a 400 ha.
- Caso Iuiu DP11 (A = 189 ha): projeto 2,34 m³/s, calculadora 2,90 (+24 %). Ver Armadilhas.

### 3.5 SCS-CN e hidrograma

Tabelas de CN, grupo hidrológico, ARC e ponderação: `references/cn-scs.md`. Passos:
1. HSG por Ksat (Geotecnia); CN por uso, tratamento e condição; ARC declarado; S = 25.400/CN − 254 (mm); Ia = 0,2·S [NRCS-NEH630-CH10 p. 10].
2. Chuva de projeto P(t) e hietograma. **Blocos alternados:** obter i(t) na IDF para t = Δ, 2Δ, …, td; converter em altura acumulada; tomar os incrementos; pôr o maior bloco no centro e os demais alternadamente em ordem decrescente de cada lado [PMSP-DRENURB-V2 p. 21-22]. Sem função na calculadora (ver seção 4). Duração ≥ Tc; com reservatório, bem maior (3 h e 6 h no PMSP) [p. 33]. DNIT: os seis maiores acréscimos se reordenam como 6, 4, 3, 1, 2, 5 [DNIT-HIDRO p. 75]. Baixio: duração total ≈ 2·Tc em 12 blocos (caso).
3. Chuva efetiva incremental pelo acumulado (`hietograma_para_efetiva`).
4. HU triangular SCS: tlag = 0,6·Tc [NRCS-NEH630-CH15 p. 8]; ΔD (duração unitária) = 0,133·Tc = Tc/7,5 [NRCS-NEH630-CH16 p. 16; DNIT-HIDRO p. 102]; ΔD ≤ 0,2 a 0,25·tp [DNIT-HIDRO p. 99]; tp = ΔD/2 + tlag; tb = 2,67·tp (8/3); qp = 0,208·A/tp (m³/s por mm, A em km², tp em h; é o 484 inglês convertido) [NRCS-NEH630-CH16 p. 33-34; DNIT: QP = A/(0,03·TB), TB em min, p. 102]. HEC-22 usa tp = (2/3)·tc [FHWA-HEC22 p. 66], igual a ΔD = 0,133·Tc.
5. Fator de pico 484 (0,208 em SI) vale para o hidrograma padrão; o NRCS cita de cerca de 600 em terreno íngreme até 100 ou menos em terreno plano e alagadiço [NRCS-NEH630-CH16 p. 34]; o HEC-22 cita ~300 em terreno plano [FHWA-HEC22 p. 66]. Perímetro plano: 484 é premissa, mostrar sensibilidade; fator menor reduz o pico.
6. Convolução (`convolucao_hu`). Pico = máximo da série.

Limites do método: CN de 40 a 98; Ia = 0,2·S fixa o CN (não trocar por 0,05 sem outro conjunto de CN); fraco com chuva pequena e CN baixo; mal no semiárido do sudoeste dos EUA [NRCS-NEH630-CH10 p. 10, 25]; perdas por transmissão em canais secos podem eliminar o escoamento [p. 7]; não substitui infiltração dentro da tempestade [p. 23].

### 3.6 Bacias maiores (só apontar)

Acima de ~50 km² ou com reservatórios, confluências e propagação: dividir em sub-bacias, hidrogramas por sub-bacia, propagação em canal e amortecimento. É modelagem tipo HEC-HMS (consultoria, D2). O que o hidráulico entrega: Tc por sub-bacia, CN ou C, IDF, TR, o hidrograma triangular e o pico de cada sub-bacia, e a lista do que a consultoria deve modelar. Redução de chuva por área: FA = 1 − 0,10·log10(A/25), FA ≤ 1 (A em km²; procedimento B do DNIT) [DNIT-HIDRO p. 74, 108]; a forma por duração vale para A > 5 km² [p. 71, 74]. Bacia > 400 km² com fluviometria: estatística de vazões [DNIT-HIDRO p. 34-35].

### 3.7 Estatística de máximos

- **Gumbel por momentos:** β = s·√6/π; μ = x̄ − 0,5772·β; P(TR) = μ − β·ln(−ln(1 − 1/TR)). É a forma de amostra infinita (função `gumbel_P_TR`).
- **Fator de frequência com n:** X_T = x̄ + K·s, K = (y − ȳn)/σn [DNIT-HIDRO p. 35-37]; HDS-2 tabela K por n [FHWA-HDS2 p. 132, Tab. 5.13]. Exemplos de K (TR 25 / TR 100): n = 10 → 2,85 / 4,32; n = 20 → 2,52 / 3,84; n = 30 → 2,39 / 3,65; n = 100 → 2,19 / 3,35; infinito → 2,04 / 3,14. **A forma por momentos subestima o quantil em amostra pequena:** com n = 10 e TR 25 dá 112,3 mm contra 126,8 mm com K de n (−11 %, série de exemplo do módulo de teste).
- Nenhuma lei é "melhor" [DNIT-HIDRO p. 34]; Gumbel, Hazen e Log-Pearson III são as do DNIT. Para vazão, o HDS-2 adota Log-Pearson III com assimetria regional (Bulletin 17C, EMA) [FHWA-HDS2 p. 93, 134]. GEV: não detalhada no corpus; mencionar como alternativa e pedir à Climatologia a distribuição ajustada.
- TR extrapolado acima de 2n anos: incerteza grande (aviso da função). Pedir intervalo de confiança à Climatologia.

### 3.8 TR e risco

TR por obra, tabela de fontes e prática do acervo: `references/tr-por-obra.md`. Risco J = 1 − (1 − 1/TR)^n [DNIT-HIDRO p. 24; PMSP-DRENURB-V2 p. 29]. Sempre reportar TR de projeto, TR de verificação e J na vida útil. Não há função na calculadora.

### 3.9 IDF

Forma i = a·TR^b/(t + c)^d, mm/h e t em min (CSB grupo 1, Plúvio 2.1: a = 5.590,88; b = 0,241; c = 40,11; d = 1,091; doc 1341:36). Wilken (São Paulo): i = 57,71·TR^0,172/(t + 22)^1,025 em mm/min, vale de 10 a 1.440 min [PMSP-DRENURB-V2 p. 19]. DNIT (Pfafstetter): P = P0·K·FS·FA com K = TR^(α + β/TR^0,25) [DNIT-HIDRO p. 107-108]. A intensidade do racional é i = P(Tc)/Tc [DNIT-HIDRO p. 128]. Pedido à Climatologia, checklist e sinais de IDF emprestada: `references/delegar-climatologia.md`. A calculadora não gera a IDF: `idf_potencial` aplica os parâmetros recebidos e avisa fora da faixa se `faixa_TR` e `faixa_t` forem passadas (passá-las sempre).

### 3.10 Chuva de projeto do semiárido baiano (lacuna declarada)

O corpus **não traz IDF, CN, C nem hietograma validados para o semiárido baiano.** O que existe é rastro do acervo, não gabarito: P1dia de TR 5 a 100 no Iuiu de 94 a 153,9 mm, TR 10 = 108,5 mm (Gumbel, doc 1051:320); P24h média de TR 10 em Irecê/Xique-Xique/Barra/Bom Sucesso de 101,2 mm (doc 670:113); Plúvio 2.1 por grupos de postos no CSB (doc 1341:36). Consequências: (1) pedir IDF e chuva de projeto à Climatologia com incerteza; (2) CN e C tomados de tabelas americanas ou rodoviárias são premissa; (3) comparar sempre dois métodos; (4) o método CN concorda mal no semiárido [NRCS-NEH630-CH10 p. 25] e há perda por transmissão em canal seco [p. 7]; (5) calibrar com vazão observada ou evento conhecido, se houver; (6) rótulo "lacuna do corpus" no parecer.

## 4. Calculadoras (mapa fórmula → função → teste)

`python -m tools.hid.hidrologia --json '{"funcao": "<nome>", ...}'` (campos planos ou dentro de `args`; `--listar` não existe neste módulo, a lista sai com função desconhecida). A saída traz `avisos`: reproduzi-los no parecer.

| Cálculo | Função (CLI) | Exemplo de entrada | Teste | Conferir nos `avisos` |
|---|---|---|---|---|
| IDF potencial | `idf_potencial` | `{"funcao":"idf_potencial","TR":100,"t":112,"a":5590.88,"b":0.241,"c":40.11,"d":1.091,"faixa_t":[10,1440]}` | `test_idf_potencial_csb_grupo1`, `test_idf_potencial_aviso_faixa` | extrapolação em TR e t |
| IDF tabelada | `idf_tabela` (Python) | tabela (t, i) ou {TR: tabela} | `test_idf_tabela_interpola_log_e_avisa` | t ou TR fora da tabela |
| Tc | `tc` com `metodo`: `kirpich` (L m, S), `california_culverts`, `kirpich_modificada_dnit` (L km, H), `giandotti` (A, L, Hm), `dooge`, `dnos`, `kerby` | `{"funcao":"tc","metodo":"kirpich_modificada_dnit","L":2.9,"H":12}` | `test_kirpich_bacia_tipica`, `test_kirpich_aviso_fora_de_faixa`, `test_california_culverts_e_giandotti_kerby_dooge`, `test_xingo_kirpich_s1` | faixa de Kirpich (aviso sempre aparece); **não usar `dnos`** (seção 6) |
| Racional | `racional` | `{"funcao":"racional","C":0.25,"i":69.5,"A":211,"unidade_area":"ha","limite_km2":3.5}` | `test_racional_unidades`, `test_racional_aviso_acima_de_2km2`, `test_csb_bacia45_racional`, `test_iuiu_dp08_racional` | A acima de `limite_km2` (padrão 2): declarar o limite adotado |
| C por TR, Cd | `coef_c_para_tr`, `coef_distribuicao` (Python) | C10, TR; A em km² | `test_csb_bacia45_racional` | C ≤ 1 |
| McMath | `mcmath` | `{"funcao":"mcmath","C":0.3,"i":41.9,"A":189,"S":0.0028}` | `test_mcmath_faixa`, `test_iuiu_dp11_mcmath` (xfail) | A fora de 50 a 400 ha |
| Critério do Iuiu | `vazao_adotada_iuiu` (Python) | A, Q racional, McMath, CN | `test_iuiu_criterio_media` | — |
| CN, chuva efetiva | `chuva_efetiva`, `retencao_S`, `hietograma_para_efetiva` | `{"funcao":"chuva_efetiva","P":129.54,"CN":75}` → 64,3 mm | `test_scs_chuva_efetiva_neh`, `test_hietograma_para_efetiva_soma_igual_total` | `lam` = 0,05 não reajusta o CN |
| HU triangular, convolução | `hu_triangular`, `convolucao_hu` | `{"funcao":"hu_triangular","A_km2":3.234,"Tc_h":0.9633,"D_h":0.16055}` | `test_hu_triangular_geometria`, `test_baixio_hu_geometria_e_qp`, `test_convolucao_conserva_volume`, `test_baixio_hut_pico_tr25` (xfail) | passo da convolução D ≈ Tc/7,5 a Tc/6; pico depende do hietograma |
| Gumbel | `gumbel` | `{"funcao":"gumbel","serie_maximos_anuais":[...],"TR":25}` | `test_gumbel_momentos_e_aviso`, `test_csb_gumbel_iuiu_pdia` | n < 20; TR > 2n; **forma de amostra infinita** |

**Sem função (usar cálculo documentado e rotular, ou abrir pendência):** blocos alternados; risco J; K de Gumbel por n (Tab. 5.13); SCS lag e Lag Kn; DNOS conforme o DNIT; Cd dentro do racional; conversão ARC; fator de pico variável. Calculadora não é editada pelo agente (guardrails).

Conferências numéricas com primário (candidatas a teste novo): `references/gabaritos-numericos.md`.

## 5. Critérios de projeto e verificação (antes de entregar)

1. **V8:** método compatível com a área e Tc, limite declarado com fontes (3.1); duas vazões por métodos diferentes; diferença > 30 % explicada.
2. **Tc:** mais de uma fórmula, razão entre elas, fórmula escolhida com faixa; unidades de L e S de cada função (L m em `kirpich`, km nas demais); Tc ≥ mínimo; Tc dentro da faixa da IDF.
3. **IDF (D7):** origem, faixa, incerteza e TR; i em mm/h; Q com limite superior da IDF quando houver intervalo. Sem IDF, bloco `[DELEGAR: climatologia]` e premissa rotulada (V12).
4. **C:** fonte, declividade, uso final, TR; C_T ≤ 1; Cd declarado.
5. **CN:** HSG com Ksat (delegado), ARC declarado com sensibilidade (CN II e III), Ia = 0,2·S, CN de 40 a 98.
6. **Sensibilidade mínima:** Tc ±20 %, C ±0,05 ou CN ±5, IDF no limite do intervalo. Dizer o quanto Q muda.
7. **TR (V8):** TR de projeto, de verificação e risco J na vida útil (`references/tr-por-obra.md`); o TR é premissa do contratante ou do projetista (D2).
8. **V1/V11:** comando e saída gravados; edição citada: IPR-715 (2005), IPR-724 (2006), HDS-2 3ª ed., HEC-22 4ª ed. (2024), NEH-630 cap. 9, 10 (2004), 15 (rascunho 2008), 16 (2007), USBR Drainage Manual (1993), PMSP vol. 2 (2012), DAEE IT DPO 11 (2017). A norma aplicada à obra (DNIT, DAEE) é norma de rodovia ou de São Paulo; dizer que é referência.

## 6. Armadilhas do acervo e da calculadora (casos negativos)

| Armadilha | Onde | Como detectar e tratar |
|---|---|---|
| McMath +24 % (2,90 contra 2,34 m³/s) no DP11 do Iuiu | `DIVERGENCIAS_bueiros.md` | S e Tc usados são do dreno, não da bacia; coluna "i" sem rótulo (41,9 mm/h daria 2,34). Pedir S do talvegue da bacia [USBR-DRAINAGE p. 57]; não ajustar a calculadora (D11) |
| Constante 0,0091 com S em % ou em m/km | Qualquer uso de McMath | S em % multiplica Q por 2,5; em m/km, por 4. Conferir a unidade de S contra 0,0091 (m/m) ou 0,0023 (m/km) |
| HUT do Baixio não reproduzido (6,03 contra 2,70 m³/s) | `DIVERGENCIAS_bueiros.md` | Geometria do HU confere (tp 0,658 h; tb 1,758 h; qp 10,22 m³/s por 10 mm; S 155,39 mm), mas o hietograma (tabela T-K, "Soma(p)") e a lâmina efetiva (3,3 mm) não estão no acervo. Sem hietograma, não reproduzir pico |
| Limite do racional diferente por projeto (50, 100, 350 ha, 2 km²) | Iuiu, Baixio, CSB, Xingó | Declarar o limite e a fonte; ver 3.1 |
| `dnos` da calculadora ≠ fórmula DNIT | `tools/hid/hidrologia.py` | 19,3 min contra 45,5 min no mesmo caso; K divide no DNIT. Usar a forma DNIT em Python à parte e abrir pendência |
| Unidade de L: `kirpich` em m, `kirpich_modificada_dnit` e `california_culverts` em km | `tools/hid/hidrologia.py` | Conferir o `entradas` da saída |
| Gumbel de amostra infinita (K 14 % a 28 % menor que o K de n, para n de 30 a 10, em TR 25 e 100) | `gumbel_P_TR` | Usar K de n (HDS-2 Tab. 5.13) para TR ≥ 25; aviso só diz "n < 20" |
| `chuva_efetiva(lam=0,05)` com CN de Ia = 0,2·S | `hidrologia.py` | O NRCS exige outro conjunto de CN [NRCS-NEH630-CH10 p. 10]; só usar 0,2 |
| Intensidade com unidade errada (mm/min no texto, mm/h nos números) | Iuiu 1051:318 | Refazer a conta e fechar com o valor do projeto (DP08: 0,83 m³/s) |
| Linha da Tab. 4.1 rotulada "Racional" com área > 350 ha | CSB 1341:145 | Era HUT (bacia 49, 2.889 ha, 110,35 m³/s); usar a coluna do PDF |
| "6,3" no lugar de 3,6 e "horas" no lugar de minutos (Picking) | DNIT-HIDRO `_texto` p. 127 e 88 | Fórmula só fecha com 3,6; conferir PDF |
| CN "cultivado Boa" do DNIT (51 a 80) como se fosse cultura em fileira | DNIT-HIDRO Tab. 11 | A cultura em fileira do NRCS dá 67 a 89; ver `references/cn-scs.md` 3.3 |
| Média ponderada de CN com partes muito diferentes | Bacias mistas | Ponderar Q se os CN diferem muito [NRCS-NEH630-CH10 p. 17] |

## 7. O que a norma e o manual exigem (resumo; detalhe em `normas-e-manuais`)

- **DNIT IPR-715:** HU sintético SCS para pontes e bueiros sem fluviometria; Tc por Kirpich modificada ou DNOS; racional com fator de distribuição; TR 10 a 20 em bueiros e 50 a 100 em pontes; bueiro dimensionado com TR 10 e verificado com 20 ou 25 [DNIT-HIDRO p. 23-24, 57, 98, 131]. **IPR-724:** racional nos dispositivos locais, C por superfície [DNIT-DREN p. 160, 224]. Norma de rodovia: em perímetro é referência.
- **DAEE-SP IT DPO 11:** racional até 2 km²; TR mínimo 25 (rural) e 100 (urbano ou obra maior); C mínimo 0,25 e CN mínimo 60; tc não maior que o da fórmula do Quadro 1 [DAEE-IT-DPO11 p. 1-2]. Obrigatória só em outorga paulista.
- **FHWA HDS-2/HEC-22:** racional < 80 ha; TR por classe de via (AASHTO) [FHWA-HDS2 p. 37]; sem fator de frequência.
- **Codevasf, ABNT e normas baianas:** sem texto aberto no corpus para hidrologia de projeto.

## 8. Referências usadas (ID, páginas-chave)

- DNIT-HIDRO (IPR-715, 2005): TR 23-24; Gumbel 34-37; CN 75-80; Tc 83-99; HU 99-103; Pfafstetter 106-109; racional 127-133.
- DNIT-DREN (IPR-724, 2006): valeta 160; sarjeta 171; corta-rio 217; Tab. 39 224; tc urbano 302. Sem tabela de TR.
- ABDER-APOSTILA (2022): TR e risco 37-39; C 53-54; CN 55-57; φ e HUT 59-60; exemplos 66-70.
- DAEE-IT-DPO11 (2017; critérios para estudos hidrológicos e hidráulicos em recursos hídricos): 1-3.
- PMSP-DRENURB-V1: TR 17, 33. V2: IDF 19; blocos alternados 21-22; risco 29-30; racional e Tc 53-58.
- FHWA-HDS2 (3ª ed.): TR 37; Tc 68-70, 79-80; métodos 90-91; Gumbel 131-133; racional 181-184. FHWA-HEC22 (4ª ed.): 56-58, 66.
- NRCS-NEH630-CH07 (12), CH09 (7-15), CH10 (10, 12-13, 17-19, 25), CH15 (8-10, 13), CH16 (10-16, 33-35); NRCS-NEH650-CH02 (11).
- USBR-DRAINAGE (1993): 57-58, 61. EMBRAPA-DREN-SUP (1984): 5.
- ENAP-HIDRO-DREN: sem método hidrológico, não citado. NRCS-TR60: barragem, fora de escopo.
- Casos: `casos/drenagem_dissipadores/` (CSB, Baixio, Iuiu, Xingó); `tools/hid/DIVERGENCIAS_bueiros.md`.

## 9. Lacunas (o que o corpus não cobre e o que pedir)

- IDF, CN, C e hietograma do semiárido baiano: Climatologia, Geotecnia, contratante.
- C por TR com números de fonte aberta (só a forma do acervo, equação-fonte a confirmar).
- A conferir nos PDFs: fórmula do Quadro 1 do DAEE, unidade de S em Dooge, faixa de Giandotti, 0,42 de Peltier, tabelas de c do DNIT (tc, A, CN, FP), parâmetros Pfafstetter dos 98 postos.
- TR de dreno parcelar, canal coletor e OAC de perímetro irrigado: só a prática do acervo; pedir ao contratante.
- Margem de erro da vazão por método; fator de pico para terreno plano; ARF do semiárido.
- Pendências para `tools/hid`: blocos alternados, risco J, K de Gumbel por n, DNOS conforme o DNIT.
