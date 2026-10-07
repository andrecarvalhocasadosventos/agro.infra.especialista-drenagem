# Baixio de Irecê — Vazões de projeto dos drenos/bueiros por hidrograma SCS (docs 898–903)
fonte: Vazões Bueiros TR-25.xls (902):1,6,9,10; Vazões Bueiros TR-50.xls (903); Vazões 51a100 (901), 101a150 (898), 151a200 (899), 201a219 (900) — abas por obra/dreno
disciplinas: [hidrologia-de-projeto-para-drenagem]
nivel: basico

## Problema
Calcular Q de pico dos drenos (TR 25 e TR 50) para dimensionar bueiros (ver caso baixio_irece_bueiros_dimensionamento) e drenos 51–219.

## Dados de entrada (amostra: aba BU-CP0-11, 902:1)
| grandeza | valor | unidade | fonte | ancoragem |
|---|---|---|---|---|
| Área | 323,4 | ha | 902:1 | ✓ |
| CN | 62,04 | — | 902:1 | ✓ |
| S | 155,39 | mm | 902:1 (S = 25400/CN − 254 confere) | ✓ |
| Tr | 25 | anos | 902:1 | ✓ |
| Tc (DNOS) | 0,9633 | h | 902:1 | ✓ |
| d total / d | 1,9266 / 0,16055 | h | 902:1 | ✓ |
| tr / ta / tb | 0,578 / 0,658 / 1,758 | h | 902:1 | ✓ |
| Chuva de projeto | tabela T–K (T=2:30,07; 5:40,76; 10:47,85; 20:54,57; 25:55,56; 50:63,31; 100:68,89) | mm | 902:1 | ✓ |
| IDF (a, b) | 23,7 / 0,895 | — | 902:1 | ✓ (sem definição da equação) |
| Qp unitário (10 mm) | 10,22 | m³/s | 902:1 | ✓ |
Outras obras: BU-CP0-12 A=964,6 ha CN 61,71; (aba seguinte) A=3832,9 ha CN 61,43 Tc 3,335 h Qp10 34,98; A=4730,4 CN 59,72; A=11456,9 CN 65,12 Tc 4,861 h Qp10 71,74; A=844,8 CN 71,2 Qp10 7,69 -> Q projeto 17,82 m³/s (902).

## Método declarado (Projeto Básico - Relatorio Irece-Final-Jul08.pdf, doc 670:113, 116-117, 119)
- Bacias ≤ 100 ha: Racional Qp = C·I·A·k/360 (A km² no texto, k = 1 / 0,95 / 0,9 por faixa de área), I = P24h/Tc (mm/h), Tc pelo DNOS: Tc = 4,2·A^a·L^b·k·I^-c com expoentes 0,3 / 0,2 / 0,4 lidos como lista solta de números (670:116; a posição de cada expoente é inferida, NÃO usar sem conferir a página); k=3,0 solo arenoso, 4,0 argiloso; A km², L km, I m/m. C do Quadro 7.4: 0,10 a 0,40 conforme textura/declividade. Bacias > 100 ha: SCS-CN, CN do Quadro 7.4 (32; 58; 56,5; 71,2). CN = 71,2 do Quadro 7.4 aparece nas abas de 902/903 (ex.: A=844,8 ha).
- Chuva: P24h = 1,10·Pdiária (Taborga Torrico, 1975), Gumbel em Bom Sucesso/Xique-Xique/Irecê/Barra; média 24 h: TR2 63,6; TR5 86,2; TR10 101,2; TR20 115,4; TR50 133,9; TR100 147,8 mm (670:113). Alturas para outras durações por equação P = f(t) (PROTECS 1981), expressão ilegível no texto.
- TR: 5 anos drenos; 25 anos bueiros; 50 anos verificação como orifício (670:119).

## Método (planilhas 902/903)
Hidrograma triangular SCS: chuva distribuída em blocos de duração d (d total/12), blocos reordenados (maior no centro, "Ordenamento"), chuva efetiva por CN/S (perdas SCS), convolução de hidrogramas parciais, pico = Qp(10mm) × lâmina efetiva. Tc pela fórmula DNOS. Vazão de pico final do BU-CP0-11 = 6,03 m³/s (TR 25) e 8,87 m³/s (TR 50, 897:1).

## Resultado
Q TR25 / TR50 por obra, em 897:1 e 896:1 (ex.: BU-CP0-11 6,03/8,87; BU-CP0-15 44,58/61,98; BU-CP0-18 137,86/185,36).

## Gabarito para calculadora
racional.py NÃO reproduz (método é HUT-SCS, não racional). Gabarito seria um hut_scs.py: entradas A, CN, Tc (DNOS), TR e tabela T–K; saída Q de pico. Caso de teste: A=323,4 ha, CN=62,04, TR=25 -> Q=6,03 m³/s (tol. 5 %, conferir fórmula DNOS no doc 902:1).

## Observações
- Falta no acervo de texto a definição de como "K" vira altura de chuva em d total; não achei equação de IDF explícita (apenas a=23,7 e b=0,895). A planilha usa a coluna "Soma(p)" cumulativa (23,2 mm em 0,16 h; 71,5 mm em 1,44 h) – pág. 902:1.
- Planilhas .xls: ERRO xlrd na ficha (doc 896-903), mas texto/valores existem em "planilha" (ok). Não há memorial descritivo textual.
