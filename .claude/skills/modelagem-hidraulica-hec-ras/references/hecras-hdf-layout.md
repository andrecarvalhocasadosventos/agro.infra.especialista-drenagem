# Layout do `.pNN.hdf` lido por `tools/dren/hecras_hdf.py`

Origem: inspeção com h5py do `.p01.hdf` real da captação no São Francisco (HEC-RAS 6.5, fev/2024, 2D, SI). Os manuais **não descrevem** o formato interno do HDF (`MAPA_DE_CONHECIMENTO.md`, G5). Marca B: derivado de arquivo, não de documento. Nenhum caminho 1D foi verificado em arquivo real.

| O que | Caminho (2D, verificado) |
|---|---|
| Versão, unidades, projeção | atributos da raiz (`File Version`, `Units System`, `Projection`); `Results/Unsteady` (`Program Version`, `Type of Run`) |
| Passo base, saída, janela | `Plan Data/Plan Information` (`Computation Time Step Base`, `Base Output Interval`, `Time Window`) |
| Equação, θ, tolerâncias, iterações | `Plan Data/Plan Parameters` (`2D Equation Set`, `2D Theta`, `2D Water Surface Tolerance`, `2D Volume Tolerance`, `2D Maximum Iterations`, `Gravity`) |
| Área e n de célula, cota mínima, faces | `Geometry/2D Flow Areas/<área>/` (`Cells Surface Area`, `Cells Center Manning's n`, `Cells Minimum Elevation`, `Faces Cell Indexes`) |
| Atributos da área (n base, tolerâncias de geometria, espaçamento) | `Geometry/2D Flow Areas/Attributes` |
| Linhas de contorno | `Geometry/Boundary Condition Lines/Attributes` |
| Contornos do evento | `Event Conditions/Unsteady/Boundary Conditions/{Flow Hydrographs, Normal Depths, ...}/<nome>` (normal depth = 1 valor, a declividade) |
| NA por célula no tempo | `Results/Unsteady/Output/Output Blocks/Base Output/Unsteady Time Series/2D Flow Areas/<área>/Water Surface` (tempo × células; `.../Time` em dias) |
| Máximos | `.../Base Output/Summary Output/2D Flow Areas/<área>/{Maximum Water Surface, Maximum Face Velocity}` (linha 0 = valor, linha 1 = tempo). **Em célula seca o máximo do resumo não é NA**: filtrar por profundidade |
| Erro de volume e passo | `.../Unsteady Time Series/2D Flow Areas/<área>/Computations/{Volume Error, Volume, Time Step}`; passos efetivos em `.../Computation Block/Global/Time` |

1D (convenção HEC-RAS 6.x, **só fixture sintética**): `Geometry/Cross Sections/Attributes` (`River`, `Reach`, `RS`); `.../Unsteady Time Series/Cross Sections/{Water Surface, Velocity Total}`; permanente: `Results/Steady/Output/Output Blocks/Base Output/Steady Profiles/Cross Sections/...`. A função busca por nome e **avisa em vez de inventar** quando não acha. Ao receber um `.hdf` 1D real, conferir os caminhos e acrescentar um teste.

Armadilhas de leitura: células de área nula existem (filtrar); unidades do `Volume Error` e do `Volume` vêm no atributo `Units` e podem ser imperiais mesmo em arquivo SI; o intervalo de saída (30 min) é maior que o passo (10 s): a estabilização é avaliada só nas saídas.
