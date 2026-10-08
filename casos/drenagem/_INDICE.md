# Índice — casos reais do Especialista Drenagem

Qualidade do rastro: A = número com doc:pág reproduzível; B = rastro bom com coeficiente/coluna inferido; C = descritivo. Nenhum número dos casos de 2026-10-08 tem ✓h: gabaritos são candidatos até conferência humana (F7).

## Casos herdados (2026-10-02, separação do Hidráulico)

| slug | projeto | o que resolve | qualidade |
|---|---|---|---|
| csb_geohidro_drenagem_pluvial_bueiros | CSB GEOHIDRO 2016 (doc 1341) | Racional/HUT-SCS TR 100, Kirpich, Cd, IDF Plúvio por grupo, bueiros celulares Manning n=0,015, bacias de entrada | B (V/Yo da Tab 4.7 não reproduzem) |
| csb_geohidro_dreno_fundo_canal_subsuperficial | CSB GEOHIDRO 2016 (doc 1341 pp.74-77) | Dreno de fundo/subpressão: q=6e-5 m³/s/m, tubos 2DN150-2DN500, MVF 30 % | B (capacidades dos tubos sem ancoragem) |
| baixio_irece_bueiros_dimensionamento | Baixio de Irecê PB 2008 (docs 896, 897, 670) | 39 bueiros: capacidade livre TR 25 + verificação orifício TR 50 (C=0,62), critérios do memorial | A |
| baixio_irece_vazoes_hut_scs | Baixio de Irecê PB (docs 898-903, 670) | Hidrograma SCS por obra (CN, Tc DNOS, TR 25/50); Racional ≤100 ha | B (fórmula Tc e IDF ilegíveis; sem racional.py) |
| salitre_rc500_800_bueiros_celulares | CSB Salitre RC500-800 (doc 1357) | Bueiros celulares TR 100, Manning; BTCC1 reproduz | A |
| iuiu_2002_drenagem_superficial_drenos_bueiros | Vale do Iuiu 2002 (doc 1051) | Racional/McMath/CN, drenos Manning n=0,03 v≤0,8, bueiros TR 25/50, queda com bacia L=6(D2−Dq) | A |
| iuiu_2002_drenabilidade_subterranea_diagnostico | Vale do Iuiu 2002 (docs 1051, 1066) | Porchet K, classes de drenabilidade, decisão de não drenar | B (sem dimensionamento de drenos) |
| xingo_lote1_drenagem_interna_canal_subsuperficial | Xingó Lote I (doc 1419) | Vazão por furo na geomembrana (Cd=0,634, 1/2400 m²), tubo PEAD Q=33,5D^2,67 i^0,5 | A |
| xingo_lote1_drenagem_transversal_bueiros | Xingó Lote I (docs 1419, 1401) | Hidrologia (Racional <2 km²/HU), bueiros por equação da energia, K=0,5, supercrítico + dissipação | B (colunas Hw/D, H do Quadro 3.39 incertas) |
| jaiba_etapas3e4_sifao_bueiro_afogado_controle_saida | Jaíba Etapas 3-4 (doc 1182) | Sifão como bueiro afogado com controle na saída, perdas DNIT/FHWA | B (Q 2,44 vs 2×1,27) |

## Casos F4 (2026-10-08) — arquivos com prefixo `2026-10-08_`

| slug | projeto (doc) | o que resolve | qualidade | tipo |
|---|---|---|---|---|
| salitre_etapa2_macrodrenos_trapezoidais_manning | Salitre Etapa 2 (docs 1584, 1585) | Macrodrenos trapezoidais Manning n=0,030, V 0,3–1,2, degraus e deságues, planilha por trecho | A | positivo |
| salitre_etapa2_macrodrenagem_inconsistencias_memorial | Salitre Etapa 2 (docs 1584, 1585) | Extensão total que não fecha, dois limites de velocidade, talvegue implausível, somas de ACP | B | negativo |
| delmiro_gouveia_drenos_lotes_racional_manning | Delmiro Gouveia (docs 1520, 1521) | Drenos de lote: racional C=0,15, IDF TR 10, Tc Kirpich + viagem, Manning n=0,025, seções ZTT | A | positivo |
| delmiro_gouveia_drenos_secao_subdimensionada_folga | Delmiro Gouveia (docs 1521, 1520) | Seção ZTT01 menor que o tirante (DT-2.23.1), folga < 25 % em 43 % dos trechos | B | negativo |
| sertao_pernambucano_canais_drenagem_laterais_adutor | Canal do Sertão Pernambucano (doc 1390) | 204 drenos laterais ao adutor, TR 100, 13 seções-padrão, afastamento 6 m | B | positivo |
| retroanalise_canal_gabiao_vs_tubo_manning | RETROANÁLISE CANAL GABIÃO.xlsx (fonte local D8) | Canal retangular em gabião × tubo DN1000 por Manning, grade de n | B | positivo |
| xingo_lote1_valetas_protecao_comprimento_critico | Xingó Lote I (doc 1419) | Comprimento crítico de valeta de crista/pé, Manning × racional por metro, TR 10 | A | positivo |
| cac_castanhao_estrada_acesso_valas_chuva_como_intensidade | CAC Castanhão (doc 1128) | Racional de valas da estrada de acesso; P (mm) usada como mm/h, vazão 12× menor | B | negativo |
| cac_trecho1_hidrologia_racional_3_5km2_e_hut | CAC Trecho 1 (doc 1139) | Racional < 3,5 km², HUT acima, C 0,20→0,40, CN 65→85, Kirpich modificada | B | positivo |
| delmiro_gouveia_hut_bhd1_tr50_bransby_williams | Delmiro Gouveia (docs 1494, 1492) | HUT BHD1 TR 50: Bransby-Williams, perdas SCS, convolução, Q=58,71 m³/s | A | positivo |
| delmiro_gouveia_tc_rotulos_velocidade_declividade | Delmiro Gouveia (docs 1494, 1492) | NERC rotulado Kirpich, km/h sob m/s, declividade BH4.5 0,0618 × 0,0043 | A | negativo |
| jaiba_etapas3e4_bueiros_greide_manning_y_d_082 | Jaíba Etapas 3-4 (doc 1182) | 23 bueiros BSTC 0,80 por Manning, Y/D ≤ 0,82, n implícito 0,013 × 0,015 | A | positivo |
| delmiro_gouveia_bueiros_tubulares_sob_canal_principal | Delmiro Gouveia 2016 (docs 1493, 1492, 1515) | Racional TR20/50, Manning parcialmente cheio y/D ≤ 75 %, 4 BUC sob canal | B | positivo |
| iuiu_2018_bueiros_sob_canal_91_obras | Vale do Iuiu 2018 (doc 1069) | 91 bueiros sob canal, RAC/MOD/HUT por faixa de área, TR 25, n 0,0165 | B/C | positivo |
| delmiro_gouveia_dreno_fundo_canal_comprimento_maximo | Delmiro Gouveia 2016 (doc 1492) | Dreno de fundo: Darcy qd, PEAD DN170/230, Lmáx; capacidade do tubo não reproduz por Manning | B | negativo |
| cac_trecho1_bueiros_sob_canal_adutor_cota_inconsistente | CAC Trecho 1 (doc 1131) | Quadro de 59 bueiros; cota do rasto de B31 incoerente (teste de monotonia) | C | negativo |

Sem caso: dreno agrícola com Hooghoudt/Ernst/Glover-Dumm calculado (nenhum projeto lido o faz); sarjeta e descida
d'água com memória de cálculo; documento específico dos CDV D-56/D-85.
