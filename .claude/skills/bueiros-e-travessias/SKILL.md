---
name: bueiros-e-travessias
description: >
  Dimensiona e verifica bueiros e travessias de talvegue sob aterro, canal e estrada: bueiro tubular e celular, controle
  de entrada e de saída (HDS-5), HW, células, V e Fr de saída, bueiro afogado, tubo parcialmente cheio
  e regime crítico, TR por obra, classe de tubo de concreto INDICATIVA (NBR 8890 via ABTC) e conferência do método legado.
  Use quando: "bueiro", "travessia", "HW/D", "controle de entrada ou de saída", "tailwater", "bueiro celular", "BDCC",
  "BTCC", "bueiro afogado", "sifão sob estrada", "Ke", "y/D do tubo", "TR do bueiro", "classe do tubo", "o bueiro passa?". Não use para: sarjeta, valeta, descida d'água, dispositivo-tipo DNIT (use
  drenagem-de-estradas-e-plataformas); canal de drenagem (use canais-de-drenagem-e-macrodrenagem); vazão, Tc, racional
  (use hidrologia-de-projeto-para-drenagem); IDF (Clima); dissipador e rip-rap (Hidráulica); dreno enterrado (use
  drenagem-subsuperficial); armadura de tubo ou aduela (Estruturas); preço (engenheiro-de-custos).
---

# Bueiros e travessias

O núcleo (`drenagem-fundamentos`) fixa convenções, fluxo, `[DELEGAR]`, parecer e a regra mestra (projeto que diverge do
método: **apontar com evidência e consequência, nunca corrigir em silêncio**); aqui só a disciplina. Tabelas longas:
`references/`. Edições: HDS-5 3ª ed. 2012; HDS-3 1961; HEC-13 1972 (arquivada); IPR-724 2ª ed. 2006. Citações `[ID p. N]`
com a página física do PDF (IPR-724: impressa = física − 4; HDS-3: impressa + 8). Pontos que dependem da **decisão F7** vão
rotulados "padrão provisório, decisão F7", com as alternativas e a fonte de cada uma.

## 1. Escopo e fronteiras

| Faz (aqui) | Recebe ou entrega a |
|---|---|
| Bueiro sob aterro: tubular, celular, arco; controle de entrada e de saída; HW, V e Fr de saída, nº de células, entrada afunilada (indicar) | **Recebe** Q, TR e TW de `hidrologia-de-projeto-para-drenagem` (não corrigir Q); IDF é do Clima (`[DELEGAR: clima]`) |
| Bueiro afogado e sifão sob aterro como "bueiro com controle na saída" | Canal, transições e sifão invertido de canal: `canais-abertos` (Hidráulica) |
| Tubo parcialmente cheio e regime crítico do tubular | Canal de drenagem a jusante (TW): `canais-de-drenagem-e-macrodrenagem` |
| **D3: dissipador na saída.** Entregar **V, Fr, y de saída**, Q por célula, TW, material e declividade a jusante, com o aviso "precisa de dissipador" | Dimensionar rip-rap ou bacia: Hidráulica (`vertedouros-e-dissipadores`), via `[DELEGAR: hidraulica]` |
| Classe de tubo de concreto **indicativa** (`tubos.py`) | Estrutura (armadura, concreto, aduela, fundação, carga móvel): `[DELEGAR: estruturas]`; fundação e berço: Geotecnia |
| TR por obra (valor) e J | Vazão para o TR: hidrologia |
| Método legado do acervo (orifício, Manning plena) só como comparação rotulada | Dreno enterrado: `drenagem-subsuperficial` |
| Quantitativos (nº, DN, m de tubo) | `[DELEGAR: orcamento]` antes da recomendação, se houver alternativas |

**Sarjeta, valeta de crista e de pé, descida d'água, caixa coletora e dispositivos-tipo do DNIT (Álbum IPR-736, ES 018/019/
021/022/026) não estão mais aqui**: ver `drenagem-de-estradas-e-plataformas`. Canal de drenagem e macrodrenagem: ver
`canais-de-drenagem-e-macrodrenagem`. Os códigos BSTC, BDTC, BTTC, BSCC, BDCC e BTCC continuam valendo como nome da obra.

## 2. Dados mínimos específicos

Pedir; o que faltar vira premissa rotulada, com a consequência:
- **Q de projeto** (pico total da travessia, não por célula), **TR** e método; Q de verificação (TR maior).
- **Geometria:** comprimento L, cotas de fundo (invert) de montante e jusante, S₀, cota do greide ou da berma, cota do
  terreno na boca, altura de aterro, esconsidade. Declividade do corpo: o IPR-724 indica **0,4 % a 5 %**; acima, degraus e berço
  com dentes (ES 023 manda dentes acima de 4 %) [DNIT-DREN p. 34]; [DNIT-ES023 p. 5].
- **HW admissível** como cota (berma ou subleito menos folga; terreno a montante; cota crítica de canal) e como HW/D.
- **TW:** seção, n e declividade do canal ou dreno a jusante (profundidade normal) ou NA controlado; para TR de projeto e de
  verificação.
- **Entrada e material:** tipo de entrada (§3.2), n do barril, células (catálogo DNIT), limite de altura por recobrimento.
- **Material a jusante** e velocidade média e máxima do talvegue [DNIT-DREN p. 101, Etapa I].
- Para a classe do tubo: DN, recobrimento hs, instalação (vala com largura bv, ou aterro com taxa de projeção), classe de
  berço, tipo de solo, sobrecarga de tráfego por metro (§3.9).

## 3. Método por nível

**Anteprojeto (padrão):** equações do HDS-5 pela calculadora, Q igual entre células iguais, TW por Manning normal, margem
declarada **±10 %** no HW [HDS5 p. 83]. **Projeto básico (se pedido):** curva Q × HW, remanso no barril e a jusante, n composto,
galgamento (eq. 3.9), cheia de verificação, amortecimento a montante, HY-8 [HDS5 p. 108]. **Executivo (D2):** conferir, não
substituir; classe, armadura, fundação e juntas são da projetista, de Estruturas e da Geotecnia.

### 3.1 Sequência (HDS-5 DG 1.2 [p. 272]; IPR-724 [DNIT-DREN p. 101-102])

1. Resumir hidrologia e local. 2. Escolher forma, material, tamanho, entrada e células. 3. HW de **entrada**. 4. HW de
**saída**. 5. HW controlante = **o maior**. 6. Comparar com o admissível; se falhar, mudar tamanho, entrada ou células. 7. V, Fr e y de
saída e aviso de dissipador (D3). 8. Encaixe (recobrimento, comprimento, berço, bocas) e repetir para Q de verificação.

### 3.2 Controle de entrada (regressões do HDS-5, Apêndice A)

Com X = Ku·Q/(A·D^0,5), **Ku = 1,811 (SI)**, A = área plena, D = altura interna, S em m/m:
- Não submersa, forma 1: HW/D = Hc/D + K·X^M + Ks·S; forma 2: HW/D = K·X^M; vale até X ≈ 3,5 [HDS5 p. 190, eqs. A.1, A.2].
- Submersa: HW/D = c·X² + Y + Ks·S; vale de X ≈ 4,0 [HDS5 p. 191, eq. A.3]. Ks = −0,5 (mitrada: +0,7).
- Transição (3,5 < X < 4,0): o HDS-5 traça curva tangente [p. 86, 190]; a calculadora **interpola linearmente** (diferença pequena).
  Hc = dc + Vc²/2g na seção de controle.
- K, M, c, Y e Ke por entrada: **`references/constantes-hds5.md`** (Tab. A.1 e A.2 [HDS5 p. 197-198]; Ke da Tab. C.2 [p. 216]).
  Constante Y do arco projetante: Tab. A.2 dá 0,57; o exemplo A.3.1 [p. 191] usa 0,53 (inconsistência do manual; vale a tabela).
- Declividade dos nomogramas = 2 %; a calculadora usa a real. Declividade nula ou adversa e mitrado: [HDS5 p. 107].
- Entrada afunilada (Tab. A.1, charts 55-59 [p. 197]) não está na calculadora: indicar e delegar à projetista. Bisel de 45° com
  muro de testa é recomendação do manual [HDS5 p. 85].
- O controle de entrada **não depende** de TW, L nem n [HDS5 p. 83, §3.1.2].

### 3.3 Controle de saída (equação da energia)

HW_o = h_o + H − L·S₀ [HDS5 p. 91-94, eqs. 3.1, 3.4, 3.5, 3.6b], com H = (1 + Ke + Ku_f n² L / R^1,33) V²/2g, **Ku_f = 19,63 (SI)**,
R = A/P (seção plena), V = Q/A.
- **TW efetivo:** h_o = TW se TW ≥ D; senão **max(TW, (dc + D)/2)**, dc ≤ D [HDS5 p. 106, §3.3.3]. Nunca TW = 0 sem justificar.
- Limites: (dc + D)/2 vale se o barril flui cheio em parte do comprimento; para **HW < 1,2 D** usar com cautela e conferir por
  remanso; abaixo de **0,75 D** não usar [HDS5 p. 94, 106]. A calculadora avisa "saída livre (TW < D)" e "HW < D".
- Perda de saída padrão H_o = V²/2g [p. 92, eq. 3.4d]; H_o = (V − V_d)²/2g (método USU) só com V_d medido [p. 92, eq. 3.4e].
- n composto: n_c = [Σ(p_i n_i^1,5)/p]^(2/3) [HDS5 p. 96, eq. 3.8]. n do barril de concreto: **0,015** (DNIT, e charts-base do HDS-3
  [FHWA-HDS3 p. 53]) ou 0,012 (nomograma do HDS-5) [DNIT-DREN p. 114]; [HDS5 p. 90, 208]. Outras fontes do mapa G2: laboratório 0,009-0,011,
  projeto 0,012 em drenagem e 0,013 em esgoto [LOC-ABTC-HISTORIA-MANNING p. 5]; HDS-3 Tab. 1: 0,011-0,013 [p. 108]. **Declarar o n**: o
  resultado muda (V de saída do HDS-5 p. 280: 6,45 m/s com n 0,012, 6,07 com 0,013).
- Perdas adicionais somam-se a H [HDS5 p. 91, eq. 3.1]: curva até 15° a cada ≥ 15 m dispensa; senão Kb = 0,50 / 0,37 / 0,25
  (R/D = 1: 90° / 45° / 22,5°) e 0,30 / 0,22 / 0,15 (R/D = 2) [HDS5 p. 140, Tab. 5.1, eq. 5.1].
- **Ke de muro de ala paralelo (caixa, aresta viva no topo)** [padrão provisório, decisão F7]: HDS-5 Tab. C.2 [p. 216] = **0,7**
  (o código usa); DNIT-DREN Tab. 30 [p. 130] = **0,2**. Ke só afeta o controle de saída. Rodar com `fonte_ke="hds5"` e `"dnit"` e
  mostrar o HW dos dois. HEC-13 Tab. 1 [p. 100] confirma os demais Ke da Tab. C.2.

### 3.4 HW admissível, folga e cheia de verificação

| Critério | Valor | Fonte |
|---|---|---|
| HW/D corrente em órgãos viários | 1,0 a 1,5 | [HDS5 p. 72] |
| Folga abaixo do ombro da estrada (exemplo do manual) | 2 ft ≈ 0,61 m | [HDS5 p. 272, DG 1.3] |
| Folga do projeto Baixio de Irecê | berma menos 1,0 m | [896:1] |
| DAEE-SP | "previsto para trabalhar em carga" (sem folga numérica) | [DAEE-IT-DPO11 p. 3, Tab. 4] |
| Afogamento como limite de projeto; HW acima da geratriz superior amortece a cheia | prática DNIT | [DNIT-HIDRO p. 23] |
| Modelo de orifício do DNIT: carga (do centro) ≤ 2 D | | [DNIT-DREN p. 91] |
| Dimensionar como canal (TR 10), verificar HW com TR 20-25 | IS-203 | [DNIT-HIDRO p. 24] |

HW de projeto, de verificação e a cota resultante vão no parecer. HW > D = **bueiro com carga**: checar V na boca de jusante.

### 3.5 Células, afastamento e arranjo

- Dividir Q igualmente entre barris **iguais**; desiguais ou em cotas diferentes exigem software [HDS5 p. 108].
- IPR-724: simples, duplo e triplo; **não recomenda mais linhas** [DNIT-DREN p. 32]; restrição de recobrimento justifica mais
  linhas ou celular mais largo que alto [DNIT-DREN p. 101, Etapa II].
- **Afastamento:** tubular em vala, 0,30 m entre tubos e 0,40 m lateral [DNIT-ES023 p. 4]; celular, 0,50 m lateral por lado
  [DNIT-ES025 p. 5]. O aviso antigo "HDS-5 cap. 3/HEC-14" foi reescrito com as duas ES (v0.2.0). Esconsidade: ≈ −7 % a 45°, evitar em
  barris múltiplos [HDS5 p. 149-150].
- Redução de capacidade de **5 % por linha adicional** (duplo 95 %, triplo 90 %) existe só no SisCCoH [LOC-SISCCOH-MANUAL-V11 p. 41],
  sem primária no corpus: não aplicar; citar como prática de software.

### 3.6 Velocidade de saída, Froude e aviso de dissipador (D3)

- **Controle de entrada:** V na profundidade normal da saída (Manning) [HDS5 p. 100, §3.1.6]. **Controle de saída:** área de dc se
  TW < dc; de TW se dc < TW < D; plena se TW > D [HDS5 p. 100; DNIT-DREN p. 102, Etapa VI]. Fr = V/√(g·A/T), nunca com y.
- Comparar V com o **material de jusante** (Tab. 31 do DNIT, `references/velocidades-admissiveis-e-revestimentos.md`, padrão da
  calculadora desde a v0.2.0). V > limite: proteção do pé ou dissipador [DNIT-DREN p. 34]; [HDS5 p. 99].
- **Entregar à Hidráulica** (`[DELEGAR: hidraulica]`): Q por célula, largura e altura da boca, **V, Fr e y de saída**, TW, material e
  declividade do canal de restituição, com a fonte do limite de V usado. O tipo e o dimensionamento (HEC-14, ressalto) **não** são daqui.

### 3.7 Bueiro afogado e sifão sob aterro

- Bueiro **com controle na saída**, cheio: h_total = h_entrada + h_atrito + h_saída (Ke da Tab. C.2; atrito de 3.4b; saída 3.4d);
  NA de montante = NA de jusante + h_total. Jaíba CS-25 sob a MG-401 (2 × 1,50 × 1,50 m, L 90 m, n 0,015): h_total 0,04 m, NA de
  montante 480,13 m [1182:56-57]; a calculadora dá 480,138 (tol. 0,01 m). Qualidade B (Q 2,44 × 2 × 1,27).
- HDS-5: o culvert em "sag" ("sifão invertido") serve a canais de irrigação sob estrada, exige curvas, tem risco de assoreamento e
  **não se recomenda em curso d'água** [HDS5 p. 139]. A capacidade extra de sifonamento **não deve ser considerada** [p. 141-142].
- Fronteira: transição de montante, perda total do sifão do canal e greide são de `canais-abertos`.

### 3.8 Tubo parcialmente cheio e regime crítico (v0.3.0)

- **Manning circular exato** (segmento circular): A = D²/8 (θ − sen θ), P = Dθ/2, T = D sen(θ/2); y/D, V, **Fr com A/T**
  (HDS-3 Chart 55 [FHWA-HDS3 p. 76]; Ex. 10-17 [p. 53-55]). Quando Q > Q plena, o tubo trabalha cheio (y = D; verificar HW).
- **Critério y/D ≤ 0,75** [padrão provisório, decisão F7: critério do acervo Delmiro, 1492:164; Jaíba usa 0,82, 1182:65]. Aviso quando
  acima. Fr entre 0,9 e 1,1: lâmina instável, evitar. n e S₀ declarados (n 0,010-0,035).
- **Regime crítico do tubular** [LOC-IME p. 151-152]: Ec = D → θc = 4,0335 rad, dc = 0,716 D, A_c = 0,601 D², Vc = 2,56 D^0,5,
  Ic = 32,82 n²/D^(1/3). O A_c = 0,60 D² do DNIT deixa de ser "ajuste próprio": é a fórmula do IME arredondada (0,2 %). A vazão crítica
  **exata** de Ec = D é ~7 % menor que a das Tabelas do DNIT (Armadilha 9).
- Bueiro tubular dimensionado "como canal" não diz o HW: **sempre** rodar HDS-5 também.

### 3.9 Classe do tubo de concreto: INDICATIVA (`tubos.py`; estrutural é de `estruturas`)

Fluxo Marston → Fens = γs (q + qm)/α (γs 1,0 fissura; 1,5 ruptura) → menor classe PA1-PA4 da Tab. 2 da ABTC [LOC-ABTC-ESPEC-TUBOS-LICITACOES p. 4;
LOC-ABTC-PROJETO-ESTRUTURAL-TUBOS p. 45-46]. Detalhe, limites, lacunas e padrões provisórios (fator de berço classe A 2,25 × 2,5, decisão F7):
`references/classe-de-tubo-indicativa.md`. Saída sempre rotulada "indicativo"; classe final: `[DELEGAR: estruturas]`. NBR 8890:2020 não aberta: citar via ABTC.

### 3.10 TR por tipo de obra

`references/tr-por-tipo-de-obra.md`: bueiro rodoviário 10-20, verificação 20-25 [DNIT-HIDRO p. 23-24]; DAEE-SP 25 rural, 100 urbano
[DAEE-IT-DPO11 p. 1]; acervo 25 a 100. **TR de bueiro de perímetro irrigado [padrão provisório, decisão F7]:** USBR 5 a 15 anos
(página a confirmar) × acervo 25 (estrada) e 50 a 100 (sob canal). Declarar TR de projeto e de verificação e J = 1 − (1 − 1/TR)^N.

### 3.11 Métodos legados do acervo (só para comparar)

- **Orifício** (Baixio, 896:1): Q = C·A·√(2 g h), C = 0,62; HW = D/2 + h. IPR-724: C 0,62-0,63 e C(L/D) de Manning: 0,770 (10), 0,674 (25),
  0,643 (50), 0,588 (75), 0,548 (100) [DNIT-DREN p. 91, Tab. 22]; vale com carga ≤ 2 D.
- **Manning em seção plena ou lâmina fixa** (Baixio, CSB, Salitre, Iuiu, Delmiro, Jaíba): dá capacidade e V, **não o HW**.
- O DNIT/ENAP dimensiona "como canal" e verifica "como orifício" [ENAP-BUEIROS p. 13]; [DNIT-DREN p. 32]. O legado subestima o HW em
  **6 a 18 %** (contra a segurança). Entregar o HDS-5 e a comparação rotulada.

## 4. Calculadoras (`tools/dren/bueiros.py` 0.3.0 e `tubos.py` 0.1.0)

| Cálculo | Função | Fórmula e fonte | Testes (`tests/dren/`) |
|---|---|---|---|
| HW de entrada | `controle_de_entrada` | HDS-5 A.1-A.3, Tab. A.1/A.2 | `test_entrada_submersa_formula_fechada`, `test_transicao_liga_os_extremos`, `test_hds5_p280_caixa_1524_q8495` |
| HW de saída | `controle_de_saida` | HDS-5 3.1, 3.4-3.6; Ke Tab. C.2 | `test_saida_formula_fechada_afogado`, `test_saida_livre_usa_dc_mais_D_sobre_2_e_avisa` |
| HW controlante e catálogo | `dimensionar_bueiro` (`fonte_ke`) | max(entrada, saída) | `test_dimensionar_ordena_por_area_e_respeita_HW_max` |
| V, y, Fr de saída; dissipador | `velocidade_de_saida`, `dissipador_necessario` | HDS-5 §3.1.6; Tab. 31 DNIT | `test_velocidade_saida_e_dissipador`, `test_hds5_p280_velocidade_de_saida_caixa_1524` |
| Tubo parcialmente cheio | `tubo_parcialmente_cheio` | Manning, segmento exato; HDS-3 | `test_hds3_ex10_circular_30in`, `test_hds3_ex15_16_17`, `test_delmiro_tubo_parcialmente_cheio`, `test_tubo_parcialmente_cheio_froude_com_profundidade_hidraulica_e_avisos` |
| Regime crítico tubular | `regime_critico_tubular_ime`, `vazao_critica_legado_dnit`, `vazao_critica_exata` | IME p. 151-152; DNIT Tab. 1-2 | `test_ime_regime_critico_tubular` |
| Legado | `orificio`, `comparar_legado_hds5` | C = 0,62; Manning | `test_baixio_legado_vs_hds5_5pct`, `test_xingo_legado_equivale_a_n_0093_abaixo_do_n_de_projeto` |
| Classe de tubo | `tubos.selecionar_tubo`, `classe_de_tubo`, `carga_solo_vala`, `fator_berco_vala` | Marston, TUBOS, ESPEC, EM 2902 | `test_espec_exemplos_de_classe`, `test_selecionar_tubo_vala_e_monotonicidade`, `test_em2902_vala_cd_e_we1` |

```
python -m tools.dren.bueiros --json '{"funcao":"controle_de_entrada","Q":8.495,"forma":"retangular","dim":[1.524,1.524],"tipo_de_entrada":"ret_alas_90_15","S0":0.02}'
python -m tools.dren.bueiros --json '{"funcao":"tubo_parcialmente_cheio","Q":0.499,"D":0.80,"n":0.015,"S0":0.005}'
python -m tools.dren.tubos --json '{"funcao":"classe_de_tubo","DN_mm":1200,"F_kN_m":65}'
```

`avisos` a reproduzir: "saída livre (TW < D)" (ir ao remanso se HW < 1,2 D); "HW de saída < D" (não aplicável); "dc ≥ D"; "arco: área de
elipse" (usar dados do fabricante); "S0 > 10 %"; "células paralelas: afastamento" (usar §3.5); "nenhuma alternativa atende HW_max";
"y/D > limite (padrão provisório, decisão F7)"; "Fr entre 0,9 e 1,1"; "Q ≥ capacidade plena"; em `tubos`: "indicativo", "sobrecarga não informada",
"de estimado", "DN > 600" e "nenhuma classe atende". `regime` (nao_submersa, transicao, submersa): reportar. **Fora da calculadora:** entrada
afunilada, esconsidade, curva de desempenho, n composto, galgamento (eq. 3.9: Cd(SI) = 0,552 × Cd da Fig. 3.11 [HDS5 p. 97]). O agente não altera `tools/`.
Exemplos numéricos: `references/exemplos-de-conferencia.md`.

## 5. Critérios de verificação (reportar atendida, violada ou não aplicável)

- Bueiro nos **dois** controles; adota-se o maior HW; legado só rotulado como comparação.
- Q, TR e método recebidos da hidrologia e do Clima; sem corrigir Q aqui.
- Regime e Fr com A/T; n do barril declarado com fonte; y/D do tubo (provisório 0,75) e Fr fora de 0,9-1,1.
- HW × cota admissível (folga, aterro) e monotonia das cotas ao longo do perfil.
- V de saída × material de jusante; **D3**: se V > limite, bloco `[DELEGAR: hidraulica]` com V, Fr, y, TW.
- Classe de tubo: só indicativa, com a fonte do berço e as lacunas; classe final `[DELEGAR: estruturas]`.
- Alternativas com custo relevante (DN × células, celular × tubular, entrada) `[DELEGAR: orcamento]` antes da recomendação.
- Dado de outra disciplina (fundação, greide, chuva) com `[DELEGAR]` e premissa provisória.

## 6. Armadilhas do acervo (casos negativos)

| # | Armadilha | Onde | Como detectar e o que fazer |
|---|---|---|---|
| 1 | Bueiro só por orifício ou Manning; HW 6 a 18 % abaixo do HDS-5 (contra a segurança) | Baixio, CSB, Xingó, Salitre | HW/D ausente; `comparar_legado_hds5`; exigir HW de entrada e de saída |
| 2 | "Capacidade livre" TR 25 passa, mas Q50 > capacidade e se aceita com carga | Baixio (BU-CP0-13: 33,4 × 27,0 m³/s) | comparar Q de verificação com a capacidade crítica e calcular HW |
| 3 | Coluna "Situação OK" com folga negativa | Baixio, aba "Sob estradas" (CS1-01: −0,96 m) | refazer a folga com a cota do terreno; nunca usar a coluna como gabarito |
| 4 | Q/célula acima da capacidade crítica: entrada afoga, HW > D, só V e Yo reportados | Salitre BTCC 7 (HW/D ≈ 2,25 hipotético) | `controle_de_entrada` com a entrada declarada; X > 4 = submersa |
| 5 | V/Yo do quadro 4.7 não reproduz Manning (28,6 × 39,2 m³/s) | CSB BTCC-17 | conferir a página; HDS-5 dá HW 2,83 m (HW/D 1,4) |
| 6 | Lâmina supercrítica de perfil lida como normal (0,96 × 0,83 m) | Xingó BU-01, 06, 24 | projeto usa energia a partir da seção crítica, K = 0,5; Manning não reproduz (xfail) |
| 7 | Q 2,44 × 2 × 1,27 = 2,54 m³/s | Jaíba CS-25 | exigir Q de projeto e por célula coerentes |
| 8 | Coeficiente impresso **1,638** na vazão crítica do celular: Tabela 2 e teoria dão **1,705** (4 % a menos) | IPR-724 p. 54-56 | usar a tabela; 2,0 × 2,0 = 9,64 m³/s |
| 9 | Tabela 1 do DNIT (tubular) usa Vc = 2,56 D^0,5 do retângulo: Q crítica ≈ 7 % acima da exata (DN 1,00: 1,53 × 1,43) | IPR-724 p. 55 | usar HDS-5; `vazao_critica_exata` |
| 10 | Ke de ala paralela 0,2 (DNIT) × 0,7 (HDS-5) | IPR-724 p. 130 × HDS5 p. 216 | mostrar os dois HW; padrão provisório, decisão F7 |
| 11 | Limite de V da calculadora legada até 2× mais permissivo que o DNIT | `LIMITE_VELOCIDADE_MATERIAL_LEGADO` | desde a v0.2.0 o padrão é a Tab. 31; reproduzir o aviso de material sem linha |
| 12 | "Declividade mínima 5 %" do bueiro: provável 0,5 % ou o intervalo "0,4 a 5 %" truncado | Iuiu 2002 (1051:331) e **Iuiu 2018 (1069:125)**, mesmo texto | hipótese a confirmar no desenho; usar 0,4 % mínimo [DNIT-DREN p. 34] |
| 13 | Orifício com C = 0,62 fixo ignora L/D (0,77 em L/D = 10; 0,548 em 100) | legado (Baixio, L/D ≈ 16) | conferir L/D e carga ≤ 2 D |
| 14 | Folga ao terreno que não fecha (0,66 × 0,464 m) | Baixio BU-CP0-15 | refazer a aritmética (`DIVERGENCIAS.md`) |
| 15 | **BUC sem HW, com S e L divergentes:** quadro dá S 0,006/0,005/0,015/0,015 e L 40-50 m; o memorial de cálculo usa S 0,005/0,005/0,005/0,007 e o quantitativo L médio 19,33 m. Com S = 0,015, Fr > 1, incompatível com Fr 0,81-0,97 da tabela. y/D 79 % (BUC-5, TR 50) passa do critério | **Delmiro Gouveia** 1492:164; 1493:282-285; 1515:99 (caso B) | `tubo_parcialmente_cheio` reproduz y, V e Fr (1 %); apontar as duas versões de S e L, o efeito no controle de entrada/saída e pedir o desenho 0364-DE-20-DR-001 |
| 16 | **91 obras sem capacidade publicada:** declividade e L de cada bueiro ausentes; método RAC/MOD/HUT por faixa de área sem limite escrito; TR 25 no texto, mas as linhas HUT só trazem Q50 e as RAC só Q15 e Q25; células de 2,0 a 3,0 m contra "limite 1,50 m"; n 0,0165; 4 bueiros sem bacia | **Vale do Iuiu 2018** (1069:124-127; caso B/C) | não há gabarito de capacidade; pedir S e L e verificar por HDS-5 (ex. BU5, 3 × Ø1,50, Q25 10,10 → 3,37 m³/s por linha); comparar com 2002 (TR 50 sob canal) |
| 17 | **Cota do rasto de B31 incoerente** (91,189 m; B30 94,246; B32 92,977; coletor 0,81 m acima do rasto) em quadro de 59 bueiros sem Q, HW ou L | **CAC Trecho 1** (1131:65-67, caso C) | teste de monotonia (rasto não sobe a jusante) e de posição (coletor abaixo do rasto); apontar, **não corrigir** (94,189 é só hipótese de digitação); perfil longitudinal ausente |
| 18 | **n implícito 0,013 contra 0,015 do canal:** 22 de 23 BSTC Ø0,80 só fecham com n ≈ 0,013, sem n declarado; com n 0,015 a capacidade cai ~13 % e E4 BC-08 estoura Y/D 0,82. V até 4,8 m/s sem dissipador e sem HW | **Jaíba Etapas 3-4** (1182:43, 65-67, caso A) | `tubo_parcialmente_cheio` com n 0,013 e 0,015: BC-08 (Q 1,10, i 0,007) Y/D 0,82 × acima; sinalizar a divergência com o n do canal; V alta → `[DELEGAR: hidraulica]` |
| 19 | Capacidade de tubo do legado Xingó (33,5·D^2,67·i^0,5) equivale a n = 0,0093: com n 0,012-0,013, 22 a 28 % menor | Xingó, tubo dreno | converter para n equivalente antes de comparar |
| 20 | Gabarito do próprio manual depende de n não informado (V 6,47 × 6,07 m/s) | HDS-5 p. 280 | declarar o n |

## 7. O que a norma e o manual exigem e a quem se aplica

- **IPR-724 (DNIT):** rodovias federais; bueiro "como canal, vertedor ou orifício" e, no projeto final, pelo método do BPR (nomogramas como o HDS-5)
  [DNIT-DREN p. 32, 101-116]. Em estrada de serviço de irrigação, por analogia declarada.
- **ES DNIT 019, 022-026, 030, 096:** execução e medição; sem projeto específico, usar o Álbum [DNIT-ES023 p. 3]. Detalhe: `drenagem-normas-e-manuais`.
- **HDS-5 e HEC-13 (FHWA):** método e ±10 % no HW [HDS5 p. 72, 83]; HEC-13 (1972, arquivada) confere Ke [p. 100]. **DAEE-SP IT DPO 11/2017:** outorga em SP; fora de SP é referência.
- **NBR 8890 (ABNT 2020, não aberta):** tubo de concreto pluvial; **citar via ABTC, não transcrever** [DNIT-ES023 p. 3].

## 8. Referências (IDs e páginas-chave)

FHWA-HDS5: p. 72, 83-94, 96-100, 105-108, 139-142, 149-150, 190-200, 208, 216, 272-281. FHWA-HDS3: p. 53-55 (Ex. 10-17), 76 (Chart 55), 108 (Tab. 1).
FHWA-HEC13: p. 100 (Tab. 1, Ke). DNIT-DREN (IPR-724): p. 32-34, 54-56, 91, 101-102, 114, 130-131. DNIT-HIDRO (IPR-715): p. 23-24. LOC-IME p. 151-152.
LOC-ABTC-PROJETO-ESTRUTURAL-TUBOS p. 17, 19-20, 29, 33, 37, 43, 45-46; LOC-ABTC-ESPEC-TUBOS-LICITACOES p. 4, 6; LOC-ABTC-ALTERACOES-NBR8890 p. 1-4;
LOC-ABTC-HISTORIA-MANNING p. 5; USACE-EM1110-2-2902 p. 25, 27, 71-72. DNIT-ES023/025. ENAP-BUEIROS e SisCCoH: didáticos. DAEE-IT-DPO11.
Casos: `casos/drenagem/` (Baixio, CSB, Salitre RC500-800, Iuiu 2002 e 2018, Xingó, Jaíba, Delmiro BUC, CAC B31); `tools/dren/DIVERGENCIAS.md`.

## 9. Lacunas do corpus e pontos da F7

- **F7 (não decididos):** TR de bueiro de perímetro irrigado; Ke de ala paralela (0,2 × 0,7); y/D ≤ 0,75; fator de berço classe A (2,25 × 2,5); n de Manning do tubo
  (0,012 × 0,013 × 0,015); limite de área do racional (na hidrologia).
- Sem fonte: TR numérico de bueiro de irrigação; norma da Codevasf para travessias; velocidade admissível do canal a jusante (perguntar). Sem caso do acervo com HDS-5 completo.
- Não abertos: NBR 8890:2020, ES DNIT 018/021, FAO-38. HDS-5 §3.4 (afunilada), nomogramas do Apêndice C e HEC-14 só ponteiros. HEC-13 e HDS-3 só em unidades inglesas.
- Sem tabela de altura de aterro por classe e DN (só o software da ABTC). Aduela (NBR 15396): domínio de Estruturas.
- Nenhum número dos casos de 2026-10-08 tem ✓h: são candidatos, não gabarito.
