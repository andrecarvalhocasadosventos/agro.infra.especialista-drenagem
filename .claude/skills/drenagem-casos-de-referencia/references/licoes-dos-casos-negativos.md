# Lições dos casos negativos (e do que o acervo faz diferente do método)

Cada linha: o que o projeto fez (`doc:pág`) · o que o método dá · consequência · teste que revela. Tudo sem `✓h`: dizer
"valor do projeto, não conferido". Regra: apontar, não corrigir (SKILL §2). "Teste na calculadora" indica se já existe
em `tests/dren/`; onde não existe, é **teste sugerido** (não escrito, fora do escopo desta skill).

## A. Hidrologia

| # | Erro no projeto | Evidência | Teste que revela | Na calculadora |
|---|---|---|---|---|
| H1 | P = 23,20 mm (5 min) usada como mm/h nas valas da estrada: Q = C·P·A/3,6e6 reproduz 7 de 7 linhas (VC1 0,039 ... VC2 0,171) | CAC Castanhão, 1128:106-112 | I = P·60/tc = 278,4 mm/h; Q(VC2; A 44.110 m², C 0,6) = 2,05 m³/s, 12 vezes a impressa | sugerido (caso traz o eval); `racional` não valida unidade |
| H2 | NERC chamada "Kirpich": 7,65 h impressa; Kirpich dá 4,92 h (L 13,21 km, S 0,00242) | Delmiro BHD1, 1494:31, 64; 1492:155 | reproduzir o Tc pela fórmula com a unidade da fonte | `test_delmiro_nerc_x_kirpich_rotulo_e_velocidade` |
| H3 | Velocidade 1,73 e 1,75 "m/s" que são km/h (0,48 e 0,49 m/s) e o critério 0,5 a 2,0 m/s aplicado ao número errado | 1494:64; 1492:155 | v = L/tc em m/s | mesmo teste |
| H4 | Declividade BH4.5 0,0618 impressa; (250 − 236)/3252,5 = 0,0043 (razão 14,4); outras 57 linhas conferem a 5 % | 1492:142 (Quadro 3.50) | S = ΔH/L por linha; |razão − 1| > 5 % | sugerido |
| H5 | Pico BHD1 TR 50 58,71 m³/s; convolução com chuva uniforme dá 61,8 (+5,3 %); tempo do pico 10,35 h x 10,36 h confere | 1494:64 | declarar "gabarito não reproduzível" (hietograma polinomial) | `test_delmiro_bhd1_pico_58_71` (xfail strict) |
| H6 | Qp do HUT "m³/s por mm" impresso 15,149 é por 10 mm (por mm = 1,515) | 1494:33; 1492:157 | conferir a unidade de Qp | confirmado em teste |
| H7 | Limite do racional e fórmula de Tc diferentes em cada projeto (50, 100, 350 ha; 2 e 3,5 km²) | acervo todo | declarar o limite usado e a faixa de cada Tc; não uniformizar | `racional(limite_km2=...)` |
| H8 | IDF emprestada de outra região ou sem faixa de duração; Tc e IDF do Baixio HUT ilegíveis | Baixio 898-903; vários | sinais de `delegar-climatologia.md` §3; `[DELEGAR: clima]` | , |
| H9 | Talvegue de 20.040,57 m numa ACP de 202,84 ha com desnível 3,87 m (vizinhas: 0,4 a 3,3 km) | Salitre 1584:99 | razão L/área e declividade fora do envelope da própria tabela; Tc cresce com L^0,77 | sugerido |

## B. Bueiros

| # | Erro ou prática | Evidência | Teste que revela | Na calculadora |
|---|---|---|---|---|
| B1 | Capacidade por orifício (C 0,62) ou Manning plena; sem contração de entrada: HW legado −8,0, −6,4 e −7,8 % em BU-CP0-13/15/18 (até −12 a −18 % com alas 90/15) | Baixio 896/897 | `comparar_legado_hds5`; o maior HW governa; **contra a segurança** | `test_baixio_legado_vs_hds5_5pct` (xfail) |
| B2 | BTCC 7 e BTCC 1 do Salitre dariam HW/D ≈ 2,25 e 1,78 pelo controle de entrada; o memorial só mostra Manning | Salitre 1357 | `dimensionar_bueiro` | Manning de V reproduz (3 %) |
| B3 | n do bueiro não declarado; as tabelas só fecham com n ≈ 0,013 (0,0128 a 0,0134 em 22 linhas); o memorial adota 0,015 no canal. Com 0,015 a capacidade cai 13 %; E3 BC-06 vai a Y/D ≈ 0,84 e E4 BC-08 estoura 0,82 | Jaíba 1182:43, 65-67 | resolver n por linha; reportar o n implícito | sugerido |
| B4 | v até 4,8 m/s no concreto sem limite nem dissipador; Q sem TR, C, área ou método | Jaíba 1182:65-67 | exigir hidrologia; Fr e V de saída; aviso "precisa de dissipador" (D3) | `velocidade_de_saida`, `dissipador_necessario` |
| B5 | BTCC-N17 (3 cel. 2x2, i 0,0045): Q impressa 39,18; Manning n 0,015, y 1,5 m dá 28,6 m³/s (−27 %); V/Yo da Tab. 4.7 lidos errados ou outra lâmina | CSB 1341:205 | recalcular Manning | `test_csb_btcc17_capacidade_manning` (xfail) |
| B6 | Lâmina do projeto é de perfil por energia (K 0,5 a partir da seção crítica), não de Manning normal: y 0,96 x 0,83 m (BU-01), 1,76 x 1,42 (BU-06), 1,87 x 1,50 (BU-24) | Xingó 1419:154 | não comparar y de perfil com y normal; V = Q/(B·y) confere (3,11 x 3,10) | `test_xingo_lamina_normal_vs_doc` (xfail) |
| B7 | Fórmula legada embutida do dreno Xingó Q = 33,5·D^2,67·i^0,5 equivale a n 0,0093; com n 0,012 a 0,013 a capacidade cai 22 a 28 % | Xingó 1419 | converter para n equivalente | sim (caso negativo em teste) |
| B8 | y/D = 79 % em BUC-5, TR 50, acima de 75 % do critério provisório; declividade e comprimento do caso divergem | Delmiro 1493:282-285 | `tubo_parcialmente_cheio` reproduz y, V e Fr a 1 % | `test_delmiro_tubo_parcialmente_cheio` |
| B9 | Texto: TR 25 e altura de célula ≤ 1,50 m; quadro: só Q50 nas 14 linhas HUT, Q15/Q25 nas RAC, 25 de 26 células de 2,00 a 3,00 m; declividade mínima "5 %" | Iuiu 2018 1069:123-125 | cruzar texto x quadro; pedir S do desenho 807-CDVF-IUI-DR-OH-07/08 | sugerido |
| B10 | Cota do rasto de B31 91,189 m (B30 94,246; B32 92,977): sobe 1,79 m em 2,41 km e o coletor (92,000) fica 0,81 m acima do rasto | CAC Trecho 1 1131:66 (Quadro 17.1) | monotonia do perfil e coletor abaixo do rasto; provável 94,189 (rastro C) | sugerido |
| B11 | Vazão: Q 2,44 x 2 x 1,27 m³/s (sifão-bueiro) | Jaíba 1182 | conferir Q do quadro x do texto | hf 0,024 reproduz |

## C. Canais de drenagem e valetas

| # | Erro ou prática | Evidência | Teste que revela | Na calculadora |
|---|---|---|---|---|
| C1 | Seção ZTT01 (0,20 x 0,20) com tirante 0,331 m (+65 %), folga adotada −0,131 m; variante DS-3.1/A −0,001 m | Delmiro 1521:165, 173 | tirante ≤ altura em todo trecho (só 2 de 194 falham) | `test_acervo_delmiro_d1_secao_menor_que_tirante` |
| C2 | Folga mínima declarada 25 % do tirante; 84 de 194 trechos abaixo (43 %); a exceção "entre seções" não se aplica | Delmiro 1520:129; 1521:120-187 | `verificar_trechos` | `test_verificar_trechos_percentual_fora_do_criterio` |
| C3 | Nomes duplicados e trocados (DT-2.10.1 duas vezes; DT-1.21.x onde é DT-2.21.x); soma de 86 itens 37.569,13 m fecha | Delmiro 1520:136-137 | chave única por dreno e conciliação entre quadros | sugerido |
| C4 | V mínima citada sem valor; 10 trechos com V < 0,5 m/s (mín. 0,292) | Delmiro 1521:156-177 | pedir o valor, não presumir | , |
| C5 | Extensão total 72.858,41 m; soma das parcelas 74.884,41 (falta Mulungú 2.026,00) | Salitre 1584:97 | `reconciliar_extensoes` | `test_salitre_n1_reconciliacao_de_extensoes` |
| C6 | Dois limites de V: memorial 0,30 a 1,2; planilha 0,3 a 1,5; DS-4.1 V 1,306 a 1,309 reprova no primeiro e passa no segundo | Salitre 1584:105; 1585:97-123 | `verificar_limites_alternativos` | `test_salitre_n2_dois_limites_de_velocidade` |
| C7 | Profundidade 1,80 m só em 10 de 83 trechos; "declividades não excedem 1 %" com 4W-38 = 1,11 %; 13 sub-ACPs 1.593,03 ha x 1.472,82 ha | Salitre 1584:99-105 | afirmação textual x tabela; contagem e soma por quadro | sugerido (conferência humana de N4, N5) |
| C8 | hmáx 0,24 m repetido em VPC-5/6/7 (alturas 0,30; 0,35; 0,40); regra 0,8·h daria 0,28 e 0,32 | Xingó 1419:78-80 | recalcular hmáx = 0,8·h; capacidade > 0,083 m³/s | teste confirma (VPC-7) |
| C9 | Duas chuvas (2,353 e 1,789 mm/min) para o mesmo TR 10 e tc 10 min; TR 10 nas valetas, 25 a 100 nos bueiros | Xingó 1419:65, 98 | pedir a IDF de cada trecho | , |
| C10 | Gabião x tubo: lâmina 80 % da altura x 85 % de D favorece o tubo; "declividade (%)" com 0,003 usada como m/m; n 0,010 fora da faixa do concreto; 88 % e 48 % são fração da grade, não probabilidade | planilha local (D8) | lâmina igual; unidade do rótulo | `test_acervo_gabiao_*` |

## D. Dreno de fundo e drenagem subsuperficial

| # | Erro ou prática | Evidência | Teste que revela | Na calculadora |
|---|---|---|---|---|
| D1 | Capacidade DN170 1,518e-4 e DN230 4,929e-4 m³/s; Manning meia seção (n 0,016, S 3e-4) dá 1,05e-3 (6,9x) e 2,31e-3 (4,7x); razão entre DN 3,25, devia ser D^(8/3) = 2,19. S do tubo pode não ser 3e-4 | Delmiro 1492:105 | `capacidade_tubo_parcial`; razão entre DN | 2 xfail strict; Lmáx = Q/qd reproduz (388 e 1.260 m) |
| D2 | Se Manning estivesse certo, Lmáx seria 2,7 km e 5,9 km; o limite de manutenção (250 m, PIL) governa de qualquer modo | Delmiro 1492:105-106 | declarar qual limite governa | , |
| D3 | q 6e-5 m³/s/m (CSB) x qd 3,9e-7 (Delmiro, Darcy): ~150x; critérios diferentes, não erro | CSB 1341:74-77; Delmiro | rotular, não comparar como gabarito | , |
| D4 | CSB 2DN150 até 200 m: Q 0,012 → 0,006 m³/s por tubo > 0,005 (limite da faixa DN150 do próprio memorial); razão entre DN não segue D^(8/3) | CSB 1341 | `dreno_de_fundo_de_canal_revestido` | `test_csb_L200_2DN150` (xfail strict) |
| D5 | Hooghoudt: viés de campo de +13,5 a +35 % (Embrapa Maniçoba) e de −21 % (laboratório): declarar a incerteza | corpus, não acervo | , | aviso na docstring |

## E. Como lidar com cada tipo

- **Erro de unidade, rótulo ou digitação** (H1 a H4, B10, C3): apontar, mostrar o recálculo, dizer que a hipótese da
  causa é rastro C e pedir confirmação ao projetista.
- **Método mais simples que o do manual** (B1, B2): não é erro formal; é diferença de método com consequência contra
  a segurança. Mostrar o HW de ambos.
- **Entrada ausente** (B3, B9, D1): "sem gabarito: faltam entradas"; listar o que pedir (S, L, n, hietograma).
- **Critério diferente** (H7, C6, D3): dizer qual vale em cada documento; não escolher pelo projetista.
- **Divergência > 5 %**: linha em `DIVERGENCIAS.md`, xfail estrito, sessão interativa com o André.
