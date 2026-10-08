# Casos de acervo de canal de drenagem: método do projetista, gabarito e divergência

Fonte: `casos/drenagem/2026-10-08_*.md` (extração F4; nenhum número tem ✓h: são candidatos a gabarito até conferência humana, F7). Formato de divergência (núcleo, seção 9): o que o projeto fez · o que o método dá · diferença e consequência · quem decide.
Comandos: `python -m tools.dren.canais_drenagem --json '{...}'` (ponto decimal). Resultados abaixo **rodados** na calculadora 0.1.0.

## 1. Salitre Etapa 2, macrodrenos trapezoidais (positivo, A) e inconsistências do memorial (negativo, B)

Método: Manning, movimento uniforme, trapezoidal, iterativo; n = 0,030; talude 1H:1V em vertissolos e 1,5H:1V nos demais; chuva crítica de 24 h TR 10 e verificação TR 50; V 0,30 a 1,2 (memorial) ou 1,5 (planilha); quedas de 1,0 e 1,5 m [1584:102-108]. "Q trecho" = demanda; "Q DRENO" = **capacidade** com a seção cheia até h; altura da seção = h (coluna de borda livre não preenchida) [1585:97-123].

| Trecho [doc:pág] | Dados | Planilha | Calculadora |
|---|---|---|---|
| DT 4.1.6/A [1585:105] | b 2,50; h 0,90; z 1; S 0,00227; n 0,030 | A 3,060; V 1,139; Q dreno 3,484 | `capacidade_trapezoidal` reproduz (V 1,138; Q 3,48, 0,2 %) |
| DT 4.1.6/B [1585:105] | b 7,80; h 0,90; S 0,00084 | V 0,804; Q 6,295 | V 0,802; Q 6,28 |
| DS 4.1/A [1585:99] | b 56; h 1,50; z 1,5; S 0,00096; Q trecho 113,2 | A 87,375; V 1,307; Q dreno 114,194 | com Q 113,2: **y_n = 1,492 m**, V 1,302, Fr 0,347; folga até o topo **0,008 m** |

Divergências a apontar (nunca corrigir em silêncio):

| Item | O que o projeto fez | O que o método dá | Consequência e decisão |
|---|---|---|---|
| N1 total de extensão | texto 72.858,41 m [1584:97] | `reconciliar_extensoes({Mulungú 2026,00; Recreio 51533,65; Tourão 21324,76}, 72858.41)` → soma 74.884,41; diferença **2.026,00 = Mulungú** | total subestimado em 2,8 %; quantitativo e custo de escavação; confirmar com o projetista qual vale |
| N2 limite de V | memorial 0,30-1,2; planilha 0,3-1,5; DS-4.1 tem V 1,306-1,309 e DT 4.1.2/A 1,230 | `verificar_limites_alternativos(1.307, [1.2, 1.5])` → {1,2: reprova; 1,5: passa}, conflito = true | seis trechos mudam de status conforme o limite; **pedir qual vale**; os dois limites são critério do projetista, sem fonte |
| N3 profundidade 1,80 m | memorial: 1,80 m no entorno das áreas irrigáveis; planilhas: h 0,90 (52 trechos), 1,80 (10), 0,75 (9), 1,50 (8), 0,70 (4) | DT 4.1.2/A: b 0,60, h 1,80, Q 2,030 contra capacidade 5,315 (2,6x); DT-4.3.1/A: 3,690 contra 7,902 (2,1x) | seção superdimensionada onde se impôs 1,80 m; "entorno das áreas irrigáveis" não definido; conferir perfis (0340-DE-00-DR-006 a 076) |
| N4 talvegue 4W21-6 | L = 20.040,57 m, 202,84 ha, desnível 3,87 m [1584:99] | fora do envelope da própria tabela (vizinhas 0,4 a 3,3 km) | Tc cresce com L^0,77 (Kirpich); L dez vezes maior infla Tc; **não se sabe se chegou ao cálculo**; pedir; provável vírgula ou zero |
| N5 contagem de ACP | texto: Recreio 47, 11.032,23 ha; Tourão 21, 3.475,53 ha | tabelas: 51 linhas, 11.293,56 ha; 22 linhas, 3.405,75 ha; sub-ACPs 4W21-n somam 1.593,03 contra 1.472,82 ha | possível sobreposição; B, depende da extração; conferir páginas |
| Folga | h = y_n em DS-4.1 (folga 0,008 m); coluna de borda livre vazia | 25 % do tirante pediria 0,37 m; USBR do PISF, 0,69 m | **lacuna do memorial**, não violação do critério dele; ver `velocidade-folga-tr-por-fonte.md` §4 |

Estruturas associadas: degraus (9, Hd 1,00 ou 1,50 m, LT = b + 2·Hd), deságues (9, Am − Bm = 2·z·Hm) conferem a B [1584:108]. Bueiro celular BC-4.1.1/1 sob DT-4.1.1: 3 células 1,0 x 1,0 m, L 20 m, n 0,015, Q cap. 1,451 por célula,
só Manning parcial, **sem controle de entrada nem cota a montante** [1584:107; 1585:100]: encaminhar a `bueiros-e-travessias` (HDS-5, entrada e saída; vale o maior HW).

## 2. Delmiro Gouveia, drenos de lote (positivo, A) e seção subdimensionada (negativo, B)

Método: Racional Q = 0,278·C·I·A (C 0,15, solo arenoso); IDF I = a/(t + b)^c com TR 10 por igualdade de coeficientes (TR **não declarado**); Tc de montante por Kirpich, a jusante Tc do nó + L/V; Manning n 0,025; seções ZTT01 a ZTT09 (talude 1:1 nas duas primeiras, 1,5:1 nas demais); quedas de 1,00 m [1520:126-130; 1521:120-187].
A vazão e o Tc são de `hidrologia-de-projeto-para-drenagem`; aqui entram a seção, a V e a folga.

| Trecho | Dados | Planilha | Calculadora |
|---|---|---|---|
| DS-1.1/C [1521:120] | Q 0,518; ZTT04 b 0,60, h 0,45, z 1,5; Io 0,00368; n 0,025 | tirante 0,43; V 0,962; Fr 0,576; folga recomendada 0,11, **adotada 0,02** | `canal_trapezoidal(Q=0.518,b=0.6,z=1.5,n=0.025,S=0.00368,h_secao=0.45)`: y_n 0,4316; V 0,962; Fr 0,576; yc 0,323; folga **0,018** contra mínimo 0,108: aviso |
| DT-2.23.1 [1521:165; 1520:134] | Q 0,120; ZTT01 b 0,20, h 0,20, z 1; Io 0,00352 | tirante 0,331; folga adotada **−0,131** | `canal_trapezoidal(Q=0.12,b=0.2,z=1,n=0.025,S=0.00352,h_secao=0.2)`: y_n 0,3307; folga −0,1307; **transborda** |

Divergências:
- **D1** seção ZTT01 menor que o tirante: tirante 65 % acima da altura; o ramo vizinho DS-2.23/A com a mesma área usa ZTT02 e passa. Outro caso marginal: DS-3.1/A, folga −0,001 m [1521:173]. Só esses dois falham em 194 trechos.
- **D2** folga: memorial manda 25 % do tirante e admite "folgas menores" entre seções e transbordamento localizado < 4 h [1520:129]; a planilha tem **84 de 194 trechos (43 %)** abaixo, com a mesma altura nas seções de montante e jusante, então a exceção "entre seções" não se aplica.
  `verificar_trechos` devolve a % fora do critério; relatar contagem e lista, não aceitar a frase. Todas as alternativas de folga da literatura (0,15 a 0,20 m) também ficam acima do 0,02 adotado em DS-1.1/C.
- **D3** Quadro 3.47: nomes duplicados e prefixos trocados (DT-1.21 a 1.26 por DT-2.21 a 2.26); soma de 86 itens = 37.569,13 m bate; erro de nome, não de extensão [1520:136-137]. Exigir chave única por dreno.
- **D4** V mínima citada sem valor; 10 trechos < 0,5 m/s (mínimo 0,292, DT-2.26.2, Io 0,0004) [1521:171, 156, 163, 177]. A calculadora **não tem padrão**: pedir; alternativa rotulada, CPS 608: 0,43 m/s.
- Tc mínimo de 10 min aplicado sem declarar (DT-1.1.1: Kirpich 3,8 min vira 10,00) [1521:120]: ponto aberto de F7 (Tc mínimo), ver hidrologia.

## 3. Sertão Pernambucano, drenos laterais ao adutor (positivo, B)

Ver `talvegues-desague-quedas.md` §3. Gabarito: inventário de 204 drenos e 162.464,0 m; 13 seções ST; afastamento 6,00 m; V crítica sem valor; TR 100 [1390:429-440].

## 4. Retroanálise de canal em gabião x tubo (positivo, B; fonte local D8)

Gabarito: `manning_retangular` (b 1,59, y 0,80, S 0,003, n 0,035) = 1,0784 m³/s; tubo DN 1000 a 85 %, n 0,010 = 1,7591 m³/s; frações 390/441 (PEAD) e 210/441 (concreto) [células B8, B19, H23, H48]. Testes `test_acervo_gabiao_*`.
Divergência de n do gabião e consequência: `revestimento-riprap-gabiao.md` §3.1. Escolha gabião x tubo e custo: Hidráulica e Orçamento; estabilidade da escavação: Geotecnia.

## 5. Mapa dos testes que cobrem estes casos

| Caso | Teste (`tests/dren/test_canais_drenagem.py`) |
|---|---|
| EM-1601 App. H Tab. H-1 (b 140 ft, S 0,0017, Q 13.500 cfs: y 10,6/11,0/11,3 ft, V 7,9/7,6/7,3 fps para n 0,034/0,036/0,038) [USACE-EM1601 p. 179] | `test_em1601_tab_h1_profundidade_normal`, `test_em1601_h1_recalculo_n036` |
| HEC-11 Exemplo 1 (D50 0,43 ft) e K1, Csg, Csf | `test_hec11_exemplo1_d50`, `test_hec11_k1_eq7_talude_2h1v_phi41`, `test_hec11_correcoes_c_sg_c_sf`, `test_hec11_talude_acima_do_repouso_erro` |
| n de rip-rap | `test_n_riprap_strickler_forma_e_divergencia` |
| Salitre Manning e limites de V e extensões | `test_acervo_salitre_dt416a_manning`, `test_acervo_salitre_outros_trechos`, `test_salitre_n2_dois_limites_de_velocidade`, `test_salitre_n1_reconciliacao_de_extensoes` |
| Delmiro | `test_acervo_delmiro_ds11c_tirante_froude`, `test_acervo_delmiro_froude_nao_e_com_y`, `test_acervo_delmiro_d1_secao_menor_que_tirante`, `test_verificar_trechos_percentual_fora_do_criterio` |
| Gabião | `test_acervo_gabiao_canal_retangular_e_tubo`, `test_acervo_gabiao_fracoes_da_grade` |
| V admissível, V mínima, borda livre | `test_velocidade_admissivel_dnit_e_em1601_divergem`, `test_verificar_velocidade_vmin_sem_padrao`, `test_borda_livre_provisoria_25_pct` |
| Regime, composto, entradas inválidas, CLI | `test_regime_supercritico_e_aviso_instavel`, `test_composto_*`, `test_entradas_invalidas`, `test_cli_json` |
