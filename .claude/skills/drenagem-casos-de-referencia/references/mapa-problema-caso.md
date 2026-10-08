# Mapa problema -> caso (drenagem)

Marca: todos sem `✓h`. "Qual." = qualidade do rastro (A reproduzível, B inferido, C descritivo). Primeiro abrir
`casos/drenagem/_INDICE.md`; depois o caso; depois a skill da disciplina para o método.

| Problema | Caso com o que dá | Qual. | O que **falta** |
|---|---|---|---|
| Tc por Kirpich + tempo de viagem, racional de lote | `delmiro_gouveia_drenos_lotes_racional_manning` (C 0,15, IDF TR 10) | A | IDF é de outro autor (Clima) |
| Tc rotulado, NERC x Kirpich | `delmiro_gouveia_tc_rotulos_velocidade_declividade` | A (neg.) | fonte primária do NERC no corpus |
| Racional abaixo de 3,5 km² + HUT acima | `cac_trecho1_hidrologia_racional_3_5km2_e_hut` | B | fórmula de Tc modificada ilegível em parte |
| Racional abaixo de 2 km² / HU por unidade | `xingo_lote1_drenagem_transversal_bueiros` | B | colunas Hw/D do Quadro 3.39 incertas |
| Limite do racional (50, 100, 350 ha, 2 km², 3,5 km²) | Baixio (≤ 100 ha), Xingó (2 km²), CAC (3,5 km²), Iuiu 2018 (faixas por área) | A/B | critério normativo: F7 |
| HUT/SCS: CN, Tc, perdas, convolução | `delmiro_gouveia_hut_bhd1_tr50_bransby_williams` (Q 58,71 m³/s; pico não reproduz: +5,3 %) | A | hietograma por polinômio cúbico |
| HUT/SCS: geometria do HU | `baixio_irece_vazoes_hut_scs` (tlag 0,578 h; tp 0,658 h; tb 1,758 h) | B | tabela T-K do hietograma; pico 6,03 x 2,70 |
| Bueiro celular por Manning | `salitre_rc500_800_bueiros_celulares` (BTCC1, 3 %) | A | HW/D pelo HDS-5 não calculado no projeto |
| Bueiro tubular parcialmente cheio y/D | `jaiba_etapas3e4_bueiros_greide_manning_y_d_082`; `delmiro_gouveia_bueiros_tubulares_sob_canal_principal` (8 casos a 1 %) | A; B | n do bueiro não declarado em Jaíba; S e L divergentes em Delmiro |
| Capacidade livre + verificação por orifício | `baixio_irece_bueiros_dimensionamento` (TR 25 e 50, C 0,62) | A | contração de entrada (HDS-5) |
| Bueiro por equação da energia, supercrítico | `xingo_lote1_drenagem_transversal_bueiros` | B | dissipação: Hidráulica (D3) |
| Bueiro afogado, controle na saída | `jaiba_etapas3e4_sifao_bueiro_afogado_controle_saida` | B | Q 2,44 x 2 x 1,27 |
| Muitos bueiros sob canal por faixa de área | `iuiu_2018_bueiros_sob_canal_91_obras` | B/C | declividade e comprimento de cada bueiro |
| Quadro de bueiros e consistência de cotas | `cac_trecho1_bueiros_sob_canal_adutor_cota_inconsistente` | C (neg.) | Q e HW (estudo HARZA 2001) |
| Valeta de crista/pé, comprimento crítico | `xingo_lote1_valetas_protecao_comprimento_critico` | A | z = 1 deduzido; IDF por trecho |
| Valas de estrada, racional | `cac_castanhao_estrada_acesso_valas_chuva_como_intensidade` | B (neg.) | fórmula da planilha não impressa |
| Macrodreno trapezoidal Manning n 0,030 | `salitre_etapa2_macrodrenos_trapezoidais_manning` | A | |
| Reconciliar extensões e limites de V | `salitre_etapa2_macrodrenagem_inconsistencias_memorial` | B (neg.) | conferência humana de N4 e N5 |
| Drenos laterais ao adutor, seções-padrão | `sertao_pernambucano_canais_drenagem_laterais_adutor` | B | Q e declividade por trecho |
| Folga e seção do dreno | `delmiro_gouveia_drenos_secao_subdimensionada_folga` | B (neg.) | critério de V mínima não informado |
| Dreno de fundo por vazão por metro | `csb_geohidro_dreno_fundo_canal_subsuperficial` (q 6e-5) | B | capacidade dos tubos sem ancoragem |
| Dreno de fundo por Darcy | `delmiro_gouveia_dreno_fundo_canal_comprimento_maximo` (qd 3,91e-7; Lmáx 388 e 1.260 m) | B (neg.) | S e n do tubo |
| Vazão por furo em geomembrana | `xingo_lote1_drenagem_interna_canal_subsuperficial` (Cd 0,634; 1/2400 m²) | A | |
| Drenabilidade, Porchet, não drenar | `iuiu_2002_drenabilidade_subterranea_diagnostico` | B | sem dimensionamento de drenos |
| Canal em gabião x tubo, grade de n | `retroanalise_canal_gabiao_vs_tubo_manning` (1,0784 e 1,7591 m³/s) | B | lâminas diferentes dos dois lados |
| Dreno agrícola (Hooghoudt, Ernst, Glover-Dumm) | **sem caso** | , | só livro: ILRI-DPA16, USBR, Embrapa |
| Sarjeta, descida d'água, caixa coletora | **sem caso** | , | memória de cálculo de projeto |
| Drenagem urbana em rede | **fora do escopo** (D: não coberto) | , | , |
