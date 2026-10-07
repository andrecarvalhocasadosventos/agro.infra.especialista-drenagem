# Baixio de Irecê — Dimensionamento de bueiros sob canais e estradas (docs 896, 897)
fonte: Bueiros_Dimensões-REV 2.xls (doc 896):1-2; Dimensoes bueiros.xls (doc 897):1 (abas "Sob canais" e "Sob estradas"); Projeto Básico - Relatorio Irece-Final-Jul08.pdf (doc 670):113-126 (memorial de critérios)
disciplinas: [bueiros-e-drenagem-superficial, hidrologia-de-projeto-para-drenagem]
nivel: basico (Projeto Básico, Vol. 5, Memórias de cálculo – Drenagem)

## Problema
Dimensionar 21 bueiros sob canais (BU-CP0-11…28, BU-CS1-01…03, BU-CS2-01) e 18 sob estradas (BUE-01…18), com Q de TR 25 e TR 50 dos drenos.

## Dados de entrada
| grandeza | valor | unidade | fonte doc:pág | ancoragem |
|---|---|---|---|---|
| Vazão TR 5 / 25 / 50 (ex. BU-CP0-15) | 17,68 / 44,58 / 61,98 | m³/s | 896:1 | ✓ (planilha nativa) |
| Rugosidade n (concreto) | 0,015 | — | 896:1 | ✓ |
| Coef. de orifício C | 0,62 | — | 896:1 ("Verificação como orifício") | ✓ |
| Relação H/D de projeto | (D − 0,10 m)/D (0,9167 p/ 1,2; 0,96 p/ 2,5; 0,9667 p/ 3,0) | — | 896:1 (derivado) | ✓ |
| Declividade adotada | 0,005 (até 0,0068) | m/m | 896:1, 897:1 | ✓ |
| Folga mínima | NB − 1,0 m (nível de berma menos 1,0 m) | m | 896:1 | ✓ |

## Método
1) Capacidade como canal (escoamento livre) com Manning n=0,015, i adotada, lâmina y=D−0,10 m; compara Q total (n células × Q unit) com Q TR 25; mostra Froude e energia/D (896:1).
2) Verificação como orifício / carga a montante: H = (Q50/(n·C·A))²/(2g) acima do eixo do bueiro, C=0,62; cota d'água a montante = cota do bueiro a montante + D/2 + H. Compara com cota do terreno ("Folga em relação ao TN ou estrada") e com cota da berma − 1,0 m. "Redimensionar!" quando a folga < 0. Sem nomograma/HY-8; sem controle de entrada/saída formal.
3) Tipos: BSCC/BDCC/BTCC/BQCC = bueiro celular simples/duplo/triplo/quádruplo; BSTC/BTTC = tubular simples/triplo.
4) Critérios declarados no Relatório do Projeto Básico (Projeto Básico - Relatorio Irece-Final-Jul08.pdf, doc 670): TR 25 anos para bueiros, TR 50 para verificação como orifício, TR 5 para drenos agrícolas e de proteção de canais (670:119); bueiros sob estrada: Q de TR 25, declividade ≤ crítica, n = 0,015, d/D ≤ 0,80 em tubulares e H = d/0,80 em celulares (folga mínima 0,25 d), V máx. 4,0 m/s (670:123); tubular: KQ = Q·n/(D^(8/3)·I^(1/2)), D teórico, Ic = 36,67·n²/D^(1/3), preferência por tubular se triplo com DN < 1200 mm; celular: KQ = Q·n/I^(1/2), Hc = (2/3)H, Vc = 2,56·√H (670:123-124). Bueiros sob canal: mesmos procedimentos + verificação TR 50 em seção plena, carga h = D (tubular) ou H (celular), Q = c·A·√(2gh), entrada afogada sem atingir a berma do canal nem o subleito da estrada (670:126). Quadro 7.6 (670:125) é a mesma tabela de 897 (sob estradas).
5) Quedas hidráulicas nos drenos (0,4 a 1,0 m de altura): bacia de dissipação Lc = 5·(Hd·D)^x e Hb = (1/4)·(Hd·D)^y, Hd = altura da queda, D = altura crítica — os expoentes x, y não são legíveis no texto extraído (670:122); conferir a página antes de usar.

## Resultado (amostra, doc 897:1)
| obra | Q25 | Q50 | tipo/DN | i | V (m/s) | folga TN (m) | situação |
|---|---|---|---|---|---|---|---|
| BU-CP0-13 | 23,55 | 33,37 | BDCC 2,0x2,0 | 0,005 | 3,556 | −0,15 | OK! (897; linha não vista em 896) |
| BU-CP0-15 | 44,58 | 61,98 | BDCC 2,5x2,5 | 0,005 | 4,136 | 0,66 | OK |
| BU-CP0-18 | 137,86 | 185,36 | BQCC 3,0x3,0 (4 cel.) | 0,005 | 4,678 | 1,28 | OK |
| BU-CP0-27 | 7,15 | 9,34 | BSCC 1,5x1,5 | 0,0068 | 3,409 | 1,17 | OK |
| BU-CS1-01 | 51,99 | 73,13 | BTCC 2,2x2,2 | 0,005 | 3,793 | −0,96 | 896: Redimensionar!; 897: OK! |
| BUE-05 (estrada) | 106,06 | 144,50 | BTCC 3,0x3,0 | 0,005 | 4,678 | −1,30 | — |
Dimensões completas: 21 + 18 linhas em 897:1.

## Gabarito para calculadora
- bueiro.py: celular 2,5x2,5 m, 2 células, n=0,015, i=0,005, y=2,4 m -> V=4,136 m/s, Q/célula=24,82, Q total=49,64 m³/s (doc 896:1) — reproduzi: V=4,1363, Q=49,636 (tol. 0,5 %).
- Orifício: Q50=61,98 m³/s, 2 células, C=0,62, A=6,25 m² por célula -> H=3,260 m sobre o eixo; cota d'água mont. = 403,335+1,25+3,260 = 407,846 m (doc 407,8455); folga ao TN (408,31) = 0,66 m. (reproduzi, tol. 0,01 m)
- BDCC 2,0x2,0: y=1,9 -> V=3,556; Q=27,03 m³/s (doc: 27,026).

## Observações
- Capacidade livre usa TR 25; TR 50 só verifica nível a montante em orifício. Em vários bueiros Q50 > capacidade livre (ex. BU-CP0-13: 33,4 > 27,0) e o projetista aceita.
- Inconsistência: no 896 (REV 2) BU-CP0-16, -26, -28, CS1-01, CS1-03 (e BUE-02, BUE-04) aparecem 'Redimensionar!' por folga negativa ao terreno; no 897 (versão final) todos aparecem 'OK!' mesmo com folga negativa (ex. CS1-01: −0,96 m). Presumir que o 897 é pós-ajuste de cota do terreno/aterro; cota de terreno da folga não é refeita. Não usar a coluna 'Situação' do 897 como gabarito.
- Ancoragem das células de .xls: marca '✓' do extrator (valor lido da planilha), sem OCR.
