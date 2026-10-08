# Salitre Etapa 2 — inconsistências internas do memorial de macrodrenagem (caso NEGATIVO)
fonte: Memorial descritivo (doc 1584):97-100, 105 e Memorial de cálculo Tomo 3.1 (doc 1585):97-123 — Projeto Salitre, CODEVASF 2014, executivo (Hydros)
disciplinas: [canais-de-drenagem-e-macrodrenagem, conferencia-de-memorial]
nivel: projeto executivo
tipo: negativo (erros e conflitos reais de documento; nenhum invalida o dimensionamento por si, mas todos seriam pegos por uma conferência automática)
qualidade: B (conferências aritméticas sobre texto extraído; o item de ACP depende de a extração ter preservado todas as linhas)

## Problema
Um revisor que recebe o memorial e a planilha de cálculo deve reconciliar totais, limites de critério e dados de bacia. O caso lista o que não fecha, com o teste que revelaria cada item. Complementa o caso positivo `2026-10-08_salitre_etapa2_macrodrenos_trapezoidais_manning.md`.

## Itens

### N1 — total de extensão de drenos não fecha (A + B)
Texto (1584:97): "extensão total ... 72.858,41 m, dos quais 2.026,00 m (Mulungú); 51.533,65 m (Recreio, inclusive 11.062,00 m de drenos especiais); 21.324,76 m (Tourão)".
Soma das três parcelas: 2.026,00 + 51.533,65 + 21.324,76 = 74.884,41 m. O total declarado (72.858,41) é Recreio + Tourão: falta exatamente 2.026,00 m (Mulungú) no total.
O Quadro 3.47 reconcilia por bacia: Recreio 40.471,65 = 15 drenos (36.524,83) + 4 extravasores CT (3.946,82); mais drenos especiais 11.062,00 (4.543 + 6.519) = 51.533,65 (B). Tourão: 8 drenos somam 21.324,76 (B).
Teste: total = soma das bacias. Gabarito: 74.884,41 m (B), não 72.858,41.

### N2 — limite de velocidade: memorial x planilha (A)
Memorial (1584:105): "0,30 m/s a 1,2 m/s". Rodapé de todas as planilhas (1585:97-123): "PARÂMETROS ATENDIDOS V = 0,3 a 1,5 m/s".
Efeito: os 5 trechos do DS-4.1 têm V = 1,306 a 1,309 m/s (1585:99) e o DT 4.1.2/A tem V = 1,230 m/s (1585:101), todos acima de 1,2 e abaixo de 1,5. Em 83 trechos de dreno (n 0,030) lidos nas planilhas 1585:97-123, esses 6 são os únicos acima de 1,2 m/s (máx. 1,309, mín. 0,509); as linhas de bueiro têm V próprio (1,37 a 2,54 m/s, limite 3,5).
Teste: V ≤ V_lim; com 1,2 o DS-4.1 reprova, com 1,5 passa. A calculadora deve exigir que o limite seja informado e sinalizar quando o documento tem dois.

### N3 — profundidade de 1,80 m x seções de 0,70 a 1,50 m (A, interpretação C)
Memorial (1584:105): "profundidade ... 1,80 m para os drenos localizados no entorno das áreas irrigáveis". Nas planilhas (83 trechos de dreno, B) a altura da seção é 0,90 m em 52 trechos, 1,80 m em 10, 0,75 m em 9, 1,50 m em 8 e 0,70 m em 4: o critério de 1,80 m vale só para parte dos drenos. Onde foi imposto, a seção fica superdimensionada para a demanda: DT 4.1.2/A (1585:101) b 0,60, h 1,80, Q trecho 2,030 contra Q dreno 5,315 m³/s (2,6 vezes) e V 1,230 m/s; DT-4.3.1/A (1585:120), com h 0,90 e b 9,00, também tem capacidade 2,14 vezes a demanda (7,902 contra 3,690), sem que o texto lido explique a folga de capacidade. O texto lido não diz quais drenos ficam "no entorno das áreas irrigáveis". Tratar o enquadramento como "não informado" até conferir os perfis (desenhos 0340-DE-00-DR-006 a 076).

### N4 — comprimento de talvegue implausível (A)
ACP 4W21-6 (1584:99): área 202,84 ha, "Ext. talvegue 20.040,57 m", cota máx 431,08, mín 427,21 (desnível 3,87 m, declividade 0,019 %). As ACPs vizinhas de 100 a 300 ha têm 0,4 a 3,3 km; a de maior área (4W-21, 1.472,82 ha) tem 4.193,21 m. Parece erro de vírgula ou zero (2.004,057 m ou 2.040,57 m: C). Como Tc cresce com L^0,77 em Kirpich (fórmula padrão), um L dez vezes maior inflaria Tc; o texto lido não mostra se esse L chegou ao cálculo de vazão (não informado).
Teste: razão L/área e declividade fora do envelope da própria tabela.

### N5 — contagem e soma das ACPs não batem com o texto (B, depende de extração)
Texto (1584:100-101): Mulungú 13 ACPs = 2.633,25 ha; Recreio 44 + 3 do dreno especial = 11.032,23 ha, 664,03 ha para o especial; Tourão 21 ACPs = 3.475,53 ha.
Tabelas 3.48-3.51 (1584:99-100), somadas por mim: Mulungú 13 linhas = 2.633,25 ha (confere); dreno especial 3 linhas = 664,03 ha (confere); Recreio + especial 51 linhas = 11.293,56 ha (texto: 47 linhas, 11.032,23; diferença 261,33 ha e 4 linhas); Tourão 22 linhas = 3.405,75 ha (texto: 21 linhas, 3.475,53; diferença de −69,78 ha). As 13 sub-ACPs 4W21-n somam 1.593,03 ha contra 1.472,82 ha da 4W-21: possível sobreposição, não esclarecida.
Teste: contagem e soma por quadro contra o texto.

### N6 — declividade de talvegue "não excedem 1 %" (B, menor)
Texto (1584:101): ACPs do Recreio com declividades que "não excedem a 1 %". Tabela: 4W-38 = (420,48 − 409,82)/960 = 1,11 %. Diferença pequena; vale como teste de afirmação textual contra tabela.

## Dados de entrada e marcas
Todos os números acima foram lidos direto das páginas (texto nativo, sem marca `!`, `~` ou `✓*`); somas e razões são B. Nenhum `✓h`. N4 e N5 precisam de conferência humana nas páginas antes de virarem gabarito de teste.

## Divergências com a norma
Nenhuma norma citada pelo documento para o limite de velocidade; os 1,2 e 1,5 m/s são critério do projetista (sem fonte informada).

## O que a calculadora e o parecer devem fazer
Reconciliar totais por soma de parcelas; parar quando o documento traz dois limites de critério e pedir qual vale; sinalizar L de talvegue fora do envelope (L/área) antes de calcular Tc.
