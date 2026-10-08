## README

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

## DIVERGENCIAS

| item | fonte A | fonte B/acervo | tratamento |
|---|---|---|---|
| Ernst, exemplo de Ritzema (q = 7 mm/d, h = 0,7, Kt = 0,5, Kb = 2,0) | WATERLOG-ENDRAIN p. 10: 0,014 L² + 1,18 L − 98,6 = 0 → **51,8 m** | ILRI-DPA16 Ex. 8.4, PDF 280–281: 0,014 L² + 2,045 L − 98,6 = 0 → **38 m** (a = 3,9 da Tab. 8.2) | A nota WATERLOG omitiu o fator geométrico a (reproduz-se com a = 1: 51,4 m, −0,8 % de 51,8). A divergência de 3,5 % do mapa (G4, #7) era uma leitura errada: a diferença real é 36 %. Padrão da calculadora = ILRI-16 (38 m). Teste com a = 1 documenta a origem. |
| Ernst, perímetro molhado u | v0.1.0: u = 2πr | ILRI-DPA16 Eq. 8.14, PDF 268: u = π r0 (semicírculo); Ex. 8.4: u = 0,157 m para r0 = 0,05 | v0.2.0 usa u = π r por padrão (aumenta a resistência radial e reduz L); `u` é argumento. |
| Hooghoudt: d equivalente | Tab. 8.1 de Hooghoudt (r0 = 0,10), ILRI-DPA16 PDF 267, e forma de Moody (USBR p. 155): reproduzem a tabela a < 1 % | Série exata (ILRI-16 Eq. 8.9–8.13): 2–3 % abaixo da Tab. 8.1 (D = 5, L = 75: 3,40 contra 3,49); 0,2 % do Ex. 8.2 | `metodo_de="moody"` é o padrão; `"serie"` opcional (ILRI-16: 64 m no Ex. 8.1 contra 65 m da tabela). |
| Glover-Dumm: profundidade média de fluxo D | USBR 5-10: D = d_e + h0/2 (t = 31,8 d) | Embrapa Maniçoba p. 3: D = D0 + (h0 + ht)/4 (t = 34,4 d no mesmo exemplo, +8 %); ILRI-16 Eq. 8.29: D = d_e | `d_medio_glover_dumm(criterio=…)`; padrão "usbr"; declarar o critério no parecer. Fator 1,16 já conferido (ILRI-16 PDF 284: freático inicial em parábola; 1,27 se horizontal). |
| Hooghoudt, termo extra | WATERLOG-DRAINAGE-EQUATION p. 2: fator (Di−Dd) | EMBRAPA-ESPACAMENTO-1990 p. 5; ILRI-16 Eq. 8.7: forma sem o fator | Não copiado (dimensionalmente inconsistente). |
| Dreno de fundo Delmiro: capacidade do tubo | Memorial (doc 1492:105): DN170 Q = 1,518e-4 m³/s; DN230 4,929e-4 m³/s (n = 0,016, S = 3e-4, meia seção) | `capacidade_tubo_parcial`: D int. 0,149 → 1,05e-3 (6,9×); 0,200 → 2,31e-3 (4,7×); razão entre DN deveria ser 2,19 (D^8/3) e o memorial dá 3,25 | 2 `xfail(strict=True)` (`test_delmiro_capacidade_dn170/230_declarada`); sem ajuste de fórmula; sessão interativa pendente (S do tubo ≠ 3e-4? n? transcrição?). qd e Lmáx = Q/qd reproduzem (1 %). USBR mediu até 1,2× o Manning pleno com carga sobre o tubo (ILRI-56 PDF 46), insuficiente para explicar 4,7–6,9×. |
| Viés do Hooghoudt | Embrapa Maniçoba p. 1 e 8 (campo): superestima L em 13,5–35 % | Embrapa 1990 p. 10 (laboratório): subestima −21 % | Aviso na docstring de `hooghoudt_espacamento`; incerteza a declarar no parecer. |
| NEH 624, Exemplo 2 (196 ft) | Solução gráfica da elipse modificada (Fig. 4-29), r do dreno não dado | — | Não implementado (gráfico); a elipse (Ex. 1, 202 ft) está implementada e testada. |
