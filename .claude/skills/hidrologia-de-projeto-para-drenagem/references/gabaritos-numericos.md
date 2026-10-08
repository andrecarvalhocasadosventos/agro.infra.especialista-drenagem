# Conferências numéricas com primário (candidatas a teste da calculadora)

Páginas = página física do PDF. Os valores da última coluna foram calculados com `tools/dren/hidrologia.py` (versão 0.3.0 na revisão da F6); testes que já travam o valor estão na coluna final do bloco 2.

## 1. Primários de norma e manual

| Primário | Entradas | Resultado do primário | Resultado da calculadora |
|---|---|---|---|
| DNIT-HIDRO p. 130 (racional) | c = 0,1828; P(40 min) = 67,33 mm, logo i = 67,33·60/40 = 101,0 mm/h; A = 2,4 km² | 12,31 m³/s (com 3,6, não "6,3") | `racional(C = 0,1828, i = 101,0, A = 2,4)`: 12,31 |
| DNIT-HIDRO p. 131 (racional, outra bacia) | c = 0,385; i = 96,1 mm/h; A = 10,5 km² | 107,9 m³/s; 28 % acima de 84,4 m³/s por descargas específicas | — |
| NRCS-NEH630-CH16 p. 16, ex. 16-1 | A = 4,6 mi² (11,914 km²); Tc = 2,3 h; ΔD = 0,3 h; Q = 1 pol (25,4 mm) | Tp = 1,53 h; qp = 1.455 ft³/s | `hidrograma_unitario_triangular`: tp = 1,53 h; qp = 1,6197 m³/s/mm = 1.453 ft³/s por pol (−0,15 %) |
| NRCS-NEH630-CH10 p. 19, ex. 10-3 | P = 5,1 pol (129,54 mm); CN 75 e 69 | Q = 2,53 e 2,03 pol | `chuva_efetiva`: 2,531 e 2,030 pol |
| NRCS-NEH630-CH10 p. 12, Tab. 10-1 | CN 74 | S = 3,51 pol | `retencao_S`: 3,514 pol |
| PMSP-DRENURB-V2 p. 21-22 (blocos alternados, Wilken, TR 5) | i = 57,71·TR^0,172/(t + 22)^1,025 mm/min; t de 10 a 100 min, Δ = 10 min | Alturas acumuladas 21,8; 33,0; 39,7; 44,2; 47,5; 49,9; 51,7; 53,2; 54,4; 55,3 mm; blocos reordenados 1,2; 1,8; 3,2; 6,7; 21,8; 11,2; 4,5; 2,4; 1,4; 0,9 mm. A coluna "Intensidade (mm/h)" da tabela impressa traz (t + 22)^1,025 e não a intensidade | `idf_potencial(TR = 5, t, a = 57,71·60, b = 0,172, c = 22, d = 1,025)·t/60`: 21,81; 33,01; 47,50 (t = 50) e 55,33 mm (t = 100) |
| FHWA-HDS2 p. 132, Tab. 5.13 (Gumbel) | n = 10, TR 25 (prob. 0,04): K = 2,8468 | X = x̄ + K·s | Série de 10 valores (60, 72, 55, 90, 110, 65, 70, 80, 95, 58): K de n dá 126,8; `gumbel_P_TR` dá 112,3 (K = 2,04) |
| ABDER-APOSTILA p. 69 (racional com retardo) | A = 8,5 km² = 850 ha; C = 0,35; i = 65,89 mm/h; φ = 1/(100·8,5)^(1/6) = 0,325 | Q = 17,9 m³/s | 0,00278·0,35·65,89·850·0,3249 = 17,7 m³/s (−1 %) |
| ABDER-APOSTILA p. 67 (Kirpich) | L = 0,49 km; i = 7 % | Tc = 0,106 h = 6,3 min | `kirpich(L = 490, S = 0,07)`: 6,40 min (+1,6 %) |
| USBR-DRAINAGE p. 57 × EMBRAPA-DREN-SUP p. 5 (McMath) | conversão de unidades | 0,0091 (S m/m) e 0,0023 (S m/km) | 0,02832/25,4·2,471^0,8 = 0,0023; × 1.000^0,2 = 0,00915 |

## 2. Gabaritos G1 (livros e planilhas) e casos L2: função e teste

Unidade original da fonte; valor SI em parênteses quando útil. Testes em `tests/dren/test_hidrologia.py`; livro = 1 %, acervo = 5 %.

| Fonte (página física) | Entradas | Resultado | Função | Teste |
|---|---|---|---|---|
| McCuen Ex. 3-12 (p. 165) | n 0,15; L 120 ft; S 0,002; i 8 pol/h; P2 3,12 pol | 14,9 min (onda cinemática, coef 0,938); 28,8 min (Eq. 3-48) | `tc_onda_cinematica`, `tc_laminar_neh` | `test_mccuen_ex_3_12_onda_cinematica_e_scs` |
| McCuen Ex. 3-13 (p. 165-166) | trechos 140/0,25, 260/1,40, 480/2,1 | 975 s = 16,2 min (depois: 547 s = 9,1 min) | `velocidade_manning`, `tempo_viagem_min` | `test_mccuen_ex_3_13_metodo_da_velocidade` |
| NEH-630 cap. 15 p. 18-21 | laminar 100 ft, n 0,15, P2 3,6 pol, S 0,08 e mais três trechos | 0,09 h; Tc total 1,75 h | `tc_laminar_neh`, `velocidade_concentrado_neh` | `test_neh630_cap15_laminar_e_velocidade_p18_21`, `test_neh630_tab_15_3_velocidade_escoamento_concentrado` |
| NEH-630 cap. 15 p. 18 e McCuen Ex. 9-23 (p. 557-558) | L 3.865 ft, Y 4,79 %, CN 63; L 6.500 ft, 1,3 %, CN 92 | 1,14 h; 1,34 h | `tc_lag_scs` | `test_lag_scs_neh_p18_e_mccuen_ex_9_23`, `test_mccuen_ex_9_23_hut_triangular_726` |
| Planilhas 001 e Redenção (aba "FAA") | n 0,13, L 150 m, i 186 mm/h, S 0,15; n 0,011, L 141,86 m, S 0,0097 | 9,0114 e 4,5032 min (coef 0,933) | `tc_onda_cinematica(coef=0.933)` | `test_planilhas_escoamento_plano_001_e_redencao` |
| McCuen Ex. 7-9 e 7-11 (p. 397, 398-399) | ver `coeficiente-c-racional.md` 5 | 19,6 / 15 ft³/s; C 0,412; 37,4 ft³/s | `racional`, `c_ponderado` | `test_mccuen_racional_ex_7_9_e_7_11` |
| McCuen Ex. 7-15 a 7-18 (p. 405-409) | P 7 pol; CN 75; CN 55/70/75/83 | Q = 4,15 pol; 2,12/3,62/4,15/5,03 pol; Q ponderado 3,62 | `chuva_efetiva`, `escoamento_ponderado` | `test_mccuen_scs_ex_7_15_a_7_18_e_ponderacao_do_escoamento` |
| IME p. 29 (Picking, Chow, California) | L 5 km; I 0,06; I 6 %; H 300 m | 40 min (39,6); 39,8 min; 41 min | `picking`, `ven_te_chow`, `california_culverts` | `test_ime_p29_exemplo_picking_chow_california`, `test_picking_e_chow_coerentes_com_tabela_de_velocidades_do_dnit` |
| Delmiro BHD1 (doc 1494:64) | L 13,21 km; A 36,34 km²; ΔH 32 m; CN 75,2; P 112,40 mm | Tc 7,65 h (NERC) e 7,53 h (B-W); S 83,77 mm; Pe 50,99 mm; Qp 1,515 m³/s/mm; pico 58,71 m³/s | `nerc`, `bransby_williams`, `hu_triangular`, `convolucao_hu` | `test_delmiro_bhd1_cadeia_tc_s_pe_hut`, `test_delmiro_nerc_x_kirpich_rotulo_e_velocidade`; pico: `test_delmiro_bhd1_pico_58_71` (**xfail estrito**: 61,8 calculado, +5,3 %) |
| CAC Trecho 1 (doc 1139:228) | L 3,0 km; h 20 m | 85,5·(27/20)^0,385 = 96 min | `kirpich_modificada_dnit` | sem teste dedicado (sugestão: 95,6 min, 1 %) |
| CAC Castanhão (doc 1128:112) | C 0,6; P 23,20 mm; tc 5 min; A 44.110 m² | Q do projeto 0,171 m³/s; com i = 278,4 mm/h, 2,05 m³/s (12×) | `racional` | sem teste dedicado (sugestão: razão 60/tc) |
| PMSP-DRENURB-V2 p. 21-22 | Wilken TR 5, t 10 a 100 min | acumulados 21,8 ... 55,3 mm | `blocos_alternados` | `test_blocos_alternados_wilken_tr5_pmsp_v2` |
| HDS-2 Tab. 5.13 | n 10, TR 25 | K = 2,8468 | `gumbel_K` | `test_gumbel_K_n10_hds2_tab_5_13` |
