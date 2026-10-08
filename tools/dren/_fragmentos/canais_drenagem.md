## README

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

## DIVERGENCIAS

| item | fonte A | fonte B/acervo | tratamento |
|---|---|---|---|
| n de rip-rap | EM-1601 Eq. 3-2 p. 29: n = K·D90(min)^(1/6), K 0,034–0,038 | HEC-11 Eq. 20 p. 166: n = 0,0395·D50^(1/6) | Diâmetros representativos diferentes; `n_riprap` implementa os dois (argumento `metodo`) e avisa; sem conciliação (F7) |
| velocidade admissível | DNIT-DREN Tab. 31 p. 131 (areia fina 0,30–0,40 m/s) | EM-1601 Tab. 2-5 p. 25 (areia fina 2,0 fps = 0,61 m/s) | `velocidade_admissivel(fonte=...)` obriga a escolha; padrão "dnit" (já adotado em bueiros.py) |
| limite de V do Salitre | memorial 0,30–1,2 m/s | planilha 0,3–1,5 m/s (DS-4.1 V = 1,307) | `verificar_limites_alternativos` devolve o resultado para cada limite e sinaliza conflito |
| folga de dreno | memorial Delmiro: mínima 25 % do tirante | planilha: 84 de 194 trechos abaixo (acervo B); ZTT01 em DT-2.23.1 transborda (y 0,331 × h 0,20 m) | 25 % entra como argumento (padrão provisório, decisão F7); `verificar_trechos` reporta % fora do critério |
| extensão total Salitre | texto: 72.858,41 m | soma das parcelas: 74.884,41 m (falta Mulungú 2.026,00 m) | `reconciliar_extensoes`; gabarito é B, conferência humana pendente |
| EM-1601 × HEC-11 (estabilidade) | D30 por V_SS local (Eq. 3-3) | D50 por V médio e SF (Eq. 6) | só HEC-11 implementado; não comparar D30 e D50 sem a graduação |
