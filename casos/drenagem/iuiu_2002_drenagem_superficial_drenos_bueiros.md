# Vale do Iuiu 2002 — Rede de drenagem superficial: vazões (Racional/McMath/CN), drenos, bueiros e quedas com bacia (doc 1051)
fonte: Volume 1 - Relatório do projeto.pdf (doc 1051, CODEVASF/Ecoplan 2002):312-322, 329-334
disciplinas: [hidrologia-de-projeto-para-drenagem, bueiros-e-drenagem-superficial, vertedouros-e-dissipadores]
nivel: basico

## Problema
Rede de drenagem da 1ª etapa (752 lotes): 112,58 km de drenos (principais 9,09; secundários 62,64; terciários 36,03; quaternários 4,82 km) + 35,565 km de valetas de proteção, 68 bueiros tubulares, 7 celulares, 30 passagens molhadas, 159 quedas com bacia de amortecimento, 11 descidas d'água (1051:313).

## Dados de entrada
| grandeza | valor | unidade | fonte doc:pág | ancoragem |
|---|---|---|---|---|
| TR drenos e demais dispositivos | 10 | anos | 1051:316 | texto |
| TR bueiros sob canal / sob estrada | 50 / 25 | anos | 1051:316, 331-332 | texto |
| P 1 dia (Gumbel) 5/10/25/50/100 anos | 94,00 / 108,49 / 126,81 / 140,40 / 153,89 | mm | 1051:320 | texto |
| Equação de P1dia | P = 65,02 − (1/0,051763)·ln[ln(TR/(TR−1))] | mm | 1051:318 (fórmula lida do PDF, garbled) | texto |
| CN | 78 (solo B, culturas em fileiras, boa) | — | 1051:316 | texto |
| Tc (Kirpich) | Tc = 0,0195·K^0,77 ; K = (L³/H)^0,5 | min | 1051:316-317 | texto |
| Racional | C = 0,3 ; I = 2,31·p·Tc^-0,55 (p = P1dia(TR)) ; Q = C·I·A/360 | — | 1051:318 | texto |
| McMath | Q = 0,0091·C·i·A^0,8·S^0,2 (A ha; S m/m; i = P/Tc) | — | 1051:317-318 | texto |
| Método CN | S=(2540/CN−25,4)·10 ; E=(P−0,2S)²/(P+0,8S) ; C=4,573+0,162·(E·24)/Td ; Q=C·A^(5/6)·10^-3 | — | 1051:317 | texto |
| Critério por área | A ≤ 50 ha Racional; 50–400 ha média McMath e CN (ignorando valores < Racional); > 400 ha CN | — | 1051:316 | texto |
| Manning drenos de terra / bueiros | n = 0,03 / 0,0165 | — | 1051:321, 331 | texto |
| Velocidade máxima nos drenos | 0,80 (até 1,00 m/s em trechos) | m/s | 1051:321, 334 | texto |
| Declividade mínima do bueiro | "5 %" (suspeito, ver Observações) | — | 1051:331 | texto |
| Ø mínimo de bueiro tubular | 0,80 | m | 1051:330 | texto |

## Método
- Drenos: seção trapezoidal sem revestimento, Manning, programa "Qdre" (Newton-Raphson), greide descendente, trechos curtos, v ≤ 0,80 m/s (1051:319-321).
- Bueiros: Manning + continuidade D = √(4Q/(π·Vmax)); sem controle de entrada/saída, sem HY-8/nomograma, sem HW/D. Sob canal (7): 2 BDTC 0,80 m, 2 BTTC 1,20 m, 4 BTCC 2,00x1,50 m (limite de altura 1,50 m), TR 50. Sob estrada (68): tubulares 0,8/1,0/1,2 m e celulares 1,5x1,5 (2), 2,0x1,5 (1), 2,0x2,0 (1), TR 25 (1051:330-332). Rampa de entrada 1V:2H em pedra argamassada (1051:331).
- Queda com bacia de amortecimento (dissipador): degrau inclinado em pedra argamassada e=0,20 m, 1V:2H se queda ≤ 2,0 m, 1V:3H se > 2,0 m; bacia com blocos dissipadores de h=0,20 m, l=0,25 m, afastamento 1,00 m; comprimento da bacia = comprimento do ressalto L = 6·(D2 − Dq) (Smetana), mín. 2,00 m, D2 = lâmina a jusante, Dq = lâmina no degrau; enrocamento 2,00 m x 0,30 m a jusante (1051:333-334).
- Descida d'água (sem blocos): desnível < 0,70 m, rampa 1V:2H, bacia de 1,00 m, enrocamento de 1,00 m; elevar v de 0,80 para 1,00 m/s reduziu as descidas de 95 para 11 (1051:334).

## Resultado
| dreno / trecho | A (ha) | L (km) | i adotada | Q McMath | Q CN | Q adotada (m³/s) | fonte |
|---|---|---|---|---|---|---|---|
| DP08 t1 | 20 | 0,61 | 0,0065 | — | — | 0,83 (Racional) | 1051:322 |
| DP10 t1 | 25 | 0,70 | 0,0057 | — | — | 0,95 | 1051:322 |
| DP11 t1 | 189 | 4,67 | 0,0028 | 2,34 | 3,87 | 3,1 (média) | 1051:322 |
| DP11 t3 | 163 | 3,71 | 0,0011 | 1,5 | 3,16 | 2,33 | 1051:322 |
| DP12 t3 | 36 | 0,80 | 0,0063 | — | — | 1,32 | 1051:322 |

## Gabarito para calculadora
- racional.py: A=20 ha, L=0,61 km, declividade da bacia ≈ 0,0065 (H = 0,0065·610 = 3,97 m — suposição minha), TR=10, C=0,3 -> P=108,49 mm; Tc=18,9 min; I=49,8 mm/h; Q=0,83 m³/s (doc 0,83). Reproduzido por mim com I em mm/h (o texto de 1051:318 diz mm/min, erro de unidade). Tol. 3 %.
- Chuva: P(TR=25)=126,81 mm e P(50)=140,40 mm pela fórmula (conferem com 1051:320).
- 50 < A ≤ 400 ha: Q_adotada = (Q_McMath + Q_CN)/2 (DP11 t1: (2,34+3,87)/2 = 3,105 ≈ 3,1). A ordem das colunas (Racional | McMath | CN | adotada) é inferida; conferir 1051:322.
- Queda: L_bacia = 6·(D2−Dq), mín. 2,00 m.

## Observações
- "Declividade mínima 5 %" do bueiro (1051:331) é provavelmente 0,5 %; conferir antes de usar.
- A equação de chuva IDF (pág. 319) está em imagem; só a tabela P1dia–P1h foi lida.
- Quadro 8.34 sem rótulos de colunas no texto extraído.
