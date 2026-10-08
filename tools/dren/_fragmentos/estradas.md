## README
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

## DIVERGENCIAS
| item | fonte A | fonte B/acervo | tratamento |
|---|---|---|---|
| Tc minimo de drenagem superficial | 5 min [IPR726 p. 258; WSDOT p. 102; IME p. 53] | 6 min [Album p. 214, OCR]; 10 min [IPR726 p. 463, IS-239]; Xingo usa tc 10 min | argumento `tc_min` (padrao provisorio 5, decisao F7) + aviso |
| TR da drenagem superficial | 10 anos [IPR726 p. 258; IME DNER] | 25 anos ENGEFER [IME p. 53]; 5-10 [IPR726 p. 258/463] | argumento `TR` (padrao provisorio 10, decisao F7) + aviso |
| Declividade minima de sarjeta/valeta | 0,5 % [DERPR-ES-DR-01-23 p. 10] | 0,3 % (0,2 % plano) [HEC-12 p. 19]; Xingo calcula i = 0,1 % | aviso, sem bloqueio |
| Dreno profundo: meia secao x secao plena | texto IME p. 83 "fluxo a meia secao" | formulas (0,2113 = 0,269 pi/4; HW) do mesmo p. dao tubo cheio | calcula cheio; aviso; `fator_capacidade` opcional |
| Folga de valeta | f = 0,2 h [IME p. 54]; Tab. 4.2 concreto 10-18 cm [IME p. 55] | 0,5 ft (~0,15 m) fixos [WSDOT p. 109] | ambas documentadas; hmax padrao 0,8 h = regra observada no Xingo (nao declarada) |
| Xingo VPC-1 (acervo, sem check-h) | calculadora: L 162,57 m (i 0,001), 1259,25 m (i 0,060) | projetista: 162,54 e 1259,04 (desvio < 0,02 %); z = 1 deduzido, nao impresso | teste de 5 %, rotulado "acervo, sem check-h" |
| Xingo VPC-5/6/7 com mesmo hmax 0,24 m (acervo) | projetista repete capacidade 0,083 m3/s | regra 0,8 h daria 0,28 e 0,32 m: capacidade maior | teste confirma capacidade > 0,083 para VPC-7 |
