# Exemplos numéricos de conferência (primário x calculadora x acervo)

Uso: validar a calculadora e treinar o agente. Todos os comandos rodam na raiz do pacote
(`python -m tools.dren.bueiros --json '{...}'`). Data da conferência: 2026-10-01. Valores "calc." foram obtidos com
`tools/dren/bueiros.py` (v0.1.0 a 0.3.0; as constantes de entrada não mudaram). Marca: **[prim.]** = número do primário; **[calc.]** = saída da calculadora; **[hip.]** = entrada
hipotética do avaliador (não é gabarito do projeto).

## 1. HDS-5, Design Guideline 1 (exemplos resolvidos pelo FHWA)

### 1.1 Caixa de concreto, 5 x 5 ft (1,524 m), Q50 = 300 cfs = 8,495 m³/s, S = 0,02, L = 76,2 m, TW = 1,219 m [HDS5 p. 279-281]

| Entrada | HW [prim.] | HW [calc.] | Desvio |
|---|---|---|---|
| aresta viva, muro de testa (chart 8, 90°/15°, `ret_alas_90_15`) | HY-8: 9,65 ft = **2,94 m**; nomograma: 109,6 − 100 = 9,6 ft | **2,959 m** (submersa, X > 4) | +0,6 % |
| bisel de 45° (chart 10, `ret_muro_bisel_45`) | 108,6 − 100 = 8,6 ft = **2,62 m** | **2,612 m** | −0,3 % |

```
python -m tools.dren.bueiros --json '{"funcao":"controle_de_entrada","Q":8.495,"forma":"retangular","dim":[1.524,1.524],"tipo_de_entrada":"ret_alas_90_15","S0":0.02}'
```

Controle de entrada governa (o HW de saída do exemplo é 103,2 − 100 = 3,2 ft). Velocidade de saída [prim.] 6,47 m/s (1524 x 1524 mm). A
descrição "square edges" não diz qual das famílias de aresta viva o exemplo usa (o chart 8 com alas de 90° e 15° reproduz
2,94 m); registrar a hipótese.

### 1.2 Tubo de concreto, 54" (1,3716 m), ponta-e-bolsa, Q25 = 200 cfs = 5,663 m³/s, S = 0,01, L = 60,96 m, TW = 1,067 m [HDS5 p. 273-274]

| Item | [prim.] | [calc.] | Desvio |
|---|---|---|---|
| HW entrada (`circ_concreto_boca_sino_muro`) | nomograma 108,0 − 100 = 8,0 ft = 2,44 m; HY-8 7,9 ft = 2,41 m | 2,415 m | +0,3 % (HY-8); −1,0 % (nomograma) |
| HW entrada com `circ_concreto_boca_sino_projetante` | idem | 2,467 m | +1,2 % (nomograma) |
| HW saída (n = 0,012, Ke = 0,2) | menor que a entrada (controle de entrada governa, p. 274) | 2,125 m | coerente |
| Velocidade de saída, lâmina normal | 15,3 ft/s = 4,66 m/s (nomograma); HY-8 14,9 ft/s | 4,64 m/s (y = 1,06 m, Fr = 1,44) | −0,4 % |

```
python -m tools.dren.bueiros --json '{"funcao":"controle_de_entrada","Q":5.663,"forma":"circular","dim":1.3716,"tipo_de_entrada":"circ_concreto_boca_sino_muro","S0":0.01}'
python -m tools.dren.bueiros --json '{"funcao":"velocidade_de_saida","Q":5.663,"forma":"circular","dim":1.3716,"n":0.012,"S0":0.01,"TW":1.067}'
```

Sugestão de teste novo (`tests/dren/test_bueiros.py`): os dois itens acima, com tolerância de 2 % (a do HDS-5 é ±10 % no HW).
Outros tamanhos de HDS-5 DG1 (72" CMP, projetante e muro, HWi = 105,8 ft; HWo = 105,5 ft; p. 273): não conferidos aqui (n do
CMP e tipo de entrada não fecham sozinhos).

Adicionais do DG1: 60" CMP de HWo = 108,9 ft > cota admissível 108 ft e 54" RCP de HWi = 108,0 ft [HDS5 p. 274]: a troca de
material de CMP para RCP (n menor, Ke menor) tira o controle da saída.

## 2. DNIT-IPR-724: capacidade "como canal", energia específica = altura (Tabelas 1 e 2)

Reproduzir: Q tal que Hc = dc + Vc²/2g = D (ou H). Conferência por função interna `_carga_critica` (bissecção em Q):

| Seção | Q crítica [prim.], m³/s | [calc.] | Desvio |
|---|---|---|---|
| BSCC 1,0 x 1,0 | 1,71 | 1,70 | -0,6 % |
| BSCC 1,5 x 1,5 | 4,70 | 4,70 | 0 |
| BSCC 2,0 x 1,5 | 6,26 | 6,26 | 0 |
| **BSCC 2,0 x 2,0** | **9,64** | **9,64** | 0 |
| BSCC 3,0 x 3,0 | 26,58 | 26,58 | 0 |
| BSTC DN 0,60 / 0,80 / 1,00 / 1,20 / 1,50 | 0,43 / 0,88 / 1,53 / 2,42 / 4,22 | 0,40 / 0,82 / 1,43 / 2,25 / 3,93 | **−7 %** (calc. menor) |

As Tabelas de celulares [DNIT-DREN p. 56] fecham com a calculadora. A **Tabela 1 dos tubulares** [p. 55] usa V = 2,56 D^0,5
(velocidade crítica do retângulo) também para o círculo: Q = A V com A = 0,60 m² (DN 1,00) dá 1,53. A energia específica crítica do círculo
com E = D exige Q = 1,43 m³/s (conferido por cálculo independente de y_c e Fr = 1: y_c = 0,689 m, V = 2,42 m/s). Resultado: a
tabela do DNIT para tubular é ≈ 7 % **contra a segurança** na vazão crítica. Registrar quando usar o DNIT; preferir HDS-5.

Sugestão de teste novo: `BSCC 2,0 x 2,0 → 9,64 m³/s` e `BSCC 3,0 x 3,0 → 26,58` com tolerância 0,5 % (DNIT-DREN p. 56). O
coeficiente "1,638" do texto não deve ser usado em teste (§ SKILL.md armadilha 8).

## 3. HEC-22, sarjeta triangular (Izzard)

Movida para `drenagem-de-estradas-e-plataformas` (função `bueiros.sarjeta_triangular_izzard`; Ex. 5.1 conferido: 2,755 m e 0,03947 m³/s).

## 4. Legado do acervo x HDS-5 (de `DIVERGENCIAS.md`)

Entrada hipotética (alas 30-75, L = 40 m, TW = 0): HW legado (orifício, C = 0,62) 3,31 / 4,51 / 5,02 m; HDS-5 3,60 / 4,82 / 5,44 m
(BU-CP0-13 / 15 / 18): **−8,0 / −6,4 / −7,8 %**. BU-CP0-27 e BU-CS1-01: −4,3 %. Dentro da incerteza do HDS-5 (±10 %), mas **sempre
para menos**. Com alas 90/15 ou 0°: −12 a −18 %. Comando de comparação:

```
python -m tools.dren.bueiros --json '{"funcao":"comparar_legado_hds5","Q":61.98,"forma":"retangular","dim":[2.5,2.5],"tipo_de_entrada":"ret_alas_30_75","n":0.015,"L":40,"S0":0.005,"TW":0,"n_celulas":2}'
```

(Q50 de BU-CP0-15 [896:1], 2 células de 2,5 x 2,5; ver `casos/.../baixio_irece_bueiros_dimensionamento.md`.)

## 5. Verificação por controle de entrada de bueiros do acervo que usaram só Manning ou energia [hip.]

Entrada hipotética `ret_alas_30_75`; declividade de jusante ou do corpo do projeto; células iguais; **[hip.] não é gabarito**:

| Obra | Q (m³/s), células, seção, S | HW/D [calc.] | Regime | Leitura |
|---|---|---|---|---|
| Salitre BTCC 1 (1357:197) | 24,16; 3; 1,5 x 1,5; 0,0051 | **1,78** (HW 2,67 m) | submersa, X = 5,3 | o projeto só mostra Manning (Yo 1,3 m; V 4,1 m/s) |
| Salitre BTCC 2 | 34,47; 3; 2,0 x 2,0; 0,0076 | 1,24 (2,48 m) | transição, X = 3,7 | passa só com HW > D |
| Salitre BTCC 7 | 60,45; 3; 2,0 x 2,0; 0,0107 | **2,25** (4,50 m) | submersa, X = 6,5 | Q/célula 20 m³/s em 2 x 2 m: acima da capacidade crítica de 9,6 m³/s |
| Xingó BU-24 (1419:154) | 48,8; 2; 3,0 x 3,0; 0,00976 | 1,01 (3,04 m) | não submersa, X = 2,8 | o projeto usa energia crítica na entrada com K = 0,5: confere com HDS-5 |
| Xingó BU-01 | 8,96; 2; 1,5 x 1,5; 0,01009 | 1,04 (1,56 m) | não submersa | idem |
| CSB BTCC-17 (1341:205) | 39,18; 3; 2,0 x 2,0; 0,0045 | 1,41 (2,83 m) | submersa, X = 4,2 | coincide com `DIVERGENCIAS.md` (HW 2,83 m, HW/D ≈ 1,4) |

Moral: o método "Manning" (Salitre, CSB, Iuiu) não revela o HW; o método "energia crítica na entrada" (Xingó) equivale ao HDS-5 não
submerso. Quando Q/célula excede a capacidade crítica da seção, a entrada afoga e **o HW passa de D**. Exigir HW/D e a cota de
montante no parecer, nunca só V e Yo.

## 6. Sifão sob aterro tratado como bueiro afogado (Jaíba, 1182:56-57)

Q = 2,44 m³/s (doc) ou 2 x 1,27 = 2,54 m³/s; 2 células 1,5 x 1,5 m; L = 90 m; n = 0,015; NA jusante 480,09 m.
htotal = hen + hf + hs; hf = (19,63 n² L/R^1,33) V²/2g; V = 0,564 m/s com 1,27 m³/s por célula; hf = 0,024 m (doc 0,02);
perda total 0,048 m (Ke = 0,5 e saída com V²/2g inteira) e **NA de montante 480,138 m** [calc.] contra 480,13 m do doc (tolerância 0,01 m); o doc soma 0,04 m com ke e kex não impressos. Teste existente: `tests/dren/test_bueiros.py` (Jaíba, listado em
`DIVERGENCIAS.md` como reproduz). A divergência Q = 2,44 x 2,54 fica no caso.

## 7. Tubo parcialmente cheio e regime crítico (v0.3.0)

- **Delmiro BUC-2 a BUC-5** (acervo 1493:282-285, sem ✓h; Manning n = 0,015): `tubo_parcialmente_cheio` reproduz y, V e Fr dos 8 casos (TR 20 e 50) dentro de 1 %. Ex.: D 0,80, S 0,005, Q 0,499 -> y 0,454 m, V 1,70 m/s, Fr 0,89 (A/T). BUC-5 em TR 50 chega a y/D = 79 %: passa do limite provisório de 75 % (aviso, decisão F7).
- **HDS-3 Ex. 10 a 17** [FHWA-HDS3 p. 53-55]: conferidos a 0,4-1,3 %; Ex. 12, 15 e 17 são leitura de gráfico (1,3 a 2,3 %), usar com 5 %.
- **Regime crítico do tubular** (`regime_critico_tubular_ime`, [LOC-IME p. 151-152]): θc = 4,0335 rad, A_c = 0,601 D², Vc = 2,56 D^0,5, Qc = 1,538 D^2,5 (impresso 1,533). Vazão crítica exata de Ec = D é ~7 % menor (`vazao_critica_exata`).
- **HDS-5 p. 280** (caixa 1,524 m, Q50 8,495 m³/s, S 0,02): V de saída 6,47 m/s (SI do texto); o CU do mesmo texto dá 6,34 e o HY-8 5,98. A calculadora com n = 0,012 dá 6,45; com n = 0,013, 6,07 (-6 %): **o gabarito depende de n**, que o texto não informa.
- **Xingó (legado)** Q = 33,5 D^2,67 i^0,5 equivale a n = 0,0093; com n de projeto 0,012-0,013 a capacidade cai 22 a 28 %.
