# Jaíba Etapas 3 e 4 — Bueiros de greide sob canal e estrada: Manning com Y/D máximo 0,82 e n implícito de 0,013
fonte: Relatório de Anteprojeto Jaíba Etapas 3 e 4 (doc 1182) pp. 43 (n do canal), 65 (critérios do sistema de drenagem), 66-67 (Tabelas 7.18 e 7.19)
disciplinas: [bueiros-e-travessias, drenagem-de-estradas-e-plataformas]
nivel: anteprojeto
tipo: positivo (com n não declarado)
qualidade: A (22 das 23 linhas reproduzem por Manning com um único n; sem hidrologia no documento)
marcas: `·` = lido por `ler` (doc nativo); sem linhas em `parametros` para estas páginas. Nenhum `✓h`.

## Problema
Bueiros de greide tubulares simples (BSTC) de 0,80 m sob canais das Etapas 3 e 4 do Jaíba: verificar vazão, lâmina e velocidade por Manning em regime permanente com lâmina máxima Y/D = 0,82.

## Dados de entrada
| grandeza | valor | fonte | marca |
|---|---|---|---|
| Diâmetro (todos os 23 bueiros, BSTC) | 0,80 m | 1182:66-67 | · |
| Critério de lâmina | Y/D máximo = 0,82 | 1182:65 | · |
| Método | Manning, regime permanente | 1182:65 | · |
| n de Manning do bueiro | não informado (n do concreto do canal é 0,015, 1182:43) | 1182:43, 65 | · |
| Hidrologia (TR, método, C, área) | não informado nestas páginas | 1182:65 | · |
| Controle de entrada (HW/D), perda de entrada | não informado | 1182:65-67 | · |

## Linhas relevantes (1182:66 Etapa 3; 1182:67 Etapa 4; D = 0,80 m)
| bueiro | i (m/m) | L (m) | Q (m³/s) | Y/D | y (m) | v (m/s) |
|---|---|---|---|---|---|---|
| E3 BC-01 | 0,005 | 25,50 | 0,36 | 0,43 | 0,34 | 1,74 |
| E3 BC-02 | 0,01 | 22,00 | 0,98 | 0,64 | 0,51 | 2,88 |
| E3 BC-06 | 0,005 | 22,50 | 0,83 | 0,74 | 0,59 | 2,10 |
| E3 BC-13 | 0,025 | 21,00 | 1,40 | 0,60 | 0,48 | 4,46 |
| E4 BC-07 | 0,036 | 28,50 | 1,08 | 0,46 | 0,37 | 4,80 |
| E4 BC-08 | 0,007 | 28,00 | 1,10 | 0,82 | 0,65 | 2,51 |
Tabelas completas: 13 bueiros na Etapa 3 (BC-01 a BC-13) e 10 na Etapa 4 (BC-01 a BC-10), todos com D = 0,80 m, L de 18,5 a 36 m, Q de 0,01 a 1,40 m³/s, i de 0,005 a 0,036.

## Método do projetista
Manning em tubo circular parcialmente cheio; para cada bueiro, Q de projeto e declividade determinam Y/D, lâmina e velocidade. Y/D de 0,82 é o limite adotado (E4 BC-08 o atinge). Declividade do bueiro "de acordo com o desnível e características topográficas locais" (1182:65).

## Resultado
Todos os 23 bueiros com Y/D ≤ 0,82 (máximo 0,82 em E4 BC-08). Velocidades de 0,96 a 4,80 m/s (maiores em i = 0,025 a 0,036).

## Gabarito candidato (pendente de ✓h)
E4 BC-08: D 0,80 m, i 0,007, Q 1,10 m³/s → Y/D 0,82, y 0,65 m, v 2,51 m/s (1182:67). E3 BC-13: i 0,025, Q 1,40 → Y/D 0,60, y 0,48 m, v 4,46 m/s (1182:66).

## Rastro
- A: valores das tabelas.
- B (conferência minha): para cada linha, com a geometria de tubo circular e Y/D impresso, o n que fecha Q = A·R^(2/3)·i^(1/2)/n fica entre 0,0128 e 0,0134 em 22 linhas; o n que fecha v fica entre 0,0129 e 0,0131. A linha E3 BC-08 (Q = 0,01 m³/s, Y/D = 0,03) não fecha por arredondamento de Y/D a duas casas (n(Q) = 0,005, n(v) = 0,012); sensibilidade extrema com lâmina de 3 cm, não erro. Valores consistentes com n = 0,013 em todas as outras.
- C: n = 0,013 é inferido; não aparece no texto lido.

## Divergências e pontos de atenção
1. O memorial adota n = 0,015 para o concreto do canal (1182:43) e não declara n para o bueiro, mas as tabelas só fecham com n ≈ 0,013. Com n = 0,015 a capacidade cai cerca de 13 % (razão 0,013/0,015) e, mantendo Q e i, duas linhas passam do critério Y/D ≤ 0,82 (derivado, B): E3 BC-06 iria a Y/D ≈ 0,84 e E4 BC-08 passaria da capacidade a Y/D = 0,82 (0,96 m³/s contra Q de 1,10 m³/s, lâmina próxima da seção plena). Teste revelador.
2. Só Manning em escoamento uniforme: sem HW/D, sem controle de entrada, sem verificação de saída. É o padrão dos projetos do acervo (PENDENCIAS §4). Em i de 0,025 a 0,036 (v até 4,8 m/s) o controle de entrada tende a comandar; o documento não verifica.
3. Hidrologia ausente: Q "de projeto" sem TR, C, área ou método (1182:65-67). Não há como reproduzir Q de nenhum bueiro.
4. Velocidade máxima de 4,8 m/s no tubo de concreto sem limite declarado e sem dissipador de saída citado.

## Fronteira (delegar)
Vazão de projeto e TR: hidrologia-de-projeto-para-drenagem e clima. Dissipador na saída: hidráulica (vertedouros-e-dissipadores).

## Teste sugerido (evals)
D = 0,80 m, i = 0,007, Q = 1,10 m³/s: com n = 0,013 a calculadora deve dar Y/D ≈ 0,82; com n = 0,015 deve dar Y/D acima de 0,82 e o agente deve sinalizar a divergência com o n do canal (0,015).
