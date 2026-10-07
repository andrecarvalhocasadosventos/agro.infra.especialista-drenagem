# Sistema Adutor Salitre RC-500 a RC-800 — Bueiros celulares de travessia (Tabela 10.9) (doc 1357)
fonte: Anteprojeto Sistema Adutor Salitre ... RC 500 - RC 800.pdf (doc 1357):100-103, 197-198
disciplinas: [bueiros-e-drenagem-superficial, hidrologia-de-projeto-para-drenagem]
nivel: anteprojeto

## Problema
Passar drenagem pluvial sob o canal principal por bueiros celulares moldados in loco (mesmo critério do CSB/GEOHIDRO), TR 100 anos, Racional/HUT.

## Dados de entrada
| grandeza | valor | un. | fonte | anc. |
|---|---|---|---|---|
| TR | 100 | anos | 1357:4/98 (Tab. de vazões TR 100 por Racional e HUT) | texto |
| Manning concreto | 0,015 | — | mesmo critério de 1341:73; confirmado pelo cálculo abaixo | derivado |
| BTCC 1: Q=24,16 m³/s, 3 cel. 1,50x1,50, i mont 0,0051, i jus 0,0101, L=52,5 m | | | 1357:197 | texto |
| Rebaixo da bacia de entrada 0,70 m; bacia 10x20 m; queda 1,17 m | | | 1357:101 | texto |

## Método
Bueiro tratado como canal aberto em Manning (igual a 1341:73), sem controle de entrada/saída; Yo tirante por câmara e V por câmara na tabela.

## Resultado (1357:197)
| bueiro | Q (m³/s) | câmaras | seção (m) | i jus | Yo (m) | Q/câm. | V (m/s) |
|---|---|---|---|---|---|---|---|
| BTCC 1 | 24,16 | 3 | 1,50x1,50 | 0,0101 | 1,3 | 8,1 | 4,1 |
| BTCC 2 | 34,47 | 3 | 2,00x2,00 | 0,0076 | 1,4 | 11,5 | 4,1 |
| BTCC 7 | 60,45 | 3 | 2,00x2,00 | 0,0107 | 1,9 | 20,2 | 5,2 |
| BDCC 5 | 16,76 | 2 | 1,50x1,50 | 0,0120 | 1,3 | 8,4 | 4,4 |

## Gabarito para calculadora
bueiro.py (Manning): b=1,5 m, y=1,3 m, n=0,015, i=0,0101 -> V=4,08 m/s (doc 4,1), Q/câmara=7,96 (doc 8,1 = 24,16/3). Tol. 3 %.

## Observações
- Aqui V e Yo reproduzem o Manning, ao contrário do caso CSB (Tab 4.7). Conferir que i usado é a de jusante.
- Colunas do extrator sem marca na tabela; usar com a página 197 aberta.
