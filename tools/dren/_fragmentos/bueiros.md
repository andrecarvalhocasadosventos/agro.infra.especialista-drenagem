## README

### `bueiros.py` v0.3.0 e `tubos.py` v0.1.0 (F5, 2026-10-08)

| módulo | função | fórmula | fonte | teste |
|---|---|---|---|---|
| bueiros | `tubo_parcialmente_cheio(Q, D, n, S0, n_celulas, limite_y_sobre_D)` | Manning com segmento circular exato; Fr = V/√(gA/T); y/D ≤ 0,75 como padrão provisório (decisão F7) | HDS-3 Chart 55 (p. 76) e Ex. 10-17 (p. 53-55); Delmiro BUC-2..5 (1493:282-285, acervo sem ✓h) | `test_hds3_ex*`, `test_delmiro_tubo_parcialmente_cheio` |
| bueiros | `regime_critico_tubular_ime(D, n)` | (3/2)A/T = D → θc = 4,0335 rad; A_c = 0,601 D²; Vc = 2,56 D^0,5; Qc = 1,538 D^2,5; Ic = 32,82 n²/D^(1/3) | IME Anexo II p. 151-152 | `test_ime_regime_critico_tubular` |
| bueiros | `velocidade_de_saida` (teste novo) | lâmina normal em declividade forte | HDS-5 DG 1.4 Step 7 (p. 280): 6,47 m/s | `test_hds5_p280_velocidade_de_saida_caixa_1524` |
| bueiros | `vazao_critica_legado_dnit` (docstring) | A_c = 0,60 D² = arredondamento do 0,601 do IME (deixa de ser "ajuste próprio") | IME p. 151-152; DNIT-DREN p. 55 | `test_legado_dnit_bstc_tabela1_*` |
| tubos | `carga_solo_vala(hs, bv, tipo_solo)` | q = Cv γ bv²; Cv = (1 − e^(−α'λ))/α'; α' = 2kμ' | TUBOS p. 17 (eqs. 2.1-2.2); EM Ap. B p. 66-68 | `test_em2902_vala_cd_e_we1` (Cd 1,274; 55,483 kN/m), `test_vala_limites_*` |
| tubos | `carga_solo_aterro_positiva(hs, de, rho, r_ap, tipo_solo)` | q = Cap γ de²; Cap por (2.4)/(2.5); plano de igual recalque e^(αλe) = αλe + αρr + 1 (2.6) | TUBOS p. 19-21 (eqs. 2.3-2.8, Tab. 2.1) | `test_aterro_positiva_*` (consistência: sem exemplo numérico no corpus) |
| tubos | `fator_berco_vala(classe, alfa_A, fonte)` | A 2,25-3,4 (padrão provisório 2,25), B 1,9, C 1,5, D 1,1; EM: 2,5 / 1,9 / 1,5 | TUBOS Tab. 4.1 p. 37; EM Tab. 3-1 p. 27 | `test_tabelas_em_e_abtc_coincidem_*`, `test_fator_berco_vala_*` |
| tubos | `fator_berco_aterro(classe, rho, hs, de, k, Cap, theta_fixo)` | a_eq = 1,431/(η − θχ); θ = (ρk/Cap)(hs/de + ρ/2) ≤ 0,33 | TUBOS eqs. 4.1-4.2 e Tab. 4.2-4.3 p. 42-43 (conferido na imagem); EM eq. 3-1 | `test_em2902_fator_de_berco_aterro_e_d_load` (Bf 6,098) |
| tubos | `d_load_em2902(W_T, Si, Bf, Hf)` | D0,01 = Hf W_T/(Si Bf) | EM eq. 3-2 p. 25; exemplo p. 71-72: 57 N/m/mm | idem |
| tubos | `coef_impacto(hs)`, `sobrecarga_multidao(de)` | φ = 1,3/1,2/1,1/1,0; qm = 5 de | TUBOS Tab. 3.3 e eq. 3.19 (p. 33) | `test_impacto_sobrecarga_e_forca` |
| tubos | `forca_de_ensaio`, `classe_de_tubo(DN, F, tipo)` | Fens = γ(q+qm)/a_eq (γ 1,0 fissura; 1,5 ruptura); menor classe PA/EA com fissura ≥ F e ruptura ≥ 1,5 F | TUBOS eqs. 5.1-5.2 p. 45; ESPEC Tab. 2 p. 4 = TUBOS Tab. 5.1 p. 46 | `test_espec_exemplos_de_classe` (PA2; EA4; PA4) |
| tubos | `selecionar_tubo(...)` | encadeia as funções acima; indicativo | idem | `test_selecionar_tubo_*`, `test_cli_*` |

Lacunas do `tubos.py`: altura máxima de aterro por classe e DN (só no software da ABTC); sobrecarga de veículo-tipo (cap. 3 do TUBOS) entra como argumento; projeção negativa, vala induzida e r_ap < 0 não implementados; diâmetro externo estimado pela espessura PA2 (ALTERACOES Tab. 1) quando não informado.

## DIVERGENCIAS

| item | fonte A | fonte B / acervo | tratamento |
|---|---|---|---|
| V de saída HDS-5 p. 280 (caixa 5×5 ft, Q50 8,495 m³/s, S 0,02) | SI do HDS-5: 6,47 m/s | CU do mesmo texto: 20,8 ft/s = 6,34 m/s (−2 %); HY-8: 19,61 ft/s = 5,98 m/s; calculadora (n 0,012): 6,45 m/s (−0,3 % do SI) | o texto não informa n; adotado 0,012. Com n 0,013 o resultado cai para 6,07 m/s (−6 %): o gabarito depende de n. Teste com 1 % contra o valor SI; CU e HY-8 registrados como comentário |
| A_c do tubular em regime crítico | DNIT-DREN Tab. 1 (p. 55): ajuste 0,60 D² | IME p. 151-152: θc = 4,0335 rad dá 0,601 D²; Qc impresso 1,533 D^2,5, recalculado 1,538 (0,3 %) | 0,601 é fórmula impressa (critério Ec = (3/2)A/T, exato só no retangular); 0,60 mantido no legado (0,2 %). Vazão crítica exata de Ec = D é ~7 % menor (já registrado) |
| EM 1110-2-2902 p. 71-72 (D-load do exemplo) | mapa G2: "Bf 6,098 não reproduz D0,01 = 57 com We = 175 130 N/m" | Bf = 1,431/(0,505 − 0,811/3) = 6,097 e D0,01 = 1,3 (145 940 + 175 130)/(1200 × 6,098) = 57,0 N/m/mm | resolvido: W_T = W_L + W_E e θ = 1/3 fixo (eq. 3-1 completa). Passa a ser teste de livro (1 %) |
| Fator de berço classe A em vala | TUBOS Tab. 4.1: 2,25 a 3,4 | EM Tab. 3-1: 2,5 | padrão provisório 2,25 (mínimo, a favor da segurança) com `alfa_A` e `fonte="em2902"` como opções; decisão F7 |
| n de Manning de tubo de concreto no teste do Xingó | legado Xingó: 33,5 D^2,67 i^0,5 | equivale a n = 0,3117/33,5 = 0,0093; com n de projeto 0,012-0,013 a capacidade cai 22-28 % | caso negativo documentado em teste; nenhum n decidido aqui (pendência do mapa G2) |
| Delmiro BUC-2..5, TR 20 e TR 50 | acervo (1493:282-285), sem ✓h | `tubo_parcialmente_cheio` reproduz y, V e Fr dos 8 casos dentro de 1 % (testes a 5 %) | sem divergência; y/D = 79 % de BUC-5 em TR 50 passa do critério provisório 75 % (aviso, decisão F7). Divergências de declividade e comprimento do caso (itens 1 e 2) continuam abertas |
| HDS-3 Ex. 12, 15, 17 (leitura de gráfico) | impresso: V 3,5 fps; V 6,0 fps; Sc 0,0026; Hc 8,4 ft | recálculo exato: 3,555; 6,077; 0,00266; 8,30 | 1,3 a 2,3 % (leitura de gráfico): testados a 5 %, rotulados "livro, leitura de gráfico" |
