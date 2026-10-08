# Catálogo dos projetos com caso de drenagem

Fonte: `casos/drenagem/_INDICE.md`. Qualidade A reproduzível, B coeficiente ou coluna inferido, C descritivo. **Nenhum
número tem `✓h`**: tudo é "valor do projeto, não conferido". Arquivos dos casos de 2026-10-08 levam o prefixo
`2026-10-08_`. Documentos citados pelo número do acervo (`consultar.py doc <n>`).

| Projeto (docs) | Nível | O que resolve | Casos | Qual. |
|---|---|---|---|---|
| **Baixio de Irecê PB 2008** (896, 897, 898-903, 670) | projeto básico/executivo | 39 bueiros: capacidade livre TR 25 + verificação por orifício TR 50 (C = 0,62); HUT/SCS por obra (CN, Tc DNOS), Racional ≤ 100 ha | `baixio_irece_bueiros_dimensionamento`; `baixio_irece_vazoes_hut_scs` | A; B |
| **CSB GEOHIDRO 2016** (1341) | projeto | Racional/HUT TR 100, Kirpich, IDF Plúvio por grupo, bueiros celulares n = 0,015, bacias de entrada; dreno de fundo q = 6e-5 m³/s/m | `csb_geohidro_drenagem_pluvial_bueiros`; `csb_geohidro_dreno_fundo_canal_subsuperficial` | B; B |
| **CSB Salitre RC500-800** (1357) | projeto | Bueiros celulares TR 100 por Manning; BTCC1 reproduz | `salitre_rc500_800_bueiros_celulares` | A |
| **Salitre Etapa 2, CODEVASF 2014** (1584, 1585) | executivo | Macrodrenos trapezoidais n = 0,030, V 0,3 a 1,2, degraus e deságues; inconsistências do memorial | `salitre_etapa2_macrodrenos_trapezoidais_manning`; `salitre_etapa2_macrodrenagem_inconsistencias_memorial` | A; B (neg.) |
| **Vale do Iuiu 2002** (1051, 1066) | projeto | Racional/McMath/CN, drenos n = 0,03 v ≤ 0,8, bueiros TR 25 (estrada) e 50 (canal), queda com bacia; Porchet e decisão de não drenar | `iuiu_2002_drenagem_superficial_drenos_bueiros`; `iuiu_2002_drenabilidade_subterranea_diagnostico` | A; B |
| **Vale do Iuiu 2018** (1069) | projeto | 91 bueiros sob canal (65 tubulares, 26 celulares), método RAC/MOD/HUT por faixa de área, TR 25, n 0,0165 | `iuiu_2018_bueiros_sob_canal_91_obras` | B/C |
| **Jaíba Etapas 3-4** (1182) | projeto | 23 bueiros BSTC 0,80 por Manning, Y/D ≤ 0,82; sifão como bueiro afogado com controle de saída | `jaiba_etapas3e4_bueiros_greide_manning_y_d_082`; `jaiba_etapas3e4_sifao_bueiro_afogado_controle_saida` | A; B |
| **Xingó Lote I** (1419, 1401) | projeto | Bueiros por equação da energia, K = 0,5, supercrítico; valetas de proteção TR 10 (comprimento crítico); tubo PEAD de dreno interno | `xingo_lote1_drenagem_transversal_bueiros`; `xingo_lote1_valetas_protecao_comprimento_critico`; `xingo_lote1_drenagem_interna_canal_subsuperficial` | B; A; A |
| **Delmiro Gouveia, CODEVASF 2016** (1492 = 1520, 1493 = 1521, 1494, 1515) | executivo | Drenos de lote (racional C = 0,15, TR 10, n = 0,025); HUT BHD1 TR 50 (Q = 58,71 m³/s); bueiros sob canal TR 20/50, y/D ≤ 75 %; dreno de fundo Darcy; rótulos e seção | `delmiro_gouveia_drenos_lotes_racional_manning`; `..._hut_bhd1_tr50_bransby_williams`; `..._bueiros_tubulares_sob_canal_principal`; `..._dreno_fundo_canal_comprimento_maximo`; `..._drenos_secao_subdimensionada_folga`; `..._tc_rotulos_velocidade_declividade` | A; A; B; B; B; A (neg.) |
| **CAC Castanhão / Trecho 1** (1128, 1131, 1139) | executivo (Trecho 1, 2002) | Racional < 3,5 km², HUT acima, C 0,20 a 0,40, CN 65 a 85; quadro de 59 bueiros sob o canal; valas da estrada de acesso | `cac_trecho1_hidrologia_racional_3_5km2_e_hut`; `cac_trecho1_bueiros_sob_canal_adutor_cota_inconsistente`; `cac_castanhao_estrada_acesso_valas_chuva_como_intensidade` | B; C (neg.); B (neg.) |
| **Canal do Sertão Pernambucano** (1390) | projeto | 204 drenos laterais ao adutor TR 100, 13 seções-padrão, afastamento 6 m, 162,464 km | `sertao_pernambucano_canais_drenagem_laterais_adutor` | B |
| **Retroanálise canal gabião x tubo** (planilha local, D8) | estudo | Canal retangular em gabião x tubo DN1000 por Manning, grade de n 441 combinações | `retroanalise_canal_gabiao_vs_tubo_manning` | B |

## Notas por projeto

- **Baixio**: gabarito mais usado do pacote (Manning 2,5x2,5 V 4,136; orifício TR 50 cota 407,846). Dois xfail. Tc e IDF
  do HUT ilegíveis: não há racional.py de gabarito.
- **CSB**: Tab. 4.7 (1341:205) com V e Yo que não reproduzem; BTCC-N17 −27 %.
- **Xingó**: não é Manning normal: perfil por energia a partir da seção crítica; xfail BU-01/06/24. Valetas: VPC-1 L =
  162,54 m (i 0,001) a 1259,04 m (i 0,060), reproduz a < 0,02 %.
- **Iuiu 2002 x 2018**: mesmo perímetro, duas premissas (TR 50 sob canal em 2002, TR 25 em 2018); a 2018 repete a
  "declividade mínima 5 %" do texto de 2002.
- **Delmiro**: o projeto de drenagem mais completo do acervo e o que concentra casos negativos (6 itens).
- **CAC**: as duas leituras negativas são de documentos diferentes (1128 e 1131); o estudo que dimensiona os bueiros
  (HARZA 2001) não está no acervo.
- **Retroanálise**: fonte local (D8), não é projeto de terceiros; serve de teste de unidade e de lâmina.
