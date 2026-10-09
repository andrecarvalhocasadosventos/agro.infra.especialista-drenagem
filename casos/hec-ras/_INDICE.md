# casos/hec-ras — índice (F4 incremental, 2026-10-09)

Origem: estudos HEC-RAS da TPF no Acervo CDV-TPF e no Data Room (só leitura; R0). Inventário: `INVENTARIO_TPF.md`.
Formato: `Agent Builder/modelos/BRIEF_CASOS.md`. **Nenhum número tem ✓h**; nada aqui é gabarito de calculadora antes de conferência humana.

| Caso | Arquivo | Tipo | Pergunta |
|---|---|---|---|
| HR-01 | `2026-10-09_tpf_sao-francisco_captacao_NA_2D.md` | positivo | NA da captação por vazão (2D) e cadeia Q posto → captação |
| HR-02 | `2026-10-09_tpf_sao-francisco_malha_e_convergencia.md` | positivo c/ ressalva | malha, n, condição inicial, estabilização (lido do `.hdf` com h5py) |
| HR-03 | `2026-10-09_tpf_sao-francisco_contorno_jusante_sem_calibracao_NEGATIVO.md` | **negativo** | declividade 0,01 % × 0,0093 %; sem calibração, sem sensibilidade de n |
| HR-04 | `2026-10-09_tpf_riachos-recife-ferreira_manchas_2D.md` | positivo | manchas TR 2-100; picos de entrada × Tab. 8; Tc de Kirpich |
| HR-05 | `2026-10-09_tpf_riachos_premissas_sem_dado_NEGATIVO.md` | **negativo** | malha 50 m, n 0,040, sem ARF, jusante, 589,69 m³/s sem origem |
| HR-06 | `2026-10-09_tpf_rio-verde_standard-step_travessia_NEGATIVO.md` | **negativo** | NA 397 m: TR 50 × 100, Q, contorno na soleira, seção sintética |

6 casos (3 positivos, 3 negativos). Sem caso de 1D com ponte/bueiro (a TPF não entregou modelo 1D: ver `INVENTARIO_TPF.md` §3); QTR500 e TR 10/25 dos riachos só pelo texto.

## Sugestões para `evals/casos_numericos.yaml`
1. Regionalização: Q_capt = Q_posto · (435.392/345.341) · (1.032/1.052); tolerância 0,5 % contra a Tab. 4 (783,77 a partir de 633,41).
2. IDF GAM: i(TR 100, 1.440 min) = 7,74 mm/h; i(TR 2, 5 min) = 103,42 mm/h (Tab. 1).
3. Kirpich do relatório: SB7 do rio Verde = 42,82 h pela fórmula contra 39,84 h na Tab. 6 (deve sinalizar divergência de 7,5 %).
4. Lag = 0,6 · Tc.
5. Vazão de referência de Muskingum-Cunge = 0,7 · Q máx. afluente (R1: 142,69).
