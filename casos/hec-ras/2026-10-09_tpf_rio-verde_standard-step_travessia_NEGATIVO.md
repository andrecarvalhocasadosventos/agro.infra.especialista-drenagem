# Caso HR-06 — NEGATIVO: NA do rio Verde na travessia do aqueduto (Standard Step, TR 100 × 50)

**Tipo:** negativo (divergência entre documentos e premissas sem dado). **Pergunta:** qual o NA de cheia no aqueduto sobre o rio Verde?
`REL-FINAL` (id 1709, p. 49-55), `ACOMP-0811` (id 1503, p. 3), `NOTAS-TPF` (`Notas_Reunioes_TPF - até 12set26.pdf`, id 1505, p. 2). **Não há arquivo de modelo** no acervo (só os dois `.zip` de HEC-RAS, que não contêm o rio Verde). O relatório não declara o software do Standard Step (o texto fala em "método Standard Step", REL-FINAL:54; o HEC-HMS é citado só para a hidrologia, REL-FINAL:50). Marcas A, B; sem ✓h.

## Dados de entrada
| Item | Valor | Fonte | Marca |
|---|---|---|---|
| Bacia até a travessia | 10.812,20 km², 7 sub-bacias; barragem de Mirorós a montante e de Maravilhas a ~2,4 km a jusante | REL-FINAL:49-50 | A |
| Vazão SB1 (regularizada por Mirorós), TR 100, Gumbel sobre máximas anuais do posto 47236000 (SisCAH) | 203,84 m³/s | REL-FINAL:50 | A |
| Demais sub-bacias | SCS por TR 100, Tc de Kirpich, lag = 60 % de Tc; HEC-HMS; Muskingum-Cunge com vazão de referência = 70 % da máxima afluente; n = 0,035 | REL-FINAL:50-52 | A |
| Vazão máxima simulada no exutório | 3.417,14 m³/s | REL-FINAL:53 | A |
| Contorno de jusante | cota 393 m = soleira do vertedor da barragem de Maravilhas (estimada por LIDAR) | REL-FINAL:54 | A |
| Seção do rio | trapézio de área molhada equivalente: base 12 m, taludes 18H:1V, n 0,035 (do posto 47249000, sem batimetria) | REL-FINAL:54 | A |
| Resultado | NA ≈ **397 m** na travessia | REL-FINAL:55; NOTAS-TPF:2 (cota alinhada) | A |

## Verificações (B)
- Lag = 0,6·Tc·60: SB1 849,24 min contra 849,42; SB3 903,96 contra 903,96 (OK).
- Vazão de referência = 0,7·Qmáx: R1 142,69; R2 1.069,61; R3 2.256,93; R4 2.808,32; R5 2.688,30; R6 2.425,98 (iguais à Tab. 7).
- Tc de Kirpich (fórmula do relatório, REL-FINAL:50): SB1 23,75 h contra 23,59; SB7 **42,82 h contra 39,84 h (+7,5 %)**; as demais sub-bacias entre −1,3 % e +0,7 % (SB7: declividade 0,02 % é muito sensível ao arredondamento).

## Problemas
1. **TR 100 × TR 50.** ACOMP-0811:3 diz: "*Verificou-se no material recebido que o TR considerado para a travessia do rio Verde foi de 50 anos*"; o REL-FINAL:50-55 e o critério de aqueduto (TR 100; `ACOMP-0812`, id 1504, p. 4) falam em TR 100. Não é possível saber qual TR gerou o NA = 397 m sem o modelo.
2. **Vazão do cálculo hidráulico não declarada.** O relatório dá 3.417,14 m³/s no exutório (REL-FINAL:53), mas a Tab. 7 traz vazões máximas afluentes de 3.224,18 (R3), 4.011,88 (R4), 3.840,43 (R5) e 3.465,68 m³/s (R6); o texto do NA diz só "vazão de TR 100" (REL-FINAL:55). A diferença entre 3.417 e 4.012 é de 17 %.
3. **Contorno de jusante = cota da soleira**, sem carga sobre o vertedor, "diante da indisponibilidade de informações hidráulicas da barragem" (REL-FINAL:54). Com Q = 3.400 m³/s o NA a jusante é a soleira mais H (carga do vertedor), não a soleira; erro de contorno desta ordem se propaga a montante em regime subcrítico. A cota 397 m é, então, um piso, não um valor conservador (C: efeito não quantificado).
4. **Seção sintética** (18H:1V e 12 m de base) em vez de seções reais (sem batimetria), e n único.
5. **Modelo 1D x 2D não declarado**, sem arquivo para reprodução.
6. NOTAS-TPF:2 fixou 397 m "para balizar o projeto do aqueduto" antes de resolver 1 a 5.

## O teste que revelaria
Refazer o Standard Step com Q = 3.417 e 4.012 m³/s, TR 50 e 100, jusante = soleira + carga do vertedor (ex.: C·L·H^1,5 para Q); sensibilidade de n 0,030-0,045; comparar NA na travessia (hoje 397 m). Exige seções do LIDAR (trecho 2,4 km).

## Gabarito do caso negativo
O parecer correto aceita 397 m apenas como "NA preliminar de aqueduto", lista os 4 itens acima e pede seções reais, TR único (100) e contorno com carga de vertedor; nenhum número aqui é ✓h.
