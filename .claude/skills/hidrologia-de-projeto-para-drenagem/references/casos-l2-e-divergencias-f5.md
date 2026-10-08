# Casos de acervo (L2) e divergências da F5 em hidrologia

Regra transversal (risco nº 1 do plano): projeto do acervo que diverge do método **não é corrigido em silêncio**. O parecer mostra o número do projeto, o número recalculado, a fonte do método e a consequência. Casos em `casos/drenagem/`; nenhum número deles tem ✓h (candidatos a gabarito). Páginas de acervo = `doc:pág`.

## 1. Delmiro Gouveia (CODEVASF 2016, Hydros): HUT da bacia BHD1, TR 50

Caso `2026-10-08_delmiro_gouveia_hut_bhd1_tr50_bransby_williams` (docs 1494:31-33, 64; 1492:155-157). Qualidade A na cadeia de 6 elos.

| Elo | Valor do projeto | Reprodução (`hidrologia.py` 0.3.0) |
|---|---|---|
| Dados | A 36,34 km²; L 13,21 km; desnível 32 m (J = 0,2422 %); CN 75,2; P pontual 118,23 mm; fra 0,95; P bacia 112,40 mm | — |
| Tc adotado | Bransby-Williams 7,53 h (a outra fórmula: 7,65 h) | `bransby_williams(13.21, 36.34, 0.2422)` = 7,53 h |
| Perdas | S = 83,77 mm; Pe total 50,99 mm | `retencao_S(75.2)`; `chuva_efetiva` (Ia = 0,2·S) |
| HUT | tp = 0,6·tc; ta = D/2 + tp = 4,99 h; tb = 2,67·ta = 13,32 h; Qp = 15,149 m³/s **por 10 mm** (o caso escreve "por mm") | `hu_triangular` devolve 1,515 m³/s por mm |
| Pico | 58,71 m³/s em t = 10,36 h | convolução com chuva uniforme em 8 blocos: 61,8 m³/s (+5,3 %), pico em 10,35 h |

O que a skill faz com isso:
- **O hietograma do projeto (polinômio cúbico por faixa de chuva, Quadro 3.3) não é recuperável**: o pico de 58,71 não reproduz (`test_delmiro_bhd1_pico_58_71`, xfail estrito); o tempo do pico confere (`test_delmiro_bhd1_tempo_do_pico_com_chuva_uniforme`). Não prometer reproduzir o pico; mostrar a faixa com blocos alternados e com chuva uniforme.
- **NERC chamado de "Kirpich"** (1494:31). A fórmula que dá 7,65 h é o NERC: 2,8·(L/√(H/L))^0,47 (L km, H/L em m/km). Kirpich de livro dá 4,92 h para os mesmos L e S (`tc` com `metodo: "kirpich"`, L 13.210 m, S 0,002422 → 295 min). Efeito: quem reimplementar o "Kirpich do Delmiro" com a fórmula de livro obtém Tc 36 % menor.
- **Velocidade em km/h sob "m/s"**: 13,21 km/7,65 h = 1,73 km/h = 0,48 m/s. O critério do próprio memorial (0,5 a 2,0 m/s, 1492:155) foi aplicado ao número na unidade errada; os dois Tc ficam abaixo de 0,5 m/s e o Tc adotado (0,49 m/s) também. Efeito na vazão: pequeno; efeito no processo: o teste de aceitação não funciona como descrito.
- **Declividade de BH4.5** (Quadro 3.50, 1492:142): impressa 0,0618; (250 − 236)/3.252,5 m = 0,0043 (razão 14,4). As outras 57 linhas conferem a 5 %. Se 0,0618 alimentou o Tc, a vazão saiu a favor da segurança; não rastreado. Teste: recalcular ΔH/L em toda linha do quadro de sub-bacias.
- **TR 5 e 20 para obras de estrada** (1492:157) × TR 25/50/100 de Baixio, Xingó e CAC: registrar como prática do projeto, sem escolher.
- **Constantes NERC (2,8; 0,47) e Bransby-Williams (0,615) sem fonte primária no corpus**: as funções existem para reproduzir o projeto. Aviso `não conferida` obrigatório; não usar em projeto novo. A forma clássica de Bransby-Williams tem outra constante (21,3 min, ver docstring).

## 2. CAC Trecho 1 (Jati/Cariús): racional até 3,5 km² e HUT acima

Caso `2026-10-08_cac_trecho1_hidrologia_racional_3_5km2_e_hut` (doc 1139:226-228, 239, 250). Qualidade B (sem exemplo numérico).

- Limite do racional **3,5 km²** (cita o Manual DNIT 2005, que não tem teto; ver `limite-area-metodos.md`). 428 bacias pelo racional, 20 por HUT (428/448 = 95,5 %).
- **C 0,20 (anteprojeto e licitado) → 0,40 (executivo); CN 65 → 85**, justificados por "energia das lâminas" vistas em campo, sem vazão observada. Tratar C 0,40 e CN 85 como calibração local do semiárido cearense, **não como valor de livro** (CN 85 é alto frente às tabelas do NRCS; conferir `cn-scs.md`). TR 100.
- Tc do HUT: Kirpich modificada **85,5·(L³/h)^0,385 min** (L km, h m) = 1,5 × 57. `kirpich_modificada_dnit(3.0, 20)` = 95,6 min (o caso dá 96 por conta própria). A Kirpich original aparece em 1128:106 (L em pés).
- Fórmulas impressas com erro provável de extração ou de redação (verificar no PDF antes de afirmar erro do projeto): "d = 7,5·tc" (a relação padrão é D = tc/7,5; com tp = d/2 + 0,6·tc daria tp = 4,35·tc); Pe = (P − 0,2S)/(P − 0,8S) sem expoente 2 e com sinal trocado (correto: (P − 0,2S)²/(P + 0,8S)); Qp = 2·A/Tb sem constante de unidade. A skill usa as formas do NRCS.
- Teste de seleção: A = 2,0 km² → racional no CAC (< 3,5 km²) e HUT no Xingó (≥ 2 km²). Citar o limite do projeto, não impor um.

## 3. CAC Castanhão: altura de chuva usada como intensidade

Caso `2026-10-08_cac_castanhao_estrada_acesso_valas_chuva_como_intensidade` (doc 1128:106-112), tipo negativo. P = 23,20 mm (altura em 5 min) entra no racional como se fosse mm/h: Q = C·P·A/3,6e6 reproduz as 7 valas do Quadro 5.6 (VC2 = 0,171 m³/s). Com i = P·60/tc = 278,4 mm/h, a vazão é **12 vezes maior** (VC2 = 2,05 m³/s, Q/Qf ≈ 5,5 contra a seção D 0,45 m, Qf 0,372). Como detectar: razão Q impressa / Q recalculada = tc/60. Ressalvas: o texto diz "altura (mm)"; se a planilha tratava P como mm/h, o erro é do texto; em ambos os casos 23,2 mm/h em 5 min no semiárido é inverossímil. P = 0,959·tc + 18,04 dá 22,84 mm em 5 min e as tabelas usam 23,20 (hipótese: 18,40). TR e fonte da "tabela 3" não informados. **Gabarito candidato: a calculadora deve apontar a diferença, não reproduzir 0,171.** Racional recalculado: `racional(C=0.6, i=278.4, A=4.411, unidade_area="ha")` = 2,05 m³/s (a função só aceita `km2` ou `ha`: converter 44.110 m²).

## 4. Divergências da F5 em hidrologia (`tools/dren/DIVERGENCIAS.md`, seção F5 "hidrologia")

| Item | Fonte A | Fonte B ou acervo | Tratamento na skill |
|---|---|---|---|
| Unidade do Tc de Picking | DNIT-HIDRO p. 88: "horas" | IME p. 29 (L 5 km, I 0,06 → 40 min) e tabela de velocidades do DNIT p. 97 | `picking` devolve minutos; "horas" do DNIT = erro de impressão; declarar |
| Faixa do Giandotti | literatura: 170 a 70.000 km² (não está no corpus) | DNIT-HIDRO p. 92: sem faixa; "pouco recomendável" em bacia pequena | aviso se A < 170 km²; faixa **não conferida**; não usar em drenagem de perímetro |
| Área de validade do Kirpich | PMSP-DRENURB-V2 p. 56: ≤ 0,5 km², S 3 a 10 %; McCuen p. 172 (física): 1 a 112 acres | DNIT-HIDRO p. 88: < 0,8 km² | declarar as três; aviso com L > 10 km (subestima Tc) |
| Coeficiente da onda cinemática | McCuen Eq. 3-47: 0,938 | planilhas internas (aba "FAA"): 0,933 | argumento `coef` (padrão 0,938, provisório, decisão F7); a aba "FAA" **não é FAA**, é onda cinemática |
| Limite de L no escoamento em lâmina | McCuen p. 165 (física): n·L/√S ≈ 100 (L ≤ 100 a 300 ft) | NEH-630 cap. 15 p. 12-13: L ≤ 100 ft (30,48 m), L máx = 100·√S/n (Eq. 15-9) | `tc_escoamento_aviso_lamina`; as planilhas (L 150 m e 141,86 m) violam os dois |
| Kerby | forma em m da `kerby` (1,44; 0,467) | McCuen Eq. 3-53 (0,83 em ft; 0,47): +2,6 % | equivalentes a 5 %; DNIT p. 86 traz outra forma, não implementada |
| Qp unitário do HUT em Delmiro | caso: "m³/s por mm", 2,08·A/ta = 15,149 | 0,208·A/ta = 1,515 por mm | 15,149 é por 10 mm; a função devolve por mm |
| Pico BHD1 TR 50 | 58,71 m³/s | 61,8 m³/s (+5,3 %) | xfail estrito; hietograma não recuperável |
| Constantes NERC e Bransby-Williams | caso Delmiro reproduz 7,65 h e 7,53 h | nenhuma fonte primária | funções "não conferidas" |
| Páginas do mapa G1 (McCuen) | mapa: "física" em alguns itens | Ex. 3-12 = p. 146 impressa (165 física); Kirpich, lag, Kerby p. 153-154 impressas (172-173 físicas) | citar física; impressa = física − 19 |
| Edição do NEH-630 cap. 15 | corpus próprio: maio/2010 (Eq. 15-4a/b; exemplos p. 18-21) | mapa do Hidráulico: rascunho out/2008 (Eq. 15-3a/b; exemplos p. 16-19) | citar a edição de 2010 (`LOC-NEH-TC-ESCOAMENTO-PLANO`) e dizer qual; padrão do agente: 2010 |
| TR por posição de plotagem | Pfafstetter p. 10: T = n/m ("californiano") | McCuen Eq. 5-5a: Weibull T = (n+1)/m | citar Pfafstetter só com o aviso; o Clima ajusta a série |
| C por TR | McCuen Tab. 7-9 p. 395: colunas "< 25 anos" e "≥ 25 anos"; usar a média da faixa | Eslamian p. 352: C igual para qualquer TR, com fator fa = 1,0 (2-10 anos), 1,1; 1,2; 1,25 (25, 50, 100 anos) e limite de 80 ha | ver `coeficiente-c-racional.md` 4; declarar qual |

Conferido nesta revisão na página física: McCuen p. 165 (n·L/√S ≈ 100) e p. 395 (colunas de C), p. 405 (Q = 0 se P < 0,2·S); NEH-630 cap. 15 p. 12 (Eq. 15-8, 0,007); Eslamian p. 352 (80 ha).

## 5. Mapa G1: onde estão os primários e os gabaritos

IDs do corpus próprio. "Física" = página do PDF (marcador `<!-- p. N -->`). Equações e tabelas de livro saíram ilegíveis do `_texto` em vários pontos: **ler na imagem** antes de calibrar.

| ID | O que serve ao Drenagem | Onde (física) |
|---|---|---|
| LOC-MCCUEN-HYDROLOGIC-ANALYSIS (2ª ed., 1998) | Tc: velocidade, lâmina, nove fórmulas (Kirpich com multiplicadores 0,4 e 0,2 para concreto/asfalto e canal revestido; lag; FAA com C); racional; SCS-CN; HU | Tc 158-173 (Ex. 3-12 p. 165; 3-13 p. 165-166; 3-14 p. 166-170); racional 394-401 (Tab. 7-9 p. 395; Tab. 7-10 p. 396; C ponderado p. 397; Ex. 7-11 p. 398-399); SCS 404-409 (Ex. 7-15 p. 405-406; 7-17/7-18 p. 408-409); HU adimensional e triangular 553-561 (Tab. 9-17 p. 556; Ex. 9-23 p. 557-559) |
| LOC-NEH-TC-ESCOAMENTO-PLANO (NEH-630 cap. 15, mai/2010) | lag, velocidade, lâmina (Eq. 15-8), Tab. 15-1, 15-3 | Eq. 15-4a/b p. 11; Eq. 15-8 p. 12; Tab. 15-3 p. 14; exemplos p. 18-21 |
| LOC-PLANILHA-ESCOAMENTO-PLANO-001 e -REDENCAO (2022) | onda cinemática com coef 0,933 (aba "FAA"), IDF de Redenção, tanque | aba "FAA" |
| LOC-ESLAMIAN-HANDBOOK-HYDROLOGY (cap. 16) | C (Tab. 16.1), CN urbano (Tab. 16.2), racional SI com fa e 80 ha | p. 350-353 |
| LOC-PFAFSTETTER-CHUVAS-INTENSAS (1957) | só localizar e citar: o Clima entrega a IDF. **Salvador (Ondina, posto 69) é o único posto da Bahia**; sem posto do semiárido baiano | método p. 7-21; exemplos p. 22-23; Quadro IV p. 27-33; α e β p. 393-398 |
| USGS-WSP1849 (Barnes, 1967) | n de canais naturais (50 canais, 0,024 a 0,075) | p. 11-14, 16-19 |
| USACE-EM1110-2-1413 | frequência coincidente (planície com dique): aderência baixa | p. 48, 100-110 |

Gabaritos G1 (valor do livro; testes de 1 % com função da calculadora; detalhe em `gabaritos-numericos.md` seção 2): McCuen Ex. 3-12 (onda cinemática e Eq. 3-48), Ex. 3-13 (velocidade, 16,2 e 9,1 min), Ex. 9-23 (lag, 1,34 h), Ex. 7-9 e 7-11 (racional), Ex. 7-15 a 7-18 (SCS-CN e ponderação de Q), NEH-630 cap. 15 p. 18 (lag 1,14 h) e p. 18-21 (velocidade, Tc 1,75 h), planilhas 001 e Redenção (9,0114 e 4,5032 min).
