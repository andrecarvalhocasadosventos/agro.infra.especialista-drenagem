# Inventário dos estudos HEC-RAS da TPF (CDV) — somente leitura (R0)

> Sessão `/treinar drenagem`, 2026-10-09 (servidor). Fontes: FTS do `catalogo.sqlite` do Acervo CDV-TPF (local,
> `D:\14 - AGRO\squad\acervo_cdv\catalogo.sqlite`, 1.660 arquivos, 6.711 páginas indexadas) e, **um a um**, os
> membros pequenos (`.prj`, `.p01`, `.u01`, `Resultados.txt`) e três `.hdf` dos dois `.zip` do Data Room.
> Nada foi extraído para o Drive nem executado; os `.hdf` foram abertos só com `h5py` (cópia em
> `D:\14 - AGRO\squad\drenagem_download\hecras\`, fora do pacote). Termos buscados no FTS: "HEC-RAS", "HEC RAS",
> HECRAS, remanso, "mancha(s) de inundação", hidrodinâmica, "standard step", batimetria, "HEC-HMS".
> Caminhos relativos à raiz do Data Room `X:\Shared drives\[Data Rooms] Ventos da Terra - Externo\1. Engenharia\[Data Room] CDV & TPF Engenharia\`.
> Páginas = página do PDF (a indexação do catálogo; ver o caveat de cada caso).

## 1. Documentos com modelagem HEC-RAS

| # | Documento (id do catálogo) | Caminho | Págs. | O que modela | Dados de entrada | Resultados |
|---|---|---|---|---|---|---|
| D1 | Relatório Final `CDV-VDT-REL-INF-GER-001-R00` (1709) | `4. Relatórios\Relatório Final\Texto e Memorias\` | 167 (153 com texto) | **3.2** captação no rio São Francisco: **2D, não permanente com Q constante** (ver D4), Manning 0,035, malha 10 m na batimetria e 50 m fora, jusante = declividade 0,01 % (p. 41-42). **3.3** rio Verde na travessia do aqueduto: Standard Step (software não declarado), TR 100 (p. 49-55). **3.4** riachos Recife e Ferreira: **2D**, Manning 0,040, malha 50 m, jusante = declividade 0,012 %, TR 2, 10, 25 e 100 (p. 55-62) | batimetria; MDT ANADEM 30 m e LIDAR; Q95, Q98, Q50, Qméd, QTR100, QTR500 regionalizadas de Morpará (Tab. 2-4, p. 40-41); hidrogramas SCS por sub-bacia (Tab. 8, p. 56-57) | NA por vazão (Tab. 5, p. 42), mapas de NA e velocidade (Fig. 26-37, p. 43-48); lâmina e velocidade por TR (Fig. 46-53, p. 58-62); NA = 397 m no rio Verde (p. 55) |
| D2 | Acompanhamento 2026.08.11 (1503) | `5. Projeto TPF - Gestao de Engenharia\01. Premissas\Arquivos comentados\` | 21 | premissas (p. 2: NA na captação por "simulação hidrodinâmica no HEC-RAS"; p. 3: rio Verde, TR 100 com nota "verificou-se que o TR considerado foi de 50 anos") | lista de premissas | sem números de HEC-RAS |
| D3 | Acompanhamento 2026.08.12 (1504) | idem | 6 | p. 4: aqueduto, TR 100, validar ausência de remanso por Standard Step | critérios | — |
| D4 | Notas de Reuniões TPF até 12set26 (1505) | `5. Projeto TPF - Gestao de Engenharia\Notas de Reuniões\` | 8 | p. 2: cota 397 m como NA da travessia do rio Verde alinhada; p. 3-6: "análise hidráulica da batimetria no HEC-RAS", "simulação hidrodinâmica bidimensional" (Sun Velloso); batimetria revelou depressão no rio | — | decisões de reunião |
| D5 | `sao francisco_HECRAS.zip` (1533), 436 MB, 317 entradas | `4. Relatórios\Outros\2026.09.29 - HECRAS\` | — | projeto HEC-RAS **6.5 (fev/2024)**, geometria `g01`, plano `p01` ("simulacao"), vazão `u01` ("contornos"); **6 pastas** `sao_francisco_{Q95,Q98,Q50,Qmed,QTR100,QTR500}` (a de QTR500 está na listagem; só QTR100 foi aberta aqui) | `.u01`: 1 hidrograma de 100 valores horários constantes; contornos "entrada" (vazão), "saida 1" e "saida 2" (declividade 0,000093); `BATIMETRIA.tif` (65 MB), `ANADEM_Captacao_recortado.tif`, shapes de apoio; `.rasmap`, `.dss` | `Resultados.txt` (NA e vazão do braço), `NA.png`, `Velocidade.png`, `.p01.hdf` (24-27 MB), `PostProcessing.hdf` |
| D6 | `riachos recife e ferreira_HECRAS.zip` (1532), 7,96 GB, 552 entradas | idem | — | projeto HEC-RAS 6.5, 4 pastas `riachos_recife_ferreira_{TR2,TR10,TR25,TR100}`; 5 condições de contorno de vazão (`Recife_SB1..SB4`, `Ferreira_SB1..`) com hidrogramas; simulação 24-set a 29-set-2026 (5 d 22 h), passo 10 s | `.u01` com hidrogramas (picos = Tab. 8 do relatório); `Terrain.hdf` | `.p01.hdf` de 0,88 a 1,29 GB; `PostProcessing.hdf` 0,4 a 0,74 GB; `resultados/SHP` (contorno de 0,5 m e limite de inundação por TR); `Hidrograma travessia.txt` |
| D7 | Q&A CDV & TPF 2026.09.23 (1514, xlsx), Acompanhamento 2026.09.09 (1400, p. 3, 10) e 2026.09.23 (1508, p. 16-17) | `4. Relatórios\Outros\...` | — | citam "manchas de inundação"/"hidrodinâmica" (FTS), conteúdo **não lido** nesta sessão (ver §3) | — | — |
| D8 | Manual de Irrigação Codevasf (1506), p. 187, 189, 324 | `4. Relatórios\Outros\2026.09.16 - Manual CODEVASF\` | 528 | só referência de método: cálculo de remanso de cheia em canal (regime permanente, partindo de jusante) e efeito de pilares | — | não é estudo HEC-RAS |

## 2. Tipologia dos estudos

| Estudo | Dimensão | Regime | Estrutura | Trecho |
|---|---|---|---|---|
| Captação São Francisco | 2D (1 área, 31.313 células) | não permanente com vazão constante por 24 h (equivale a permanente) | nenhuma (NA para cota de captação) | trecho do rio com batimetria; 6 vazões |
| Rio Verde | 1D Standard Step (declarado no relatório; **sem arquivo do modelo no acervo**) | permanente, subcrítico | aqueduto (NA 397 m) | Barragem Maravilhas até a travessia (~2,4 km, p. 50) |
| Riachos Recife e Ferreira | 2D (1 área) | não permanente com hidrogramas SCS | sifão sob riacho Recife; o canal corre paralelo aos riachos (p. 55) | manchas de inundação, TR 2-100 |

## 3. Lacunas e itens não lidos

- Data Room: a listagem do diretório `4. Relatórios\` inteiro estourou o tempo (Drive saturado); só o `2026.09.29 - HECRAS` foi lido (listagem dos `.zip` por `zipfile`, sem extrair). **Não** inventariado: outras pastas de `4. Relatórios\Outros\` com possível HEC-RAS sem texto indexado, e o conteúdo de D7.
- Catálogo: 299 arquivos com texto e 292 páginas pendentes de OCR; o FTS não enxerga conteúdo ainda não extraído. O relatório final está `parcial` (153 de 167 páginas). Não há `.hdf`/`.prj` HEC-RAS no catálogo (só os dois `.zip`, não abertos pelo pipeline).
- QTR500 de São Francisco e TR 2/10/25 do rio Recife: só o texto de `.u01`/`.p01` de TR 2 e TR 100 dos riachos e de Q95/Q50/QTR100 de SF; nenhuma saída `.hdf` dos riachos foi aberta (arquivos de 0,9 a 1,3 GB; teto de leitura do Drive).
- Rio Verde: nenhum arquivo de modelo no acervo; os números vêm só do texto do relatório.
