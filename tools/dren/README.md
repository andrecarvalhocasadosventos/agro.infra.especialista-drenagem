Migrado de tools/hid em 2026-10-08 (D2).

# tools/dren - calculadoras hidraulicas verificaveis

Convencoes (D5, D10, D14): SI em toda interface (m, m3/s, m/s, Pa ou m.c.a. declarado, kg/m3);
nomes em portugues sem acento; cada funcao publica tem docstring com formula, fonte e faixa de
validade; cada modulo tem CLI que imprime JSON com `entradas`, `saidas`, `metodo`, `avisos`, `versao`.

```
cd "<RAIZ>"            # Especialista Hidraulica
set PYTHONIOENCODING=utf-8
python -m tools.dren.perdas --json "{\"funcao\": \"hf_darcy\", \"Q\": 0.1, \"L\": 500, \"D\": 0.3, \"eps\": 1e-4}"
python -m tools.dren.perdas --funcao hf_hazen_williams --Q 0.47 --L 4596 --D 0.7 --C 130
python -m tools.dren.canais --json "{\"funcao\": \"y_normal\", \"secao\": {\"tipo\": \"trapezoidal\", \"b\": 5, \"z\": 1.5}, \"Q\": 22, \"n\": 0.0142857, \"S0\": 0.00015}"
python -m tools.dren.<modulo> --listar        # lista as funcoes da CLI
```

Secoes na CLI de canais: `{"tipo": "trapezoidal", "b":, "z":}`, `retangular {b}`, `triangular {z}`,
`circular {D}`, `composta {partes: [{secao, cota_fundo, n}]}`.

Versao dos modulos: `perdas` 0.1.0, `canais` 0.1.0. Infra comum em `_cli.py`.
Python usado: o do sistema (Python 3.14, pytest 9.1, numpy 2.4); o `.venv` de "Especialista Orcamento" nao existe nesta
copia do Drive. Os modulos usam so a stdlib.

## Resultado dos testes (`python -m pytest tests/dren/test_perdas.py tests/dren/test_canais.py -q`)

```
107 passed, 3 xfailed in 90.51s
```

Os 3 xfail sao divergencias > 5 % vs acervo, listadas em `DIVERGENCIAS.md` (nao ajustadas).
O tempo e dominado por 2 testes de CLI (subprocess a partir do Drive G:).

## Modulo `perdas.py`

| funcao | formula | fonte | teste |
|---|---|---|---|
| `reynolds(Q,D,nu)` | Re = 4Q/(pi D nu) | Porto, Hidraulica Basica, cap. 6 | `test_reynolds_definicao` |
| `colebrook_f(Re,eps,D)` | 1/sqrt(f) = -2 log10(eps/3,7D + 2,51/(Re sqrt f)), Newton tol 1e-10 | Colebrook (1939); Porto cap. 6; White | `test_colebrook_valores_de_moody`, `test_colebrook_satisfaz_equacao` |
| `swamee_jain_f(Re,eps,D)` | f = 0,25/[log10(eps/3,7D + 5,74/Re^0,9)]^2 | Swamee & Jain (1976) | `test_colebrook_vs_swamee_jain_menos_2pct` (< 2 % exceto canto Re<2e4 e eps/D>=1e-3: ate 3,1 %) |
| `fator_atrito(Re,eps,D)` | laminar 64/Re (Re<=2000); aviso na transicao 2000<Re<4000 | Porto cap. 6 | `test_laminar_e_transicao` |
| `hf_darcy(Q,L,D,eps,nu)` | hf = f L V^2/(2 g D) = 8 f L Q^2/(pi^2 g D^5) | Porto cap. 6; Azevedo Netto | `test_darcy_formula_equivalente_8fLQ2`, `test_cac_sifao_perda_continua` |
| `hf_hazen_williams(Q,L,D,C)` | hf = 10,643 L Q^1,852/(C^1,852 D^4,87); avisos de validade (20 C, turbulento, 50 mm<=D<=~3 m, V<=3 m/s) | Porto; Azevedo Netto | `test_hazen_williams_formula_e_avisos`, `test_iuiu_hazen_williams`, `test_xingo_hazen_williams_trecho2`, `test_iuiu2018_hazen_c_implicito` |
| `C_HAZEN_WILLIAMS` | FoFo novo 130, PEAD 150, PRFV 150, aco revestido 130, concreto 120-130 | Porto; Azevedo Netto (pag. nao verificada) | `test_C_tipicos` |
| `C_hazen_implicito(Q,D,J)` | inversa de Hazen-Williams | derivada | `test_iuiu2018_hazen_c_implicito` |
| `J_manning_strickler_tubo(Q,D,K)` | J = (Q/(K A R^(2/3)))^2, R = D/4 | Chow cap. 5; caso CAC 1130:63-64 | `test_cac_manning_strickler_tubo` |
| `hf_localizada(Q,D,K)`, `K_LOCALIZADO` | hL = K V^2/2g; K tipicos (entrada 0,5/1,0, saida 1,0, curva 90 0,4, curva 45 0,2, reducao 0,15, gaveta 0,2, borboleta 0,3, retencao 2,5) | Azevedo Netto (tab. K, pag. nao verificada); Porto cap. 6; Macintyre | `test_hf_localizada`, `test_csb_perda_localizada_casa_de_bombas` |
| `diametro_equivalente_paralelo(n,D)` | D_eq = n^0,4 D (demonstracao na docstring) | derivacao de Darcy; caso CSB 1357:146 | `test_equivalente_paralelo_demonstracao_numerica`, `test_csb_diametro_equivalente` |
| `vazao_por_linha(Q,[D])` | q_i = Q D_i^2,5 / sum D_j^2,5 | derivada de Darcy (f igual) | `test_vazao_por_linha` |
| `Q_para_V`, `D_para_V`, `velocidade` | Q = V pi D^2/4; D = sqrt(4Q/(pi V)) | continuidade | `test_Q_e_D_para_V`, `test_csb_velocidade_por_tubo`, `test_xingo_velocidades` |
| `potencia_hidraulica(Q,H,eta)` | P[kW] = rho g Q H/(1000 eta) | Porto; Macintyre | `test_csb_potencia`, `test_irece_potencia_hidraulica` |
| `gradiente_hidraulico(Q,D,eps)` | J = f V^2/(2 g D) | Porto cap. 6 | `test_linha_piezometrica` |
| `linha_piezometrica(perfil,Q,D,eps,H0)` | cota_i = H0 - sum J L_trecho; pressao = cota - z | Porto cap. 6/7 | `test_linha_piezometrica` |

## Modulo `canais.py`

| funcao | formula | fonte | teste |
|---|---|---|---|
| `trapezoidal(b,z)`, `retangular(b)`, `circular(D)`, `composta(partes)` | A, P, Rh, B, Dh = A/B | Chow, Tab. 2-1; Porto | `test_geometria_trapezio`, `test_geometria_circular`, `test_composta_soma_das_partes` |
| `manning_Q(secao,y,n,S0)`, `manning_Q_AR` | Q = A Rh^(2/3) S0^(1/2)/n | Chow; Porto | `test_manning_ida_e_volta`, `test_csb_geohidro_manning`, `test_xingo_*`, `test_iuiu_ponte_calhas` |
| `manning_y_normal(secao,Q,n,S0)` | bissecao (tol 1e-12) em Q(y) = Q; circular ate 0,938 D | Chow cap. 6 | `test_irece_cp0_trecho1`, `test_cac_canal_manning_strickler`, `test_circular_manning_cheio_e_maximo` |
| `y_critica(secao,Q)` | Q^2 B/(g A^3) = 1; retangular (q^2/g)^(1/3) | Chow cap. 3 | `test_y_critica_retangular_livro`, `test_y_critica_trapezoidal_satisfaz_Fr1`, `test_circular_critica` |
| `froude(secao,y,Q)` | Fr = V/sqrt(g A/B) (Dh, **nao y**; armadilha Baixio de Irece) | Chow | `test_froude_armadilha_dh_vs_y`, `test_irece_cs2_trecho1_e_froude_rotulado` |
| `energia_especifica`, `declividade_critica`, `regime`, `velocidade` | E = y + V^2/2g; Sc = (nQ/(A_c R_c^(2/3)))^2; fluvial/torrencial/critico (tol 1 %) | Chow cap. 3 e 6 | `test_regime_e_declividade_critica`, `test_y_critica_trapezoidal_satisfaz_Fr1` |
| `borda_livre(y,V,criterio,Q,C)` | usbr: f = sqrt(C y), C 0,46-0,76 (aprox. do abaco, interpolado em log Q); lencastre: y/4 (como no caso CSB, fonte primaria nao verificada); cdv: 2V^2/2g + 0,10 y + 0,10 (D-31); bureau_q: 0,34 log10 Q - 0,01 / 0,23 log10 Q + 0,10 (caso CSB) | USBR Design of Small Canal Structures 1978 / DS-3; casos CSB e CDV | `test_borda_livre_criterios`, `test_csb_geohidro_borda_livre_*` |
| `remanso_passo_padrao(...)` | energia entre secoes com Sf medio (Manning), bissecao por passo no ramo fluvial/torrencial; classifica M1, M2, S1, S2, S3, H2, A2...; para ao cruzar y_c | Chow cap. 10; Porto | `test_remanso_*` |
| `ressalto_hidraulico(secao,y1,Q)` | Belanger (retangular); funcao momento numerica (trapezoidal); dE = E1 - E2; L ~ 6 y2 (4,5<Fr1<9, USBR EM-25, aproximacao declarada); tipo por Fr1 | Chow cap. 15; USBR EM-25 | `test_belanger_retangular`, `test_ressalto_trapezoidal_momentum`, `test_tipos_de_ressalto` |
| `secao_hidraulica_otima(tipo,Q,n,S0,z)` | retangular b = 2y; trapezoidal b/y = 2(sqrt(1+z^2) - z), theta = 60 graus, R = y/2 | Chow cap. 7 | `test_otima_*` |
| auxiliares dos casos: `orificio_carga`, `vertedor_lateral_Le`, `perda_grade_kirschmer`, `comporta_velocidade_vao`, `comporta_perda_carga` | h = (Q/Cd A)^2/2g; Le = 0,1Q/(1,84 he^1,5); dh = m (s/w)^(4/3) sin(theta) Va^2/2g; V = (Q/N)/(L h); hL = CS (H1/H2) v^2/2g | casos Baixio de Irece e Vale do Iuiu | `test_irece_tomada_orificio`, `test_iuiu_vertedor_lateral`, `test_iuiu_grade_kirschmer`, `test_irece_comporta_*` |

## Limites desta versao

- Referencias de Hazen-Williams, K localizados e borda livre "Lencastre"/"Bureau": paginas dos livros nao verificadas (marcado nas docstrings).
- Secao circular: sem ressalto; remanso e ressalto assumem canal prismatico, alfa = 1.
- Gabaritos de `ancoragem`, `bomba` (NPSH), `transiente_moc` e valor presente nao entram aqui (ver `DIVERGENCIAS.md`).

## Modulos `hidrologia.py` e `bueiros.py`

Calculadoras de hidrologia de projeto e de bueiros (stdlib; CLI `python -m tools.dren.hidrologia|bueiros --json '{"funcao": ..., ...}'`). Testes: `tests/dren/test_hidrologia.py`, `tests/dren/test_bueiros.py`; divergencias dos casos em `DIVERGENCIAS.md`.

| funcao | formula | fonte |
|---|---|---|
| `idf_potencial`, `idf_tabela` | i = a TR^b/(t+c)^d (mm/h, t min); interpolacao log-log | DAEE IT DPO 11; Tucci |
| `kirpich`, `kirpich_modificada_dnit`, `california_culverts`, `giandotti`, `dooge`, `dnos`, `kerby` | Tc (min); avisos de faixa (Kirpich < 0,5 km2, 3-10 %) | DNIT IPR-715; Silveira 2005 |
| `racional`, `mcmath`, `coef_c_para_tr`, `coef_distribuicao` | Q = C i A/3,6 (A km2); McMath 0,0091 C i A^0,8 S^0,2 (A ha, S m/m) | DNIT IPR-715; casos Iuiu/CSB |
| `chuva_efetiva`, `hidrograma_unitario_triangular`, `convolucao_hu` | SCS-CN, tlag = 0,6 Tc, qp = 0,208 A/tp, tb = 2,67 tp | NRCS NEH-630 cap. 10 e 16 |
| `gumbel_P_TR` | momentos; aviso n < 20 | Gumbel; DNIT |
| `controle_de_entrada`, `controle_de_saida`, `dimensionar_bueiro` | HDS-5 eqs. A.1-A.3 (Tab. A.1), 3.1/3.4 (Ke da Tab. C.2) | FHWA HDS-5 (2012) |
| `velocidade_de_saida`, `dissipador_necessario` | lamina normal/critica; V > limite do material (simplificado) | HDS-5 cap. 4; HEC-14/15 |
| `verificacao_por_orificio`, `verificacao_manning_plena`, `comparar_legado_hds5` | metodos legados do acervo (Baixio de Irece, CSB, Xingo) x HDS-5 | casos do acervo |

`bueiros.py` traz uma funcao interna minima de Manning/lamina critica (circular, retangular, arco) a unificar com `canais.py`.

## Modulo `bombas.py`

Reutiliza `hf_darcy`, `hf_localizada`, `hf_hazen_williams` de `perdas.py`. CLI: `python -m tools.dren.bombas --json '{"funcao": "...", ...}'` (`--listar`).

| funcao | formula | fonte | teste |
|---|---|---|---|
| `curva_do_sistema(Hgeo,Q_lista,L,D,eps,K_total,n_linhas,metodo,C)`, `sistema(...)` | H = Hgeo + hf(Q/n) + hL(Q/n); Darcy/Colebrook ou Hazen-Williams | Porto cap. 6/7; Macintyre | `test_sistema_usa_perdas_do_modulo_perdas`, `test_xingo_curva_do_sistema_Hman_max` |
| `curva_da_bomba(pontos_QH, pontos_Q_eta, pontos_Q_npshr, modelo)` -> `CurvaBomba` | H = a - bQ^2 (minimos quadrados em Q^2) ou grau 2; eta e NPSHr por interpolacao linear | Macintyre | `test_curva_ajuste_*`, `test_interpolacao_*`, `test_iuiu_curva_da_bomba_EB2` |
| `ponto_de_operacao(sis,bomba,n_paralelo,Q_bep)` | bissecao de Hb(Q/n) = Hs(Q); aviso fora de 70-120 % de Q_bep | Macintyre | `test_ponto_de_operacao_*`, `test_paralelo_*` |
| `associacao_paralelo`, `associacao_serie` | paralelo: soma de Q a mesma H (retencao fecha acima do shut-off); serie: soma de H | Macintyre | `test_paralelo_duas_bombas_iguais_dobra_Q_na_mesma_H`, `test_serie_soma_H` |
| `afinidade(...)`, `rotacao_para_vazao_alvo(...)` | Q~N, H~N^2, P~N^3; diametro: corte (D, D^2, D^3) ou geometrica (D^3, D^2, D^5); N tal que r^2 H0(q/r) = Hs(Q_alvo) | Macintyre; Karassik | `test_afinidade_*`, `test_rotacao_para_vazao_alvo_forma_fechada` |
| `potencia`, `energia_anual`, `custo_energia`, `opex_energia` | P = rho g Q H/(1000 eta) (rho 998); E = P h; **5.000 h/ano (CDV, D-09)** parametrizavel | Porto cap. 7 | `test_potencia_*`, `test_energia_custo_e_opex_5000_h`, `test_irece_potencia_*`, `test_iuiu_potencia_*` |
| `npsh_disponivel`, `pressao_atmosferica`, `pressao_vapor` | NPSHd = pa/g + hs - hf - pv/g; ISA p = 101325(1-2,25577e-5 z)^5,25588; Antoine (1-100 C); 1 m.c.a. = 9,81 kPa | Macintyre; ISO 2533; ANSI/HI 9.6.1 | `test_npsh_nivel_do_mar_*`, `test_iuiu_npsh_*`, `test_xingo_npsh_poco_seco` |
| `verificar_cavitacao` | NPSHd >= NPSHr + max(0,5 m; 10 %); referencia ANSI/HI 9.6.1 (tabela da norma nao reproduzida) | ANSI/HI 9.6.1 | `test_verificar_cavitacao_margens` |
| `submergencia_minima` | S = D(1 + 2,3 Fr_D), Fr = V/sqrt(gD); so a submergencia, geometria completa do poco e da norma (nao aberta) | ANSI/HI 9.8 | `test_submergencia_hi98` |
| `numero_de_conjuntos`, `modulacao` | n = ceil(Q/Qb) + reserva; vazoes nominais k Qb | pratica de projeto | `test_numero_de_conjuntos_e_modulacao` |
| `rotacao_especifica` | nq = N sqrt(Q)/H^0,75 (rpm, m3/s, m); radial < 25, Francis 25-50, misto 50-100, axial > 100 (faixas aproximadas) | Macintyre; KSB | `test_rotacao_especifica_e_tipo_de_rotor` |
| `tempo_parada`, `inercia_minima_sugerida` | I dw/dt = -T (T constante ou ~ w^2); so cinematica, sem transiente (-> `transiente_moc.py`) | Wylie & Streeter; Chaudhry | `test_tempo_parada_e_inercia` |

## Modulo `ancoragem.py`

CLI: `python -m tools.dren.ancoragem --json '{"funcao": "...", ...}'`. Pressoes em Pa (ou `unidade_p`: kPa, MPa, bar, mca, kgf/cm2); forcas em N/kN/daN.

| funcao | formula | fonte | teste |
|---|---|---|---|
| `empuxo_em_curva(p,D,angulo,Q)` | F = 2 p A sin(theta/2) (estatica) + 2 rho Q V sin(theta/2) (dinamica); direcao -(90 - theta/2) graus (para fora da curva) | Porto cap. 7; CAC Quadro IV.1 | `test_curva_90_DN1000_10bar_estatica`, `test_irece_curva_*`, `test_cac_*` |
| `empuxo_em_reducao(p,D1,D2,Q,p2)` | F = p1 S1 - p2 S2 + rho Q (V1 - V2); estatica p (S1 - S2). **Armadilha:** a planilha do Irece usou so S_menor (2,9x menos) | momento linear | `test_irece_reducao_700_400_planilha_x_fisico` |
| `empuxo_reducao_planilha` | reproduz o erro da planilha (so auditoria) | doc 922 | idem |
| `empuxo_em_te`, `empuxo_em_tampao`, `empuxo_em_valvula_fechada`, `empuxo_em_extremidade` | F = p A (+ rho Q V na derivacao) | Porto cap. 7 | `test_extremidades_p_A`, `test_irece_te_*` |
| `resultante_vetorial` | soma de componentes; |R| e angulos | planilha Irece | `test_irece_resultante_no_1L2` |
| `pressao_de_ensaio_para_calculo` | 1,5 PN ou pressao maxima de transiente (escolha do projetista; NBR 12266/7665/12215) | norma | `test_pressao_de_ensaio_para_calculo` |
| `bloco_gravidade_pre_dimensionamento` | W = FS F/mu; V = W/gamma_c; A = W/sigma_adm. **[DELEGAR]** Geotecnia (taludes, passivo, sigma_adm) e Estruturas (armadura) | pratica; CAC W = 4F | `test_bloco_gravidade_*`, `test_cac_volume_do_bloco_W_igual_4F` |


### Transientes hidraulicos (`transientes.py`)

Golpe de ariete (stdlib; CLI `python -m tools.dren.transientes --json '{"funcao": ..., ...}'`). Teste: `tests/dren/test_transientes.py`; divergencias dos casos em `DIVERGENCIAS.md` (secao Transientes). Nivel: anteprojeto (padrao: celeridade, Joukowsky, Michaud, coluna rigida, pre-dimensionamento) e basico (MOC, a pedido).

| funcao | formula | fonte |
|---|---|---|
| `celeridade`, `celeridade_material`, `propriedades_material` | a = sqrt((K/rho)/(1 + K D c1/(E e))); c1 = 1 (c1: juntas), 1 - nu^2 (c2: ancorado), 1 - nu/2 (c3: ancorado a montante); tabela E, nu (aco, FoFo, concreto, PRFV, PEAD, PVC); aviso viscoelastico | Chaudhry 1979 p. 35-37; Wylie & Streeter 1993 |
| `joukowsky`, `tempo_critico`, `classificar_manobra`, `michaud_allievi` | dh = a dV/g; Tc = 2L/a; Michaud dh = 2 L V/(g T), T > 2L/a | Chaudhry 1979 p. 10-12; Michaud |
| `oscilacao_massa_chamine`, `estabilidade_thoma`, `chamine_de_equilibrio` | Z_max = Q0/A_ch sqrt(L A_ch/(g A_t)); T = 2 pi sqrt(L A_ch/(g A_t)); A_th = L A_t/(2 g alpha H); RK4 com atrito | Chaudhry 1979 cap. 10-11 |
| `parada_de_bomba_coluna_rigida`, `volante_de_inercia` | coluna rigida + I d(w^2/2)/dt = -P; bissecao em I | Karney & Nault 2019; Chaudhry cap. 4 |
| `moc_reservatorio_tubo_valvula` | MOC C+/C-, dt = dx/a (Courant 1), atrito quase-permanente, envoltorias e serie na valvula; vapor so sinalizado | Wylie & Streeter; Wichowski 2006; Lund 2007 |
| `moc_parada_de_bomba` | contorno de bomba (parabola homologa + inercia) e retencao; **sem Suter (limitacao declarada)** | Chaudhry cap. 4; Wylie cap. 12 |
| `reservatorio_hidropneumatico`, `tanque_unidirecional`, `ventosa` | RHO politropico n = 1,2 + coluna rigida; TUD por coluna rigida; A = Q_ar/v_ar | Boulos 2005; Parmakian; caso Irece EB2 |
| `pressao_de_projeto`, `envoltoria_vs_perfil` | V5: max(permanente + margem, envoltoria) -> PN 6/10/16/20/25; P = H - z, trechos < 0 e < pressao de vapor | criterio do projeto |


### Drenagem subsuperficial (`drenos.py`)

CLI: `python -m tools.dren.drenos --json '{"funcao": "...", ...}'`. Unidades: m, m/d (q e K), m3/s (tubos), dias. Teste: `tests/dren/test_drenos.py`; divergencias em `DIVERGENCIAS.md` (secao Drenos e dissipadores). ILRI 16 e FAO 38 **nao estao no corpus**: Ernst e as tabelas indicativas sao "a confirmar".

| funcao | formula | fonte |
|---|---|---|
| `hooghoudt_espacamento`, `d_equivalente_hooghoudt` | L^2 = (8 K2 d_e h + 4 K1 h^2)/q, d_e de Moody (d_e = d/(1 + d/L (2,55 ln d/r - C)); d/L > 0,31: L/(2,55 (ln L/r - 1,15))), iteracao em L | USBR Drainage Manual 1993, 5-5 (p. 155) e 5-11 |
| `donnan_espacamento` | L^2 = 4 K (b^2 - a^2)/q; dreno na barreira: q/2 | USBR 5-11 (ex.: 347 m) |
| `ernst_espacamento` | h = q Dv/Kv + q L^2/(8 KD) + q L ln(a Dr/u)/(pi Kr) | Ernst 1962 / ILRI 16 (a confirmar) |
| `glover_dumm_altura/tempo/espacamento`, `tempo_de_drenagem` | h_t = 1,16 h0 exp(-t/j), j = mu L^2/(pi^2 K d_med) | Glover/Dumm 1954; USBR 5-10 (31,8 d) |
| `vazao_de_dreno`, `capacidade_tubo_dreno`, `diametro_minimo_dreno` | Q = q L comprimento; Manning pleno (n 0,016/0,011) ou legado Xingo Q = 33,5 D^2,67 i^0,5 | Manning; Xingo doc 1419 |
| `dreno_de_fundo_de_canal_revestido`, `vazao_por_furo_geomembrana`, `vazao_infiltracao_geomembrana` | Q = q L / n tubos, DN pela faixa CSB; orificio Cd = 0,634; Q1m = Qc A1/2400 | CSB doc 1341:74-77; Xingo doc 1419:18-22 |
| `criterio_de_filtro_hidraulico` | D15f/D85s <= 4(5); D15f/D15s >= 4(5); geotextil: [DELEGAR: geotecnia] | Terzaghi |
| `porosidade_drenavel`, `recomendacao_indicativa`, `diagnostico_drenabilidade` | tabelas indicativas (aviso); decisao do Iuiu 2002 | FAO 38/ILRI (a confirmar); doc 1051:162 |

### Vertedouros e dissipadores (`dissipadores.py`)

CLI: `python -m tools.dren.dissipadores --json '{"funcao": "...", ...}'`. Reutiliza `canais` (secoes, `froude`, `y_critica`, `ressalto_hidraulico`). Teste: `tests/dren/test_dissipadores.py`. Curvas de L/y2, Ho/W_B e C do ogee **digitalizadas** dos graficos do corpus (+-2 %).

| funcao | formula | fonte |
|---|---|---|
| `vertedor_retangular` (delgada/espessa/ogee), `vertedor_triangular`, `coeficiente_implicito` | Kindsvater-Carter (Ce = C2 + C1 H/P, ft^0,5/s x 0,5521); 1,705 L H^1,5 (aviso); ogee C0(P/H0) x [C/C0](He/H0) x 0,5521 (2,18 SI), pilares/encontros; C = Q/(L H^1,5) | USBR WMM 2001 cap. 7; Small Dams 1987 9.12 |
| `vertedor_lateral_demarchi`, `vertedor_lateral`, `vertedor_linear_iuiu` | De Marchi simplificado (E constante, C_M = 0,50 a confirmar); legados Iuiu Le = 0,1Q/(1,84 he^1,5), Hmed = (Qe/(1,84 L))^(2/3) | Chow cap. 12; doc 1052 |
| `bacia_usbr` (I/II/III/IV/auto) | Fr1, y2 = C y1/2 (sqrt(1+8Fr1^2)-1) (C = 1,1 tipo IV), L = (L/y2)(Fr1) y2, blocos e soleiras, TW requerido e rebaixamento do piso (sobreafogamento <= 5 %) | EM-25 (Fig. 12-14, secoes 3-4); HEC-14 cap. 8.2-8.4 |
| `bacia_saf` | L_B = 4,5 y2/C/Fr1^0,76; blocos y1, defletores 40-55 %, soleira 0,07 y2/C | HEC-14 8.5 |
| `bacia_de_impacto_usbr_vi` | W_B = H0/(H0/W_B)(Fr), Tab. 9.2; Q <= 11,3 m3/s, V <= 15,2 m/s | HEC-14 9.4; EM-25 |
| `rip_rap_saida` | hs/ye = 0,86 (D50/ye)^-0,55 Fr - Co; Ls = 10 hs, L_B = 15 hs, W_B = Wo + 2 L_B/3 | HEC-14 10.1 (CSU) |
| `queda_vertical`, `escada_rand`, `bacia_queda_smetana`, `rampa_em_degraus` | Nd = q^2/(g h^3), Ld = 4,30 h Nd^0,27, y1 = 0,54 h Nd^0,425, y2 = 1,66 h Nd^0,27, L = 6,9 (y2-y1) (legado Jaiba); L = 6(D2-Dq) (legado Iuiu, Smetana); regime nappe/skimming (Chanson, a confirmar) | HEC-14 11.1.1; docs 1182, 1051 |
| `selecionar_dissipador` | lista ordenada por limites (Fr1, V1, Q, TW, material a jusante) com justificativa | HEC-14/EM-25 |


### `bueiros.py` v0.2.0 (2026-10-01)

Mudancas (detalhe no CHANGELOG da docstring e em `DIVERGENCIAS.md`): `dissipador_necessario(V, material, fonte="dnit", criterio="min")` usa a Tabela 31 do DNIT-DREN p. 131 (`LIMITE_VELOCIDADE_DNIT`; a tabela antiga ficou em `LIMITE_VELOCIDADE_MATERIAL_LEGADO`) e cita a fonte em `metodo`; `fonte_ke="hds5"|"dnit"` em `dimensionar_bueiro` e `comparar_legado_hds5` (`ke_entrada`); aviso de afastamento entre celulas cita DNIT-ES023 p. 4 e DNIT-ES025 p. 5.

| funcao nova | formula | fonte |
|---|---|---|
| `vazao_critica_legado_dnit`, `vazao_critica_exata` | legado: Vc = 2,56 H^0,5 (celular Q = 1,705 B H^1,5; tubular A_c = 0,60 D^2, ~7 % acima da exata); exata: dc + Vc^2/2g = H | DNIT-DREN p. 55-56 (Tab. 1 e 2) |
| `sarjeta_triangular_izzard` (CLI) | Q = (0,376/n) Sx^1,67 SL^0,5 T^2,67; T = [Q n/(Ku Sx^1,67 SL^0,5)]^0,375 | HEC-22 p. 79-80 (eqs. 5.2, 5.4; Ex. 5.1) |

Testes: `tests/dren/test_bueiros.py` (HDS-5 p. 273-274 e 280, HEC-22 p. 80, legados DNIT rotulados "legado", Ke, Tab. 31).

## hidrologia 0.2.0 (2026-10-02)

Correcoes vindas da redacao da skill `hidrologia-de-projeto-para-drenagem` (conferidas no primario): `dnos` conforme
DNIT-HIDRO p. 89 (forma antiga em `dnos_legado`); `mcmath` com `S_unidade` ("m/m" 0,0091 | "m/km" 0,0023) e aviso
sobre declividade do canal principal; `gumbel_P_TR(n=...)` com fator de frequencia de amostra finita; `chuva_efetiva`
converte CN para Ia = 0,05 S (`cn_para_lambda_005`); novas `blocos_alternados`, `risco_hidrologico`, `tr_para_risco`.
Testes novos a partir de DNIT-HIDRO p. 130, NRCS-NEH630-CH10 p. 19 e CH16 p. 16, HDS-2 p. 132, PMSP-V2 p. 21-22.
Suite: 381 passed, 22 xfailed. O agente que fez a edicao foi interrompido antes do relatorio; esta nota substitui-o.


## F5 (2026-10-08): módulos e funções novas

### bueiros

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


### canais_drenagem

| módulo | função | fórmula | fonte | teste |
|---|---|---|---|---|
| canais_drenagem 0.1.0 | `manning_trapezoidal`, `profundidade_normal`, `profundidade_critica`, `canal_trapezoidal`, `capacidade_trapezoidal` | Q = A R^(2/3) S^(1/2)/n; Fr = V/√(g A/T) (nunca y); Q²/g = A³/T | Manning SI; USACE-EM1110-2-1601 App. H Tab. H-1 p. 179; aviso Fr 0,89–1,13 FHWA-HEC11 p. 38 | test_canais_drenagem (livro 1 %; acervo Salitre DT 4.1.6/A, DS 4.1, Delmiro DS-1.1/C, gabião, sem ✓h, 5 %) |
| canais_drenagem | `manning_composto`, `profundidade_normal_composta` | seção dividida: Q = ΣAi Ri^(2/3) S^(1/2)/ni, interface fora do perímetro | Chow cap. 6 (sem página no corpus; teste só de consistência) | consistência |
| canais_drenagem | `velocidade_admissivel`, `verificar_velocidade`, `verificar_limites_alternativos` | Tab. 31 DNIT (via `bueiros.limite_velocidade`) ou Tab. 2-5 EM-1601 (fps→m/s); V_min sem padrão; dois limites do documento reportados | DNIT-DREN p. 131; USACE-EM1110-2-1601 Tab. 2-5 p. 25 | test_canais_drenagem (Salitre N2, Delmiro D4) |
| canais_drenagem | `n_riprap` | EM-1601: n = K·D90(min)^(1/6), K 0,034/0,036/0,038 (D em ft); HEC-11: n = 0,0395·D50^(1/6) | USACE-EM1110-2-1601 Eq. 3-2 p. 29; FHWA-HEC11 Eq. 20 p. 166 | test_canais_drenagem |
| canais_drenagem | `d50_riprap_hec11` | D50 = C·0,001 V³/(d^0,5 K1^1,5); K1 = [1−sen²θ/sen²φ]^0,5; Csg = 2,12/(Ss−1)^1,5; Csf = (SF/1,2)^1,5 | FHWA-HEC11 Eq. 6–9 p. 48–49 (expoente de Csf conferido na imagem), Exemplo 1 p. 78 (0,43 ft) | test_canais_drenagem (livro 1 %) |
| canais_drenagem | `borda_livre`, `verificar_secao`, `verificar_trechos` | folga = h − y_n ≥ 0,25·y_n (padrão provisório, decisão F7); % de trechos fora do critério | memorial Delmiro Gouveia (doc 1520 p. 129), caso acervo | test_canais_drenagem (Delmiro D1/D2, sem ✓h) |
| canais_drenagem | `reconciliar_extensoes` | Σ parcelas × total declarado; aponta parcela omitida | caso negativo Salitre N1 (74.884,41 × 72.858,41 m) | test_canais_drenagem |

Não implementado: D30 de rip-rap do EM-1601 Eq. 3-3 (Sf, Cs, CV, CT incompletos no texto); dissipador de saída de bueiro (D3, Hidráulico); velocidade admissível por tensão do HEC-15 (sem página confirmada).


### drenos

| módulo | função | fórmula | fonte | teste |
|---|---|---|---|---|
| drenos (0.2.0) | `d_equivalente_serie` | d = (πL/8)/(ln(L/πr0)+F(x)), x = 2πD/L, F = 2Σ ln coth(nx) (x>0,5) ou π²/4x + ln(x/2π) (x≤0,5) | ILRI-DPA16 Eq. 8.9–8.13, PDF 268 (impr. 270) | `test_ilri16_exemplo_8_2_d_serie`, `test_d_serie_ramos_e_limites` |
| drenos | `d_equivalente_hooghoudt` (Moody) | inalterada | USBR 5-5 p. 155; conferida com ILRI-DPA16 Tab. 8.1 (PDF 267) a < 1 % | `test_ilri16_tab_8_1_d_equivalente_moody` |
| drenos | `hooghoudt_espacamento(metodo_de="moody"\|"serie")` | L² = (8 K₂ d_e h + 4 K₁ h²)/q | ILRI-DPA16 Ex. 8.1 (65 m; série 64), 8.2 (vala, 72 m), 8.3 (95 m), PDF 276–279; Embrapa Maniçoba p. 3 (d=0, 16,96 m) | `test_ilri16_exemplo_8_1…8_3`, `test_hooghoudt_manicoba_dreno_na_barreira_16_96` |
| drenos | `elipse_espacamento` | S = √(4K(m²+2am)/q) | NRCS-NEH624-CH04 Eq. 4-8, PDF 63–66 (Ex. 1: 202 ft) | `test_elipse_neh624_exemplo_1` |
| drenos | `fator_geometrico_ernst` | a por Kb/Kt e Db/Dt, interpolação bilinear; Kb/Kt<0,1 → 1; >50 → 4 | ILRI-DPA16 Tab. 8.2, PDF 272 | `test_fator_geometrico_ernst_tabela_8_2` |
| drenos | `ernst_espacamento` (u padrão = πr) | h = qDv/Kv + qL²/(8ΣKD) + qL ln(aDr/u)/(πKr) | ILRI-DPA16 Eq. 8.17–8.21, PDF 270–272 | `test_ernst_u_padrao_semicirculo`, `test_ernst_waterlog_endrain_exemplo_4_sem_fator_a` |
| drenos | `ernst_duas_camadas_dreno_no_topo` | Eq. 8.23: Dv = h, Dr = Do, ΣKD = KbDb + Kt(Do + h/2), a pela Tab. 8.2 | ILRI-DPA16 Ex. 8.4, PDF 280–281 (L = 38 m; 0,01/0,15/0,54 m) | `test_ernst_ilri16_exemplo_8_4_38_m` |
| drenos | `glover_dumm_*` (parâmetro `fator`) e `d_medio_glover_dumm` | h_t = 1,16 h0 e^(−αt), α = π²Kd/(μL²); L = π√(KDt/(μ ln(1,16 h0/ht))); fator 4/π = 1,27 para freático inicial horizontal | **fator 1,16 conferido**: ILRI-DPA16 Eq. 8.31–8.33, PDF 284 (impr. 286); Embrapa Maniçoba p. 2–3 (12,72 m) | `test_glover_dumm_manicoba_12_72_m`, `test_glover_dumm_fator_116_ilri16`, `test_d_medio_glover_dumm_criterios_divergem` |
| drenos | `capacidade_tubo_parcial` | Manning, círculo parcialmente cheio, geometria exata (θ = 2 acos(1−2y/D)) | Chow cap. 5; caso Delmiro 1492:105 | `test_tubo_parcial_meia_secao_e_geometria_exata`, `test_delmiro_*` |
| drenos | `vazao_unitaria_darcy_dreno_fundo`, `comprimento_maximo_dreno_fundo` | qd = K H²/X (2 lados); Lmáx = Q/qd | caso Delmiro (doc 1492:105–106), acervo, sem ✓h | `test_delmiro_qd_darcy_e_lmax` |
| drenos | `necessidade_envoltorio_ilri56` | HFG = exp(0,332 − 0,132K + 1,07 ln PI); iₓ = q1max/(Ks Ap/2) | ILRI-56 Fig. 7, PDF 47 (impr. 27) | `test_necessidade_envoltorio_hfg_ilri56` |
| drenos | `envoltorio_granular_pontos_controle` | pontos 1–7: D15c ≤ 7d85f; D50c = 5D15c; D100c ≤ 9,5 mm; D15f ≥ 4d15c; D15f = D15c/5; D5f > 0,074 mm; D60f = D60c/5; D85 > abertura | ILRI-56 PDF 66–68 (impr. 46–48) | `test_envoltorio_pontos_de_controle_ilri56` (consistência; o livro não traz exemplo numérico) |
| drenos | `faixa_K_por_textura`, `coeficiente_drenagem_tipico` | tabelas | ILRI-56 Tab. 14, PDF 175; PDF 42 | `test_tabelas_paginadas_ilri56` |

Tabelas ainda sem página (permanecem "indicativas"): `POROSIDADE_DRENAVEL` por textura (só o intervalo geral < 5 % a 35 % tem página: ILRI-DPA16 PDF 44) e `RECOMENDACAO_INDICATIVA` por classe de K (FAO-38 fora do corpus).


### estradas
| modulo | funcao | formula | fonte | teste |
|---|---|---|---|---|
| estradas | sarjeta_triangular (reusa bueiros.sarjeta_triangular_izzard) | Q = (0,376/n) Sx^1,67 SL^0,5 T^2,67 | HEC-12 p. 39-41; HEC-22 p. 79-80 | test_estradas (gabaritos 4-6, 1 % / 5 %) |
| estradas | sarjeta_composta | Izzard integrado por trechos: Q = (Ku/n) SL^0,5 {[d^(8/3)-y1^(8/3)]/Sw + y1^(8/3)/Sx}; Eo = Qw/Q | HEC-12 p. 41-43 (Eo da Chart 4 so como conferencia) | gabarito 7 (Eo 0,694 x 0,69; Q 3,10 x 3,0 ft3/s, 5 %) |
| estradas | valeta_manning | Manning trapezoidal; Fr = V/sqrt(g A/T) | IME p. 53-54 | round-trip e conferencia a mao |
| estradas | vazao_por_metro, comprimento_critico, valeta_comprimento_critico | q = I sum(C w)/3,6e6; L = Q_Manning/q; hmax padrao 0,8 h | IME p. 53-55 e p. 84 (eq. 4.19); caso Xingo VPC-1 | acervo sem check-h, 5 %: 162,57 m (i 0,001) e 1259,2 m (i 0,060) |
| estradas | folga_valeta | f = 0,2 h (terra, Q <= 0,3 m3/s); Tab. 4.2 (concreto) | IME p. 54-55 | test_folga_ime |
| estradas | caixa_coletora_grelha | Qi = 1,66 P d^1,5; Qi = 0,67 A sqrt(2 g d); menor (capacidade) / maior (carga) | HEC-12 p. 86 eqs. 17-18 | test_caixa_coletora_grelha_hec12_p86 |
| estradas | dreno_profundo_contribuicao / _capacidade / _comprimento_critico | q = K(H^2-d^2)/(2X); Scobey 0,2113 C D^2,625 I^0,5; HW 0,2785 C D^2,63 I^0,54; L = Q/q | IME p. 82-84 | test_dreno_profundo_* (consistencia; a fonte nao traz exemplo numerico) |
| estradas | criterio_projeto | tc adotado = max(tc, tc_min); tc_min 5 min e TR 10 anos: padrao PROVISORIO | IPR726 p. 258; WSDOT p. 102 | test_criterio_projeto_padrao_provisorio |

Nao implementado: descida d'agua em degraus/rapida (sem formula com pagina no corpus; so desenhos, Album p. 40-47); folga de terra para 0,3-10 m3/s (EQ 4.7 do IME ilegivel); K = 100 d10^2 (unidade ambigua no IME p. 83).


### hidrologia
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

