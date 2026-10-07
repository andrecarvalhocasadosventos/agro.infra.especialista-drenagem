# Jaíba Etapas 3 e 4 — Sifão invertido sob a MG-401 tratado como bueiro afogado com controle na saída (doc 1182)
fonte: Relatorio de Anteprojeto_Jaiba Etapas 3 e 4.pdf (doc 1182):56-57
disciplinas: [bueiros-e-drenagem-superficial]
nivel: anteprojeto

## Problema
Canal CS-25 (Etapa 4) em aterro (~1,70 m) cruza a rodovia MG-401 na estaca 1+480; solução: sifão de galeria dupla.

## Dados de entrada
| grandeza | valor | unidade | fonte doc:pág | ancoragem |
|---|---|---|---|---|
| Vazão | 2,44 | m³/s | 1182:57 | texto |
| Células | 2 (1,50 x 1,50 m), 1,27 m³/s cada | — | 1182:57 | texto |
| Comprimento | 90,00 | m | 1182:57 | texto |
| Manning n | 0,015 | — | 1182:57 | texto |
| NA jusante / profundidade / velocidade a jusante | 480,09 m / 1,20 m / 0,64 m/s | — | 1182:57 | texto |
| Coeficientes de perda | DNIT (2005) e FHWA (2012); valores de ke e kex não impressos | — | 1182:56 | texto |

## Método
"Hidraulicamente, o sifão é similar a um bueiro afogado, com controle na saída" (1182:56). htotal = hen + hf + hs; hen = ke·V²/2g; hf = (19,63·n²·L/R^1,33)·V²/2g (equação FHWA em unidades SI); hs = kex·(V²/2g − Vex²/2g). Sem nomograma/HY-8.

## Resultado (Tabela 7.12, 1182:57)
V = 0,57 m/s; Rh = 0,38 m; h entrada 0,01; h distribuída 0,02; h saída 0,01; h total 0,04 m; NA montante = 480,09 + 0,04 = 480,13 m.

## Gabarito para calculadora
- bueiro.py (controle de saída, afogado): Q=2,44 m³/s, 2 células 1,5x1,5, L=90 m, n=0,015, NA jusante 480,09 -> V = 1,22/2,25 = 0,542... (doc 0,57 usa Q/célula 1,27, que somado dá 2,54 ≠ 2,44: divergência interna). Com Q/célula = 1,27: V=0,564 m/s; hf = 19,63·0,015²·90/0,375^1,33 · V²/2g = 0,024 m (doc 0,02); NA montante = 480,13 m (tol. 0,01 m).

## Observações
- Divergência: vazão 2,44 m³/s vs 2 células x 1,27 = 2,54 m³/s (1182:57). Provavelmente Q de projeto 2,54 arredondado ou erro de digitação; a velocidade e as perdas do doc usam 1,27 por célula.
- Perda entrada/saída com valores 0,01 m (ke ≈ 0,5 e kex ≈ 1,0 supostos, não impressos).
- Único caso do acervo com declaração explícita "controle na saída"; o "controle de entrada" explícito aparece no Xingó (energia crítica na entrada) e no Baixio (orifício TR 50).
