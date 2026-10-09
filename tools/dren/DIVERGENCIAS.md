# Divergencias: hidrologia.py e bueiros.py x casos do acervo

Regra (D11): divergencia > 5 % nao se corrige ajustando formula; o teste fica `xfail` e entra aqui.
Referencia do metodo: HDS-5 3a ed. (2012), Tabela A.1 (constantes conferidas no PDF do acervo, p.197 do arquivo).

| caso | valor do projetista | valor calculado | teste | hipotese |
|---|---|---|---|---|
| Baixio de Irece, BU-CP0-15 (folga ao TN) | folga 0,66 m (TN 408,31) | 408,31 - 407,846 = 0,464 m | `test_baixio_folga_ao_tn` | inconsistencia aritmetica do gabarito do caso (a cota 407,846 reproduz com 0,01 m); TN implicito seria 408,51. Conferir a planilha 897:1. |
| Baixio, legado (orificio, C=0,62) x HDS-5, obras BU-CP0-13 / 15 / 18 | HW legado 3,31 / 4,51 / 5,02 m | HDS-5 3,60 / 4,82 / 5,44 m (-8,0 / -6,4 / -7,8 %) | `test_baixio_legado_vs_hds5_5pct` | **Materia de treinamento.** Entrada hipotetica: alas 30-75 (a mais favoravel), L=40 m, TW=0. O orificio trata a entrada como afogada com C=0,62 e nao ve a contracao de entrada (regressao submersa do HDS-5, c e Y) nem o regime de transicao. Com entradas menos eficientes (alas 90/15 ou 0 graus) a diferenca sobe a -12 a -18 %. BU-CP0-27 e BU-CS1-01 ficam em -4,3 % (passam). O controle de entrada governa em todas (saida: 3,4 a 4,8 m). O legado subestima HW, ou seja, e contra a seguranca, sobretudo quando Q50 afoga a entrada. |
| CSB BTCC-N17 (3 cel. 2x2, i=0,0045) | Q = 39,18 m3/s | Manning n=0,015, y=1,5 m: 3 x 9,54 = 28,6 m3/s (-27 %) | `test_csb_btcc17_capacidade_manning` | V/Yo da Tab. 4.7 (1341:205) lidos errados pelo extrator ou tabela com outra lamina; 4,4 m/s ~ Q/A_total. Ja anotado no caso. Pelo HDS-5 o HW seria 2,83 m (HW/D ~ 1,4), dentro da ordem de grandeza; o projeto nao declara HW. |
| Xingo BU-01 / BU-06 / BU-24 (lamina supercritica) | y = 0,96 / 1,76 / 1,87 m; V = 3,10 / 4,46 / 4,36 | Manning normal: y = 0,83 / 1,42 / 1,50 m; V = 3,6 / 5,5 / 5,4 | `test_xingo_lamina_normal_vs_doc` | O projeto usa equacao da energia a partir da secao critica na entrada com K=0,5 (1419:154), nao escoamento uniforme; a lamina do doc e de perfil, nao de y normal. O caso ja avisa que Manning nao reproduz. A continuidade Q/(B y)=V confere (3,11 x 3,10). |
| Iuiu DP11 t1 (McMath, A=189 ha) | Q McMath = 2,34 m3/s | 2,90 m3/s (+24 %) com S=0,0028 (declive do dreno), Tc Kirpich 125 min, i=P1d/Tc | `test_iuiu_dp11_mcmath` | S e Tc da bacia (nao do dreno) nao constam do caso; coluna "i" do quadro 8.34 sem rotulo. i implicito de 41,9 mm/h daria 2,34; possivel i da IDF/Tc diferente. |
| Baixio, HUT-SCS BU-CP0-11 (A=323,4 ha, CN 62,04, TR 25) | Q = 6,03 m3/s | 2,70 m3/s (hietograma triangular 12 blocos de 55,56 mm) | `test_baixio_hut_pico_tr25` | Geometria do HU reproduz (tlag 0,578 h; tp 0,658 h; tb 1,758 h; qp(10 mm) = 10,22 m3/s) e S=155,39 mm. O pico depende do hietograma (tabela T-K e "Soma(p)": 71,5 mm em 1,44 h, nao recuperaveis do acervo) e da lamina efetiva (3,3 mm com 55,56 mm). |

## Reproduzem (dentro da tolerancia do caso)
Baixio: Manning 2,5x2,5 (V 4,136; Q 24,82), 2x2 (V 3,556), orificio TR50 (h 3,260; cota 407,846); Salitre BTCC1/2/7 e BDCC5 (V, 3 %); Jaiba (hf 0,024; NA montante 480,138 vs 480,13 com tol. 0,01 m; vale tambem com Q=2,44); CSB bacia 45 (Tc 112 min vs 114,09; i; Q 9,6 vs 9,58); Iuiu (Gumbel P1d, DP08 Q=0,83, criterio media McMath/CN); Xingo Kirpich S1 (9,08 h vs 8,91 h, +1,9 %); Baixio HU (geometria).

## Observacoes de metodo
- Constantes K, M, c, Y (Tabela A.1/A.2) conferidas no PDF. Correcao de uma lembranca: submersa 30-75 graus tem c=0,0347 (nao 0,0385).
- Transicao 3,5 < Ku Q/(A D^0,5) < 4,0: o HDS-5 usa curva tangente; aqui, interpolacao linear entre os pontos-limite.
- Arco: area/perimetro de elipse (aproximacao); usar dados de fabricante em projeto.
- Dooge (unidade de S), DNOS (expoentes, unidade de Tc) e Kirpich modificada DNIT 1,42 (doc 1341:46) nao foram conferidos na fonte primaria; avisos nas docstrings.
- Tabela de velocidades admissiveis (`LIMITE_VELOCIDADE_MATERIAL`) e simplificada (tipo Fortier-Scobey via HEC-15); conferir antes de uso.


## v0.2.0 (2026-10-01): divergencias entre fontes primarias (achados da skill bueiros-e-drenagem-superficial)

| item | fonte A | fonte B | tratamento no codigo |
|---|---|---|---|
| Ke de muros de ala **paralelos**, geratriz reta (caixa de concreto) | HDS-5 3a ed., Tabela C.2, **p. 216**: "Wingwalls parallel (extension of sides), square-edged at crown" = **0,7** | DNIT-DREN (IPR-724) Tabela 30, **p. 130** (impressa 126): "Muros de ala paralelos, geratriz reta" = **0,2** | Padrao HDS-5 (0,7, mais conservador). Parametro opcional `fonte_ke="dnit"` em `dimensionar_bueiro`/`comparar_legado_hds5` e `ke_entrada()` usa 0,2. Demais linhas da Tab. 30 coincidem com a C.2 (a linha "muro de testa paralelo ao aterro" do DNIT funde 0,5 e 0,2 do HDS-5). Efeito: He = Ke V^2/2g, so no controle de saida; o controle de entrada nao depende de Ke. Declarar a escolha no parecer. |
| Constante **Y** da entrada submersa, arco/elipse de chapa projetante (`arco_corrugado_projetante`) | HDS-5 Tabela A.2 (chart 34/3, 16-19/5, 41-43/3), **p. 198**: c = 0,0496, **Y = 0,57** | HDS-5 exemplo A.3.1, **p. 191** ("Chart 34, Scale 3"): c = 0,0496, **Y = 0,53** | O modulo usa 0,57 (tabela, tres linhas concordam; o 0,53 do exemplo e inconsistencia interna do manual). Teste `test_arco_projetante_usa_Y_da_tabela_A2_nao_do_exemplo` trava o valor. Efeito: HW/D submerso 0,04 D menor com 0,53 (a tabela e mais conservadora). |
| Limite de velocidade do material a jusante | `LIMITE_VELOCIDADE_MATERIAL` v0.1.0 (Fortier-Scobey simplificado, sem pagina) | DNIT-DREN Tabela 31, **p. 131** (impressa 127): areia fina 0,30-0,40; cascalho fino 0,50-0,80; argila 0,80-1,30; concreto 4,50 m/s etc. | v0.2.0: padrao = Tabela 31 (criterio "min" da faixa, conservador); tabela antiga mantida como `LIMITE_VELOCIDADE_MATERIAL_LEGADO` (ate 2x mais permissiva; concreto 6,0 x 4,5). Cascalho grosso e enrocamento nao existem na Tab. 31: caem no legado com aviso. |
| Vazao critica de bueiro tubular (metodo "como canal") | DNIT-DREN Tabela 1, **p. 55**: Vc = 2,56 D^0,5 (velocidade critica do retangulo aplicada ao circulo), A critica ~0,60 D^2; DN 1,00 = 1,53 m3/s | Exata (dc + Vc^2/2g = D; Fr = 1): DN 1,00 = 1,43 m3/s (dc = 0,689 m) | `vazao_critica_legado_dnit` reproduz a tabela (+-2 %) e fica **+7,7 %** acima da exata em qualquer DN (contra a seguranca); testes rotulados "legado". A_c = 0,60 D^2 e ajuste proprio a coluna da tabela. Celulares (Tab. 2, p. 56): 2x2 = 9,64 e 3x3 = 26,58 m3/s reproduzem (Q = 1,705 B H^1,5; o coeficiente impresso 1,638 nao e usado). |
| Fonte do aviso de afastamento entre celulas | v0.1.0 citava "HDS-5 cap. 3/HEC-14" (nao fixa afastamento) | DNIT-ES023 **p. 4**: folga de 0,30 m entre tubos (linha dupla/tripla) e 0,40 m lateral; DNIT-ES025 **p. 5**: folga lateral minima de 0,50 m por lado (celular) | Aviso reescrito com as duas ES. Sao folgas construtivas em vala, nao criterio hidraulico. |

Conferidos sem divergencia (testes novos, tolerancia 2 %): HDS-5 p. 279-281 caixa 1,524 m, Q = 8,495 m3/s, S = 0,02 (`ret_alas_90_15` 2,96 m x 2,94 m; `ret_muro_bisel_45` 2,61 m x 2,62 m); HDS-5 p. 273-274 DN 1,3716 m, Q = 5,663 m3/s (`circ_concreto_boca_sino_muro` 2,415 m x 2,41-2,44 m; V saida 4,64 m/s x 4,66 m/s); HEC-22 p. 80 Exemplo 5.1 (Q 0,051 -> T 2,755 m x 2,76 m; T 2,5 m -> Q 0,03947 x 0,0395 m3/s). Nota: o texto do exemplo HDS-5 p. 280 e a HY-8 p. 280 dao 2,94 m, e a velocidade de saida 6,47 m/s do mesmo exemplo nao foi testada (so a do exemplo p. 274).


## F5 (2026-10-08): divergências registradas pelos módulos

### bueiros

| item | fonte A | fonte B / acervo | tratamento |
|---|---|---|---|
| V de saída HDS-5 p. 280 (caixa 5×5 ft, Q50 8,495 m³/s, S 0,02) | SI do HDS-5: 6,47 m/s | CU do mesmo texto: 20,8 ft/s = 6,34 m/s (−2 %); HY-8: 19,61 ft/s = 5,98 m/s; calculadora (n 0,012): 6,45 m/s (−0,3 % do SI) | o texto não informa n; adotado 0,012. Com n 0,013 o resultado cai para 6,07 m/s (−6 %): o gabarito depende de n. Teste com 1 % contra o valor SI; CU e HY-8 registrados como comentário |
| A_c do tubular em regime crítico | DNIT-DREN Tab. 1 (p. 55): ajuste 0,60 D² | IME p. 151-152: θc = 4,0335 rad dá 0,601 D²; Qc impresso 1,533 D^2,5, recalculado 1,538 (0,3 %) | 0,601 é fórmula impressa (critério Ec = (3/2)A/T, exato só no retangular); 0,60 mantido no legado (0,2 %). Vazão crítica exata de Ec = D é ~7 % menor (já registrado) |
| EM 1110-2-2902 p. 71-72 (D-load do exemplo) | mapa G2: "Bf 6,098 não reproduz D0,01 = 57 com We = 175 130 N/m" | Bf = 1,431/(0,505 − 0,811/3) = 6,097 e D0,01 = 1,3 (145 940 + 175 130)/(1200 × 6,098) = 57,0 N/m/mm | resolvido: W_T = W_L + W_E e θ = 1/3 fixo (eq. 3-1 completa). Passa a ser teste de livro (1 %) |
| Fator de berço classe A em vala | TUBOS Tab. 4.1: 2,25 a 3,4 | EM Tab. 3-1: 2,5 | padrão provisório 2,25 (mínimo, a favor da segurança) com `alfa_A` e `fonte="em2902"` como opções; decisão F7 |
| n de Manning de tubo de concreto no teste do Xingó | legado Xingó: 33,5 D^2,67 i^0,5 | equivale a n = 0,3117/33,5 = 0,0093; com n de projeto 0,012-0,013 a capacidade cai 22-28 % | caso negativo documentado em teste; nenhum n decidido aqui (pendência do mapa G2) |
| Delmiro BUC-2..5, TR 20 e TR 50 | acervo (1493:282-285), sem ✓h | `tubo_parcialmente_cheio` reproduz y, V e Fr dos 8 casos dentro de 1 % (testes a 5 %) | sem divergência; y/D = 79 % de BUC-5 em TR 50 passa do critério provisório 75 % (aviso, decisão F7). Divergências de declividade e comprimento do caso (itens 1 e 2) continuam abertas |
| HDS-3 Ex. 12, 15, 17 (leitura de gráfico) | impresso: V 3,5 fps; V 6,0 fps; Sc 0,0026; Hc 8,4 ft | recálculo exato: 3,555; 6,077; 0,00266; 8,30 | 1,3 a 2,3 % (leitura de gráfico): testados a 5 %, rotulados "livro, leitura de gráfico" |

### canais_drenagem

| item | fonte A | fonte B/acervo | tratamento |
|---|---|---|---|
| n de rip-rap | EM-1601 Eq. 3-2 p. 29: n = K·D90(min)^(1/6), K 0,034–0,038 | HEC-11 Eq. 20 p. 166: n = 0,0395·D50^(1/6) | Diâmetros representativos diferentes; `n_riprap` implementa os dois (argumento `metodo`) e avisa; sem conciliação (F7) |
| velocidade admissível | DNIT-DREN Tab. 31 p. 131 (areia fina 0,30–0,40 m/s) | EM-1601 Tab. 2-5 p. 25 (areia fina 2,0 fps = 0,61 m/s) | `velocidade_admissivel(fonte=...)` obriga a escolha; padrão "dnit" (já adotado em bueiros.py) |
| limite de V do Salitre | memorial 0,30–1,2 m/s | planilha 0,3–1,5 m/s (DS-4.1 V = 1,307) | `verificar_limites_alternativos` devolve o resultado para cada limite e sinaliza conflito |
| folga de dreno | memorial Delmiro: mínima 25 % do tirante | planilha: 84 de 194 trechos abaixo (acervo B); ZTT01 em DT-2.23.1 transborda (y 0,331 × h 0,20 m) | 25 % entra como argumento (padrão provisório, decisão F7); `verificar_trechos` reporta % fora do critério |
| extensão total Salitre | texto: 72.858,41 m | soma das parcelas: 74.884,41 m (falta Mulungú 2.026,00 m) | `reconciliar_extensoes`; gabarito é B, conferência humana pendente |
| EM-1601 × HEC-11 (estabilidade) | D30 por V_SS local (Eq. 3-3) | D50 por V médio e SF (Eq. 6) | só HEC-11 implementado; não comparar D30 e D50 sem a graduação |

### drenos

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

### estradas
| item | fonte A | fonte B/acervo | tratamento |
|---|---|---|---|
| Tc minimo de drenagem superficial | 5 min [IPR726 p. 258; WSDOT p. 102; IME p. 53] | 6 min [Album p. 214, OCR]; 10 min [IPR726 p. 463, IS-239]; Xingo usa tc 10 min | argumento `tc_min` (padrao provisorio 5, decisao F7) + aviso |
| TR da drenagem superficial | 10 anos [IPR726 p. 258; IME DNER] | 25 anos ENGEFER [IME p. 53]; 5-10 [IPR726 p. 258/463] | argumento `TR` (padrao provisorio 10, decisao F7) + aviso |
| Declividade minima de sarjeta/valeta | 0,5 % [DERPR-ES-DR-01-23 p. 10] | 0,3 % (0,2 % plano) [HEC-12 p. 19]; Xingo calcula i = 0,1 % | aviso, sem bloqueio |
| Dreno profundo: meia secao x secao plena | texto IME p. 83 "fluxo a meia secao" | formulas (0,2113 = 0,269 pi/4; HW) do mesmo p. dao tubo cheio | calcula cheio; aviso; `fator_capacidade` opcional |
| Folga de valeta | f = 0,2 h [IME p. 54]; Tab. 4.2 concreto 10-18 cm [IME p. 55] | 0,5 ft (~0,15 m) fixos [WSDOT p. 109] | ambas documentadas; hmax padrao 0,8 h = regra observada no Xingo (nao declarada) |
| Xingo VPC-1 (acervo, sem check-h) | calculadora: L 162,57 m (i 0,001), 1259,25 m (i 0,060) | projetista: 162,54 e 1259,04 (desvio < 0,02 %); z = 1 deduzido, nao impresso | teste de 5 %, rotulado "acervo, sem check-h" |
| Xingo VPC-5/6/7 com mesmo hmax 0,24 m (acervo) | projetista repete capacidade 0,083 m3/s | regra 0,8 h daria 0,28 e 0,32 m: capacidade maior | teste confirma capacidade > 0,083 para VPC-7 |

### hidrologia
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

## Revisão de fórmula F5 (Opus, 2026-10-08)

Revisão por amostra das calculadoras F5 contra o primário (texto + imagem do PDF quando o texto perdeu expoente). Páginas = marcador `<!-- p. N -->` do `_texto` (DNIT-HIDRO, HDS-5, HDS-2, ILRI-DPA16 e HEC-22 estão no corpus do Hidráulico). Suíte após a revisão: 269 passed, 14 xfailed (eram 266 + 14; +3 testes novos, nenhum resultado existente mudou).

| item | veredito | fonte p. N | efeito |
|---|---|---|---|
| hidrologia `picking`: unidade | conferido | IME p. 29 (Eq. 3.5/3.8: 39,6 → 40 min); DNIT-HIDRO p. 88 | Minutos. O rótulo "horas" do DNIT é contradito pela própria p. 88 (velocidades médias de 5,4 e 8,6 km/h, só possíveis em minutos: em horas o exemplo do IME daria 0,13 km/h). Docstring reforçada; sem mudança de cálculo. |
| hidrologia `tc_onda_cinematica`: 0,938 × 0,933 | conferido | McCuen Eq. 3-47, p. 165 (Ex. 3-12: 0,938); HDS-2 3ª ed. Eq. 3.6, p. 70 (α = 0,93 CU; 6,9 SI) | 0,938 é a constante exata da dedução (720^0,4/89,4^0,6 = 0,9378). 0,933 é arredondamento publicado (HEC-22 2ª ed., fora do corpus). Diferença de 0,5 % no Tt. Docstring atualizada. Escolha do padrão: lista F7. |
| hidrologia `tc_lag_scs`: 1140 | conferido | NEH-630 cap. 15, Eq. 15-4a/b, p. 11 | lag = L^0,8 (S+1)^0,7/(1900 √Y); Tc = lag/0,6 → 1900 × 0,6 = 1140; (S+1) = 1000/CN − 9. Testes NEH p. 18 (1,14 h) e McCuen Ex. 9-23 passam. |
| hidrologia `nerc` (2,8; 0,47) | pendente F7 | sem primário (busca no corpus dos dois especialistas: nenhum NERC nem Watkins e Fiddes) | Só reproduz o caso Delmiro. Continua "não conferida". |
| hidrologia `bransby_williams` (0,615) | pendente F7 | sem primário no corpus | A forma SI usual na literatura (58 L/(A^0,1 S^0,2) min, S em m/km; Pilgrim e Cordery, fora do corpus) dá 0,610 com J em %. O 0,615 do caso fica 0,8 % acima: coerente, mas não conferido. Docstring anotada. |
| hidrologia `dnos` | conferido | DNIT-HIDRO p. 89 | (10/K) A^0,3 L^0,2/I^0,4, min, A em ha, L em m, I em %; tabela K confere com as 6 linhas. |
| hidrologia `kirpich_modificada_dnit` 1,42 | conferido | DNIT-HIDRO p. 88 (0,95) e p. 90 (1,42, "50 % maiores") | 1,5 × 0,95 = 1,425; o manual imprime 1,42 (−0,35 %). A implementação usa o 1,42 impresso, em h × 60. |
| bueiros `tubo_parcialmente_cheio`: geometria e Fr | conferido | HDS-3 Chart 55 (p. 76); recálculo independente | A = D²(θ − sen θ)/8, P = Dθ/2, T = D sen(θ/2), Fr = V/√(gA/T). Delmiro (D 0,80; n 0,015; S 0,005; Q 0,499): y 0,454, V 1,695, Fr 0,888, recalculado à mão. Ramo de busca até 0,82 D = ponto em que Q = Q pleno: correto. Ressalva: a faixa de aviso de Fr (0,9–1,1) difere da de `canais_drenagem` (0,89–1,13, HEC-11 p. 38); harmonizar na F7 (critério, não erro). |
| tubos eq. 2.6 (plano de igual recalque) | conferido no primário, com ressalva (pendente F7) | TUBOS p. 19 (eqs. 2.3–2.6) e p. 20 (sinal + para ρ·r_ap > 0; Tab. 2.1 p. 21 só tem valores positivos) | O código segue a forma impressa, e^(αλe) = αλe + αρr + 1. Ressalva: nessa forma (El Debs) λe não depende de hs. Na equação completa de Spangler (fora do corpus) λe depende de H. Comparar com o software ou com o manual da ACPA antes de liberar `carga_solo_aterro_positiva` para projeto básico. |
| tubos berço classe A em vala: 2,25 × 2,5 | conferido | TUBOS Tab. 4.1, p. 37 (2,25 a 3,4, "dependendo do tipo de execução e da qualidade de compactação"); EM 1110-2-2902 p. 71 (Concrete Cradle 2,5) | As duas tabelas foram transcritas corretamente. A escolha do valor é critério: lista F7. |
| bueiros V de saída HDS-5 p. 280 e n = 0,012 | conferido | HDS-5 p. 280 (6,47 m/s); p. 90 ("n = 0.012 for smooth walled culverts"); p. 212 (Chart 15B: caixa em controle de saída, n = 0,012); p. 297 (DG 3.4.3: RCB com n = 0,012) | O n = 0,012 não foi adotado livremente: é o n do ábaco usado na solução e o n típico do próprio HDS-5 para concreto. O teste a 1 % fica legítimo. Atualiza a linha "o texto não informa n" acima. |
| drenos Ernst u = π r | conferido | ILRI-DPA16 Eq. 8.14, p. 268 (u = perímetro de semicírculo, dreno meio cheio); Ex. 8.4, p. 281 (u = π × 0,05 = 0,157) | Correto. Não implementado: Eq. 8.15 (u = b + 2r0 para tubo em vala com envoltório), cabe passar `u` explícito. |
| drenos fator a de Ernst (Tab. 8.2) | conferido | ILRI-DPA16 Tab. 8.2, p. 272 (42 valores conferidos); Ex. 8.4, p. 281 | Linhas = Kb/Kt, colunas = Db/Dt (só essa orientação reproduz a = 3,9). O livro tira a média simples dos 4 vizinhos (3,925); a bilinear dá 3,90; os dois arredondam para 3,9. L = 38 m reproduzido. |
| drenos ILRI-56 Fig. 7 / HFG | conferido | ILRI-56 p. 47 (fluxograma) e Eq. 34, p. 167 do PDF (impr. 147, imagem: "K the hydraulic conductivity in m/d") | HFG = e^(0,332 − 0,132K + 1,07 ln PI), com K em m/d; i_x = q1max/(Ks Ap/2). Unidade de K confirmada na imagem. |
| drenos Glover-Dumm 1,16 e 4/π | conferido | ILRI-DPA16 Eqs. 8.29–8.33, p. 284 | 1,27 = 4/π (freático inicial horizontal), 1,16 (parábola de 4º grau, Dumm 1960); L = π√(KDt/μ)/√ln(1,16 h0/ht). Maniçoba 12,72 m recalculado à mão. |
| estradas sarjeta composta (5/3, 8/3) | conferido | HEC-12 p. 41–43; identidade algébrica com o Eo do HEC-22 | ∫y^(5/3)dy/S = (3/8)y^(8/3)/S por trecho; Ku = 0,376 ≈ 3/8 (o mesmo da triangular). Qw/Qs = (Sx/Sw)[(d/y1)^(8/3) − 1] leva exatamente a Eo = 1/{1 + (Sw/Sx)/[(1 + (Sw/Sx)/(T/W − 1))^(8/3) − 1]}: é a fórmula de Eo do HEC-22. |
| estradas hmax = 0,8 h | conferido (critério) | IME p. 54 (folga f = 0,2 h em valeta de terra, Q ≤ 0,3 m³/s) | 0,8 h = h − 0,2 h: coincide com a folga do IME, além de ser a regra observada no Xingó. A escolha entre 0,2 h, a Tab. 4.2 do IME e os 0,15 m do WSDOT fica na lista F7. |
| estradas `caixa_coletora_grelha`: vertedor × orifício | corrigido (aviso e docstring; fórmulas inalteradas) | HEC-12 p. 86 (eqs. 17–18) e p. 87 ("transition … results in interception capacity less than that computed by either") | O "menor dos dois" era chamado de conservador, mas perto da interseção d* a capacidade real é menor que as duas equações. Agora há aviso quando d (ou a carga calculada) fica entre 0,5 d* e 2 d*. Teste novo: `test_caixa_coletora_grelha_aviso_transicao_hec12_p87`. Versão 0.1.1. |
| canais `d50_riprap_hec11` | conferido | HEC-11 Eqs. 6–9, p. 48–49 (imagem); Chart 2, p. 79 (C = 1,61 SF^1,5/(Ss − 1)^1,5) | Eq. 6 em CU (0,001); conversão para SI equivale a 0,001 × 0,3048^−1,5 = 0,00594. O C entra depois da Eq. 6, como produto (a ordem é irrelevante); 2,12/1,2^1,5 = 1,613 = o 1,61 do Chart 2. Teste novo, livro com leitura de gráfico, 5 %: Ex. 2 (Ss 2,60; SF 1,6; C 1,6; D50 1,44 ft; recálculo 1,49 ft, +3,7 %). |
| canais seção composta | corrigido (fonte e aviso; fórmula inalterada) | USACE-EM1110-2-1601 Sec. 5-6d, Eq. 5-24, p. 60 (conveyance method por subseções canal/bermas); James e Brown (1977) na mesma página | A fonte agora está no corpus. Novo aviso para 1,0 < y/h_main < 1,4 (Manning impreciso com lâmina rasa na berma, sem ajuste). Teste `test_composto_aviso_lamina_rasa_na_berma_em1601_p60`. Ressalva: o Fr de seção composta (A/T da seção toda) é indicativo. Versão 0.1.1. |
| canais aviso de Froude 0,89–1,13 | conferido | HEC-11 p. 38 ("transition zone occurs between Froude numbers of 0.89 and 1.13") | Correto; ver a ressalva de harmonização em `tubo_parcialmente_cheio`. |

### Decisões do André (sessão F7)

Escolha entre fontes ou critério normativo. Não são erros de fórmula.

| decisão | alternativas | recomendação do revisor |
|---|---|---|
| coeficiente da onda cinemática | 0,938 (dedução exata, McCuen) × 0,933 (planilhas, HEC-22 2ª ed.) × 0,93 (HDS-2) | 0,938 como padrão; 0,933 só para reproduzir as planilhas (0,5 %) |
| berço classe A em vala | 2,25 (mín. TUBOS) × 2,5 (EM 2902) × até 3,4 (TUBOS, compactação controlada) | 2,25 em anteprojeto; 2,5 só com berço executado e fiscalizado; > 2,5 só com justificativa |
| NERC e Bransby-Williams | aceitar a constante do caso × conseguir o primário (TRRL LR 706 / FSR; ARR) × não usar | manter só para reproduzir o Delmiro; em projeto novo, Kirpich modificada/DNOS (conferidos) até haver o primário |
| `carga_solo_aterro_positiva` | forma simplificada do TUBOS (he fixo) × equação completa de Spangler | usar em anteprojeto; conferir com o software da ABTC antes do projeto básico |
| faixa de Fr instável | 0,9–1,1 (bueiros) × 0,89–1,13 (HEC-11 p. 38) | unificar em 0,89–1,13 (faixa com fonte) |
| folga/hmax de valeta | 0,2 h (IME p. 54) × Tab. 4.2 IME (concreto) × 0,15 m (WSDOT) | 0,2 h em terra e Tab. 4.2 em concreto (IME, nacional), checando o mínimo de 0,15 m |
| colmatação de grelha em sag | sem colmatação × 50 % (HEC-12 Ex. 14) | 50 % em grelha isolada em ponto baixo |
| n de concreto do bueiro | 0,012 (HDS-5) × 0,013 × 0,015 (prática DNIT/acervo) | 0,013 em projeto (folga de idade e juntas); 0,012 só para reproduzir o HDS-5 |

## Revisão técnica F7 (Opus)

### Lote A (drenagem-fundamentos, hidrologia-de-projeto-para-drenagem, bueiros-e-travessias, drenagem-de-estradas-e-plataformas)

Revisor Opus, 2026-10-08. 59 itens amostrados nas quatro skills (11 + 16 + 16 + 16): 40 conferidos, 19 corrigidos na skill,
0 pendentes. Suíte inalterada (269 passed, 14 xfailed). **Nenhum erro numérico de calculadora**; achados abaixo, não corrigidos.

| módulo / função | achado | fonte p. N | efeito |
|---|---|---|---|
| estradas `folga_valeta` (terra, 0,3 < Q ≤ 10 m³/s) | `ValueError` "EQ 4.7 do IME ilegível"; a forma está no primário: **f = √(46·h)**, f e h em cm (o `_texto` perde o radical) | DNIT-DREN p. 162 (imagem) | função sem resposta nessa faixa. Hipótese a conferir: é a forma USBR F = √(C·y) com C = 1,5 ft (1,5 × 30,48 ≈ 46); se h for a lâmina, e não a profundidade da valeta, o resultado muda. h = 100 cm → f = 68 cm |
| estradas `folga_valeta` (concreto, Q > 2,8 m³/s) | `ValueError`; a Tab. 36 do DNIT (= Tab. 4.2 do IME) dá **20 cm** acima de 2,80 m³/s | DNIT-DREN p. 163 | linha faltante |
| hidrologia `MCMATH_CONST["m/m"]` = 0,0091 | conversão exata 0,02832/25,4 × 1000^0,2 × 2,471^0,8 = 0,00915 | USBR-DRAINAGE p. 57 (forma inglesa) | −0,6 % em Q; dentro de 1 %, só registro |
| hidrologia `coef_distribuicao` (docstring) | cita só o CSB (doc 1341:47); o primário é o DNIT | DNIT-HIDRO p. 131 (A^−0,10, A em km²); Burkli-Ziegler A^−0,15 com A em ha, p. 132 | só citação |
| fonte HEC-12, eq. 4 | imprime "K = 0.56 (0.016)"; o SI correto é 0,376 (conversão de 0,56 dá 0,377; HEC-22 p. 79) | FHWA-HEC12 p. 39 (imagem) | nenhum: `sarjeta_triangular` usa 0,376 e reproduz o Ex. 4 (0,0572 m³/s) |

Decisões do André (novas no lote A; as da revisão F5 acima não se repetem):

| decisão | alternativas (fonte, página) | efeito numérico | recomendação do revisor |
|---|---|---|---|
| TR de bueiro de perímetro irrigado | USBR 5 a 15 anos (página não localizada no corpus); DNIT 10 a 20 no projeto e 20 a 25 na verificação [DNIT-HIDRO p. 23-24]; DAEE 25 rural e 100 urbano [DAEE-IT-DPO11 p. 1]; acervo 25 (estrada) e 50 a 100 (sob canal) | risco em 25 anos: TR 10 = 93 %; 25 = 64 %; 50 = 40 %; 100 = 22 % | 25 em travessia de estrada de serviço e 50 sob canal adutor, verificando com o TR seguinte; USBR só depois de achar a página |
| Ke de ala paralela (caixa, topo com aresta viva) | 0,7 [FHWA-HDS5 p. 216; FHWA-HEC13 p. 100] × 0,2 [DNIT-DREN p. 130, Tab. 30] | ΔHW de saída = 0,5·V²/2g: 0,23 m com V = 3 m/s; nulo se a entrada governa | 0,7 (duas fontes FHWA concordam; a linha do DNIT funde duas da C.2); 0,2 só para reproduzir projeto DNIT |
| limite de área do racional | 80 ha (HDS-2, Eslamian); 2 km² [DAEE-IT-DPO11 p. 1]; 3 km² (PMSP); sem teto (DNIT); acervo 50 ha a 3,5 km² (`limite-area-metodos.md`) | Cd = A^−0,10: −7 % em 2 km² e −12 % em 3,5 km² sobre o racional puro | regra operativa da skill: racional puro até 80-100 ha; até 2 km² com Cd e conferência por McMath ou SCS; 2 a 3,5 km² só com HUT de comparação |
| Tc mínimo de drenagem superficial | 5 min [DNIT-IPR726 p. 258; WSDOT p. 102; LOC-IME p. 53]; 6 min [LOC-DNIT-ALBUM-2018 p. 214, OCR]; 10 min [DNIT-IPR726 p. 463, IS-239; Xingó] | L crítico +12 % (IDF CSB grupo 1) a +19 % (Wilken) de 5 para 10 min | 5 min, com a sensibilidade a 10 min no parecer; 10 só em vicinal sem pavimento ou por pedido do cliente |
| TR da drenagem superficial | 10 [DNIT-IPR726 p. 258]; 5 a 10 [p. 258, 463]; 25 ENGEFER [LOC-IME p. 53]; 50 em sag [WSDOT p. 104] | de 10 para 25: I × 2,5^b = +25 % (b = 0,241, CSB) ou +17 % (b = 0,172, Wilken) | 10; 25 quando a falha da valeta atinge o canal adutor ou a plataforma da EB |
| declividade mínima de sarjeta e valeta | 0,5 % [DERPR-ES-DR-01-23 p. 10] × 0,3 % (0,2 % em terreno muito plano) [FHWA-HEC12 p. 19] | Q ∝ √S: 0,3 % dá 23 % menos capacidade que 0,5 % | 0,5 % como padrão; 0,3 % em terreno plano com justificativa; abaixo de 0,3 % (Xingó 0,1 %) só revestida e com plano de manutenção |
| y/D máximo de tubo parcialmente cheio | 0,75 (Delmiro, 1492:164) × 0,82 (Jaíba, 1182:65) | Q/Q pleno = 0,91 em y/D 0,75 e 1,00 em 0,82: 9,7 % de capacidade | 0,75 no TR de projeto; 0,82 como teto na verificação |

### Lote B (canais-de-drenagem-e-macrodrenagem, drenagem-subsuperficial, drenagem-normas-e-manuais, drenagem-casos-de-referencia)

Reconstituído pelo orquestrador em 2026-10-09 a partir das seções "Revisão técnica" das 4 skills (a escrita original
do lote B neste arquivo foi sobrescrita pela gravação concorrente do lote A). Nenhum erro numérico de calculadora.

| item | veredito | fonte | efeito |
|---|---|---|---|
| `drenos.criterio_de_filtro_hidraulico`: fator único 4 de Terzaghi | pendente F7 (decisão) | DNIT-DREN p. 252–253 (D15f ≤ 5·D85s e ≥ 5·D15s) | fator 4 é mais exigente na retenção e menos na permeabilidade que o DNIT |
| `drenos.POROSIDADE_DRENAVEL` (tabela sem página) | pendente F7 (decisão) | EMBRAPA-DREN-SUBT Tab. 3 p. 14 | L de Glover-Dumm muda +13 % areia, +8 % franco, −18 % argila |
| Wesseling Q = 89·d^2,714·s^0,571 ausente | pendente F7 (decisão: incluir função) | FAO-IDP62 p. 214; Embrapa p. 16 (expoente 0,572) | Manning com declividade subestima ~1,8× a capacidade do lateral corrugado; pesa no D-86 |
| 1,2 L/s/ha dos evals dsub-03/04 | pendente (origem) | sem fonte no corpus (1 L/s/ha = 8,64 mm/d) | 10,4 mm/d está fora da faixa de irrigado árido 1–2 mm/d (FAO-IDP62 p. 113–114) |
| `canais_drenagem` sem velocidade mínima | pendente F7 (decisão) | NRCS-CPS608-2023 p. 2 (0,43 m/s); Salitre 1584:105 (0,30) | Delmiro: trecho com V = 0,292 m/s falha com qualquer piso |
| folga de dreno 25 % do tirante | pendente F7 (decisão) | CPS608 p. 2 e HEC-15 p. 34 (0,15 m) | proposta max(25 %; 0,15 m): DS-1.1/C Delmiro 0,108 → 0,15 m |
| docstring `canais_drenagem` "Exemplo 1 p. 78" do HEC-11 | corrigir (só texto) | HEC-11 p. 72 | nenhum |
| `hidrologia.racional`: aviso "2–3 km²" | pendente F7 (decisão) | IPR-726 p. 259 (racional até 4 km², corrigido até 10 km²); DAEE 2 km² | o "3" não tem fonte |
| 6 xfail de acervo com strict=False | proposta | regra 5 de `drenagem-casos-de-referencia` | nenhum número muda |
