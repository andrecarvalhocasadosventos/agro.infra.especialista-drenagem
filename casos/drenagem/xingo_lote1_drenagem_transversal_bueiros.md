# Canal Xingó Lote I — Hidrologia (Racional/HU) e bueiros celulares por equação da energia com regime supercrítico (docs 1419, 1401)
fonte: v. 5. Memorial de cálculo e dimensionamentos.pdf (doc 1419):26-28, 62, 153-155; v. 3. t. 3. Obras civis.pdf (doc 1401; 1433 é cópia):51
disciplinas: [hidrologia-de-projeto-para-drenagem, bueiros-e-drenagem-superficial, vertedouros-e-dissipadores]
nivel: basico

## Problema
Vazões das bacias dos aquedutos (S1 a S6) e dimensionamento dos bueiros celulares de travessia sob o canal Xingó (BU-01…), com restituição ao talvegue.

## Dados de entrada
| grandeza | valor | unidade | fonte doc:pág | ancoragem |
|---|---|---|---|---|
| TR | 100 | anos | 1419:26 e 1419:154 | texto |
| Critério de método | Racional se A < 2,0 km² ou Tc < 1 h; senão Hidrograma Unitário | — | 1419:26 | texto |
| Bacias dos aquedutos | S1 Tigre A=168,0 km² L=35,67 km CN 76,19; S2 Baboseira 78,8 km² 24,95 km CN 76,13; S3 20,7 km² 13,96 km CN 76,35; S4 30,7 km² 18,33 km CN 79,47; S5 62,1 km² 22,39 km CN 77,36; S6 Xingozinho 1318,2 km² 98,79 km CN 67,45 | — | 1419:28 | texto |
| Tc: média de Corpo de Engenheiros dos EUA, Ven Te Chow e Kirpich (S1: 8,41 / 9,53 / 8,91 -> média 8,95 h; S6 19,08 h) | | h | 1419:28 | texto |
| Distância fundo do canal a geratriz superior do bueiro | ≥ 1,5 | m | 1419:153 | texto |
| Manning bueiro de concreto | 0,015 | — | 1419:154 | texto |
| Coef. perda de carga de entrada | K = 0,5 | — | 1419:154 | texto |
| Manning canal de restituição | 0,030 (enrocamento) / 0,018 (concreto) | — | 1419:154 | texto |
| Dimensões celulares (B x H) | 1,0x1,5; 1,5x1,5; 1,5x2,0; 2,0x1,5; 2,0x2,0; 2,5x2,0; 2,5x2,5; 3,0x2,0; 3,0x2,5; 3,0x3,0 m | m | 1419:153 | texto |

## Método
Equação da energia entre seções (perdas contínuas + expansão/contração, C), com energia na entrada igual à energia crítica e K = 0,5 de entrada; escoamento no bueiro supercrítico (declividade ~0,6 a 1,2 %), exigindo dissipador de energia ao final antes do canal de restituição (1419:154). Não usa nomograma/HY-8; controle é de entrada (regime crítico na entrada) por construção. Tipo de dissipador: "definido no projeto de drenagem em função das descargas e da condição de deságue"; em entradas/saídas de bueiros, caixas de pedra argamassada ou arrumada (1401:51). Sem critério Froude/USBR/SAF/HEC-14 declarado.

## Resultado (1419:154-155; colunas parcialmente inferidas)
| bueiro | km | tipo | dim. (m) | i (%) | Q (m³/s) | V (m/s) | lâmina (m) |
|---|---|---|---|---|---|---|---|
| BU-01 | 3+777,17 | BDCC | 1,50x1,50 | 1,009 | 8,96 | 3,10 | 0,96 |
| BU-06 | 9+158,98 | BDCC | 2,50x2,50 | 1,190 | 39,30 | 4,46 | 1,76 |
| BU-10 | 14+334,66 | BQCC | 2,00x2,00 | 1,070 | 39,60 | 3,34 | 1,48 |
| BU-24 | 24+298,50 | BDCC | 3,00x3,00 | 0,976 | 48,80 | 4,36 | 1,87 |
| BU-04 | 7+875,90 | BSCC | 1,50x1,50 | 0,860 | 3,31 | 2,86 | 0,77 |
Verificação por continuidade: BU-01 4,48 m³/s por célula / (1,50·0,96) = 3,11 m/s ✓; BU-24 24,4/(3,0·1,87) = 4,35 ✓; BU-06 19,65/(2,5·1,76) = 4,47 ✓.

## Gabarito para calculadora
- bueiro.py (Manning supercrítico, n=0,015): BSCC 1,50x1,50, i=1,009 %: para y=0,96 e 2 células, V=3,1 m/s e Q = 8,96 m³/s coerente com continuidade; usar Q e V como saída de verificação (tol. 3 %). A lâmina de 0,96 m só é reproduzida por curva de remanso/energia, não por Manning normal (conferir página).
- Tc: Kirpich para S1 (L=35,67 km, S=0,36 %) deve dar ≈ 8,9 h (doc 8,91 h, tol. 3 %).

## Observações
- Os rótulos das colunas "Hw/D", "H", "Controle" no 1419:154-155 não se alinham com os valores extraídos (há 7 números após o tipo, ex. BU-01: 1,009 | 1,51 | 0,50 | 8,96 | 3,10 | 0,96 | 1,11). Suponho 1,51 = Hw (m), 0,50 = K de entrada, 1,11 = lâmina crítica ou H; NÃO confirmado -> usar só declividade, Q, V e lâmina verificadas por continuidade. Conferir com `89_app_revisao.py` na pág. 154/155.
- Quadro 3.37 (vazões máximas dos bueiros, 1419:63) e quadros de hidrogramas (1419:36-47) não lidos.
- Dissipador: nenhum dimensionamento no texto lido, apenas a exigência. Em 1401:51 só há texto de especificação (concreto armado, NBR 6118/7187, DNIT 117/2009).
