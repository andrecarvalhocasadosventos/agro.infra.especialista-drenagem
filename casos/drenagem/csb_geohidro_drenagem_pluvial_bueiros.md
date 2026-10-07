# Canal do Sertão Baiano (CSB) — Drenagem pluvial: hidrologia de projeto e bueiros/OAC sob o canal (doc 1341)
fonte: Memoriais descritivo e de cálculo - Sistema de drenagem.pdf (doc 1341; 1372 é cópia idêntica, mesmo tamanho/páginas, usar 1341):45-47, 70-73, 33-36, 145, 205
disciplinas: [hidrologia-de-projeto-para-drenagem, bueiros-e-drenagem-superficial]
nivel: anteprojeto
(páginas = página do PDF/catálogo; o número impresso no rodapé é página-1)

## Problema
Anteprojeto GEOHIDRO 2016 do sistema adutor CSB (297 km): proteger o canal com valetas/canais de desvio e passar as bacias de contribuição por bueiros celulares sob o canal e overchutes. Trechos 1 a 5: 96+90+77 = 263 bacias; 45+50+41 = 136 bueiros de travessia e 27+11+12 = 50 overchutes (doc 1341:72).

## Dados de entrada
| grandeza | valor | unidade | fonte doc:pág | ancoragem |
|---|---|---|---|---|
| TR travessias (bueiros, overchutes) | 100 | anos | 1341:45 (texto); 1341:70 repete 100 a "todo o sistema" | ✓ |
| TR valetas e canais de desvio | 50 | anos | 1341:45 (diverge de 1341:70, que diz 100 para tudo) | ✓ |
| Limite Racional | A ≤ 350 | ha | 1341:46 | ✓ |
| Limite HUT 1 ordenada | 350 < A ≤ 2000 | ha | 1341:46 | ✓ |
| HUT 11 ordenadas | A > 2000 | ha | 1341:46 | ✓ |
| Tc (bacias grandes) | Kirpich modificada: Tc = 1,42 (L³/H)^0,385, Tc em h, L km, H m (manual DNIT) | — | 1341:46 | texto |
| Tc (valetas, pequenas bacias) | tabela de Ramser (ex.: 1 ha=2,7 min; 100 ha=26 min; 400 ha=74 min) | min | 1341:73 | texto |
| C10 (rural) | 0,05–0,30 (agrícola); adotado 0,20 nas bacias da Tab 4.1 | — | 1341:47, 145 | ✓ |
| C para TR | C_T = 0,8·T^0,1·C10 (TR 100 → 0,25) | — | 1341:47, 145 | ✓ |
| Cd | Cd = A^-0,10 (A km², bacias > 100 ha) | — | 1341:47 | texto |
| C valetas | 0,10 | — | 1341:74 | ✓ |
| IDF (Plúvio 2.1) I = K·TR^a/(t+b)^c, grupo 1 (Juazeiro…Filadélfia): K=5590,88 a=0,241 b=40,11 c=1,091; grupo 2: 6492,73/0,237/45,02/1,083; grupo 3: 8701,04/0,243/55,26/1,111 | | mm/h, t em min | 1341:36 | texto |
| Manning grama / alv. pedra / concreto armado | 0,024 / 0,020 / 0,015 | — | 1341:73 | ✓ |
| Bacia 45 (exemplo) A=211 ha, L=2,9 km, Hmax=471 m, Hmin=459 m | | | 1341:145 | ✓ |
| Bacia 45: Tc 114,09 min; i(TR100)=69,54 mm/h; C=0,25; Cd=0,93 | | | 1341:145 | texto (tabela) |

## Método
- Vazão: Racional Q = C·Cd·i·A/360 (A ha) até 350 ha; HUT-SCS (CN, S) acima (1341:46-47, 82, 99). Atenção: nas linhas da Tab 4.1 com A > 350 ha o único valor vem na coluna HUT 01 ou HUT 11, mas o extrator de parâmetros rotulou como "Método Racional" (ex.: bacia 49, 2889 ha, 110,35 m³/s é HUT 11). Usar a coluna do PDF.
- Bueiro: "calculado como canal aberto, Manning, n = 0,015" (1341:73); sem nomograma/HY-8, sem HW/D e sem controle de entrada/saída declarados. Seções celulares de concreto moldado in loco, padrão DNIT; bueiros de estrada: tubulares CA-3 (1341:71).
- Bacia de entrada padronizada: base 10 m, extensão 10 ou 20 m, rebaixo de 0,70 m abaixo da cota de montante do bueiro, enrocada; quedas em gabião com degrau 1,17 m (1341:71). Dissipação por ressalto na bacia de entrada (sem Froude/USBR explícito).
- Valetas: trapezoidal 1V:1,5H, grama; v > 2,00 m/s -> alvenaria de pedra; enrocamento 10 m no início do canal de descarga (1341:71, 73).

## Resultado
| item | valor | fonte |
|---|---|---|
| Bacia 45 Q100 racional | 9,58 m³/s | 1341:145 |
| Bacia 46 (133 ha) / 47 (111 ha) / 48 (30 ha) | 9,19 / 10,12 / 3,00 m³/s | 1341:145 |
| Bacia 49 (2889 ha, HUT 11) | 110,35 m³/s | 1341:145 / 205 |
| Bueiro BTCC-Nº17: Q=39,18; 3 cel. 2,00x2,00; i=0,0045; L=40 m; CFM 453,728 CFE 453,638 CFJ 453,548 | | 1341:205 |
| BDCC-Nº19 (Q=14,25; 2 cel. 1,50x1,50; i=0,0085; L=43 m) | | 1341:205 |
| BTCC-Nº25 (Q=110,35; 3 cel. 3,00x3,00; i=0,0040; L=54,5 m) | | 1341:205 |
| 2 BTCC-Nº23 (Q=190,45; 3,00x3,00; i=0,0019; L=56 m) | | 1341:205 |
| BSCC-Nº30 (Q=1,93; 1 cel. 1,50x1,50; i=0,015; L=58,5 m) | | 1341:205 |

## Gabarito para calculadora
- racional.py: A=211 ha, L=2,9 km, H=12 m, grupo 1, TR=100, C10=0,20, Cd=A_km2^-0,1 -> Tc ≈ 112 min (doc 114,09), i ≈ 69,5 mm/h (doc 69,54), C=0,2536, Cd=0,928, Q ≈ 9,59 m³/s (doc 9,58). Tolerância ±3 %. (reproduzido por mim com os parâmetros do doc)
- bueiro.py (Manning, canal aberto): BTCC 1,50x1,50 não consta aqui; para Salitre ver caso próprio. Para bueiro 31: ver Observações (não reproduz).

## Observações
- Divergências: TR 100 vs 50 para valetas (1341:45 x 1341:70); V obra 4,4 m/s do BTCC-Nº17 não reproduz com Manning n=0,015 e y=1,5 m (dá 3,18 m/s e 28,6 m³/s para 3 células, abaixo dos 39,2 m³/s). 4,4 ≈ Q/A_total (39,2/9). A coluna V/Yo da Tab 4.7 pode estar lida errada pelo texto (ex. "1,8" onde se esperaria 5,8) -> não usar V/Yo como gabarito sem conferir a página. Sugestão: `python 89_app_revisao.py` nas linhas parametro da pág. 205 antes de uso.
- Q 1341:205 vem de Tab 4.1 (pág. 145 e seguintes), consistente.
- Quadros 3.13/3.14 de C e CN estão em anexo (pp. 82-139, hidrogramas); só a bacia 5 foi vista (CN 66, S 131 mm, A 386,5 km², Tc 632,5 min, 1341:82).
