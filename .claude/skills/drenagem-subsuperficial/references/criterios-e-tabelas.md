# Critérios de projeto e tabelas paginadas (lençol, descarga, K, μ, velocidades)

Faixas largas por natureza: o próprio ILRI-56 as chama de "muito, muito amplas" e manda conferir a experiência local
[ILRI-56 p. 42]. Servem para **calibrar** e para rotular premissa; nunca substituem K medido e recarga da Irrigação.

## 1. Descarga de projeto q (mm/d; 1 mm/d = 0,116 L/s/ha; 1 L/s/ha = 8,64 mm/d)

| Condição | q | Fonte |
|---|---|---|
| Clima úmido | 7 a 14 mm/d | [ILRI-56 p. 42] |
| Clima moderado | 4 a 7 mm/d | [ILRI-56 p. 42] |
| Irrigado com alguma chuva | 2 a 4 mm/d | [ILRI-56 p. 42] |
| Irrigado árido | 1 a 2 mm/d | [ILRI-56 p. 42; FAO-IDP62 p. 114, Tab. 8] |
| Úmido temperado 7 a 15; úmido tropical 10 a 15 | mm/d | [FAO-IDP62 p. 114, Tab. 8] |
| Árido: lixiviação | 2 a 4 mm/d bastam | [FAO-IDP62 p. 113] |
| Brasil, FAO 1980: solos pesados < 1,5; maioria 1,5 a 3,0; extremos 3,0 a 4,5; > 4,5 só arroz em solo leve | mm/d | [EMBRAPA-DREN-SUBT p. 13, Tab. 2] |
| Exemplos de projeto brasileiros | Maniçoba 8 mm/d; Bebedouro 3,6 mm/d médio (13,6 de pico) | [EMBRAPA-MANICOBA-1988 p. 3; EMBRAPA-BEBEDOURO-1986 p. 5 (número degradado)] |
| Rebaixamento entre duas regas mensais | 40 mm × μ 5 % → 0,8 m; 30 d → 1,3 mm/d | [FAO-IDP62 p. 114, Fig. 35] |

Chuva: Embrapa manda tomar a chuva extrema de TR 2 a 5 anos, descontar escoamento, evaporação e retenção, e chegar à
percolação líquida [EMBRAPA-DREN-SUBT p. 13]; FAO-62 usa TR 2 a 5 anos para clima úmido [FAO-IDP62 p. 112]. A chuva
vem do Clima; q de irrigação vem da Irrigação.

## 2. Lençol de projeto e profundidade do dreno

| Situação | Lençol (meio do vão) | Dreno | Fonte |
|---|---|---|---|
| Culturas de raiz rasa, úmido | 0,5 m | 0,7 a 1 m | [ILRI-56 p. 42] |
| Grãos, úmido | 0,7 m | ~1 m | [ILRI-56 p. 42] |
| Alimentos irrigados, sem sal | 0,9 m | 1,2 a 1,5 m | [ILRI-56 p. 42] |
| Árido irrigado, risco de sal | 0,9 a 1,5 m | 1,2 a 3 m | [ILRI-56 p. 42] |
| Culturas anuais irrigadas | 0,8 a 0,9 m | | [FAO-IDP62 p. 113] |
| Fruteiras irrigadas | 1,0 a 1,2 m | | [FAO-IDP62 p. 113] |
| Anuais / hortícolas / árvores (textura grossa × fina) | 1,0 × 1,2 / 1,0 × 1,1 / 1,2 × 1,6 m | dreno ~0,5 m mais fundo | [EMBRAPA-DREN-SUBT p. 12-13, Tab. 1] |
| Grama e culturas de campo, clima de chuva leve | 0,3 a 0,5 m para q 7 a 10 mm/d | | [FAO-IDP62 p. 113] |

Rebaixamento transitório (hortícolas 0,30 m em 4 a 6 h; culturas em clima quente 0,30 m em 1 dia; clima frio 0,20 m em
1 dia) [FAO-IDP62 p. 114]. Salinidade e sobreposição de dois lençóis (safra × pousio) são da Irrigação [FAO-IDP62 p. 113].

Escolha de profundidade não é só agronômica: dreno mais fundo reduz espaçamento mas pode exigir DN maior, coletor mais
fundo e bombeamento; no exemplo do Egito, dreno a 1,60 m (20 cm mais raso que 1,80 m) exigiu 50 m em vez de 80 m e custou cerca de 60 % mais [FAO-IDP62 p. 111].

## 3. K por textura (ILRI-56 Tab. 14, p. 175; `faixa_K_por_textura`)

| Textura | K (m/d) |
|---|---|
| Brita / cascalho natural | 1.500 a 3.500 / 100 a 1.500 |
| Areia com cascalho | 5 a 100 |
| Areia grossa cascalhenta | 10 a 50 |
| Areia média | 1 a 5 |
| Franco-arenoso, areia fina | 1 a 3 |
| Franco-argila bem estruturada | 0,5 a 2 |
| Franco-arenoso muito fino | 0,2 a 0,5 |
| Argila mal estruturada | 0,002 a 0,2 |
| Argila densa | 0 a 0,002 |

Projeto: **média geométrica** dos K medidos [ILRI-56 p. 43]; ensaio de furo de trado: Embrapa Anexo 1 (K = C Δh/Δt;
exemplo K 0,84 m/d) [EMBRAPA-DREN-SUBT p. 30-34]; Porchet no Iuiu (constante 423, 500 testes; fórmula em imagem,
conferir) [Iuiu doc 1066:23-24]. Faixa de três ordens de grandeza = a premissa mais perigosa do parecer: mostrar L em K
mínimo, médio e máximo da faixa. K varia mais que q (Iuiu: 0,4 a 2,1 m/d; Delmiro: o projetista cita ± uma ordem).

## 4. Porosidade drenável μ

Tabela paginada [EMBRAPA-DREN-SUBT p. 14, Tab. 3, FAO 1980]: argila, franco-argilo-siltoso, franco-argilo-arenoso 0,01 a
0,03; franco-argiloso, franco-siltoso, silte 0,03 a 0,08; franco, franco-arenoso muito fino 0,08 a 0,12; franco-arenoso,
areia franca, areia fina 0,12 a 0,22; areia média e grossa, cascalho 0,22 a 0,35. ILRI-DPA16 (glossário, PDF 44): "< 5 %
(argila) a 35 % (areia grossa e com cascalho)"; μ depende da profundidade do freático (cap. 3 e 11.3.5; Ex. 11.1: 0,04).
**A tabela `porosidade_drenavel` da calculadora (`POROSIDADE_DRENAVEL`) tem outras faixas (ex.: areia 0,15 a 0,30; argila
0,01 a 0,05) e nenhuma página**: usar a Tab. 3 da Embrapa no parecer e registrar a diferença. Maniçoba mediu μ de 7,8 % e
24 % (areia) [EMBRAPA-MANICOBA-1988 p. 1].

## 5. Grades e velocidades do tubo (conversão SI)

| Item | Valor | Fonte |
|---|---|---|
| Velocidade não assoreante | ~1,4 ft/s = 0,43 m/s | [NRCS-NEH624-CH04 p. 87] |
| Máxima por solo ao redor | areia e franco-arenoso 3,5 ft/s (1,07 m/s); silte 5,0 (1,52); franco-argilo-siltoso 6,0 (1,83); argila 7,0 (2,13); areia grossa/cascalho 9,0 (2,74) | [NRCS-NEH624-CH04 p. 88] |
| Declividade usual do dreno de campo | 0,02 a 1,0 % | [EMBRAPA-DREN-SUBT p. 17] |
| n | 0,011 (cerâmica/concreto, junta boa) a 0,016 (PEAD corrugado) | [NRCS-NEH624-CH04 p. 88] |
| Espessura mínima do envoltório | 3 pol = 7,6 cm (NEH); seixo ≥ 5 cm (Embrapa) | [NRCS-NEH624-CH04 p. 87; EMBRAPA-DREN-SUBT p. 22] |
| Linha de dreno | < 300 m (limpeza e manutenção) | [EMBRAPA-DREN-SUBT p. 20] |
| Chegada no coletor | ≥ 10 cm acima do espelho de água | [EMBRAPA-DREN-SUBT p. 20] |

## 6. O que as tabelas sem página fazem na calculadora

`recomendacao_indicativa(K)` (profundidade e espaçamento por classe de K) e `porosidade_drenavel` são ordens de grandeza
sem página (FAO-38 fora do corpus). Podem orientar uma pergunta ao usuário; **não entram em parecer como dado**. Os
valores paginados são os de `faixa_K_por_textura` e `coeficiente_drenagem_tipico` (ILRI-56).

## 7. Referências da skill (IDs e páginas-chave; movido do SKILL.md na revisão F7)

- ILRI-DPA16 (Hidráulico): Hooghoudt Eq. 8.3-8.7 p. 264-266; Tab. 8.1 p. 267; d série Eq. 8.9-8.14 p. 268; Ernst
  Eq. 8.17-8.21 p. 270-272, Tab. 8.2 p. 272, Ex. 8.1-8.4 p. 276-281; Glover-Dumm Eq. 8.28-8.33 p. 283-284.
- USBR-DRAINAGE (PDF = impr. + 19): d_e de Moody p. 173-174; exemplo transitório p. 187; Donnan p. 188-190; tubo e
  envoltório p. 231-256 (mapa H15; página exata a confirmar).
- NRCS-NEH624-CH04: elipse Eq. 4-8 p. 63-66; grades e velocidades p. 87-88; dimensionamento de linha p. 93; filtros
  p. 96-102.
- FAO-IDP62: critérios p. 111-114; Anexo 20 (tubos) p. 211-217; Anexo 17 (fórmulas) p. 193-200.
- ILRI-56-ENVELOPE (próprio): p. 42-47, 66-68, 175 (PDF = impr. + 20).
- EMBRAPA-DREN-SUBT p. 12-18, 20; EMBRAPA-MANICOBA-1988 p. 1-3, 7-8; EMBRAPA-ESPACAMENTO-1990 p. 5-10;
  EMBRAPA-BEBEDOURO-1986 (números degradados, só localização); WATERLOG-ENDRAIN p. 7-10; DNIT-DREN p. 252-253.
- Casos: `csb_geohidro_dreno_fundo_canal_subsuperficial`, `xingo_lote1_drenagem_interna_canal_subsuperficial`,
  `iuiu_2002_drenabilidade_subterranea_diagnostico`, `2026-10-08_delmiro_gouveia_dreno_fundo_canal_comprimento_maximo`.
  Nenhum número tem `✓h`.
- Divergências: `tools/dren/DIVERGENCIAS.md`, seção "drenos".
