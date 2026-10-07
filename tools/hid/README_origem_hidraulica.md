# tools/hid - calculadoras hidraulicas verificaveis

Convencoes (D5, D10, D14): SI em toda interface (m, m3/s, m/s, Pa ou m.c.a. declarado, kg/m3);
nomes em portugues sem acento; cada funcao publica tem docstring com formula, fonte e faixa de
validade; cada modulo tem CLI que imprime JSON com `entradas`, `saidas`, `metodo`, `avisos`, `versao`.

```
cd "<RAIZ>"            # Especialista Hidraulica
set PYTHONIOENCODING=utf-8
python -m tools.hid.perdas --json "{\"funcao\": \"hf_darcy\", \"Q\": 0.1, \"L\": 500, \"D\": 0.3, \"eps\": 1e-4}"
python -m tools.hid.perdas --funcao hf_hazen_williams --Q 0.47 --L 4596 --D 0.7 --C 130
python -m tools.hid.canais --json "{\"funcao\": \"y_normal\", \"secao\": {\"tipo\": \"trapezoidal\", \"b\": 5, \"z\": 1.5}, \"Q\": 22, \"n\": 0.0142857, \"S0\": 0.00015}"
python -m tools.hid.<modulo> --listar        # lista as funcoes da CLI
```

Secoes na CLI de canais: `{"tipo": "trapezoidal", "b":, "z":}`, `retangular {b}`, `triangular {z}`,
`circular {D}`, `composta {partes: [{secao, cota_fundo, n}]}`.

Versao dos modulos: `perdas` 0.1.0, `canais` 0.1.0. Infra comum em `_cli.py`.
Python usado: o do sistema (Python 3.14, pytest 9.1, numpy 2.4); o `.venv` de "Especialista Orcamento" nao existe nesta
copia do Drive. Os modulos usam so a stdlib.

## Resultado dos testes (`python -m pytest tests/hid/test_perdas.py tests/hid/test_canais.py -q`)

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

Calculadoras de hidrologia de projeto e de bueiros (stdlib; CLI `python -m tools.hid.hidrologia|bueiros --json '{"funcao": ..., ...}'`). Testes: `tests/hid/test_hidrologia.py`, `tests/hid/test_bueiros.py`; divergencias dos casos em `DIVERGENCIAS_bueiros.md`.

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

Reutiliza `hf_darcy`, `hf_localizada`, `hf_hazen_williams` de `perdas.py`. CLI: `python -m tools.hid.bombas --json '{"funcao": "...", ...}'` (`--listar`).

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

CLI: `python -m tools.hid.ancoragem --json '{"funcao": "...", ...}'`. Pressoes em Pa (ou `unidade_p`: kPa, MPa, bar, mca, kgf/cm2); forcas em N/kN/daN.

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

Golpe de ariete (stdlib; CLI `python -m tools.hid.transientes --json '{"funcao": ..., ...}'`). Teste: `tests/hid/test_transientes.py`; divergencias dos casos em `DIVERGENCIAS.md` (secao Transientes). Nivel: anteprojeto (padrao: celeridade, Joukowsky, Michaud, coluna rigida, pre-dimensionamento) e basico (MOC, a pedido).

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

CLI: `python -m tools.hid.drenos --json '{"funcao": "...", ...}'`. Unidades: m, m/d (q e K), m3/s (tubos), dias. Teste: `tests/hid/test_drenos.py`; divergencias em `DIVERGENCIAS.md` (secao Drenos e dissipadores). ILRI 16 e FAO 38 **nao estao no corpus**: Ernst e as tabelas indicativas sao "a confirmar".

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

CLI: `python -m tools.hid.dissipadores --json '{"funcao": "...", ...}'`. Reutiliza `canais` (secoes, `froude`, `y_critica`, `ressalto_hidraulico`). Teste: `tests/hid/test_dissipadores.py`. Curvas de L/y2, Ho/W_B e C do ogee **digitalizadas** dos graficos do corpus (+-2 %).

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

Mudancas (detalhe no CHANGELOG da docstring e em `DIVERGENCIAS_bueiros.md`): `dissipador_necessario(V, material, fonte="dnit", criterio="min")` usa a Tabela 31 do DNIT-DREN p. 131 (`LIMITE_VELOCIDADE_DNIT`; a tabela antiga ficou em `LIMITE_VELOCIDADE_MATERIAL_LEGADO`) e cita a fonte em `metodo`; `fonte_ke="hds5"|"dnit"` em `dimensionar_bueiro` e `comparar_legado_hds5` (`ke_entrada`); aviso de afastamento entre celulas cita DNIT-ES023 p. 4 e DNIT-ES025 p. 5.

| funcao nova | formula | fonte |
|---|---|---|
| `vazao_critica_legado_dnit`, `vazao_critica_exata` | legado: Vc = 2,56 H^0,5 (celular Q = 1,705 B H^1,5; tubular A_c = 0,60 D^2, ~7 % acima da exata); exata: dc + Vc^2/2g = H | DNIT-DREN p. 55-56 (Tab. 1 e 2) |
| `sarjeta_triangular_izzard` (CLI) | Q = (0,376/n) Sx^1,67 SL^0,5 T^2,67; T = [Q n/(Ku Sx^1,67 SL^0,5)]^0,375 | HEC-22 p. 79-80 (eqs. 5.2, 5.4; Ex. 5.1) |

Testes: `tests/hid/test_bueiros.py` (HDS-5 p. 273-274 e 280, HEC-22 p. 80, legados DNIT rotulados "legado", Ke, Tab. 31).

## hidrologia 0.2.0 (2026-10-02)

Correcoes vindas da redacao da skill `hidrologia-de-projeto-para-drenagem` (conferidas no primario): `dnos` conforme
DNIT-HIDRO p. 89 (forma antiga em `dnos_legado`); `mcmath` com `S_unidade` ("m/m" 0,0091 | "m/km" 0,0023) e aviso
sobre declividade do canal principal; `gumbel_P_TR(n=...)` com fator de frequencia de amostra finita; `chuva_efetiva`
converte CN para Ia = 0,05 S (`cn_para_lambda_005`); novas `blocos_alternados`, `risco_hidrologico`, `tr_para_risco`.
Testes novos a partir de DNIT-HIDRO p. 130, NRCS-NEH630-CH10 p. 19 e CH16 p. 16, HDS-2 p. 132, PMSP-V2 p. 21-22.
Suite: 381 passed, 22 xfailed. O agente que fez a edicao foi interrompido antes do relatorio; esta nota substitui-o.
