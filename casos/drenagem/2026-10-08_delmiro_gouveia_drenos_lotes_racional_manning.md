# Delmiro Gouveia — drenos superficiais dos lotes irrigados (Racional C=0,15, IDF TR 10, Tc por Kirpich + viagem, Manning n=0,025, seções ZTT)
fonte: Memorial descritivo Tomo II (doc 1520, duplicata 1492):120-137 e Memória de cálculo hidráulico Vol. 2 Tomo I (doc 1521, duplicata 1493):120-187 — Projeto de Irrigação Delmiro Gouveia, CODEVASF 2016, executivo (Hydros)
disciplinas: [canais-de-drenagem-e-macrodrenagem, hidrologia-de-projeto-para-drenagem]
nivel: projeto executivo
tipo: positivo (as colunas da planilha se reproduzem; falhas de seção e de critério estão no caso `2026-10-08_delmiro_gouveia_drenos_secao_subdimensionada_folga.md`)
qualidade: A para o fluxo Racional -> Manning (194 trechos com Q = A·V e Froude < 1); B no critério (TR 10 e Tc mínimo de 10 min não vêm em texto)

## Problema
Dimensionar 86 drenos (37,6 km) dos setores SH-11 e SH-12, em solos arenosos sem rede hidrográfica definida, para escoar com segurança os excedentes pluviais após o início da irrigação. Seções padronizadas em terra (ZTT) ou concreto (ZTC), declividade de fundo próxima à do terreno, quedas para limitar a velocidade.

## Dados de entrada
| grandeza | valor | un. | fonte | anc. |
|---|---|---|---|---|
| método | Racional Q = 0,278·C·I·A (A em km²) | — | 1520:126 | A |
| C | 0,15 (solo arenoso, declividade 2–7 %, grama; Gribbin 2009) | — | 1520:127 | A |
| IDF | I = a/(t+b)^c; TR 10: a 963,95, b 9,787, c 0,724 (Quadro 3.44; também 5, 20, 50, 100 anos) | mm/h, min | 1520:127 | A |
| TR dos drenos | não informado em texto; a planilha usa a=963,9531, b=9,786982, c=0,724272, iguais à linha TR 10 do Quadro 3.44 | anos | 1521:120, 122 | B |
| Tc da ACP de montante | Kirpich com L (m) e H (m); fórmula só em imagem no memorial | min | 1520:127 | A (fórmula não legível) |
| Tc a jusante | Tc do nó anterior + tempo de viagem = L do trecho / V | min | 1520:127-128 | A |
| Manning | n = 0,025, drenos escavados em terra | — | 1520:129 | A |
| folga | mínima de 25 % do tirante; folgas menores e transbordamento localizado < 4 h admitidos entre seções | — | 1520:129 | A |
| quedas | módulos de 0,25 m, agrupados em quedas de 1,00 m (4 módulos) | m | 1520:129 | A |
| seções padrão | ZTT01 b 0,20/h 0,20 (A 0,080 m²) até ZTT09 b 2,50/h 1,90 (A 9,961 m²); talude 1:1 (ZTT01, ZTT02) e 1,5:1 nas demais | — | 1520:130 (Quadro 3.45) | A |

## Método do projetista
Cada sub-bacia é dividida em ACPs; o primeiro trecho de dreno recebe só a ACP de montante, e cada trecho seguinte soma as áreas a montante mais a área direta (1520:126). Para cada trecho a planilha calcula Tc total, intensidade, precipitação de projeto (I·Tc/60), Q, declividade de fundo Io = (desnível do terreno − nº de quedas × queda unitária)/L, e verifica o tirante, V, Froude (com profundidade hidráulica A/T) e folga na seção escolhida (1521:120-187). Declividade inversa do terreno ou V muito baixa levam a aprofundamento do dreno a jusante (1520:129).

## Resultado e gabarito (valores lidos; conferências em B)
Trecho DS-1.1/C (1521:120; Quadro 3.46 em 1520:131): A total 13,92 ha, C 0,15, Tc de montante 13,44 min + viagem 3,52 = Tc 16,95 min, I = 89,21 mm/h, P = 25,21 mm, Q = 0,518 m³/s; ZTT04 (b 0,60, h 0,45, 1,5:1), n 0,025, Io 0,00368 (desnível 5,75 m, 20 quedas de 0,25 m, L 203 m), tirante 0,43 m, A molhada 0,538 m², P 2,156 m, R 0,250 m, V 0,962 m/s, Froude 0,576, folga recomendada 0,11 m e adotada 0,02 m.
Trecho DS-1.1/A, o de montante (1521:120): 5,15 ha, L 280 m, desnível 2 m (cotas 240,0 e 238,0) -> Tc 10,01 min, I = 110,89 mm/h, Q = 0,238; ZTT03.
Trecho DS-1.2/G (1521:122): 63,66 ha, Tc 31,27 min, I 65,39, Q 1,736 m³/s, Io 0,00298, ZTT07 (b 1,40, h 1,05), tirante 0,626, V 1,187, Froude 0,567.
Gabarito para a calculadora (tolerância 1 %): I(Tc) = 963,9531/(Tc + 9,786982)^0,724272 -> I(16,95) = 89,22; Q = 0,278·0,15·I·0,1392 = 0,518 (B, reproduz); Manning com b 0,60, z 1,5, Io 0,00368, n 0,025 e Q 0,518 -> tirante 0,431 (A mol. 0,537, V 0,965; planilha 0,43, 0,538 e 0,962); tempo de viagem = 203/(0,962·60) = 3,52 min; Kirpich padrão (0,0195·L^0,77·(H/L)^−0,385) com L 280 e H 2 -> 10,01 min (reproduz a planilha).
Totais: 194 trechos no Quadro 3.46 (1520:131-135); Q = A_molhada·V em todos (B); Froude < 1 em todos (máximo 0,844 em DS-2.5/A); V entre 0,29 e 1,19 m/s; soma das extensões do Quadro 3.47 = 37.569,13 m (86 itens, B; confere com "TOTAL" em 1520:137).

## Rastro
A: critérios e valores da planilha. B: reprodução de I, Q, V, tempo de viagem e Io; TR 10 inferido por igualdade de coeficientes; total de extensão. C: fórmula de Kirpich (imagem não lida) e piso de 10 min para Tc.

## Divergências / observações
- Tc mínimo de 10 min: nas linhas de montante com Kirpich < 10 min (DT-1.1.1: L 145 m, H 3,5 m, Kirpich padrão 3,8 min) a planilha usa 10,00 min (1521:120). O memorial não declara esse piso (C).
- A planilha cita "a 963,9531" para a recorrência sem imprimir o TR; o memorial não diz TR dos drenos (não informado).
- A planilha fixa C = 0,15 em todas as ACPs; o memorial justifica por solo arenoso homogêneo (1520:127).
- Vazão decresce a jusante com a mesma área (DS-2.10/D, E, F: 47,38 ha, Q 1,476, 1,381, 1,333; 1520:133) porque Tc cresce sem amortecimento; comportamento típico do Racional com Tc acumulado, não erro.

## Marcas de ancoragem
Valores lidos direto das páginas (texto nativo, sem marca `!`, `~` ou `✓*`). Nenhum `✓h`: gabarito provisório até conferência humana.

## Fronteira
Chuva de 24 h por TR e IDF são do Clima; bueiros sob estradas e passagens molhadas dos lotes (Anexo 7.2) e drenagem do sistema viário por CN/HU (Anexos 7.3–7.5) são de outros lotes.
