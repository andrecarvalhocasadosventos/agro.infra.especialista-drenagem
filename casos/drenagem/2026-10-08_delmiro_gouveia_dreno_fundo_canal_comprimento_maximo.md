# Delmiro Gouveia (AL) — Dreno subterrâneo de fundo do Canal Principal: vazão unitária por Darcy, capacidade do tubo PEAD e comprimento máximo (DN170 e DN230)
tipo: NEGATIVO (capacidade do tubo dreno declarada não reproduz por Manning com os próprios dados do memorial; erro inócuo no projeto, relevante para a calculadora)
qualidade: B (qd e Lmáx reproduzem; capacidades dos tubos não; equação de qd ilegível na extração)
fonte: doc 1492, Vol. 1 Tomo II, Memorial descritivo, pp. 102-106 (CODEVASF 2016, Projeto Básico, Hydros). Duplicata: doc 1520 (pág. +2). Não é o dreno agrícola de parcela (Hooghoudt/Glover-Dumm): nenhum projeto lido do acervo tem espaçamento de drenos agrícolas calculado; ver "Lacunas".
disciplinas: [drenagem-subsuperficial]
nivel: projeto básico
legenda de marcas: `✓` ancorado na camada de texto; `✓*` magnitude não provada; `·` sem testemunha (valor lido com `ler`, a extração não trouxe o número, notação científica); `!`/`~` nenhum; `✓h` nenhum.

## Pergunta de engenharia
Que comprimento de tubo dreno sob o fundo de um canal revestido com geomembrana, em corte, drena a vazão que o solo contribui, e como isso define DN e poços de inspeção?

## Dados de entrada
| grandeza | valor | un. | fonte doc:pág | marca |
|---|---|---|---|---|
| Seção do canal | trapezoidal, talude 1,5H:1V, base 1,35 m, tirante 0,90 m, altura 1,25 a 1,76 m, geomembrana PEAD + proteção de concreto | — | 1492:102 | texto |
| Carga H (plano do tubo à superfície potencial do lençol) | 1,26 | m | 1492:105 | ✓ |
| X (distância horizontal; metade da largura de raspagem) | 4,06 | m | 1492:105 | ✓ |
| Condutividade hidráulica do solo natural | 10⁻⁴ (areno-siltoso, < 35 % na #200) | cm/s | 1492:105 | · |
| Relação entre materiais | KT1 < KT2 < KSN < KMD (valores máximos normais esperados, "tendência ao superdimensionamento") | — | 1492:103-104 | texto |
| Vazão unitária qd (dois lados) | 3,910·10⁻⁷ | m³/(s·m) | 1492:105 | · |
| DN170 (Ø interno) | 170 (149) | mm | 1492:105 | ✓ |
| DN230 (Ø interno) | 230 (200) | mm | 1492:105 | ✓ |
| Manning n, PEAD corrugado de parede simples (DNIT 2006) | 0,016 | adim. | 1492:105 | ✓ |
| n recomendado para parede dupla | 0,010 | adim. | 1492:105 | ✓ |
| Declividade do tubo ("de projeto do canal") | 0,00030 | m/m | 1492:105 | ✓ |
| Regime | uniforme, fluxo livre, meia seção | — | 1492:105 | texto |
| Q capacidade DN170 / DN230 | 1,518·10⁻⁴ / 4,929·10⁻⁴ | m³/s | 1492:105 | · |
| Lmáx DN170 / DN230 | 388 / 1.260 | m | 1492:105-106 | ✓ |
| Limite de manutenção (limpeza) | 200 a 300 m; trecho máximo adotado 250 m | m | 1492:106 | texto |
| Regra de DN: L < 350 m só DN170 (1 PIL); L > 350 m, transição DN170 → DN230 no PIL anterior | — | 1492:106 | texto |
| Sensibilidade citada pelo projetista | K pode variar uma ordem de magnitude para mais ou para menos | — | 1492:106 | texto |

## Método do projetista
1. Seção de drenagem crítica na estaca E2+00 com 4 materiais (solo natural, aterro local, aterro de empréstimo, material drenante), usando só o K máximo normal.
2. Modelo conceitual: Darcy, qd = K·I·A, integrado ao longo da seção para um lado do tubo e dobrado para dois lados (a equação do PDF está em imagem e sai embaralhada no texto). A forma qd = K·H²/(2X) por lado, K·H²/X nos dois lados, é rastro C: reproduz 3,91·10⁻⁷ com H, X e K lidos.
3. Capacidade do tubo: Manning, meia seção, n = 0,016, S = 0,0003.
4. Lmáx = Q/qd.
5. Concepção: trechos de no máximo 250 m, PIL (poço de inspeção e limpeza) entre eles, DN170 até 350 m e DN230 acima (1492:106).

## Resultado
Lmáx DN170 = 388 m; Lmáx DN230 = 1.260 m (1492:105-106). Solução adotada: tubo por trechos de 250 m com PIL, DN230 só quando o comprimento total passa de 350 m.

## Gabarito para a calculadora (nenhum número promovido; `✓h` pendente)
- Reproduzem (rastro B): Lmáx = Q/qd (1,518·10⁻⁴ / 3,91·10⁻⁷ = 388 m; 4,929·10⁻⁴ / 3,91·10⁻⁷ = 1.260 m); qd = K·H²/X com K = 10⁻⁶ m/s, H = 1,26 m, X = 4,06 m → 3,91·10⁻⁷ m³/(s·m).
- NÃO reproduzem: Q capacidade. Teste que revela o erro: Manning, seção circular meia cheia, D = 0,149 m, n = 0,016, S = 0,0003 → Q ≈ 1,05·10⁻³ m³/s (documento: 1,518·10⁻⁴; razão ≈ 6,9×). Para D = 0,200 m → Q ≈ 2,31·10⁻³ (documento: 4,929·10⁻⁴; razão ≈ 4,7×). Teste independente de qualquer hipótese: com n e S iguais e a mesma lâmina relativa, Q ∝ D^(8/3); a razão DN230/DN170 deveria ser (200/149)^(8/3) ≈ 2,19, e o documento dá 3,25 (equivale a Q ∝ D⁴).
- Hipóteses não testadas para a diferença: S diferente do impresso, n ou área distintos, ou transcrição incorreta do valor no memorial. Nenhuma está documentada.

## Rastro
- A: H, X, DN, Ø interno, n, S, Lmáx (✓ na extração).
- B: qd (reconstituído de K, H, X); Lmáx = Q/qd.
- C: forma exata da equação de qd; interpretação "meia seção" (lâmina y = D/2); origem do K = 10⁻⁴ cm/s (ensaio não citado).

## Divergências
1. Capacidade do tubo: ver Gabarito (6,9× e 4,7×; razão entre DN fora da lei D^(8/3)).
2. Efeito no projeto: se o Manning estivesse correto, Lmáx seria da ordem de 2,7 km (DN170) e 5,9 km (DN230) com o mesmo qd; o limite de manutenção (250 m) governa de qualquer modo, e a concepção com PIL não muda. Com K 10 × maior (a sensibilidade que o próprio memorial cita), Lmáx pelos valores do documento cairia para ≈ 39 m (DN170) e, pelo Manning acima, para ≈ 270 m; ou seja, o erro de capacidade só importaria se o K real fosse alto.
3. S do tubo: 0,00030 é a "declividade de projeto do canal" (1492:105); o tubo sob o fundo é longitudinal e pode ter outra declividade; não informado.
4. Comparação entre projetos do acervo (não é erro): CSB usa q = 6·10⁻⁵ m³/s/m por critério próprio (caso `csb_geohidro_dreno_fundo_canal_subsuperficial`); Delmiro usa Darcy com K máximo e gradiente H/X (qd ≈ 3,9·10⁻⁷, ~150× menor); CAC Trecho 1 adota 2 drenos PVC Ø150 perfurados com descarga gravitária para o bueiro mais próximo, sem cálculo (doc 1131:28). As 3 ordens de grandeza não são reconciliadas por nenhum dos documentos.

## Lacunas
Não há dreno agrícola (Hooghoudt, Ernst, Glover-Dumm) com espaçamento calculado no acervo consultado: buscas `Hooghoudt` e `espaçamento entre drenos` sem resultado de cálculo; Vale do Iuiu decide por não drenar (caso `iuiu_2002_drenabilidade_subterranea_diagnostico`). O Anexo 7.1 do Delmiro ("Drenagem dos Lotes Irrigados", drenos SH-11 e SH-12, doc 1493:8) não foi lido; o título sugere drenos superficiais dos lotes. Um "espaçamento entre drenos (4,0 m)" aparece nos orçamentos do CSB (docs 1177/1178, TR e anexos) como parâmetro de quantitativo, não lido.

## Fronteira
K medido e envoltório: Geotecnia. Subpressão e estabilidade do revestimento: Hidráulica/Geotecnia. DN do tubo dreno (D-86 do CDV): este caso é insumo, não resposta.
