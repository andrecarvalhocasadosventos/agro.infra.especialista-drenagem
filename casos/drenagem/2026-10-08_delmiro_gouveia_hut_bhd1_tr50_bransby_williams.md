# Delmiro Gouveia (CODEVASF 2016, Hydros) — Hidrograma unitário triangular da bacia BHD1, TR 50: Tc por Bransby-Williams, fra, perdas SCS e convolução
fonte: Vol. 3 Tomo I Estudos hidrológicos e hidrogeológicos (doc 1494; 1524 = duplicata) pp. 31-33 (método, CN, Quadro 3.4) e p. 64 (planilha BHD1 TR 50); Vol. 1 Tomo II Memorial descritivo (doc 1492) pp. 155-157
disciplinas: [hidrologia-de-projeto-para-drenagem]
nivel: basico
tipo: positivo
qualidade: A (cadeia reproduzida por cálculo independente em 6 elos; fra e Ppontual dependem de fórmulas ilegíveis)
marcas: `·` = lido por `ler` (doc 1494 híbrido; p. 64 é planilha em texto nativo). CN do Quadro 3.2 consta em `parametros` com `✓` (1494:31, sub-bacia 1: 75,2). Demais valores sem linha em `parametros`. Nenhum `✓h`.

## Problema
Vazão de pico de uma bacia de 36 km² do sertão alagoano por HUT-SCS com chuva de projeto TR 50 anos, e o que fixa o Tc adotado.

## Dados de entrada (1494:64, aba "BACIA BHD1, PERÍODO DE RECORRÊNCIA IGUAL A 50 ANOS")
| grandeza | valor | unidade | marca |
|---|---|---|---|
| Comprimento do rio principal L | 13,21 | km | · |
| Área A | 36,34 | km² | · |
| Desnível | 32,00 | m | · |
| CN (sub-bacia 1: planossolo B-C) | 75,20 | — | ✓ (1494:31) |
| Pmax diária (TR 50) | 132 | mm | · |
| Ppontual para duração tc | 118,23 | mm | · |
| fra | 0,95 | — | · |
| Pbacia(tc) | 112,40 | mm | · |
| S | 83,77 | mm | · |
| tc Bransby-Williams / "Kirpich" (rótulo do documento) | 7,53 / 7,65 | h | · |
| tc adotado | 7,53 | h | · |
| dt (intervalo, 8 intervalos) | 0,941 | h | · |
| ta / tb | 4,990 / 13,32 | h | · |
| Qp unitário | 15,149 | m³/s por mm | · |
| Pico do hidrograma total | 58,71 (t = 10,36 h) | m³/s | · |

## Método do projetista (1494:31-33; 1492:155-157)
- Tc: "por rotina de trabalho" duas fórmulas; adotado Bransby-Williams `tc = 0,615·L/(A^0,1·J^0,2)` (h; L km, A km², J em %), o outro só como referência (1494:31).
- Chuva pontual para a duração tc a partir das máximas diárias, por equações de intensidade média em função da duração (Quadro 3.42 do Vol. 1 e item 2.2.3 do Vol. 3, não lidos); redução pela área por `fra` (fórmula ilegível no texto, 1494:32).
- Hietograma: tc dividido em 8 intervalos; distribuição temporal SCS por polinômio cúbico por faixa de precipitação (0-50, 50-75, 75-100, 100-125 mm e > 125 mm; coeficientes no Quadro 3.3, 1494:32).
- Perdas: SCS-CN, Pe = (P − 0,2S)²/(P + 0,8S); S = 25400/CN − 254.
- HUT: tp = 0,6·tc; ta = D/2 + tp; tb = 2,67·ta; Qp = 2,08·A/ta (1494:32-33).
- Convolução dos hidrogramas parciais (colunas Q0 a Q8 e Qtotal, 1494:64).
- Critério: tc adotado deve dar velocidade de translação "mais próxima da esperada, entre 0,5 e 2,00 m/s" (1492:155).

## Resultado
Q50 = 58,71 m³/s para BH 1 no Quadro 3.4 (1494:33), igual ao pico da planilha 1494:64. Quadro 3.4, BH 1: 22,45 (TR 5); 32,28 (10); 43,11 (20); 58,71 (50); 82,85 (100) m³/s.

## Gabarito candidato (pendente de ✓h)
BHD1 TR 50: A 36,34 km², L 13,21 km, desnível 32 m, CN 75,2, tc 7,53 h, Pbacia 112,40 mm → Qpico 58,71 m³/s (1494:33 e 64).

## Rastro (B = conferência minha)
- A: todos os números da tabela.
- B: S = 25400/75,2 − 254 = 83,77 (confere). J = 32/13210 = 0,2422 % → B-W = 0,615·13,21/(36,34^0,1·0,2422^0,2) = 7,532 h (confere 7,53). tp = 0,6·7,53 = 4,518 h; ta = 0,941/2 + 4,518 = 4,989 (confere 4,990); tb = 2,67·4,99 = 13,32 (confere); Qp = 2,08·36,34/4,99 = 15,15 (confere). Pe total = (112,40 − 0,2·83,77)²/(112,40 + 0,8·83,77) = 50,99 mm, igual ao último acumulado de chuva efetiva da planilha (50,99). Pbacia/Ppontual = 0,951 (fra impresso 0,95).
- C: forma exata de `fra` e da equação de duração (Ppontual) não recuperáveis do texto.

## Divergências (rótulos de Tc e velocidade têm caso próprio: delmiro_gouveia_tc_rotulos_velocidade_declividade)
1. 1494:31 rotula "Kirpich" a fórmula que o Memorial (1492:155) chama de NERC; a planilha 1494:64 reproduz com NERC, não com Kirpich.
2. A coluna "vel (m/s)" da planilha está em km/h nas linhas dos métodos.
3. Qp aparece como "m³/s" em 1494:33 e "m³/s/mm" em 1492:157; o correto é por mm.
4. O Memorial (1492:157) usa TR 5 e 20 para as obras de estrada (Quadro 3.55); o Vol. 3 calcula TR 5 a 100. TR 5/20 para bueiros de estrada de serviço difere dos TR 25/50/100 de Baixio, Xingó e CAC.
5. A constante 0,615 de B-W reproduz o valor impresso, mas não foi conferida contra o primário.

## Fronteira (delegar)
Chuva diária e equações de duração: clima. Obras e bueiros: bueiros-e-travessias.

## Teste sugerido (evals)
Entrada A 36,34 km², L 13,21 km, ΔH 32 m, CN 75,2, Pbacia 112,4 mm, tc B-W: a calculadora deve dar tc = 7,53 h, S = 83,77 mm, Pe = 50,99 mm, Qp unitário 15,15 m³/s/mm; pico por convolução 58,71 m³/s (tolerância 5 % por causa do hietograma polinomial).
