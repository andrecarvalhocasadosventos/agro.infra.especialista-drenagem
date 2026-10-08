# Salitre Etapa 2 — macrodrenos trapezoidais (Manning n=0,030, V 0,30–1,2 m/s, degraus e deságues)
fonte: Memorial descritivo (doc 1584):95-108 e Memorial de cálculo hidráulico Tomo 3.1 (doc 1585):97-123 — Projeto Salitre, CODEVASF 2014, executivo (Hydros)
disciplinas: [canais-de-drenagem-e-macrodrenagem, hidraulica-de-canais-de-drenagem]
nivel: projeto executivo
tipo: positivo (os números da planilha reproduzem Manning; as inconsistências do memorial estão no caso `2026-10-08_salitre_etapa2_macrodrenagem_inconsistencias_memorial.md`)
qualidade: A para os trechos conferidos (Manning reproduz a coluna V e Q dreno); critério de velocidade B (memorial e planilha divergem)

## Problema
Dimensionar a rede de macrodrenagem da Etapa 2 (72 km de drenos, secundários a quaternários) que recebe talvegues naturais, águas de chuva e efluentes da irrigação, em seção trapezoidal, mantendo o fluxo natural dos riachos (Mulungú, Recreio, Tourão).

## Dados de entrada (critérios)
| grandeza | valor | un. | fonte | anc. |
|---|---|---|---|---|
| chuva de projeto | crítica de 24 h, TR 10 anos; TR 50 anos só para verificar a cheia | — | 1584:102 | A (texto) |
| fórmula | Manning, movimento uniforme, seção trapezoidal, cálculo iterativo | — | 1584:105 | A |
| n dos drenos | 0,030 | — | 1584:105; 1585:97-123 (rodapé "Rugosidade nos Drenos 0,030") | A |
| talude | 1,0H:1,0V em Vertissolos (maioria); 1,5H:1,0V em Cambissolos, Argissolos e Planossolos | — | 1584:105 | A |
| velocidade | 0,30 a 1,2 (memorial) / 0,3 a 1,5 (rodapé das planilhas) | m/s | 1584:105 / 1585:97-123 | A (divergem) |
| profundidade | 1,80 para drenos no entorno das áreas irrigáveis (para viabilizar a drenagem subterrânea) | m | 1584:105 | A |
| n dos bueiros | 0,015; V máx. no bueiro 3,5 | m/s | 1585:100 (rodapé) | A |
| talvegue/ACP | área, comprimento, cota máx. e mín. por ACP (Quadros 3.48–3.51) | — | 1584:99-100 | A |

## Método do projetista
Planilha por dreno (Memória de Cálculos, Eng. Agr. Jorge Leandro, nov/2010): colunas cota mont/jus, desnível, L, I = desnível/L, Q do trecho, Q DRENO (capacidade Manning da seção), V, b, h, talude 1/z, n, altura, largura, área, perímetro, raio hidráulico (1585:97-123). "Q trecho" é a demanda; "Q DRENO" é a capacidade. A altura da seção é igual a h (a coluna free board não aparece preenchida nas linhas lidas). Seções escolhidas para minimizar escavação em 2ª e 3ª categoria (1584:105). Quedas (degraus) de 1,0 e 1,5 m onde a declividade natural levaria a V erosiva (1584:106).

## Resultado e gabarito (valores lidos; conferência de Manning em B)
Trecho DT 4.1.6/A (1585:105): desnível 1,448 m, L 637 m, I 0,00227, Q trecho 3,015 m³/s, b 2,50 m, h 0,90 m, 1V:1H, n 0,030 -> A 3,060 m², P 5,046 m, R 0,606 m, V 1,139 m/s, Q dreno 3,484 m³/s.
Trecho DT 4.1.6/B (1585:105): desnível 1,012 m, L 1.200 m, I 0,00084, Q trecho 6,239, b 7,80, h 0,90, 1V:1H -> A 7,830, P 10,346, R 0,757, V 0,804, Q dreno 6,295.
Trecho DS 4.1/A (1585:99): L 1.066 m, I 0,00096, Q trecho 113,2, b 56,00, h 1,50, talude 1,5H:1V -> A 87,375 m², R 1,423 m, V 1,307, Q dreno 114,194. Os 5 trechos do DS-4.1 repetem a seção (87,375 m², 3.798 m no total).
Trecho DS-3.2/A (1585:98): I 0,00159, Q 4,060, b 3,60, h 0,90, 1V:1H -> A 4,050, V 1,005, Q dreno 4,071.
Gabarito para a calculadora: Manning trapezoidal com os b, h, z, n, I acima deve devolver V e Q dreno com tolerância 1 % (conferido em B: DT 4.1.6/A V 1,138 e Q 3,48; DT 4.1.6/B V 0,802 e Q 6,28; DS 4.1/A V 1,307 e Q 114,2; a diferença de 0,2 % no trecho B é arredondamento da planilha).
Quadro 3.47 (1584:97): seção mínima e máxima por dreno, p. ex. DS-4.1 87,375 m² (b 56 m, h 1,5 m, z 1,5 -> (56+1,5·1,5)·1,5 = 87,375, B), DT-4.1.1 3,08 m², DS-3.2 4,05 a 14,94 m² (batem com 1585:98, A).

## Estruturas associadas
- Degraus (Quadro 3.57, 1584:108): 9 quedas com Hd = 1,00 ou 1,50 m; Hd = cota montante do degrau menos cota jusante (p. ex. DG-3.2/1: 418,232 − 417,232 = 1,00) e Ht = TN − cota montante (419,213 − 418,232 = 0,98); largura LT = b + 2·Hd com talude 1:1 (13,5 -> 15,5; 9,0 -> 12,0 com Hd 1,5) (B, os 9 degraus conferem).
- Deságues (Quadro 3.56, 1584:108): 9 confluências; Am − Bm = 2·z·Hm (DQ-4.1.4.4: 9,98 − 6,00 = 3,98 = 2·1·1,990, B); os 9 conferem.
- Bueiro celular BC-4.1.1/1 sob o dreno DT-4.1.1 (Quadro 3.55, 1584:107; planilha 1585:100): 3 células 1,0x1,0 m, L 20 m, cotas 412,458/412,358, I 0,005, n 0,015; por célula Q 0,920, h 0,70, V 2,073, Q cap. 1,451 m³/s (total demandado 2,75 m³/s, capacidade 3 x 1,451 = 4,35). Só Manning de canal parcialmente cheio; sem controle de entrada nem verificação de cota a montante (lição já conhecida do acervo, ver PENDENCIAS §4).

## Rastro
A: critérios, colunas da planilha e quadros 3.47, 3.55-3.57. B: reprodução de Manning e das relações geométricas dos degraus e deságues. C: leitura de "altura" = h (a coluna free board está vazia no texto extraído).

## Divergências
Memorial V 0,30–1,2 x planilha V 0,3–1,5; memorial "profundidade 1,80 m" para os drenos do entorno x h de 0,70 a 1,80 m nas planilhas (1,80 só em 10 de 83 trechos). Detalhe no caso das inconsistências.

## Marcas de ancoragem
Valores lidos direto das páginas (texto nativo, sem marca `!`, `~` ou `✓*`). Nenhum `✓h`: gabarito provisório até conferência humana.

## Fronteira
Chuva de 24 h por TR (IDF/desagregação) é do Clima; vazão das ACPs (Racional/McMath/SCS) é de Hidrologia (outro lote); bueiro celular HDS-5 é do lote L3.
