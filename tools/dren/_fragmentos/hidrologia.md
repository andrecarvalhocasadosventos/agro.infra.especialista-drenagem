## README
Linhas novas/alteradas de `hidrologia.py` v0.3.0 (módulo | função | fórmula | fonte | teste):

| módulo | função | fórmula | fonte | teste |
|---|---|---|---|---|
| hidrologia | `picking(L_km, I)` | Tc[min] = 5,3 (L²/I)^(1/3) | IME p. 29 (Eq. 3.5, exemplo 40 min); DNIT-HIDRO p. 88 (rótulo "horas" divergente) | `test_ime_p29_exemplo_picking_chow_california`, `test_picking_e_chow_coerentes_com_tabela_de_velocidades_do_dnit` |
| hidrologia | `ven_te_chow(L_km, I_pct)` | Tc[min] = 25,2 (L/√I)^0,64 | DNIT-HIDRO p. 89 (imagem); IME p. 29 | idem |
| hidrologia | `nerc(L_km, H_m)` | Tc[h] = 2,8 (L/√(H/L))^0,47 | caso Delmiro (doc 1492:155), não conferida no primário | `test_delmiro_nerc_x_kirpich_rotulo_e_velocidade` |
| hidrologia | `bransby_williams(L_km, A_km2, J_pct, coef=0,615)` | Tc[h] = 0,615 L/(A^0,1 J^0,2) | caso Delmiro (doc 1494:31), constante não conferida | `test_delmiro_bhd1_cadeia_tc_s_pe_hut` |
| hidrologia | `tc_onda_cinematica(n, L_m, S, i_mm_h, coef=0,938)` | Tt[min] = 0,938 (nL/√S)^0,6 / i^0,4 (ft, pol/h) | McCuen Eq. 3-47, p. 146 impressa (165 física); planilhas FAA: coef 0,933 | `test_mccuen_ex_3_12_onda_cinematica_e_scs`, `test_planilhas_escoamento_plano_001_e_redencao` |
| hidrologia | `tc_laminar_neh(n, L_m, P2_mm, S)` | Tt[h] = 0,007 (nL)^0,8/(P2^0,5 S^0,4) | NEH-630 cap. 15 Eq. 15-8 (p. 12); McCuen Eq. 3-48 | `test_mccuen_ex_3_12...`, `test_neh630_cap15_laminar_e_velocidade_p18_21` |
| hidrologia | `tc_escoamento_aviso_lamina` | L ≤ 100 ft; nL/√S ≤ 100 (L máx = 100 √S/n) | NEH-630 cap. 15 p. 12–13 (Eq. 15-9); McCuen p. 146 | `test_aviso_limite_de_lamina_neh_100_ft` |
| hidrologia | `tc_lag_scs(L_m, CN, Y_pct)` | Tc[h] = L^0,8 (1000/CN − 9)^0,7 / (1140 √Y) (ft, %) | NEH-630 cap. 15 Eq. 15-4a/b (p. 11); McCuen Eq. 3-56 | `test_lag_scs_neh_p18_e_mccuen_ex_9_23` |
| hidrologia | `velocidade_concentrado_neh`, `velocidade_manning`, `tempo_viagem_min` | V = k √S (Tab. 15-3); V = R^(2/3) √S/n; t = L/(60 V) | NEH-630 cap. 15 Tab. 15-3 (p. 14), Eq. 15-1, 15-10 | `test_neh630_tab_15_3...`, `test_mccuen_ex_3_13_metodo_da_velocidade` |
| hidrologia | `c_ponderado`, `escoamento_ponderado` | ΣC·A/ΣA; ΣQ(P,CN)·A/ΣA (pondera Q, não CN) | McCuen Ex. 7-11 (p. 398–399), Ex. 7-17/7-18 (p. 408–409) | `test_mccuen_racional_ex_7_9_e_7_11`, `test_mccuen_scs_ex_7_15_a_7_18...` |
| hidrologia | `tc` (CLI) novos métodos | `picking`, `ven_te_chow`, `nerc`, `bransby_williams`, `onda_cinematica`, `laminar_neh`, `lag_scs` | ver acima | `test_cli_v03_metodos_novos_de_tc` |
| hidrologia | `dooge`, `giandotti`, `kirpich`, `kirpich_modificada_dnit`, `dnos` (docstrings e avisos) | inalteradas; conferidas no primário | Dooge: PMSP-DRENURB-V2 p. 57 (A km², S m/m, min; 140–930 km²); Giandotti: DNIT-HIDRO p. 91–92 (sem faixa de área no corpus); Kirpich: PMSP p. 56, McCuen Eq. 3-55, DNIT p. 88; Kirpich mod. (1,42): DNIT p. 90; DNOS e tabela K: DNIT p. 89 | `test_dooge_forma_pmsp_p57...`, `test_giandotti_forma_dnit...`, `test_kirpich_equivale...`, `test_dnos_tabela_K...`, `test_kirpich_modificada_fator_142...` |

Gabaritos G1 cobertos: 1, 2, 4, 5, 6 (parcial: R-1 e R-3 não recalculáveis), 7, 8, 9, 14, 15 (parte de Tc e IDF; o tanque não foi implementado).
Não cobertos: 3 (Ex. 3-14, falta Tab. 3-15), 10 (qu da Fig. 7-9c), 11 (LP3), 12 (Tab. 9-17), 13 (Pfafstetter, IDF é do Clima), 16, 17.

## DIVERGENCIAS
| item | fonte A | fonte B/acervo | tratamento |
|---|---|---|---|
| Unidade do Tc de Picking | DNIT-HIDRO p. 88 (impressa 84): "TC em horas" | IME p. 29: exemplo L 5 km, I 0,06 → 40 min; tabela de velocidades do próprio DNIT (p. 97, V = 1,132 H^0,333 km/h) | `picking` retorna minutos; aviso no CLI; o rótulo "horas" do DNIT tratado como erro de impressão |
| Faixa de área do Giandotti | Tucci/literatura: 170 a 70.000 km² (não consta do corpus) | DNIT-HIDRO p. 92: sem faixa, só "pouco recomendável" em bacia pequena (2,1 km/h) | aviso quando A < 170 km², texto "não consta do corpus"; faixa continua não conferida |
| Área de validade do Kirpich | PMSP-DRENURB-V2 p. 56: ≤ 0,5 km² (7 bacias do Tennessee); McCuen p. 172: 1 a 112 acres | DNIT-HIDRO p. 88: < 0,8 km² | docstring registra as três; aviso por L > 10 km (PMSP p. 56) e declividade 3–10 % |
| Coeficiente do escoamento em lâmina (onda cinemática) | McCuen Eq. 3-47: 0,938 | planilhas internas (aba FAA): 0,933 | `coef` é argumento (padrão 0,938, provisório, decisão F7); ambos testados |
| Limite de L do escoamento em lâmina | McCuen: 100–300 ft, ou nL/√S ≈ 100 | NEH-630 cap. 15: 100 ft (Eq. 15-9) | aviso nos dois critérios; as planilhas (L 150 m e 141,86 m) violam ambos |
| Kerby | forma em m da `kerby` (1,44, exp. 0,467) | McCuen Eq. 3-53 (0,83 em ft, exp. 0,47): +2,6 % | teste de equivalência a 5 %; DNIT p. 86 traz outra forma (37 (L^a/I)^0,47) não implementada |
| Qp unitário do HUT em Delmiro | caso diz "m³/s por mm" (1494:33; 1492:157) com Qp = 2,08 A/ta = 15,149 | Qp por mm = 0,208 A/ta = 1,515 | 15,149 é por 10 mm (1 cm); `hidrograma_unitario_triangular` já devolve por mm; teste confirma |
| Pico BHD1 TR 50 (Delmiro, 58,71 m³/s) | caso doc 1494:64 | convolução com chuva uniforme em 8 blocos: 61,8 m³/s (+5,3 %); tempo do pico 10,35 h × 10,36 h confere | `xfail(strict=True)` (`test_delmiro_bhd1_pico_58_71`): hietograma por polinômio cúbico (Quadro 3.3) não recuperável; sessão interativa pendente |
| Constantes NERC (2,8; 0,47) e Bransby-Williams (0,615) | caso Delmiro reproduz 7,65 h e 7,53 h | nenhuma fonte primária no corpus | funções marcadas "não conferida"; só para reproduzir o projeto |
| Páginas do mapa G1 para McCuen | Mapa: "física" em alguns itens | Ex. 3-12 é a p. 146 impressa (165 física); Kirpich/lag/Kerby: p. 153–154 impressas (172–173 físicas) | citadas aqui como impressa (física) |
