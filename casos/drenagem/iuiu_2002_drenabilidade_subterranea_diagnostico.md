# Vale do Iuiu 2002 — Investigação de drenabilidade (Porchet), classes e decisão de NÃO prever drenagem subterrânea parcelar (doc 1051)
fonte: Volume 1 - Relatório do projeto.pdf (doc 1051):54, 151-152, 160-164, 312; Volume 9 - Tomo V e VI - Investigações da drenabilidade dos solos.pdf (doc 1066, 1416 p.):23-24, 44-45
disciplinas: [drenagem-subsuperficial]
nivel: basico (diagnóstico; sem dimensionamento de drenos)

## Problema
Decidir se o perímetro (Cambissolos eutróficos e Podzólicos Vermelho-Amarelos eutróficos, substrato calcário a 2-3 m) precisa de drenagem subterrânea em nível parcelar.

## Dados de entrada
| grandeza | valor | unidade | fonte | ancoragem |
|---|---|---|---|---|
| Condutividade hidráulica (UHP II) | 0,44 a 1,98 | m/dia | 1051:162 | texto |
| Condutividade hidráulica (UHP III) | 0,78 a 2,12 (média); 0,42 a 2,12 (mediana) | m/dia | 1051:162 | texto |
| Profundidade da barreira | > 1,5 m (2,0 a 3,0 m na maioria) | m | 1051:162 | texto |
| Classe de solo | D3 (moderadamente permeáveis na superfície, pouco permeáveis a 1-2 m) | — | 1051:162 | texto |
| Ensaios | Porchet (ausência de lençol) | — | 1051:154, 157 | texto |

## Método
Ensaio de Porchet em furos de trado (500 testes): K em m/dia calculado a partir de r (cm), alturas h0 e ht (cm) e tempos t0 e tn (s), com constante 423 (1066:23; a fórmula está em imagem/garbled no texto: forma K = 423·r·ln[(h0+r/2)/(ht+r/2)]/(tn−t0) é inferida, conferir a página). Exemplo do Quadro 3.1 (1066:24): teste Porchet nº 1, perfil 156 cm, unidade Ce1, camada 156-56 cm, K = 0,05 m/dia; nº 2 K = 0,56; nº 3 K = 0,16; nº 4 K = 0,52. Classes de drenabilidade investigadas (1066:44, total 3.427,03 ha): boa 68,87 % (2.360,06 ha); restrita 16,38 % (561,44 ha); pobre 10,78 % (369,49 ha); crítica/descartável 3,97 % (136,04 ha). UHP I (Cambissolos eutróficos) K médio 0,07 a 2,18 m/dia.
Tabela de "Parâmetros de Classes de Drenabilidade" (boa / restrita / pobre / crítica) por profundidade da barreira e condutividade hidráulica; classes boa e restrita não demandam drenagem subterrânea parcelar; pobre/crítica -> outros usos (pastagem, silvicultura) (1051:162-163). Anteprojeto de drenagem parcelar (superficial) em 5 áreas amostrais (EP12, EP25, EP9, TO21, TO29) (1051:54). Conclusão: "o sistema de drenagem projetado é apenas superficial" (1051:312).

## Resultado
Sem drenos subterrâneos. Talvegues usados como drenos principais, com escavação/retificação possível (1051:163). Alerta: elevação do lençol possível com irrigação de baixa eficiência.

## Gabarito para calculadora
Não há equação de espaçamento (Hooghoudt/Ernst), recarga ou coeficiente de drenagem -> NÃO valida dreno.py. Serve só como teste de decisão: K entre 0,4 e 2,1 m/dia e barreira > 1,5 m -> drenabilidade boa/restrita -> sem drenagem subterrânea parcelar.

## Observações
Lacuna conhecida mantida: nenhum cálculo de espaçamento/profundidade de drenos agrícolas neste documento. Valores de K lidos do texto; as tabelas de classe estão em 1051:160 (não lidas em detalhe).
