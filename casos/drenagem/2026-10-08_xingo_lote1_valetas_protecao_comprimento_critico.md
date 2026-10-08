# Xingó Lote I — Valetas de proteção de crista de corte (VPC) e pé de aterro (VPA): comprimento crítico por declividade
fonte: v. 5 Memorial de cálculo e dimensionamentos (doc 1419) pp. 64-66, 78-80, 86, 90, 98-100, 104, 108, 112 (doc 1451 = duplicata)
disciplinas: [drenagem-de-estradas-e-plataformas]
nivel: basico
tipo: positivo (com 1 inconsistência interna, ver Divergências)
qualidade: A (VPC-1 e VPA-5 reproduzidos por cálculo independente); B nas demais seções
marcas: `·` = sem linha em `consultar.py parametros` para estas páginas; valor lido por `ler` (texto nativo). Nenhum `!`, `~` ou `✓*` usado. Nenhum `✓h`.

## Problema
Dado o revestimento, a geometria da valeta e a chuva de projeto, qual o comprimento máximo (crítico) de valeta antes de transbordar, em função da declividade longitudinal?

## Dados de entrada (VPC-1, 1419:66; chuva do trecho km 0 a 33+890)
| grandeza | valor | unidade | fonte | marca |
|---|---|---|---|---|
| Período de retorno | 10 | anos | 1419:65, 1419:66 | · |
| Tempo de concentração | 10 (fixo) | min | 1419:65 | · |
| Intensidade I (trecho km 0 a 33+890) | 2,353 | mm/min | 1419:66 | · |
| Intensidade I (trecho km 33+890 ao fim) | 1,789 | mm/min | 1419:98, 1419:99 | · |
| Seção trapezoidal VPC-1: base b / largura no topo / altura h | 0,20 / 0,60 / 0,20 | m | 1419:66 | · |
| Revestimento: concreto, n de Manning | 0,016 | — | 1419:65 (texto), 1419:66 (tabela) | · |
| Altura máxima de lâmina hmáx (VPC-1) | 0,16 | m | 1419:66 | · |
| Contribuição externa: largura b=10,00 m, C=0,30 | — | — | 1419:66 | · |
| Contribuição da própria valeta: largura 0,60 m, C=0,90 | — | — | 1419:66 | · |
| Qracional por metro (VPC-1) | 0,0001388 · L | m³/s com L em m | 1419:66 | · |
Outras seções (mesma estrutura, mesma tabela por declividade): VPC-2 (topo 0,70, h 0,20, Qrac/m 0,0001424, 1419:67), VPC-3 (topo 0,80, h 0,25, 0,0001459, 1419:68), VPC-5 (topo 1,00, h 0,30, contribuição externa 20 m, 0,0002706, 1419:78), VPA-5 (com talude de 8 m, C=0,70, externa 10 m, Qrac/m 0,0003726, 1419:86). No trecho km 33+890 em diante: VPC-1 Qrac/m 0,0001056 (1419:98), VPC-2 0,0001083 (1419:99), VPC-3 0,0001109 (1419:100).

## Método do projetista (1419:64-65)
Comprimento crítico por igualdade entre capacidade de Manning (Q1 = A1·R^(2/3)·I1^(1/2)/n) e vazão racional por unidade de comprimento (Q2 = 0,278·C·I2·A2, com A2 = b·L, b = largura do implúvio):
`L = A1·R^(2/3)·I1^(1/2) / (0,278·n·C·I2·b)`. Tabela por declividade de 0,001 a 0,060 m/m (passo 0,001). Seção trapezoidal revestida de concreto; valeta de crista a mais de 3,0 m da crista do corte; valeta de pé de aterro a mais de 1,0 m do pé do talude (1419:65). Dissipação a jusante do lançamento "deverá ser avaliada" (sem critério numérico).

## Resultado (VPC-1, trecho km 0 a 33+890, 1419:66)
| i (m/m) | QManning (m³/s) | v (m/s) | L crítico (m) |
|---|---|---|---|
| 0,001 | 0,023 | 0,392 | 162,54 |
| 0,010 | 0,071 | 1,239 | 514,00 |
| 0,050 | 0,160 | 2,771 | 1149,34 |
| 0,060 | 0,175 | 3,035 | 1259,04 |
Mesma valeta com I = 1,789 mm/min (1419:98): L(0,001) = 213,76 m (razão 1,315 = 2,353/1,789).
VPA-5 (1419:86), i = 0,001: QManning 0,083, v 0,539, L 222,14 m (hmáx 0,24).

## Gabarito candidato (pendente de ✓h)
VPC-1, I = 2,353 mm/min, n = 0,016, hmáx = 0,16: L(i=0,001) = 162,54 m; L(i=0,060) = 1259,04 m (1419:66). VPA-5: L(0,001) = 222,14 m (1419:86).

## Rastro
- A: todos os números da tabela acima (lidos de 1419:66, 86, 98).
- B (conferência minha, não do projetista): Qrac/m = 0,278 · (I em mm/h = 141,18) · (0,9·0,60 + 0,3·10,00) · 1e-6 = 1,389e-4 (documento: 0,0001388). VPA-5: 0,9·1,00 + 0,7·8,00 + 0,3·10,00 = 9,5 → 3,728e-4 (documento: 0,0003726). Manning com z = 1 (deduzido de topo 0,60 = base 0,20 + 2·0,20), y = 0,16 m: A = 0,0576 m², R = 0,0883 m, Q(0,001) = 0,0226 m³/s, v = 0,392 m/s, L = 162,7 m (documento: 0,023; 0,392; 162,54).
- C: z = 1 não é impresso; a regra hmáx = 0,8·h é observada em VPC-1, 2, 3 e 5, não declarada.

## Divergências e pontos de atenção
1. VPC-5, VPC-6 e VPC-7 (1419:78, 79, 80), com alturas h = 0,30, 0,35 e 0,40 m (topo 1,00, 1,10, 1,20 m), têm o mesmo hmáx = 0,24 m e a mesma capacidade de Manning (Q = 0,083 m³/s em i = 0,001, v = 0,539 m/s). Pela regra 0,8·h observada nas outras seções, hmáx seria 0,28 e 0,32 m para VPC-6 e VPC-7. Indício de cópia de linha ou de limite não declarado. Efeito: conservador (profundidade extra não usada), L crítico ligeiramente menor que o possível. Não é erro de segurança.
2. Duas chuvas (2,353 e 1,789 mm/min) para o mesmo TR 10 e tc 10 min, separadas em km 33+890. A equação IDF de cada trecho não está nestas páginas (diz "curvas IDF previamente definidas", 1419:65). Origem da divisão: não informado.
3. Velocidade chega a 3,0 m/s (i = 0,06) em concreto; limite admissível de velocidade não informado nestas páginas.
4. TR 10 anos e tc 10 min para valetas, enquanto os bueiros do mesmo projeto usam TR 25/50/100 (1419:63). Coerente com o porte, mas o critério de escolha não é explicado.
5. Valores de C (0,30 externo, 0,90 revestimento, 0,70 talude) sem justificativa de fonte.

## Fronteira (delegar)
IDF de 10 min, TR 10 por trecho: clima. Dissipador na saída da valeta: hidráulica (vertedouros-e-dissipadores). Traçado e deságue seguro: terraplenagem.

## Teste sugerido (evals)
Entrada: seção VPC-1, n 0,016, I 2,353 mm/min, C composto, i = 0,001 e 0,060; saída esperada L = 162,5 m e 1259 m (tolerância 2 % por arredondamento da tabela). Segundo teste: o mesmo com hmáx = 0,8·h e h = 0,40 (VPC-7): a calculadora deve dar capacidade maior que a do documento (0,083 m³/s).
