---
name: bueiros-e-drenagem-superficial
description: >
  Dimensiona e verifica bueiros tubulares e celulares (controle de entrada e de saída pelo HDS-5, HW admissível, número
  de células, velocidade de saída, bueiro afogado e sifão sob aterro), canais de drenagem e valetas, sarjetas, descidas
  d'água e drenagem de estradas de serviço (HEC-15, HEC-22 e Manual de Drenagem de Rodovias IPR-724 do DNIT), com os
  dispositivos-tipo do DNIT (Álbum IPR-736), o TR por tipo de obra e a conferência do método legado do acervo
  (orifício e Manning em seção plena). Use quando: "bueiro", "HW/D", "controle de entrada", "controle de saída",
  "tailwater" do bueiro, "bueiro celular", "BDCC", "BTCC", "bueiro afogado", "sifão sob estrada", "Ke", "valeta",
  "sarjeta", "descida d'água", "velocidade admissível", "tensão trativa", "revestimento de valeta", "TR do bueiro",
  "dispositivo-tipo do DNIT", "o bueiro passa?", "quantas células". Não use para: vazão de projeto, Tc, IDF, método
  racional, SCS (use hidrologia-de-projeto-para-drenagem); bacia de dissipação, rip-rap, vertedouro, extravasor (use
  vertedouros-e-dissipadores); dreno enterrado, subpressão, filtro (use drenagem-subsuperficial); canal de irrigação em
  si, sifão invertido de canal, aqueduto (use canais-abertos); método geral, convenções, delegação (use
  hidraulica-fundamentos); preço (use engenheiro-de-custos).
---

# Bueiros e drenagem superficial

O núcleo (`hidraulica-fundamentos`) fixa convenções, V1-V12, `[DELEGAR]` e formato do parecer; aqui só a disciplina. Tabelas longas: `references/`. Edições: HDS-5 3ª ed. 2012; HEC-15 3ª ed. 2005;
HEC-22 4ª ed. 2024; IPR-724 2ª ed. 2006; Álbum IPR-736 5ª ed. 2018 (V11). Citações `[ID p. N]` com a página física do PDF
(no IPR-724 a página impressa é a física menos 4).

## 1. Escopo e fronteiras

| Faz (aqui) | Recebe ou entrega a |
|---|---|
| Bueiro sob aterro: tubular, celular, arco; controle de entrada e de saída; HW, V de saída, nº de células, entrada afunilada (indicar) | **Recebe** Q, TR e TW da `hidrologia-de-projeto-para-drenagem` (só receber; não corrigir Q) |
| Bueiro afogado e sifão sob aterro como "bueiro com controle na saída" (NA de montante) | O canal de irrigação, as transições e o sifão invertido de canal ficam em `canais-abertos` |
| Canais de drenagem, valetas, sarjetas, descidas d'água, drenagem de estradas de serviço (Manning, revestimento, velocidade e tensão) | Canal de irrigação em si: `canais-abertos` |
| Quando o bueiro **precisa** de dissipador (V de saída x material de jusante) | O dimensionamento da bacia e do rip-rap é de `vertedouros-e-dissipadores` (entregar V, y, Fr, Q por célula, TW, material) |
| Dispositivo-tipo DNIT (código, uso, ES de execução) | Estruturas: classe do tubo (NBR 8890), armadura, carga móvel; Geotecnia: fundação e berço; Terraplenagem: greide e altura de aterro; Orçamento: quantitativos (V6) |
| Critério de TR por obra (valor) | A vazão para esse TR é da hidrologia; IDF é de Climatologia |
| Método legado do acervo (orifício, Manning plena) como comparação rotulada | Dreno enterrado e envoltório: `drenagem-subsuperficial` |

## 2. Dados mínimos específicos

Pedir, e rotular como premissa o que faltar (com a consequência):
- **Q de projeto** (pico, total da travessia, não por célula), **TR** e como foi obtido; Q de verificação (TR maior).
- **Geometria da travessia:** comprimento L, cotas de fundo (invert) de montante e jusante, declividade S₀, cota do greide ou da berma, cota do terreno
  na boca, altura de aterro, esconsidade. Declividade do corpo: o IPR-724 indica **0,4 % a 5 %**; acima disso, degraus e berço com
  dentes (ES 023 manda dentes acima de 4 %) [DNIT-DREN p. 34]; [DNIT-ES023 p. 5].
- **HW admissível:** como cota (berma ou subleito menos folga; terreno a montante; cota crítica de canal) e como HW/D.
- **TW (tailwater):** seção, n e declividade do canal ou dreno a jusante (profundidade normal) ou NA de jusante controlado; para
  TR de projeto e de verificação.
- **Entrada e material:** tipo de entrada (§3.2), n do barril, número e dimensões das células (catálogo DNIT), limite de altura
  por recobrimento.
- **Material do canal a jusante** e velocidade média e máxima no talvegue [DNIT-DREN p. 101, Etapa I].
- Para canal de drenagem ou valeta: solo, revestimento, declividade, talude, folga, vazão afluente (Racional por metro linear para sarjeta).

## 3. Método por nível

**Anteprojeto (padrão):** equações do HDS-5 pela calculadora, Q igual entre células iguais, TW por Manning normal, margem declarada: **±10 %** no HW [HDS5 p. 83].
**Projeto básico (se pedido):** curva Q x HW em vários Q, remanso no barril e a jusante, n composto, galgamento (eq. 3.9), cheia de verificação, amortecimento
a montante, HY-8 [HDS5 p. 108]. **Executivo (D2):** conferir, não substituir: classe do tubo, armadura, fundação, recobrimento e juntas são da projetista, da
Estruturas e da Geotecnia.

### 3.1 Sequência (HDS-5 DG 1.2, [HDS5 p. 272]; IPR-724 [DNIT-DREN p. 101-102])

1. Resumir hidrologia e local (Q, TW, S₀, L, cotas, HW admissível). 2. Escolher forma, material, tamanho, entrada e células.
3. Calcular HW de **entrada**. 4. Calcular HW de **saída**. 5. HW controlante = **o maior** (V3). 6. Comparar com o admissível; se
falhar, mudar tamanho, entrada (bisel, afunilado) ou nº de células. 7. Velocidade de saída e necessidade de dissipador. 8. Verificar encaixe
(recobrimento, comprimento, berço, bocas) e repetir para Q de verificação e curva de desempenho.

### 3.2 Controle de entrada (regressões do HDS-5, Apêndice A)

Com X = Ku·Q/(A·D^0,5), **Ku = 1,811 (SI)**, A = área plena do barril, D = altura interna, S = declividade (m/m):
- Não submersa, forma 1: HW/D = Hc/D + K·X^M + Ks·S; forma 2: HW/D = K·X^M; vale até X ≈ 3,5 [HDS5 p. 190, eqs. A.1, A.2].
- Submersa: HW/D = c·X² + Y + Ks·S; vale a partir de X ≈ 4,0 [HDS5 p. 191, eq. A.3]. Ks = −0,5 (mitrada: +0,7).
- Zona de transição (3,5 < X < 4,0): o HDS-5 traça curva tangente [p. 86, 190]; a calculadora **interpola linearmente** entre os dois
  extremos (diferença pequena, `DIVERGENCIAS_bueiros.md`). Hc = dc + Vc²/2g na seção de controle.
- K, M, c, Y e Ke por tipo de entrada: **`references/constantes-hds5.md`** (Tabelas A.1 e A.2 [HDS5 p. 197-198]; Ke da Tabela C.2 [p. 216]).
- Declividade dos nomogramas = 2 %; a calculadora usa a real. Declividade nula ou adversa e mitrado: [HDS5 p. 107].
- A entrada afunilada (lateral ou de declividade) eleva a capacidade e usa a Tabela A.1 charts 55-59 [HDS5 p. 197]; a calculadora não
  cobre: indicar e delegar à projetista. Bisel de 45° em todo bueiro com muro de testa é a recomendação do manual [HDS5 p. 85].
- Controle de entrada **não depende** de TW, de L nem de n [HDS5 p. 83, §3.1.2].

### 3.3 Controle de saída (equação da energia)

HW_o = h_o + H − L·S₀ [HDS5 p. 91-94, eqs. 3.1, 3.4, 3.5, 3.6b], com
H = (1 + Ke + Ku_f n² L / R^1,33) V²/2g, **Ku_f = 19,63 (SI)**, R = A/P (seção plena), V = Q/A.
- **TW efetivo:** h_o = TW se TW ≥ D; senão h_o = **max(TW, (dc + D)/2)**, com dc ≤ D [HDS5 p. 106, §3.3.3]. TW vem da profundidade
  normal do canal de jusante, de remanso ou de campo [p. 91]. Nunca TW = 0 sem justificar.
- Limites: o método de (dc + D)/2 vale se o barril flui cheio em parte do comprimento; para **HW < 1,2 D** usar com cautela e
  conferir por remanso; abaixo de **0,75 D** não usar [HDS5 p. 94, 106]. A calculadora avisa "saída livre (TW < D)" e "HW < D".
- Saída: perda padrão H_o = V²/2g [p. 92, eq. 3.4d]. Para canais de irrigação e transição suave, o manual traz H_o = (V − V_d)²/2g
  (método USU) [p. 92, eq. 3.4e]; usar só com V_d medido e justificar.
- n composto (fundo revestido ou liso, parede corrugada): n_c = [Σ(p_i n_i^1,5)/p]^(2/3) [HDS5 p. 96, eq. 3.8]. n do barril: **n = 0,015**
  (DNIT) ou 0,012 (nomograma HDS-5 para concreto) [DNIT-DREN p. 114]; [HDS5 p. 90, 208]; declarar a escolha.
- Perdas adicionais (curvas, junções, grelhas) somam-se a H [HDS5 p. 91, eq. 3.1]: curva até 15° a cada ≥ 15 m dispensa o cálculo; senão
  Kb = 0,50 / 0,37 / 0,25 (R/D = 1: 90° / 45° / 22,5°) e 0,30 / 0,22 / 0,15 (R/D = 2) [HDS5 p. 140, Tabela 5.1, eq. 5.1].

### 3.4 HW admissível, folga e cheia de verificação

| Critério | Valor | Fonte |
|---|---|---|
| HW/D corrente em órgãos viários | 1,0 a 1,5 | [HDS5 p. 72] |
| Folga abaixo do ombro da estrada (exemplo do manual) | 2 ft ≈ 0,61 m | [HDS5 p. 272, DG 1.3] |
| Folga do projeto Baixio de Irecê | berma menos 1,0 m ("NB − 1,0 m") | [896:1] |
| Folga DAEE-SP para bueiro | "previsto para trabalhar em carga" (sem folga numérica) | [DAEE-IT-DPO11 p. 3, Tabela 4] |
| Afogamento da galeria como limite de projeto; permitir HW acima da geratriz superior (amortece a cheia) | prática DNIT | [DNIT-HIDRO p. 23] |
| Modelo de orifício do DNIT: carga hidráulica (do centro) ≤ 2 D | | [DNIT-DREN p. 91] |
| Dimensionar como canal (TR 10) e verificar o HW com TR 20-25 | IS-203 | [DNIT-HIDRO p. 24] |

HW de projeto, de verificação e cota resultante vão no parecer. Quando HW > D, declarar **bueiro com carga** e checar velocidade de
saída (V alta no pé da boca de jusante) [DNIT-HIDRO p. 24].

### 3.5 Número de células, afastamento e arranjo

- Dividir Q igualmente entre barris **iguais** (cálculo manual); barris desiguais ou em cotas diferentes exigem software [HDS5 p. 108].
- O IPR-724 admite simples, duplo e triplo; **não recomenda mais linhas** por alagar faixa ampla [DNIT-DREN p. 32]; restrição de
  recobrimento justifica mais linhas ou celular mais largo que alto [DNIT-DREN p. 101, Etapa II].
- **Afastamento entre linhas:** tubular em vala, folga de **0,30 m** entre tubos (linha dupla ou tripla) e 0,40 m de folga lateral por lado
  [DNIT-ES023 p. 4]; celular em vala, folga lateral mín. **0,50 m** por lado para fôrmas [DNIT-ES025 p. 5]. O aviso da calculadora
  ("≥ D/2 ou ≥ 0,6 m, HDS-5 cap. 3/HEC-14") **não tem fonte** no HDS-5 lido (que não fixa afastamento): usar a ES, não o aviso. Esconsidade de entrada: efeito pequeno (≈ −7 % a 45°) e evitar em barris múltiplos [HDS5 p. 149-150].
- Celular com paredes intermediárias: usar a **área livre** de cada célula.

### 3.6 Velocidade de saída e necessidade de dissipador

- **Controle de entrada:** V = velocidade em profundidade normal na saída (Manning) [HDS5 p. 100, §3.1.6]. **Controle de saída:**
  área do escoamento = a de dc se TW < dc; a de TW se dc < TW < D; a área plena se TW > D [HDS5 p. 100; DNIT-DREN p. 102, Etapa VI].
- Comparar com a velocidade do **material de jusante** (Tabela 31 do DNIT, `references/velocidades-admissiveis-e-revestimentos.md`).
  V > limite: proteção do pé ou dissipador [DNIT-DREN p. 34]; [HDS5 p. 99]. O tipo (Fr, TW, ressalto) é de `vertedouros-e-dissipadores` (HEC-14). **Entregar** a `vertedouros-e-dissipadores`: Q por célula, largura e altura da boca, y e V de saída,
  Fr, TW, material, declividade do canal de restituição.
- A tabela de limites da calculadora é mais permissiva que a do DNIT em vários materiais (areia, cascalho, concreto): ver §6, armadilha 11.

### 3.7 Bueiro afogado e sifão sob aterro

- Tratar como bueiro **com controle na saída**, cheio: h_total = h_entrada + h_atrito + h_saída, com Ke da Tabela C.2, atrito de 3.4b e saída 3.4d;
  NA de montante = NA de jusante + h_total. Caso Jaíba CS-25 sob a MG-401 (2 x 1,50 x 1,50 m, L = 90 m, n = 0,015): h_total 0,04 m, NA de
  montante 480,13 m [1182:56-57]. Qualidade B (Q 2,44 x 2 x 1,27).
- HDS-5: o culvert em "sag" (chamado de "sifão invertido") serve a canais de irrigação sob estrada; exige curvas (perdas Kb), tem risco de assoreamento e
  **não se recomenda em curso d'água** [HDS5 p. 139]. A linha piezométrica não cruza a geratriz superior: o nome "sifão" é impróprio; a capacidade extra de
  sifonamento em bueiro comum é esporádica e **não deve ser considerada** [HDS5 p. 141-142, §5.2.5].
- Fronteira: a transição de montante, a perda total do sifão do canal e o greide são de `canais-abertos`; aqui só o NA de montante
  da travessia e a velocidade na entrada e na saída.

### 3.8 Canais de drenagem e valetas (detalhe em `references/valetas-sarjetas-descidas.md`)

- **DNIT:** valeta trapezoidal, revestida (obrigatório em terreno permeável), a 2-3 m da crista ou do pé; Racional + Manning; fixar a velocidade máxima pelo
  revestimento (Tabela 31) e o n; h por tentativa; regime pela altura crítica (evitar h a ±10 % de hc); folga pela Tabela 36 (10 a 20 cm); escalonar se
  v > admissível (declividade de trecho ≤ 2 %, E ≤ 50 m) [DNIT-DREN p. 158-164].
- **HEC-15:** método recomendado = **tensão trativa**, τp ≥ SF·τd, τd = γ d S₀, SF ≥ 1 [HEC15 p. 31, 35]; TR 5 a 10 anos [p. 33]. τp, n e velocidade equivalente:
  `references/velocidades-admissiveis-e-revestimentos.md`. Em solo e pedra pequena a tensão é **mais restritiva** que a Tabela 31: no básico, verificar as duas.
- Froude com a profundidade hidráulica A/B (V2), nunca com y em seção trapezoidal.

### 3.9 Sarjetas, descidas d'água e estradas de serviço (detalhe no mesmo arquivo)

- **Sarjeta de corte (DNIT):** q = C i A/(36×10⁴), i para **5 min e TR 10**; Manning; comprimento crítico d = 36×10⁴ A R^(2/3) I^(1/2)/(C i L n) (eq. 3.03) [DNIT-DREN p. 170-174].
  **Sarjeta pavimentada (HEC-22):** Izzard, Q = (0,376/n) Sx^1,67 S_L^0,5 T^2,67 (SI) [HEC22 p. 79]; TR e espalhamento pela Tabela 5.1 [p. 70].
- **Descida d'água (DNIT):** rápido ou degraus; **Q = 2,07 L^0,9 H^1,6** (Método I) e V no pé = √(2 g h) (superestima), ou perfil de linha d'água (Método II) [DNIT-DREN p. 186-190].
- **Bueiro de greide:** sem carga a montante sempre que possível; policiar V de jusante [DNIT-DREN p. 202].
- **Estrada de serviço de irrigação:** o corpus é rodoviário; aplicar IPR-724 e HEC-22 como **analogia declarada**, TR 25 como premissa do núcleo (V8).

### 3.10 Dispositivos-tipo do DNIT

`references/dispositivos-tipo-dnit.md`: códigos do Álbum **IPR-736** (BSTC, BDTC, BTTC, BSCC, BDCC, BTCC; VPC, VPA, STC, SZC, DAR, DAD, DES, DEB, CCS, CCT) e ES de execução
(023 tubulares, 025 celulares, 026 bocas e caixas, 019 transposição, 022 dissipadores). Escolher o dispositivo **depois** da hidráulica. O Álbum é orientador, não normativo [DNIT-ALBUM PDF p. 23].

### 3.11 TR por tipo de obra

`references/tr-por-tipo-de-obra.md`: bueiro rodoviário 10-20 com verificação 20-25 [DNIT-HIDRO p. 23-24]; sarjeta 10 [DNIT-DREN p. 171]; canal de beira de estrada 5-10
[HEC15 p. 33]; DAEE-SP 25 rural, 100 urbano; acervo 25 a 100. O TR é decisão do projeto: declarar projeto, verificação e J = 1 − (1 − 1/TR)^n.

### 3.12 Métodos legados do acervo (só para comparar)

- **Orifício** (Baixio, doc 896:1): Q = C·A·√(2 g h), C = 0,62; HW = D/2 + h. O IPR-724 dá C entre 0,62 e 0,63 e C(L/D) de Manning: 0,770 (10), 0,674 (25),
  0,643 (50), 0,588 (75), 0,548 (100) [DNIT-DREN p. 91, Tabela 22]; só vale com carga ≤ 2 D.
- **Manning em seção plena ou lâmina fixa** (Baixio, CSB, Salitre, Iuiu): dá capacidade e V, **não o HW**.
- No DNIT/ENAP o bueiro tubular se dimensiona "como canal" e se verifica "como orifício" [ENAP-BUEIROS p. 13]; [DNIT-DREN p. 32]. Esse é o método normativo
  da rodovia; o HDS-5 é mais completo. O legado subestima o HW em **6 a 18 %** (`DIVERGENCIAS_bueiros.md`). Entregar sempre o HDS-5 e a comparação com o legado, rotulada.

## 4. Calculadoras (`tools/hid/bueiros.py`; `canais.py`)

| Cálculo | Função | Fórmula e fonte | Testes (`tests/hid/test_bueiros.py`) |
|---|---|---|---|
| HW de entrada | `controle_de_entrada` | HDS-5 A.1-A.3, Tab. A.1/A.2 | `test_entrada_submersa_formula_fechada`, `test_entrada_nao_submersa_forma1_usa_carga_critica`, `test_transicao_liga_os_extremos`, `test_ku_si_equivale_a_unidades_inglesas` |
| HW de saída | `controle_de_saida` | HDS-5 3.1, 3.4, 3.5; Ke Tab. C.2 | `test_saida_formula_fechada_afogado`, `test_saida_livre_usa_dc_mais_D_sobre_2_e_avisa` |
| HW controlante e catálogo | `dimensionar_bueiro` | max(entrada, saída); ordena por área | `test_dimensionar_ordena_por_area_e_respeita_HW_max` |
| V, y, Fr de saída; dissipador | `velocidade_de_saida`, `dissipador_necessario` | HDS-5 §3.1.6; limite da calculadora | `test_velocidade_saida_e_dissipador` |
| Legado | `orificio`, `comparar_legado_hds5` (CLI); `verificacao_manning_plena` (só Python) | orifício C = 0,62; Manning | `test_orificio_ida_e_volta`, `test_baixio_legado_vs_hds5_5pct` |
| Valeta, canal, y_normal, y_crítica, Fr, folga | `canais.y_normal`, `y_critica`, `froude`, `manning_Q`, `borda_livre` | Manning, Chow | `tests/hid/test_canais.py` |

Comandos de exemplo (SI):

```
python -m tools.hid.bueiros --json '{"funcao":"controle_de_entrada","Q":8.495,"forma":"retangular","dim":[1.524,1.524],"tipo_de_entrada":"ret_alas_90_15","S0":0.02}'
python -m tools.hid.bueiros --json '{"funcao":"controle_de_saida","Q":5.663,"forma":"circular","dim":1.3716,"n":0.012,"Ke":0.2,"L":60.96,"S0":0.01,"TW":1.067}'
```

O que conferir em `avisos`: "saída livre (TW < D)" (energia aproximada; ir ao remanso se HW < 1,2 D); "HW de saída < D" (resultado não aplicável);
"dc ≥ D" (barril crítico a seção cheia); "arco: área de elipse" (usar dados do fabricante); "S0 > 10 %" (fora da validade); "células paralelas:
afastamento" (usar §3.5, não a fonte citada no aviso); "nenhuma alternativa atende HW_max". `regime` = nao_submersa, transicao ou submersa: reportar.
**Fora da calculadora (lacuna; calcular e registrar):** sarjeta de Izzard, descida d'água (eq. 2,07 L^0,9 H^1,6), tensão trativa HEC-15, n composto,
galgamento da estrada (eq. 3.9: Cd(SI) = 0,552 × Cd da Fig. 3.11 [HDS5 p. 97]), entrada afunilada, esconsidade, curva de desempenho. Pedir ao dono do
pacote novas funções; o agente não altera `tools/`.

Exemplos numéricos de conferência (HDS-5 DG1, DNIT, HEC-22, Salitre/Xingó/CSB): `references/exemplos-de-conferencia.md`.

## 5. Critérios de projeto e verificação (antes de entregar)

- **V1:** todo número com unidade e fonte; comando e saída gravados em `pareceres/`.
- **V2:** regime declarado em canal e valeta (Froude com A/B); n do barril e da valeta com fonte.
- **V3:** bueiro nos **dois** controles; adota-se o maior HW; legado só rotulado como comparação.
- **V6:** alternativas com custo relevante (DN x células, material, entrada, dissipador) vão ao Orçamento antes da recomendação final.
- **V8:** Q recebida com método compatível com a bacia e TR declarado; não corrigir Q aqui.
- **V9:** dissipador por V de saída x material, Fr e TW; dimensionamento é da vizinha.
- **V11:** edição citada; norma não aberta (NBR 8890) só citada.
- **V12:** cada dado de outra disciplina (fundação, classe do tubo, greide, chuva) com `[DELEGAR]` e premissa provisória.

Checklist: Q, TR e TW de origem; entrada e Ke; HW_i, HW_o, HW; folga à cota admissível; V de saída x material; TR de verificação; esconsidade; recobrimento;
n escolhido e porquê; quantitativos para o Orçamento; pendências para o básico.

## 6. Armadilhas do acervo (casos negativos)

| # | Armadilha | Onde | Como detectar e o que fazer |
|---|---|---|---|
| 1 | Bueiro verificado só por orifício ou Manning; HW 6 a 18 % abaixo do HDS-5 (sempre contra a segurança) | Baixio, CSB, Xingó, Salitre | HW/D ausente no memorial; rodar `comparar_legado_hds5`; exigir HW de entrada e de saída |
| 2 | "Capacidade livre" TR 25 passa, mas Q50 > capacidade e o projetista aceita com carga | Baixio (BU-CP0-13: 33,4 x 27,0 m³/s) | comparar Q de verificação com a capacidade crítica (Tabela 2 do DNIT) e calcular HW |
| 3 | Coluna "Situação OK" com folga negativa; planilha final marca OK onde a REV 2 marcava "Redimensionar!" | Baixio, aba "Sob estradas" (CS1-01: −0,96 m) | refazer a folga com a cota do terreno; nunca usar a coluna "Situação" como gabarito |
| 4 | Q/célula acima da capacidade crítica da seção: a entrada afoga e HW > D, mas só se reporta V e Yo | Salitre BTCC 7 (20 m³/s por célula em 2 x 2 m: HW/D ≈ 2,3 por HDS-5, entrada hipotética) | `controle_de_entrada` com a entrada declarada; X > 4 = submersa |
| 5 | V/Yo do quadro 4.7 que não reproduz Manning (3 células 2 x 2, i = 0,0045: 28,6 x 39,2 m³/s) | CSB BTCC-17 | não usar V/Yo sem conferir a página; HDS-5 dá HW 2,83 m (HW/D 1,4) |
| 6 | Lâmina supercrítica de perfil lida como lâmina normal (0,96 x 0,83 m) | Xingó BU-01, 06, 24 | método do projeto é energia a partir da seção crítica com K = 0,5; Manning normal não reproduz (xfail documentado) |
| 7 | Q 2,44 x 2 x 1,27 = 2,54 m³/s | Jaíba CS-25 | exigir Q de projeto e Q por célula coerentes; ke e kex não impressos |
| 8 | Coeficiente impresso **1,638** na vazão crítica do celular (Q = 1,638 L H^1,5): a Tabela 2 do próprio manual e a teoria dão **1,705** (2/3 · 2,56): 4 % a menos | IPR-724 p. 54-55 | usar a tabela; conferir 2,0 x 2,0 = 9,64 m³/s |
| 9 | Tabela 1 do DNIT (tubular) usa Vc = 2,56 D^0,5 do retângulo: Q crítica ≈ 7 % acima da exata (DN 1,00: 1,53 x 1,43 m³/s) | IPR-724 p. 55 | usar HDS-5, não a tabela de tubular |
| 10 | Ke de muros de ala paralelos = 0,2 no DNIT x 0,7 no HDS-5 (caixa, aresta viva no topo) | IPR-724 p. 130 x HDS5 p. 216 | usar 0,7; registrar |
| 11 | Limite de velocidade da calculadora até 2× mais permissivo que o DNIT (areia, cascalho; concreto 6,0 x 4,5 m/s); HEC-15 não traz tabela de velocidade | `bueiros.py` x IPR-724 p. 131 | comparar a V de saída com a Tabela 31; abrir pendência |
| 12 | "Declividade mínima 5 %" do bueiro: provavelmente 0,5 % ou o intervalo "0,4 a 5 %" do IPR-724 truncado | Iuiu 1051:331 | hipótese a confirmar na página; usar 0,4 % mínimo (DNIT-DREN p. 34) |
| 13 | Orifício com C = 0,62 fixo: ignora L/D (C de Manning: 0,77 em L/D = 10; 0,643 em 50; 0,548 em 100); conservador para L/D < 50, contra a segurança acima | legado (Baixio, L/D ≈ 16) | conferir L/D e carga ≤ 2 D contra [DNIT-DREN p. 91] |
| 14 | Folga ao terreno do gabarito que não fecha (0,66 x 0,464 m; cota 407,846 reproduz) | Baixio BU-CP0-15 | refazer a aritmética da folga; ver `DIVERGENCIAS_bueiros.md` |

## 7. O que a norma e o manual exigem e a quem se aplica (resumo; detalhe em `normas-e-manuais`)

- **IPR-724 (DNIT):** rodovias federais; bueiro "como canal, vertedor ou orifício" e, no projeto final, pelo método da Circular nº 5 do BPR (nomogramas de
  entrada e de saída, como o HDS-5) [DNIT-DREN p. 32, 101-116]. Em estrada de serviço de irrigação aplica-se por analogia.
- **ES DNIT 019, 022-026, 030, 096:** execução e medição; sem projeto específico, usar o Álbum [DNIT-ES023 p. 3].
- **HDS-5, HEC-15, HEC-22 (FHWA):** método, ±10 % no HW, critério de HW do órgão [HDS5 p. 72, 83]; valetas e sarjetas [HEC15 p. 33; HEC22 p. 70].
- **DAEE-SP IT DPO 11/2017:** outorga em SP (TR mínimo, velocidade); fora de SP é referência [DAEE-IT-DPO11 p. 1-4].
- **NBR 8890 (ABNT 2020, não aberta):** tubo de concreto pluvial; substitui NBR 9793/9794; **citar, não transcrever** [DNIT-ES023 p. 3; `NAO_ABERTOS.md`].

## 8. Referências (IDs e páginas-chave)

FHWA-HDS5: p. 83-94, 96-100, 105-108, 139-142, 149-150, 190-200, 208, 216, 272-281. FHWA-HEC15: p. 29-35, 98. FHWA-HEC22: p. 70, 79-80. FHWA-HDS4: cap. 9 (p. 158,
remete ao HDS-5). DNIT-DREN (IPR-724): p. 32-34, 54-56, 91, 101-102, 114, 130-134, 158-190, 202. DNIT-HIDRO (IPR-715): p. 23-24. DNIT-ALBUM (IPR-736): Sumário PDF p. 9-15,
Introdução p. 23. DNIT-ES019/022/023/024/025/026/030/096. ENAP-BUEIROS e ABDER-APOSTILA: didáticos (repetem o DNIT). PMSP-DRENURB-V2 p. 30. DAEE-IT-DPO11. Casos:
`casos/drenagem_dissipadores/`; `tools/hid/DIVERGENCIAS_bueiros.md`.

## 9. Lacunas do corpus e o que pedir

- **ES DNIT 018 (sarjetas e valetas) e 021 (descidas d'água)**, citadas pelo IPR-724, ausentes do corpus. **Álbum IPR-736 sem OCR** (escaneado): só o Sumário foi lido.
- HDS-5 §3.4 (afunilada), nomogramas do Apêndice C, DG 3 e DG 4; HEC-15 caps. 4, 5, 7; HEC-14: só ponteiros.
- Sem fonte: TR numérico de bueiro de **irrigação**; norma da Codevasf para travessias; velocidade admissível do canal de drenagem do projeto (perguntar ao usuário).
- Calculadora sem: sarjeta de Izzard, descida d'água, tensão HEC-15, afunilada, galgamento, esconsidade, curva de desempenho, n composto.
- NBR 8890 não aberta (classes e cargas: Estruturas). TW composto ou remanso a jusante: `canais-abertos`; velocidade erosiva real do solo: Geotecnia.
