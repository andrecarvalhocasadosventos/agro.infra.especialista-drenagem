# Índice — casos reais de drenagem, bueiros, vertedouros e dissipadores (acervo Projetos de Referência)
Qualidade do rastro: A = número com doc:pág e reproduzido por cálculo independente; B = rastro bom mas com coluna/fórmula/coeficiente inferido ou ilegível; C = descritivo, sem memória numérica.
Páginas = página do catálogo (PDF). Duplicatas: 1372 = 1341; 1433 = 1401; 1451 = 1419; 1378 = 1346 (mesmo arquivo em outra pasta).

| slug | projeto | o que resolve | qualidade |
|---|---|---|---|
| csb_geohidro_drenagem_pluvial_bueiros | CSB GEOHIDRO 2016 (doc 1341) | Racional/HUT-SCS TR 100, Kirpich, Cd, IDF Plúvio por grupo, bueiros celulares Manning n=0,015, bacias de entrada | B (V/Yo da Tab 4.7 não reproduzem) |
| csb_geohidro_dreno_fundo_canal_subsuperficial | CSB GEOHIDRO 2016 (doc 1341 pp.74-77) | Dreno de fundo/subpressão: q=6e-5 m³/s/m, tubos 2DN150-2DN500, MVF 30 % | B (capacidades dos tubos sem ancoragem) |
| baixio_irece_bueiros_dimensionamento | Baixio de Irecê PB 2008 (docs 896, 897, 670) | 39 bueiros: capacidade livre TR 25 + verificação orifício TR 50 (C=0,62), critérios do memorial | A |
| baixio_irece_vazoes_hut_scs | Baixio de Irecê PB (docs 898-903, 670) | Hidrograma SCS por obra (CN, Tc DNOS, TR 25/50); Racional ≤100 ha | B (fórmula Tc e IDF ilegíveis; sem racional.py) |
| salitre_rc500_800_extravasores_laterais | CSB Salitre RC500-800 (docs 1357, 1368) | Vertedores de soleira espessa por HEC-RAS (Q 24-32 m³/s, L 40-105 m), câmara de dissipação | B (C inferido ≈1,53) |
| salitre_rc500_800_bueiros_celulares | CSB Salitre RC500-800 (doc 1357) | Bueiros celulares TR 100, Manning; BTCC1 reproduz | A |
| iuiu_2002_drenagem_superficial_drenos_bueiros | Vale do Iuiu 2002 (doc 1051) | Racional/McMath/CN, drenos Manning n=0,03 v≤0,8, bueiros TR 25/50, queda com bacia L=6(D2−Dq) | A |
| iuiu_2002_extravasores_controle_dissipador_eb1 | Vale do Iuiu 2002 (docs 1051, 1052, 1076) | Extravasor laterais Hmed=(Q/1,84L)^(2/3), dissipador EB1/AP1 | A (vertedor) / C (dissipador sem critério) |
| iuiu_2002_drenabilidade_subterranea_diagnostico | Vale do Iuiu 2002 (docs 1051, 1066) | Porchet K, classes de drenabilidade, decisão de não drenar | B (sem dimensionamento de drenos) |
| xingo_lote1_drenagem_interna_canal_subsuperficial | Xingó Lote I (doc 1419) | Vazão por furo na geomembrana (Cd=0,634, 1/2400 m²), tubo PEAD Q=33,5D^2,67 i^0,5 | A |
| xingo_lote1_drenagem_transversal_bueiros | Xingó Lote I (docs 1419, 1401) | Hidrologia (Racional <2 km²/HU), bueiros por equação da energia, K=0,5, supercrítico + dissipação | B (colunas Hw/D, H do Quadro 3.39 incertas) |
| xingo_lote1_extravasores_bypass_descargas_fundo | Xingó Lote I (doc 1419) | Vertedor C=1,83, soleira NAE+0,1, descarga de fundo Cd=0,61 | B (L e Qext não explicados) |
| jaiba_etapas3e4_extravasores_e_canal_em_degraus | Jaíba Etapas 3-4 (doc 1182) | 24 extravasores (C≈1,60, h=0,15) e escada de dissipação (Dn, Ld, y1, y2, L) | A |
| jaiba_etapas3e4_sifao_bueiro_afogado_controle_saida | Jaíba Etapas 3-4 (doc 1182) | Sifão como bueiro afogado com controle na saída, perdas DNIT/FHWA | B (Q 2,44 vs 2×1,27) |
| rookwood_weir_vertedor_ogee_e_descarga_ambiental_58m3s | Rookwood Weir (doc 1458) | Configuração de ogee de 209 m e outlet ambiental 58 m³/s com bacia USBR | C (sem memória de cálculo) |

Pulados / fora de alcance: 1372, 1433, 1451, 1378 (duplicatas); 1457 (hidráulica do EIS Rookwood, não lido); documentos de Baixio de Irecê 898-901 e 903 foram usados só como amostra (ver vazões). Nenhum documento-alvo ficou sem texto (pendente_ocr). As planilhas .xls (896-903) exibem ERRO xlrd na ficha mas têm texto de planilha utilizável.
