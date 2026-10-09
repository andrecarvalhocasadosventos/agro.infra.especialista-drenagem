---
name: hidrologia-de-projeto-para-drenagem
description: >
  Transforma chuva em vazão de projeto para drenagem de perímetro irrigado: tempo de concentração (Kirpich, Kirpich
  modificada DNIT, DNOS, Picking, Ven Te Chow, NERC, Bransby-Williams, Giandotti, Dooge, lâmina NEH, lag SCS), método
  racional (C ponderado, limite de área), McMath, SCS-CN com hidrograma unitário e blocos alternados, TR e risco, o que
  consumir de chuvas-intensas-e-idf e os casos Delmiro Gouveia e CAC. Use quando: "vazão de projeto da bacia", "tempo
  de concentração", "Kirpich", "NERC", "método racional", "coeficiente C", "McMath", "curva CN", "hidrograma
  unitário", "hietograma", "TR × risco", "risco na vida útil", "a IDF recebida cobre o Tc?", "racional vale até quantos km²?". Não
  use para: bueiro e HW/D (use bueiros-e-travessias); sarjeta, valeta, descida (drenagem-de-estradas-e-plataformas);
  canal (canais-de-drenagem-e-macrodrenagem); dreno agrícola (drenagem-subsuperficial); ajustar IDF e séries
  (chuvas-intensas-e-idf, Clima); reservatório (reservatorios-e-pequenas-barragens); preço (engenheiro-de-custos).
---

# Hidrologia de projeto para drenagem de perímetro irrigado

Convenções, V-regras, delegação e parecer estão em `drenagem-fundamentos` e no perfil do agente; não se repetem. Tabelas longas em `references/`: `tc-formulas.md`, `coeficiente-c-racional.md`, `cn-scs.md`, `tr-por-obra.md`, `limite-area-metodos.md`, `delegar-climatologia.md`, `casos-l2-e-divergencias-f5.md`, `gabaritos-numericos.md`, `normas-e-referencias.md`. Páginas `[ID p. N]` = física do PDF.

## 1. Escopo e fronteiras

**Entrega:** vazão de pico (e, quando preciso, hidrograma) por bacia, TR e método, com Tc, C ou CN, IDF e faixa de validade declarados.

**Regra D7-Hid / D13-Clima (MATRIZ §2, ajuste ao Clima):** o Drenagem **consome** a IDF e a chuva de projeto entregues pela skill `chuvas-intensas-e-idf` (Especialista Clima: máximas anuais, GEV/Gumbel com IC 90 %, TR máximo 2n, desagregação com fonte, ARF) e a **cita**; não ajusta IDF nem desagrega série. Escolhe método e TR e calcula a vazão. Pedido: `[DELEGAR: clima]` (`references/delegar-climatologia.md`, com o contrato A1 a D2 do Clima).

**Fronteiras:**
- A obra que usa a vazão: bueiro e HW/D em `bueiros-e-travessias`; sarjeta, valeta, descida em `drenagem-de-estradas-e-plataformas`; canal em `canais-de-drenagem-e-macrodrenagem`. Esta skill entrega Q e termina.
- Dreno subsuperficial (recarga, K): `drenagem-subsuperficial`.
- Amortecimento em reservatório ou barragem: só se menciona que a duração da chuva deve ser bem maior que Tc [PMSP-DRENURB-V2 p. 33]; o cálculo é de `reservatorios-e-pequenas-barragens`.
- Grupo hidrológico (Ksat) e uso do solo final: `[DELEGAR: geotecnia]` e projeto agronômico (`[DELEGAR: irrigacao]`).
- Simulação distribuída de bacia grande: consultoria (D2-Hid: executivo fora); só se aponta (3.6).

**Nível de projeto:**
- Anteprojeto (padrão): racional ou McMath em bacia pequena, SCS-CN com HU triangular acima, Tc por duas fórmulas, IDF recebida do Clima, TR por obra com risco calculado. Margem de erro da vazão: sem valor no corpus: o DNIT mostra razão de 5 entre fórmulas de Tc em bacias < 2,5 km² [DNIT-HIDRO p. 85].
- Projeto básico: hietograma por blocos alternados com durações ≥ Tc, convolução com HU, ARC declarado e sensibilidade, calibração com vazão observada se houver.
- Executivo: conferir a projetista (D2-Hid; no pacote, nível de `PLANO.md` §1.3).

## 2. Dados mínimos específicos

Pedir antes de calcular; o que faltar vira premissa rotulada.

1. Bacia: área, comprimento do talvegue L, desnível H (ou S), declividade média, forma; delimitada em planta com divisor.
2. Uso e cobertura **final** (perímetro implantado), solo e grupo hidrológico (Ksat de Geotecnia), lençol raso ou camada restritiva.
3. TR de projeto e de verificação por obra (`references/tr-por-obra.md`) e vida útil.
4. IDF local com posto, n, faixa, IC e desagregação (ou P(t, TR) tabelada), **do Clima**; unidade declarada (mm/h, não mm).
5. Para HU: duração da chuva de projeto, distribuição temporal, ARC. Se há reservatório a jusante, o volume.
6. Vazão observada (posto, n de anos) na bacia ou em bacia semelhante.

## 3. Método por nível

### 3.1 Qual método por tamanho de bacia

As fontes divergem (80 ha no HDS-2 e na Eslamian; 2 km² no DAEE; 3 km² no PMSP; 4 a 10 km² na ABDER; sem teto no DNIT) e cada projeto do acervo usa o seu (50 ha, 100 ha, 350 ha, 2 km², 3,5 km² no CAC). **Ponto aberto F7: padrão provisório, decisão F7.** Tabela completa e regra do agente em `references/limite-area-metodos.md`. Regra operativa: racional puro até 80 a 100 ha; até 2 km² com Cd = A^-0,10 e conferência por McMath ou SCS-CN; de 2 a 3,5 km² só com justificativa e HUT de comparação; acima de 3,5 km² ou Tc > 1 h, SCS-CN com HUT. Duas vazões por métodos diferentes; adotar a maior com justificativa; diferença > 30 % exige explicação. Citar o limite do projeto analisado, nunca impor o do agente.

### 3.2 Tempo de concentração

Fórmulas, faixa, unidade e fonte: `references/tc-formulas.md`. Pontos operativos:
- Kirpich e California são **a mesma fórmula** (0,95·(L³/H)^0,385 h), calibradas em bacias pequenas: ≤ 0,5 km² (PMSP p. 56), 0,004 a 0,45 km² (HDS-2 p. 80), < 0,8 km² (DNIT p. 88); L > 10 km subestima Tc. McCuen: multiplicar por 0,4 (concreto, asfalto) ou 0,2 (canal revestido).
- **Kirpich modificada do DNIT** = 1,42·(L³/H)^0,385 h = Kirpich × 1,5 (1,425, diferença de 0,35 %), indicada para qualquer área e padrão sem dado observado [DNIT-HIDRO p. 90, 98]; o CAC usa 85,5·(L³/h)^0,385 min (= 1,5 × 57): com L = 3 km, h = 20 m dá 96,0 min; a calculadora (1,42 × 60 = 85,2) dá 95,6 min (−0,35 %). **DNOS** (K = 4, forma DNIT) é a outra indicada [p. 89]. Mostrar as duas e a razão.
- **Picking** (min; o DNIT imprime "horas", erro) e **Ven Te Chow** (min, I em %): conferidos no IME p. 29 (L 5 km: 40 e 39,8 min); só bacias pequenas [DNIT-HIDRO p. 88-89].
- **NERC e Bransby-Williams**: só para reproduzir projeto (Delmiro: 7,65 h e 7,53 h); constantes sem primário no corpus, aviso obrigatório. O que o Delmiro chamou de "Kirpich" é NERC (Kirpich dá 4,92 h).
- Giandotti: bacia grande, faixa não conferida; Dooge: 140 a 930 km², S em m/m; Kerby: só escoamento sobre o terreno (L ≤ 365 m).
- **Perímetro plano** (S < 0,5 %): várias fórmulas saem da faixa [NRCS-NEH650-CH02 p. 11]; usar o **método da velocidade**: lâmina (onda cinemática McCuen, coef 0,938; planilhas usam 0,933: divergência F7) ou lâmina NEH com P2 do Clima; raso concentrado (Tab. 15-3); Manning no canal. **Limite de L em lâmina: 100 ft (30,48 m), ou McCuen-Spiess L máx (ft) = 100·√S/n** [NRCS-NEH630-CH15 p. 12-13]; acima, avisar.
- Lag SCS (`tc_lag_scs`): bacias até ~8 km², CN de 50 a 95. Tc mínimo de bacia 15 min [ABDER-APOSTILA p. 67]; **Tc mínimo de drenagem superficial (5, 6 ou 10 min): ponto aberto F7**, de `drenagem-de-estradas-e-plataformas`. Duração da chuva do racional = Tc [DNIT-HIDRO p. 127].

### 3.3 Método racional

Q[m³/s] = C·i·A/3,6 (A em km², i em mm/h) = C·i·A/360 (A em ha) [DNIT-HIDRO p. 127; FHWA-HDS2 p. 181]. No `_texto` do DNIT sai "6,3"; é 3,6 (exemplo da p. 130: 0,1828 × 101,0 × 2,4/3,6 = 12,31 m³/s).

- i = IDF(t = Tc, TR) = P(Tc)·60/Tc. **P é altura em mm; i é mm/h.** Usar P como i erra por tc/60 (CAC Castanhão: 12 vezes).
- C por uso, solo, declividade e TR: `references/coeficiente-c-racional.md`. C ponderado por área (`c_ponderado`; McCuen Ex. 7-11: 0,412). Fontes divergem sobre C por TR (McCuen: colunas < 25 e ≥ 25 anos; Eslamian: C único com fa de 1,0 a 1,25); declarar.
- **Cd**: Q × A^-0,10 (A em km²) para bacias > 1 km² [DNIT-HIDRO p. 131] (`coef_distribuicao`); Burkli-Ziegler A^-0,15 com **A em ha** (obra urbana) [p. 132]. Não está em `racional`: dizer se multiplicou C ou Q.
- C por TR: C_T = 0,8·T^0,1·C10 (`coef_c_para_tr`) é do acervo (CSB); a equação-fonte do PMSP está em imagem (a confirmar); o FHWA não endossa [FHWA-HEC22 p. 56-57]. Só anteprojeto, rotulado.
- Vários trechos: maior tc para a bacia total, checando o tc menor [FHWA-HDS2 p. 183-184].
- **C e CN do acervo são calibração local, não valor de livro**: CAC passou C de 0,20 para 0,40 e CN de 65 para 85 por visita de campo, sem vazão observada. Apontar; não corrigir.

### 3.4 McMath

Q[m³/s] = 0,0091·C·i·A^0,8·S^0,2, i em mm/h, A em ha, S em m/m [doc 1051:317]. Origem: USBR, planejamento de drenagem agrícola, Q = C·i·s^0,2·A^0,8 (cfs, pol/h, s em m por 1.000 m, acres), C de 0,20 a 0,75 [USBR-DRAINAGE p. 57-58]. Conversão exata com S em m/m: 0,02832/25,4 × 1000^0,2 × 2,471^0,8 = **0,00915**; o 0,0091 do acervo e da calculadora fica 0,6 % abaixo; com S em m/km vale 0,0023 [EMBRAPA-DREN-SUP p. 5] (recalculado na F7).
- S é a declividade do **canal principal** da bacia [USBR-DRAINAGE p. 57], não a do dreno nem a média da bacia (`S_tipo` avisa); em % multiplica Q por 2,5 e em m/km por 4.
- C de McMath tem tabela própria (`coeficiente-c-racional.md` 1.5); não misturar com o do racional. Sem limite de área no corpus; Iuiu usa 50 a 400 ha (aviso da função fora disso).
- Caso Iuiu DP11 (A = 189 ha): projeto 2,34 m³/s, calculadora 2,90 (+24 %). Ver Armadilhas.

### 3.5 SCS-CN e hidrograma

Tabelas de CN, HSG, ARC e ponderação: `references/cn-scs.md`. Passos:
1. HSG por Ksat (Geotecnia); CN por uso, tratamento e condição; ARC declarado; S = 25.400/CN − 254 (mm); Ia = 0,2·S [NRCS-NEH630-CH10 p. 10]; P < Ia → Q = 0 [McCuen p. 405]. Ponderar o **escoamento** (`escoamento_ponderado`), não o CN, se os CN diferem muito.
2. Chuva de projeto P(t) do Clima e hietograma por **blocos alternados** (`blocos_alternados`): i(t) para t = Δ, 2Δ, …, td; acumulado; incrementos; maior bloco no centro e os demais alternados em ordem decrescente [PMSP-DRENURB-V2 p. 21-22]. Duração ≥ Tc; com reservatório, bem maior (3 e 6 h no PMSP) [p. 33].
3. Chuva efetiva incremental: `hietograma_para_efetiva`.
4. HU triangular SCS (`hu_triangular`): tlag = 0,6·Tc [NRCS-NEH630-CH15 p. 8]; ΔD = 0,133·Tc = Tc/7,5 [NRCS-NEH630-CH16 p. 16; DNIT-HIDRO p. 102]; ΔD ≤ 0,2 a 0,25·tp [DNIT p. 99]; tp = ΔD/2 + tlag; tb = 2,67·tp; qp = 0,208·A/tp **m³/s por mm** (A km², tp h; é o 484 inglês) [NRCS-NEH630-CH16 p. 33-34]. O "2,08" do Delmiro (15,149 é por 10 mm; por mm, 1,515) e o 726 do McCuen (Ex. 9-23, ft³/s): conferir a unidade antes de comparar.
5. Fator de pico 484: padrão; ~600 em terreno íngreme e ≤ 100 em plano e alagadiço [NRCS-NEH630-CH16 p. 34]. Perímetro plano: premissa com sensibilidade.
6. Convolução (`convolucao_hu`); pico = máximo. 

Limites do método: CN de 40 a 98; Ia = 0,2·S fixa o CN (Ia = 0,05·S exige outro conjunto: `cn_para_lambda_005` converte, com aviso); fraco com chuva pequena e CN baixo e mal no semiárido [NRCS-NEH630-CH10 p. 10, 25]; perda por transmissão em canal seco [p. 7].

### 3.6 Bacias maiores (só apontar)

Acima de ~50 km² ou com reservatórios e propagação: sub-bacias, hidrogramas, propagação e amortecimento = modelagem tipo HEC-HMS (consultoria, D2-Hid). O Drenagem entrega Tc, CN ou C, IDF, TR, hidrograma triangular e pico por sub-bacia, e a lista do que a consultoria modela. ARF: só o que o Clima entregar. Bacia > 400 km² com fluviometria: estatística de vazões [DNIT-HIDRO p. 34-35].

### 3.7 Estatística de máximos (consumir, não ajustar)

O ajuste (GEV, Gumbel, L-momentos, IC) é do Clima. Aqui só se confere: Gumbel por momentos (amostra infinita) **subestima o quantil em amostra pequena**; com n, X_T = x̄ + K(n, TR)·s [DNIT-HIDRO p. 35-37; FHWA-HDS2 p. 132, Tab. 5.13] (`gumbel_K`; n = 10, TR 25: 2,8468 contra 2,04; −11 % no quantil da série de teste). TR acima de 2n: incerteza grande (aviso da função e regra D1 do Clima).

### 3.8 TR e risco

TR por obra e prática do acervo: `references/tr-por-obra.md`. **Ponto aberto F7: TR de bueiro de perímetro irrigado (USBR 5 a 15 anos × acervo 25/50 e 100): padrão provisório, decisão F7.** J = 1 − (1 − 1/TR)^n [DNIT-HIDRO p. 24; PMSP-DRENURB-V2 p. 29] (`risco_hidrologico`, `tr_para_risco`). Reportar TR de projeto, TR de verificação e J na vida útil.

### 3.9 IDF

Forma i = a·TR^b/(t + c)^d (mm/h; t em min), vinda do Clima. Exemplos: CSB grupo 1 (a = 5.590,88; b = 0,241; c = 40,11; d = 1,091; doc 1341:36); Wilken: i = 57,71·TR^0,172/(t + 22)^1,025 mm/min, 10 a 1.440 min [PMSP-DRENURB-V2 p. 19]. `idf_potencial` aplica os parâmetros recebidos e avisa fora da faixa se `faixa_TR` e `faixa_t` forem passadas (passá-las sempre). Sinais de IDF emprestada: `delegar-climatologia.md` seção 3.

### 3.10 Chuva de projeto do semiárido baiano (lacuna declarada)

O corpus **não traz IDF, CN, C nem hietograma validados para o semiárido baiano.** Rastro do acervo (não gabarito): Iuiu P1dia TR 10 = 108,5 mm (Gumbel, doc 1051:320); P24h de TR 10 em Irecê e vizinhos 101,2 mm (doc 670:113); Plúvio 2.1 no CSB (doc 1341:36); Salvador é o único posto da Bahia no Pfafstetter. Consequências: (1) pedir IDF e chuva de projeto ao Clima com incerteza; (2) CN e C de tabelas americanas ou rodoviárias são premissa; (3) comparar dois métodos; (4) o CN concorda mal no semiárido [NRCS-NEH630-CH10 p. 25]; (5) calibrar com vazão ou evento conhecido; (6) rótulo "lacuna do corpus" no parecer.

## 4. Calculadoras (mapa fórmula → função → teste)

`python -m tools.dren.hidrologia --json '{"funcao": "<nome>", ...}'` (campos planos ou em `args`). No CLI: `idf_potencial`, `idf_tabela`, `tc`, `racional`, `mcmath`, `gumbel`, `chuva_efetiva`, `blocos_alternados`, `risco_hidrologico`, `tr_para_risco`, `hu_triangular`. O resto é Python (`from tools.dren import hidrologia`). A saída traz `avisos`: reproduzi-los no parecer. Versão 0.3.0.

| Cálculo | Função | Exemplo de entrada | Teste | Conferir nos `avisos` e unidades |
|---|---|---|---|---|
| IDF | `idf_potencial`, `idf_tabela` | `{"funcao":"idf_potencial","TR":100,"t":112,"a":5590.88,"b":0.241,"c":40.11,"d":1.091,"faixa_t":[10,1440]}` | `test_idf_potencial_csb_grupo1`, `test_idf_potencial_aviso_faixa`, `test_idf_tabela_interpola_log_e_avisa` | extrapolação em TR e t |
| Tc (CLI `tc` + `metodo`) | `kirpich` (L m, S), `california_culverts`, `kirpich_modificada_dnit` (L km, H m), `dnos` (A ha, L m, I %, K ou `terreno`), `picking` (L km, I m/m), `ven_te_chow` (L km, I %), `giandotti`, `dooge`, `kerby`, `nerc`, `bransby_williams`, `onda_cinematica`, `laminar_neh`, `lag_scs` | `{"funcao":"tc","metodo":"kirpich_modificada_dnit","L":2.9,"H":12}` | `test_kirpich_bacia_tipica`, `test_kirpich_equivale_as_formas_do_pmsp_e_do_mccuen`, `test_dnos_forma_dnit_p89`, `test_dnos_tabela_K_por_terreno_dnit_p89`, `test_ime_p29_exemplo_picking_chow_california`, `test_giandotti_forma_dnit_e_aviso_de_faixa`, `test_dooge_forma_pmsp_p57_unidades_e_faixa`, `test_cli_v03_metodos_novos_de_tc`, `test_xingo_kirpich_s1` | unidade de L por função; Python devolve h em `nerc`, `bransby_williams`, `giandotti`, `tc_laminar_neh`, `tc_lag_scs`, o CLI devolve min; `dnos_legado` não usar |
| Lâmina, velocidade | `tc_onda_cinematica`, `tc_laminar_neh`, `tc_escoamento_aviso_lamina`, `velocidade_concentrado_neh`, `velocidade_manning`, `tempo_viagem_min` | n 0,15, L 36,6 m, S 0,002, i 203,2 mm/h | `test_mccuen_ex_3_12_onda_cinematica_e_scs`, `test_neh630_cap15_laminar_e_velocidade_p18_21`, `test_aviso_limite_de_lamina_neh_100_ft`, `test_planilhas_escoamento_plano_001_e_redencao` | L > 30,48 m e nL/√S > 100; `coef` 0,938 ou 0,933 |
| Racional, C | `racional`, `c_ponderado`, `coef_c_para_tr`, `coef_distribuicao` | `{"funcao":"racional","C":0.25,"i":69.5,"A":211,"unidade_area":"ha","limite_km2":3.5}` | `test_racional_unidades`, `test_racional_aviso_acima_de_2km2`, `test_csb_bacia45_racional`, `test_iuiu_dp08_racional`, `test_mccuen_racional_ex_7_9_e_7_11` | A acima de `limite_km2` (padrão 2): declarar o limite; C ≤ 1 |
| McMath | `mcmath`, `vazao_adotada_iuiu` | `{"funcao":"mcmath","C":0.3,"i":41.9,"A":189,"S":0.0028}` | `test_mcmath_faixa`, `test_iuiu_criterio_media`, `test_iuiu_dp11_mcmath` (xfail) | A fora de 50 a 400 ha; `S_unidade`, `S_tipo` |
| CN, chuva efetiva | `chuva_efetiva`, `retencao_S`, `hietograma_para_efetiva`, `escoamento_ponderado`, `cn_para_lambda_005` | `{"funcao":"chuva_efetiva","P":129.54,"CN":75}` → 64,3 mm | `test_scs_chuva_efetiva_neh`, `test_hietograma_para_efetiva_soma_igual_total`, `test_mccuen_scs_ex_7_15_a_7_18_e_ponderacao_do_escoamento` | `lam` 0,05 converte o CN e avisa |
| Hietograma | `blocos_alternados` | `{"funcao":"blocos_alternados","a":3462.6,"b":0.172,"c":22,"d":1.025,"TR":5,"duracao_total":100,"dt":10}` | `test_blocos_alternados_wilken_tr5_pmsp_v2` | duração múltipla de dt |
| HU, convolução | `hu_triangular`, `convolucao_hu`, `tlag_de_tc` | `{"funcao":"hu_triangular","A_km2":3.234,"Tc_h":0.9633,"D_h":0.16055}` | `test_hu_triangular_geometria`, `test_baixio_hu_geometria_e_qp`, `test_convolucao_conserva_volume`, `test_delmiro_bhd1_cadeia_tc_s_pe_hut`, `test_delmiro_bhd1_tempo_do_pico_com_chuva_uniforme`; xfail: `test_baixio_hut_pico_tr25`, `test_delmiro_bhd1_pico_58_71` | passo D ≈ Tc/7,5; pico depende do hietograma |
| Risco, TR | `risco_hidrologico`, `tr_para_risco` | `{"funcao":"risco_hidrologico","TR":25,"vida_util":25}` → 64 % | `test_risco_hidrologico_e_tr_para_risco` | — |
| Gumbel | `gumbel` (CLI), `gumbel_K`, `gumbel_P_TR(n=...)` | `{"funcao":"gumbel","serie_maximos_anuais":[...],"TR":25}` | `test_gumbel_momentos_e_aviso`, `test_gumbel_K_n10_hds2_tab_5_13`, `test_csb_gumbel_iuiu_pdia` | n < 20; TR > 2n; sem `n` é amostra infinita |

**Sem função (cálculo documentado e rotulado, ou pendência):** Lag DNIT (Kn) e George Ribeiro; fator de pico variável; conversão AMC I/III; Cd dentro do racional; ARF (do Clima). Calculadora não é editada pelo agente (guardrails). Conferências com primário: `references/gabaritos-numericos.md`.

## 5. Critérios de projeto e verificação (antes de entregar)

1. **V8:** método compatível com a área e Tc, limite declarado com fontes (3.1); duas vazões por métodos diferentes; diferença > 30 % explicada.
2. **Tc:** mais de uma fórmula, razão entre elas, fórmula escolhida com faixa; unidade de L e da saída de cada função; Tc dentro da faixa da IDF; escoamento em lâmina ≤ 30,48 m.
3. **IDF (D7-Hid):** origem (posto, n, desagregação, IC), faixa, TR; i em mm/h; Q com o limite superior da IDF. Sem IDF, `[DELEGAR: clima]` e premissa rotulada (V12).
4. **C:** fonte, declividade, uso final, TR; C_T ≤ 1; Cd declarado. **CN:** HSG com Ksat (delegado), ARC com sensibilidade (II e III), Ia = 0,2·S, CN de 40 a 98.
5. **Sensibilidade mínima:** Tc ±20 %, C ±0,05 ou CN ±5, IDF no limite do intervalo. Dizer o quanto Q muda.
6. **TR (V8):** TR de projeto, de verificação e J na vida útil; o TR é premissa do contratante ou do projetista (D2-Hid).
7. **Projeto do acervo que diverge:** mostrar o número do projeto, o recalculado, a fonte e a consequência; **nunca corrigir em silêncio** (núcleo, seção 9).
8. **V1/V11:** comando e saída gravados; edição citada (IPR-715 2005, IPR-724 2006, HDS-2 3ª ed., HEC-22 4ª ed., NEH-630 cap. 10 e 16, USBR 1993, PMSP v. 2 2012, DAEE 2017); NEH cap. 15: 2010 no corpus próprio, rascunho de 2008 no do Hidráulico (dizer qual). Norma de rodovia ou de São Paulo é referência, não regra do perímetro.

## 6. Armadilhas do acervo e da calculadora (casos negativos)

Detalhe, números e testes dos casos: `references/casos-l2-e-divergencias-f5.md`.

| Armadilha | Onde | Como detectar e tratar |
|---|---|---|
| **Altura de chuva (mm) usada como intensidade (mm/h)**: vazão 12 vezes menor | CAC Castanhão 1128:106-112 | Recalcular Q = C·(P·60/tc)·A; razão Q impressa/recalculada = tc/60. A skill aponta, não reproduz 0,171 |
| **NERC rotulado "Kirpich"**; velocidade em km/h sob "m/s"; declividade de BH4.5 0,0618 contra 0,0043 | Delmiro 1494:31, 64; 1492:142 | Kirpich de livro dá 4,92 h, não 7,65 h; v = L/tc em m/s; recalcular ΔH/L de cada sub-bacia |
| Pico BHD1 58,71 m³/s não reproduzido (61,8; +5,3 %) | Delmiro 1494:64 | Hietograma polinomial não recuperável; geometria e tempo do pico conferem |
| C 0,20→0,40 e CN 65→85 sem calibração; "d = 7,5·tc"; Pe sem expoente 2 | CAC Trecho 1 1139:227-228 | Calibração local, não livro; formas do NRCS; verificar o PDF antes de afirmar erro |
| Limite do racional diferente por projeto (50, 100, 350 ha, 2 e 3,5 km²) | Iuiu, Baixio, CSB, Xingó, CAC | Declarar o limite e a fonte (`limite-area-metodos.md`) |
| McMath +24 % (2,90 contra 2,34 m³/s) no DP11 do Iuiu | `DIVERGENCIAS.md` | S e Tc usados são do dreno, não da bacia; coluna "i" sem rótulo (41,9 mm/h daria 2,34). Pedir S do talvegue; não ajustar a calculadora (D11-Hid: > 5 % vai a `DIVERGENCIAS.md`) |
| HUT do Baixio não reproduzido (6,03 contra 2,70 m³/s) | `DIVERGENCIAS.md` | Geometria confere (tp 0,658 h; tb 1,758 h; qp 10,22 por 10 mm; S 155,39 mm); hietograma (tabela T-K) e lâmina efetiva (3,3 mm) não estão no acervo |
| Picking em "horas" no DNIT | DNIT-HIDRO p. 88 | Minutos (IME p. 29; DNIT p. 97) |
| Onda cinemática com 0,933 e L > 100 ft; aba "FAA" que não é FAA | Planilhas 001 e Redenção | `coef` explícito; apontar o limite de L; Tti = 9,0114 e 4,5032 min reproduzem com 0,933 |
| `dnos_legado` (19,3 min) × `dnos` (45,5 min no mesmo caso) | `hidrologia.py` | Usar `dnos` (forma DNIT, K divide) |
| Unidade de L (`kirpich` em m; demais em km) e de saída (h × min) | `hidrologia.py` | Conferir `entradas` e o nome do campo |
| Gumbel de amostra infinita (K 14 % a 28 % menor que o K de n, n de 30 a 10, TR 25 e 100) | `gumbel_P_TR` | Usar K de n (HDS-2 Tab. 5.13) para TR ≥ 25; aviso só diz "n < 20" |
| "6,3" no lugar de 3,6; mm/min sob mm/h (Iuiu 1051:318); linha "Racional" com A > 350 ha que era HUT (CSB 1341:145) | DNIT `_texto` p. 127; Iuiu; CSB | Conferir o PDF e refazer a conta (Iuiu DP08: 0,83 m³/s) |
| CN "cultivado Boa" do DNIT (51 a 80) como cultura em fileira (NRCS: 67 a 89); CN ponderado com partes muito diferentes | DNIT Tab. 11; bacias mistas | `cn-scs.md` 3.3; ponderar Q |

## 7. Normas e referências

Resumo do que IPR-715, IPR-724, DAEE IT DPO 11 e FHWA HDS-2/HEC-22 exigem, e a lista de IDs com páginas-chave:
`references/normas-e-referencias.md`. Norma de rodovia ou de São Paulo é referência, não regra do perímetro.

## 8. Lacunas (o que o corpus não cobre e o que pedir)

- IDF, CN, C e hietograma do semiárido baiano: Clima, Geotecnia, contratante.
- Fonte primária de NERC e Bransby-Williams; faixa de Giandotti; Kerby do DNIT p. 86 (não implementado).
- C por TR com números de fonte aberta (só a forma do acervo, equação-fonte a confirmar); fórmula do Quadro 1 do DAEE; tabelas de c do DNIT (tc, A, CN, FP); parâmetros Pfafstetter dos 98 postos.
- TR de dreno parcelar, canal coletor e OAC de perímetro irrigado: só a prática do acervo; pedir ao contratante.
- Margem de erro da vazão por método; fator de pico em terreno plano; ARF do semiárido.
- **Decisões F7 em aberto:** limite de área do racional; TR de bueiro de perímetro; Tc mínimo de drenagem superficial; coeficiente 0,938 × 0,933 da onda cinemática; edição do NEH cap. 15.
- Testes sugeridos para `tests/dren`: `kirpich_modificada_dnit(3,0; 20)` = 95,6 min (CAC, doc 1139:228); razão 60/tc do CAC Castanhão (doc 1128:112; Q 0,171 contra 2,05 m³/s para VC2); recálculo de ΔH/L do Quadro 3.50 de Delmiro (1492:141-142; BH4.5 = 0,0043).

## Revisão técnica

2026-10-08, revisor Opus (F7, lote A). **16 itens amostrados: 11 conferidos, 5 corrigidos, 0 pendentes.** Conferidos no
primário: Q = C·i·A/3,6 e o exemplo 12,31 m³/s [DNIT-HIDRO p. 127, 130; o `_texto` imprime 6,3]; Cd = A^−0,10, A em km²
[p. 131]; DAEE IT DPO 11 (racional ≤ 2 km², TR 25 rural e 100 urbano, C ≥ 0,25, CN ≥ 60) [DAEE-IT-DPO11 p. 1-2]; lag SCS
(maioria < 2.000 acres, CN 50 a 95) [NRCS-NEH630-CH15 p. 11]; fator de pico 600 a ≤ 100 [NRCS-NEH630-CH16 p. 22, 34];
faixas do Kirpich (1 a 112 acres [FHWA-HDS2 p. 80]; < 0,8 km² [DNIT-HIDRO p. 88]; ≤ 0,5 km² [PMSP-DRENURB-V2 p. 56]);
Wilken 57,71/0,172/22/1,025 [PMSP-DRENURB-V2 p. 19]; K de Gumbel n = 10, TR 25 = 2,8468 × 2,04; chuva efetiva 64,3 mm.
Corrigidos: CAC 85,5 dá 96,0 min (o 95,6 é da calculadora, 1,42 × 60); Burkli-Ziegler com A em ha [p. 132]; McMath
0,00915 é a conversão exata (0,0091 fica 0,6 % abaixo); McCuen-Spiess com L em ft; rótulos D7, D2 e D11 eram decisões do
Hidráulico (agora D7-Hid, D2-Hid, D11-Hid); description sem "TR do bueiro" (é de `bueiros-e-travessias`) e com "a IDF
recebida cobre o Tc?" no lugar de "a IDF serve?" (colidia com `chuvas-intensas-e-idf`). §7 e §8 movidas para
`references/normas-e-referencias.md`. **Pendências para o André:** limite de área do racional e TR de bueiro de
perímetro (decisão, ver `DIVERGENCIAS.md` F7 Lote A); duas tabelas de TR (`tr-por-obra.md` aqui e `tr-por-tipo-de-obra.md`
em bueiros) a fundir na próxima edição.
