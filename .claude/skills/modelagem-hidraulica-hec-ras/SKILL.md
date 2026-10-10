---
name: modelagem-hidraulica-hec-ras
description: >
  Especifica, confere e interpreta estudos de cheia e remanso com HEC-RAS 6.x (1D, 2D com difusão ou SWE, 1D/2D, chuva na malha): 1D × 2D, dados mínimos, malha e Courant, n de Manning, calibração e sensibilidade, contornos e condição inicial, pontes e bueiros no modelo, critérios de aceitação (casos negativos da TPF) e leitura de `.hdf` com `tools/dren/hecras_hdf.py` (só leitura; HEC-RAS não instalado). Use quando: "HEC-RAS", "mancha de inundação", "NA de cheia de rio ou riacho", "1D ou 2D", "malha 2D", "Courant", "contorno de jusante", "normal depth", "calibrar o n", "sensibilidade de n", "conferir o modelo da TPF", "ler o .hdf", "NA e velocidade máximos", "remanso de ponte". Não use para: Q de bacia, Tc, SCS (use hidrologia-de-projeto-para-drenagem); IDF, TR e ARF (Clima); dimensionar bueiro (use bueiros-e-travessias); remanso em canal de adução, vertedouro, dissipador, captação (Hidráulica); MDT e batimetria (Geoprocessamento); preço (orçamento).
---

# Modelagem hidráulica com HEC-RAS (cheias, travessias, manchas)

Premissa de treinamento (D9, determinação do André em 2026-10-09; R0: não é decisão de projeto do CDV). O especialista **especifica, confere e interpreta**; não executa o HEC-RAS (não instalado no servidor) e não "inventa" resultado. A calculadora `tools/dren/hecras_hdf.py` só lê arquivos. Convenções, níveis de projeto, delegação e parecer: núcleo `drenagem-fundamentos`.

Páginas: "p. N" = página física do PDF (= número impresso). Os manuais usam ft, cfs e acre-ft; a skill escreve SI e dá a unidade original quando cita número. Equações numeradas dos manuais saíram da extração (só estão na imagem): conferir no PDF antes de codificar. Mapa de localização: `referencias/MAPA_DE_CONHECIMENTO.md` (grupo G5) e `referencias/_mapa_parcial/HECRAS.md`.

## 1. Escopo e fronteiras

Dentro: mancha de inundação e NA de cheia de rio ou riacho; travessia (aqueduto, sifão, bueiro) sob cheia; remanso causado por estrutura de drenagem; NA e velocidade na captação como **entrada** para a Hidráulica; leitura crítica de modelo entregue por terceiro.

| Tema | Dono | Ação do Drenagem |
|---|---|---|
| Q de projeto, hidrograma por sub-bacia | Drenagem (`hidrologia-de-projeto-para-drenagem`) | calcula; a chuva vem do Clima |
| IDF, chuva por TR, **ARF** | Clima | `[DELEGAR: clima]`; sem ARF o pico fica sem redução por área (caso HR-05) |
| Remanso em canal de adução, vertedouro, bacia, comporta, sifão (regime) | Hidráulica | `[DELEGAR: hidraulica]`; a Hidráulica pode pedir o NA de cheia a jusante como contorno |
| Captação e bombas | Hidráulica | entrega NA e velocidade com ponto, TR e incerteza (HR-01) |
| Dimensionar bueiro (HW/D) | `bueiros-e-travessias` | o HEC-RAS só confere a cota de montante |
| MDT, batimetria, LIDAR, delimitação de bacia | Geoprocessamento (onda 2, ainda sem especialista) | consome, cita fonte, resolução, data e datum; pede à equipe |

## 2. Escolha do modelo

| Situação | Modelo | Fonte |
|---|---|---|
| Canal confinado, seções reais, Q conhecido, remanso de ponte ou bueiro | 1D permanente (energia, Standard Step) | [USACE-HECRAS-HRM-66 p. 24-33] |
| Mesmo trecho com onda de cheia, armazenamento, comportas | 1D não permanente (Saint-Venant, esquema implícito) | [USACE-HECRAS-HRM-66 p. 41-48] |
| Planície larga, riachos paralelos ao canal, escoamento sem direção única, confluência, mancha | 2D | [USACE-HECRAS-2DUM-66 p. 270-273] |
| Calha bem definida e planície larga | 1D/2D acoplado (calha em 1D, planície em 2D) | [USACE-HECRAS-2DUM-66 p. 51-52] |
| Chuva direta na malha | 2D com chuva e perdas (CN, déficit-constante, Green-Ampt) | [USACE-HECRAS-2DUM-66 p. 165-168] |

Permanente **não** serve para maré, onda rápida, fluxo reverso, galgamento de dique, rio muito plano, bombas e comportas complexas [USACE-HECRAS-2DUM-66 p. 270-273].

**Equação 2D (corrige o PLANO §11.2 item 1).** O padrão do programa é a **difusão**; o manual manda desenvolver com difusão e depois rodar um segundo plano em SWE e comparar; se houver diferença significativa, a SWE é a mais precisa [USACE-HECRAS-2DUM-66 p. 196]. A SWE é obrigatória nas situações da lista de p. 196-197 (onda muito dinâmica, ruptura, cheia relâmpago, contração ou expansão abrupta, rio muito plano, maré, manobra de comporta, superelevação em curva, detalhe em estrutura, regime misto). SWE-ELM é o solver original e mais rápido; SWE-EM é explícito, mais conservativo em momentum, exige malha ortogonal e passo por CFL [USACE-HECRAS-2DUM-66 p. 211; USACE-HECRAS-HRM-66 p. 108-109]. Regra do especialista: **mancha de cheia em planície lenta = difusão aceitável como primeira rodada; cheia dinâmica, estrutura ou travessia = SWE-ELM, com a comparação difusão × SWE no parecer.**

## 3. Dados mínimos (pedir e registrar a premissa)

1. **Terreno**: MDT de terra nua em raster; o canal exige batimetria; incluir diques, muros e estradas; **não incluir pontes** [USACE-HECRAS-MAPPER-66 p. 33]; tamanho de célula do terreno capaz de captar o canal e as feições abruptas (o manual não dá número). Resolução, data, fonte e **datum vertical** declarados (os manuais não tratam datum brasileiro nem SIRGAS; ver lacunas). A projeção do projeto é obrigatória [USACE-HECRAS-MAPPER-66 p. 22, 30].
2. **Q e TR**: do Clima/hidrologia, com ARF; hidrograma por sub-bacia com pico, tempo ao pico e volume; TR por obra pelas tabelas da hidrologia.
3. **n por uso do solo** (mapa) e n do canal; fonte do valor.
4. **Contorno de jusante com fonte**: NA conhecido, curva-chave ou declividade **medida**; nível inicial.
5. **Estruturas**: geometria de ponte, bueiro, vertedouro; cotas.
6. **Duração** e intervalo de saída; passo de cálculo.
7. Dado observado para calibrar (marca de cheia, curva-chave, NA de posto), se existir.

## 4. Montagem do modelo

**Fluxo**: projeto e unidades, geometria, escoamento e contornos, plano, execução, resultados [USACE-HECRAS-UM-66 p. 32-42]. Passos de um modelo 2D de 1 a 16 em [USACE-HECRAS-2DUM-66 p. 13-14].

**Malha 2D.** O limite do polígono 1D/2D fica em terreno alto [USACE-HECRAS-2DUM-66 p. 51-52]. O tamanho da célula segue a declividade da superfície da água e as barreiras ao fluxo; o manual **não dá tamanho numérico** [USACE-HECRAS-2DUM-66 p. 53, 56, 198-199]. Breaklines em diques, estradas, margens e terreno alto; região de refinamento ao longo do canal e breakline no eixo [USACE-HECRAS-2DUM-66 p. 57-63]. Problemas típicos de malha (mais de 8 lados, centros duplicados, faces colineares) [USACE-HECRAS-2DUM-66 p. 64-69]. **Teste de consistência**: refinar a malha e reduzir o passo juntos; testar ao menos duas resoluções de ΔX e dois ΔT [USACE-HECRAS-2DUM-66 p. 201]. No arquivo, ler a área de célula (mediana, p95, máximo): `hecras_hdf.py malha`.

**Passo de tempo e Courant.** SWE-ELM: alvo C = 1,0, aceitável até 3,0 se o evento varia devagar; difusão: até 5,0; **C ≈ 1,0 em zonas de alta velocidade, onda rápida ou 2D que parte seco** [USACE-HECRAS-2DUM-66 p. 200-201]. O programa calcula o Courant pela velocidade da face e a distância entre os centros das células [USACE-HECRAS-2DUM-66 p. 203-204]; o passo pode ser fixo, por Courant (mínimo menor que metade do máximo) ou por divisor [USACE-HECRAS-2DUM-66 p. 201-205]. No 1D: Δt ≤ Tempo de subida/20 e Courant ótimo 1,0 [USACE-HECRAS-UM-66 p. 314-316]. Parâmetros de plano 2D: θ entre 0,6 e 1,0 (padrão 1,0); tolerância de nível e de volume 0,01 ft; máximo de 20 iterações [USACE-HECRAS-2DUM-66 p. 210-211]. Subir iterações é último recurso.

**Contornos 2D.** Quatro externos: hidrograma de vazão, hidrograma de nível, normal depth e curva-chave; normal depth e curva-chave só para saída; duas condições não dividem a mesma face [USACE-HECRAS-2DUM-66 p. 141-142]. **Normal depth exige declividade de atrito**, que pode vir da declividade do terreno junto ao contorno [USACE-HECRAS-2DUM-66 p. 144-145]; no 1D não permanente a profundidade normal raramente existe e o contorno deve ficar longe do trecho de interesse [USACE-HECRAS-UM-66 p. 251-252]. Regra do especialista: **normal depth só com declividade medida, seção uniforme e sem barragem, soleira ou remanso a jusante**; com estrutura a jusante, usar NA ou curva-chave com carga (caso HR-06). Contorno de jusante ruim é causa conhecida de instabilidade [USACE-HECRAS-UM-66 p. 320].

**Condição inicial.** Padrão seco; opções: nível único, restart, rampa de condição inicial (fração padrão 0,1) [USACE-HECRAS-2DUM-66 p. 187-195]. Um 2D ligado direto a um trecho 1D não parte seco [USACE-HECRAS-2DUM-66 p. 187]. A condição inicial entra no parecer (no caso HR-02 o arquivo partia de 382,4 m contra NA final de 390,8 m e o relatório não dizia).

**Hidrogramas internos** de sub-bacia: cuidado com dupla propagação [USACE-HECRAS-2DUM-66 p. 163-165]. Conferir pico e volume do `.u01` contra a tabela da hidrologia (caso HR-04: 3 de 3 picos iguais à Tab. 8).

## 5. Rugosidade, calibração e sensibilidade

- **n**: tabela de Chow no HRM [USACE-HECRAS-HRM-66 p. 124-126]; o UM tem só n por forma de fundo aluvial [USACE-HECRAS-UM-66 p. 305]; o Mapper traz n por classe NLCD (EUA), válido para profundidade apreciável e **não para escoamento raso nem chuva na malha** [USACE-HECRAS-MAPPER-66 p. 61]. No 2D o n por face usa o centroide; n composto por cota só a partir da v6.4 [USACE-HECRAS-2DUM-66 p. 75]. Mapa de n: camada de cobertura mais regiões de calibração (prioridade da região de calibração sobre o override e sobre a base) [USACE-HECRAS-MAPPER-66 p. 97-99]. **n idêntico entre a seção 1D e a zona 2D conectada**, senão o modelo fica instável [USACE-HECRAS-2DUM-66 p. 94, 97]. n único em todas as células = sinal de que não houve mapa de uso do solo: `hecras_hdf.py malha` avisa.
- **Calibração**: cotas observadas têm incerteza (cota ±1 ft; curva-chave ±5 %) [USACE-HECRAS-UM-66 p. 299-300]; oito passos (permanente contra curva-chave e marcas de cheia; eventos; armazenamento; n para as cotas; fatores vazão-rugosidade; sazonais; verificação em evento não usado; reajuste) [USACE-HECRAS-UM-66 p. 309]; não forçar n irreal [USACE-HECRAS-UM-66 p. 310-311]. Calibração automática de n existe no 1D não permanente e exige série de cotas [USACE-HECRAS-UM-66 p. 725-728]. **Os manuais não dão limite numérico de erro de calibração.**
- **Sensibilidade de n (padrão do especialista: ±20 %)**: a regra de "mais e menos 20 %" está em [USACE-HECRAS-HRM-66 p. 389], escrita para ruptura de barragem (n de canal 0,025 a 0,075, de planície 0,05 a 0,15); o UM pede uma "faixa realista" (exemplo 0,035 com faixa 0,03 a 0,045) [USACE-HECRAS-UM-66 p. 328]. Rodar n -20 %, base, +20 %; relatar a variação de NA no ponto de projeto. Se a variação passar de **0,3 m**, a cota de projeto não vem de um único n (limiar do caso HR-05, premissa de treinamento).
- **Sensibilidade de TR** (2, 5, 10, 25, 50, 100) como análise de incerteza [USACE-HECRAS-UM-66 p. 328]; **sensibilidade numérica** (passo, θ, espaçamento de seções) [USACE-HECRAS-UM-66 p. 327-329].
- **ARF**: entrega do Clima; sem ele em bacia grande o pico fica sem redução (caso HR-05, Recife-SB1 de 932 km²).

## 6. Pontes e bueiros no modelo

- **Ponte (1D)**: quatro seções (1 a jusante, 2 e 3 junto ao pé do aterro, 4 a montante); seção 2 e 3 nunca a "1 ft" da face; coeficientes de contração e expansão por Tab. 3-3 (transição gradual 0,1 e 0,3; ponte típica 0,3 e 0,5; abrupta 0,6 e 0,8) [USACE-HECRAS-HRM-66 p. 131, 173-175, 180]. Baixa vazão: energia, momentum, Yarnell, WSPRO (só subcrítico); alta vazão: pressão e vertedor; escolha do método em [USACE-HECRAS-HRM-66 p. 181-189, 196-198]. Ponte em 2D: abordagem simplificada ou detalhada [USACE-HECRAS-HRM-66 p. 204-208]; **WSPRO não existe para ponte dentro do 2D** [USACE-HECRAS-2DUM-66 p. 110]. Ponte fora do terreno raster [USACE-HECRAS-MAPPER-66 p. 33].
- **Bueiro**: até 25 barris idênticos; quatro seções; controle de entrada e de saída [USACE-HECRAS-HRM-66 p. 210-214, 218-222]; as equações FHWA de entrada têm precisão de cerca de 10 % e os nomogramas foram calculados para declividade de 2 % [USACE-HECRAS-HRM-66 p. 219-220]. **Dimensionar o bueiro segue `bueiros-e-travessias`; dissipador é da Hidráulica (R5).** O HEC-RAS confere a cota de montante; o pós-processador pode dar cota diferente da seção a montante porque o motor usa curvas pré-calculadas [USACE-HECRAS-UM-66 p. 272].
- Coeficientes de contração e expansão: padrão 0,1 e 0,3 no permanente contra 0,0 no não permanente [USACE-HECRAS-UM-66 p. 35, 170]; não confundir ao trocar o tipo de escoamento.

## 7. Estabilidade e erros comuns de cálculo

Causas e remédios: espaçamento de seções (rios íngremes a cerca de 100 ft, rios largos e planos a cerca de 5.000 ft; testar interpolando seções) [USACE-HECRAS-UM-66 p. 312-313]; passo grande demais ou pequeno demais [USACE-HECRAS-HRM-66 p. 384-386]; n subestimado ou mudança abrupta de n [USACE-HECRAS-HRM-66 p. 390]; vertedor lateral com coeficiente alto demais, erro mais comum [USACE-HECRAS-2DUM-66 p. 91-92]; 2D que parte seco ou com contorno alto demais (usar rampa) [USACE-HECRAS-2DUM-66 p. 190-191]; contorno de jusante [USACE-HECRAS-UM-66 p. 320]. Como achar: janela de cálculo, saída em nível computacional, log detalhado [USACE-HECRAS-UM-66 p. 329-335]; sistema de erros, avisos e notas [USACE-HECRAS-UM-66 p. 611-612]. **Balanço de volume**: o log traz o erro de volume do modelo e de cada 2D (exemplo do manual: ganho de 0,02 % "muito baixo") [USACE-HECRAS-2DUM-66 p. 207-208]; o manual não fixa limiar de aceitação.

## 8. Resultados e mapas

Resultados em `.pNN.hdf` por plano (resultados e cópia da geometria) [USACE-HECRAS-UM-66 p. 45]; mapas padrão: profundidade, cota da lâmina, velocidade; tipos adicionais (limite de inundação, Courant, Froude, tensão, tempo de chegada, duração, recessão) [USACE-HECRAS-MAPPER-66 p. 135-137]. **Dinâmico × armazenado**: o dinâmico é interpolado e "não é a resposta exata"; publicar o armazenado e dizer qual foi usado [USACE-HECRAS-MAPPER-66 p. 133-134, 138-139]. Modo de renderização 2D afeta profundidade e volume; o manual dá "Hybrid" como padrão na p. 23 e "Sloping" na p. 152-153: conferir na versão usada [USACE-HECRAS-MAPPER-66 p. 23, 152-153]. Terreno associado à geometria e ao plano é necessário para profundidade [USACE-HECRAS-MAPPER-66 p. 38-39]. Velocidade máxima **de face** não é a velocidade do canal.

## 9. Calculadora: `tools/dren/hecras_hdf.py` (somente leitura)

Não executa o HEC-RAS, não escreve no arquivo, não importa código do arquivo. h5py do venv do squad. Unidades: as do arquivo (atributo `Units System`); não converte. Fórmula → função → teste:

| Pergunta | Função | Teste |
|---|---|---|
| Versão, equação 2D, θ, tolerâncias, passo base e de saída | `plano` | `test_plano_e_passo`, `test_real_plano_contornos_hr03` |
| Malha (área de célula: mediana, média, p95, máx.), n usados, parâmetros de geometria | `malha` | `test_malha_e_n`, `test_real_q95_malha_e_manning` |
| NA e profundidade finais e máximos em células molhadas, velocidade máxima de face, **estabilização** (máx. dNA nas últimas 2 h), erro de volume | `resultados_2d` | `test_resultados_2d_e_estabilizacao`, `test_real_resultados_hr02` |
| Courant estimado por célula (só velocidade, como o programa, e por celeridade) | `courant` | `test_courant_estimado`, `test_courant_difusao_limite_5` |
| Contornos do evento e linhas de contorno; declividade do normal depth | `contornos` | `test_contorno_normal_depth` |
| NA e velocidade máximos por seção (1D) e n por seção | `secoes_1d` | `test_secoes_1d` (fixture sintética) |
| Tudo acima mais `avisos` agregados | `verificar` | `test_avisos_basicos`, `test_cli` |
| Arquivo × relatório (tolerância 5 %) | `comparar` | `test_comparar` |

```bash
python -m tools.dren.hecras_hdf --funcao verificar --arquivo "<...>.p01.hdf" > saida_1.json
python -m tools.dren.hecras_hdf --funcao courant --arquivo "<...>.p01.hdf" --dt_s 5
```

**Avisos que o parecer reproduz**: n único; normal depth (com a declividade em %); estabilização não demonstrada (dNA > 0,01 m em 2 h); velocidade de face isolada (máximo contra p95); Courant acima de 3,0 (SWE) ou 5,0 (difusão); equação = difusão; célula máxima ≫ mediana. **Limites**: (a) o Courant é estimativa com dX = raiz da área da célula, não o número do programa; (b) o layout 1D (secoes) foi verificado só com fixture sintética, pois a TPF não entregou 1D; (c) erro de volume é lido, sem limiar; (d) arquivos de entrada (`.g`, `.u`, `.p`) em texto não são lidos pela calculadora: ler com Read quando precisar (ex.: `Friction Slope`, `Initial Storage Elev`). Reprodução dos casos: malha, n, estabilização e velocidade do HR-02 dentro de 5 % (`test_real_*`, rodam se houver a cópia local dos `.hdf` de 24-27 MB; o repositório guarda só a fixture sintética). Layout dos grupos HDF: `references/hecras-hdf-layout.md`.

## 10. Critérios de aceitação de modelo (checklist do parecer)

Origem: os 6 casos TPF (`casos/hec-ras/`; nenhum número com ✓h). Resultado sem cumprir os itens 1 a 7 sai como **"indicativo de mancha"**, nunca como cota de projeto.

1. **Versão, unidades, projeção e datum** declarados (`plano`).
2. **Terreno**: fonte, resolução, data; batimetria no canal.
3. **n**: valor, fonte e mapa (um único n em planície e canal exige justificativa; HR-05 e HR-03).
4. **Malha**: mediana, p95 e máximo da célula; breaklines na calha e em obras; **duas resoluções** (HR-05: malha de 50 m em calha estreita sem teste).
5. **Contornos com fonte**: normal depth só com declividade medida e conferida entre texto e arquivo (HR-03: 0,01 % no texto contra 0,0093 % no arquivo); jusante **sem soleira sem carga** (HR-06).
6. **Condição inicial e duração** declaradas; **estabilização** dNA ≤ 0,01 m em 2 h nas células de interesse, ou justificada (HR-02: 0,0005 m no Q95; 0,040 m em 10 células no QTR100, nota obrigatória).
7. **Entradas conferidas contra a hidrologia**: pico, volume, TR único (HR-04: picos do `.u01` iguais à Tab. 8; HR-06: TR 100 contra TR 50 e Q 3.417 contra 4.012 m³/s sem explicação).
8. **Calibração ou verificação** contra dado observado; sem dado, registrar "NA sem calibração, incerteza não quantificada" (HR-03).
9. **Sensibilidade de n (±20 %) e de TR**; variação de NA no ponto de projeto < 0,3 m ou cota por faixa.
10. **Courant** estimado e passo; balanço de volume do log.
11. **Discrepância texto × arquivo** listada.
12. **Seções reais** nas travessias 1D; seção sintética (HR-06: trapézio 18H:1V) só como preliminar.
13. Nenhuma cota de projeto de um único n sem calibração; NA sempre com **ponto, TR e incerteza** (HR-01: o NA da malha varia 0,3 a 0,8 m; "NA = x" sem lugar não se cita).

**O que os 3 casos negativos ensinam**: HR-03 (contorno de jusante sem calibração, declividade texto × arquivo, n sem sensibilidade); HR-05 (malha grossa, n único, sem ARF, jusante sem descrição, pico de 589,69 m³/s sem origem); HR-06 (TR 100 × 50, vazão do cálculo não declarada, contorno na soleira, seção sintética, sem arquivo para reprodução; NA 397 m = "preliminar de aqueduto").

## 11. Nível de projeto e entregáveis

- **Anteprojeto**: modelo conferido, mancha "indicativa", sensibilidade de n declarada, lista de premissas sem dado.
- **Projeto básico**: acrescenta calibração ou verificação, duas malhas, sensibilidade de n e de TR, hidrogramas conferidos, cota de projeto por faixa.
- **Consultoria**: modelagem nova, calibração com campanha, dam break, sedimentos (fora da skill; dizer o que ela entrega).
- **Parecer replicável**: arquivos `.prj/.g/.p/.u` e versão; resumo de entradas; tabela de NA e velocidade por cenário **e local**; mapas com escala e limiar de lâmina; premissas sem dado; sensibilidade; o que falta; `saida_<n>.json` e `comando.txt` de `hecras_hdf.py`.

## 12. Armadilhas

Padrão = difusão (rodar a SWE e comparar); Courant só de velocidade; velocidade máxima de face lida como velocidade do rio; n do Mapper (NLCD) usado em escoamento raso; mapa dinâmico publicado como definitivo; normal depth com declividade do texto diferente da do arquivo; jusante na soleira; TR do relatório diferente do TR do modelo; Q de entrada diferente da tabela de hidrologia; ARF esquecido; coeficientes de contração e expansão de ponte copiados do permanente para o não permanente; n diferente entre seção 1D e zona 2D; cota de montante do pós-processador diferente da seção; `±20 %` atribuído ao UM (está no HRM p. 389).

## 13. Lacunas do corpus

Sem tamanho de célula nem passo numéricos para chuva na malha; sem limiar de erro de volume nem de estabilização; sem critério de aceitação de calibração; sem tabela de n da Caatinga ou de planície brasileira (só Chow no HRM e NLCD no Mapper); sem tratamento de datum vertical e terreno brasileiros (ANADEM, LIDAR); sem catálogo das mensagens de erro; formato interno do HDF não descrito nos manuais; Applications Guide e HDS-7/HEC-18 (pontes, erosão) sem URL verificada. Tabelas 6-3 a 6-6 de bueiro e apêndice WSPRO só localizadas (`MAPA_DE_CONHECIMENTO.md`, G5).
