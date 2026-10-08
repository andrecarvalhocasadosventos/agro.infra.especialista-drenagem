# Delmiro Gouveia (AL) — Bueiros tubulares de drenagem transversal sob o Canal Principal (BUC-2 a BUC-5): Racional TR 20, verificação TR 50, Manning parcialmente cheio
tipo: positivo (com divergências documentais listadas; nenhum número promovido a gabarito sem `✓h`)
qualidade: B (colunas da planilha mapeadas por derivação geométrica; capacidade reproduzível por Manning, sem HW nem controle de entrada)
fontes: CODEVASF 2016, Projeto Básico (Hydros), Delmiro Gouveia
- doc 1493, Vol. 2 Tomo I, MC hidráulico, mecânico e civil, pp. 282-285 (Anexo 7.6, "Drenagem transversal ao canal")
- doc 1492, Vol. 1 Tomo II, Memorial descritivo, pp. 163-165 (Quadros 3.60 e 3.61)
- doc 1515, Vol. 5 Tomo II, Memória dos quantitativos, pp. 98-101 (bueiros do canal)
- duplicatas no acervo (não usar como fonte extra): 1520 = 1492 (pág. +2), 1521 = 1493 (pág. +1), 1538 = 1515
disciplinas: [bueiros-e-travessias, hidrologia-de-projeto-para-drenagem]
nivel: projeto básico
legenda de marcas: `✓` ancorado na camada de texto; `✓*` magnitude não provada (separador); `·` sem testemunha (valor lido com `consultar.py ler`, sem linha extraída); `!`/`~` nenhum usado neste caso; `✓h` nenhum. "texto" = lido na página com `ler`, sem linha extraída.

## Pergunta de engenharia
Como o projetista passou a vazão de 4 sub-bacias de 6,7 a 73,6 ha pelo canal principal (berma esquerda, 1.697 m, trapezoidal) com bueiros tubulares de concreto, e com que critério verificou a vazão de TR 50?

## Dados de entrada
| grandeza | valor | un. | fonte doc:pág | marca |
|---|---|---|---|---|
| TR de dimensionamento / verificação | 20 / 50 | anos | 1493:282-285; 1492:164 | ✓ |
| IDF TR 20: I = a/(Tc+b)^c | a = 1123,7; b = 9,79; c = 0,72 | mm/h, min | 1493:282-283 | ✓ |
| IDF TR 50 | a = 1335,1; b = 9,79; c = 0,72 | idem | 1493:284-285 | ✓ |
| C (deflúvio), único para as 5 sub-bacias | 0,22 | adim. | 1493:283 | ✓ |
| Método de vazão | Racional (Q = C·i·A/360, A em ha) | — | 1493:282 ("método Racional já calculada") | texto |
| Áreas SB-1 / SB-2 / SB-3 / SB-4 / SB-5 | 51,750 / 6,680 / 73,590 / 8,880 / 11,820 | ha | 1493:283 | ✓* (SB-1, 2, 3, 4, 5: "51,750" lido como 51,75 ha; a leitura é coerente com Q) |
| Tc SB-1..SB-5 | 22,40 / 11,65 / 31,26 / 17,46 / 15,78 | min | 1493:283 | ✓ |
| Comprimento do talvegue (SB-1..5) | 750 / 300 / 1.025 / 422 / 397,25 | m | 1493:283 | ✓ |
| Cota mont. / jus. do talvegue (SB-1..5) | 306/276; 286/277; 306/275; 285/277; 285/277 | m | 1493:283 | ✓ |
| Q TR 20 (SB-1..5) | 2,878 / 0,499 / 3,432 / 0,557 / 0,777 | m³/s | 1493:283 | ✓* (SB-1, SB-3), ✓ demais |
| Q TR 50 (SB-1..5) | 3,420 / 0,593 / 4,078 / 0,662 / 0,923 | m³/s | 1493:285; 1492:164 (Quadro 3.60) | ✓* (SB-3 em 1493:284), ✓ demais |
| Manning (concreto) | 0,015 | adim. | 1493:282; 1492:164 | ✓ |
| Critério de tirante | y ≤ 75 % do diâmetro | — | 1492:164 | texto |
| Declividade do bueiro (MC) SB-2 / 3 / 4 / 5 | 0,005 / 0,005 / 0,005 / 0,007 | m/m | 1493:282, 284 | ✓ |
| Bueiros adotados (Quadro 3.61) | BUC-2 Ø0,80 ×1; BUC-3 Ø1,20 ×2; BUC-4 Ø0,80 ×1; BUC-5 Ø0,80 ×1 | m | 1492:164 | ✓ |
| BUC-1 (SB-1, Q 2,878 / 3,420) | eliminado (acesso passou a vir da estrada vicinal) | — | 1492:164 | texto |

## Método do projetista
1. Racional por sub-bacia, com i da IDF "I = a/(Tc+b)^c" (a, b, c por TR); Tc em min (método de cálculo do Tc não informado); C = 0,22 (justificativa não informada).
2. Dimensionamento a TR 20 e verificação a TR 50 por Manning em seção circular parcialmente cheia (tubo como canal; cada linha leva Q/nº de linhas), escolhendo o tipo com maior tirante limitado a 75 % de D (1492:164).
3. Sem controle de entrada, sem HW/D, sem cota de inundação a montante, sem velocidade de saída crítica ou dissipador (o memorial diz só que a declividade do terreno natural supera a crítica e que a declividade de projeto "aproxima-se da crítica", com fundação da ala de montante abaixo do TN, 1492:164).

## Resultado (ordem das colunas mapeada por mim; ver Rastro)
Dimensionamento TR 20 (1493:282), por linha:
| bueiro (sub-bacia) | linhas | Q/linha (m³/s) | S (m/m) | D (m) | y (m) | A mol. (m²) | V (m/s) | y/D | Fr |
|---|---|---|---|---|---|---|---|---|---|
| BUC-2 (SB-2) | 1 | 0,499 | 0,005 | 0,80 | 0,454 | 0,294 | 1,70 | 57 % | 0,89 |
| BUC-3 (SB-3) | 2 | 1,716 | 0,005 | 1,20 | 0,753 | 0,747 | 2,30 | 63 % | 0,91 |
| BUC-4 (SB-4) | 1 | 0,557 | 0,005 | 0,80 | 0,487 | 0,321 | 1,74 | 61 % | 0,87 |
| BUC-5 (SB-5) | 1 | 0,777 | 0,007 | 0,80 | 0,546 | 0,366 | 2,12 | 68 % | 0,97 |
Verificação TR 50 (1493:284): BUC-2 y = 0,508 m (63 %), V = 1,76 m/s, Fr 0,85; BUC-3 y = 0,853 (71 %), V = 2,37, Fr 0,85, Q/linha 2,039; BUC-4 y = 0,550 (69 %), V = 1,80, Fr 0,81; BUC-5 y = 0,630 (79 %), V = 2,17, Fr 0,86.
Quantitativo (1515:99-101): 3 BSTC Ø800 + 1 BDTC Ø1200, extensão média 19,33 m (tubulares).

## Gabarito para a calculadora (propostas; promover só com `✓h`)
- Racional por sub-bacia: Q = 0,22·i·A/360 com i tabelado reproduz Q em todas as 5 linhas e nos 2 TR (SB-1: i = 91,01 mm/h, A = 51,75 ha, Q = 2,878). Tolerância 1 %.
- Capacidade parcialmente cheia (Manning, seção circular, θ pela geometria): D = 0,80, n = 0,015, S = 0,005, Q = 0,499 → y = 0,454 m, V = 1,70 m/s, Fr = 0,89 (BUC-2, TR 20). Tolerância 3 %.
- Fr da tabela é com profundidade hidráulica A/B (0,294/0,79), não com y: confere (0,89). Ver lição de Froude em `PENDENCIAS_DE_TREINAMENTO.md` §4.

## Rastro
- A: Q = C·i·A/360 reproduzida com os i da tabela nas 5 sub-bacias, TR 20 e TR 50 (diferença ≤ 0,001 m³/s por arredondamento).
- B: mapeamento das colunas (Yo, θ, largura, área, perímetro, V, R, y/D, hv, E, Fr): confirmado por geometria da seção circular (SB-2: θ = 3,4112 rad dá A = 0,294 m², B = 0,79 m, P = 1,36 m, V = Q/A = 1,70, Fr = 0,89). O cabeçalho do PDF vem em desordem no texto extraído.
- C: origem do C = 0,22 e do método de Tc; função da cota de montante/jusante no Tc (pode ser Kirpich, não informado).

## Divergências
1. Declividade do bueiro: Quadro 3.61 (1492:164) dá BUC-2 = 0,006, BUC-3 = 0,005, BUC-4 = 0,015, BUC-5 = 0,015; o MC (1493:282, 284) usa 0,005, 0,005, 0,005, 0,007. Mesma Q por linha nos dois. Com S = 0,015 o Froude passaria de 1 (regime supercrítico), incompatível com Fr = 0,81 a 0,97 da tabela e com o texto "próxima da crítica" (inferência C). Decidir qual vale exige o desenho 0364-DE-20-DR-001 (não lido).
2. Comprimento do bueiro: 40 / 50 / 40 / 40 m no Quadro 3.61 (1492:164) × extensão média de 19,33 m no quantitativo (1515:99). Diferença de 2× em tubo e escavação; coluna "Comprimento" do Quadro 3.60 (50, 40, 50, 40, 40) tem o mesmo número e é de sub-bacia, não de bueiro (rótulo ambíguo).
3. IDF × tabela: com a, b, c e Tc impressos, a fórmula dá i de 1,2 % a 1,8 % acima do i tabelado (ex.: SB-1 TR 20: 92,3 × 91,0 mm/h); a tabela é internamente coerente com Q. Fórmula/Tc ou b arredondados diferentes: não informado.
4. Critério y ≤ 75 % de D é verificado só no dimensionamento (TR 20: máximo 68 %). Na verificação TR 50, BUC-5 chega a 79 %; o texto não diz se o critério vale para a verificação.
5. Memorial × norma: bueiro tratado como canal parcialmente cheio com Fr entre 0,81 e 0,97, perto do crítico; nenhum HDS-5 (controle de entrada), cota de inundação ou Ke. Para tubo de Ø0,80 com 40 m (se o comprimento do Quadro 3.61 valer) o controle de saída/entrada pode governar. Lição de `PENDENCIAS_DE_TREINAMENTO.md` §4 se repete.

## Fronteira
IDF e chuva por TR: Clima. Dissipador na saída (V ≈ 2 m/s, Fr ≈ 0,9): Hidráulica (D3). Aterro, cobrimento mínimo e greide do canal: Terraplenagem.
