# Classe de tubo de concreto indicativa (`tools/dren/tubos.py` 0.1.0)

Uso: anteprojeto; o dimensionamento estrutural (armadura, concreto, aduela) é de Estruturas.

Fluxo [LOC-ABTC-PROJETO-ESTRUTURAL-TUBOS, "TUBOS"; LOC-ABTC-ESPEC-TUBOS-LICITACOES, "ESPEC"; USACE-EM1110-2-2902]:
q = carga vertical do solo (vala: Cv·γ·bv², TUBOS p. 17; aterro de projeção positiva: Cap·γ·de², p. 19-20); qm = sobrecarga × coeficiente
de impacto (Tab. 3.3 [p. 33]: ≤ 0,30 m 1,3; ≤ 0,60 1,2; ≤ 0,90 1,1; > 0,90 1,0); Fens = γs (q + qm)/α, γs = 1,0 (fissura) e 1,5 (ruptura) [TUBOS p. 45];
classe = menor PA1-PA4 cuja força isenta de fissura ≥ Fens e cuja ruptura ≥ 1,5·Fens (ESPEC Tab. 2 [p. 4] = TUBOS Tab. 5.1 [p. 46]).
Exemplos ESPEC [p. 6]: DN1200/65 kN/m → PA2; DN800 esgoto/85 → EA4; DN400/37 → PA4.
- **Limites:** recobrimento mínimo hs ≥ 0,6 m em tráfego normal [TUBOS p. 29]; DN > 600 sempre armado; abaixo de DN 500 só ponta-e-bolsa;
  acima de PA4 usar galeria celular NBR 15396 [LOC-ABTC-ALTERACOES-NBR8890 p. 1, 4]. **NBR 8890:2020 não aberta**: citar via ABTC, não transcrever.
- **Fator de berço de classe A em vala** [padrão provisório, decisão F7]: TUBOS Tab. 4.1 [p. 37] dá 2,25 a 3,4; EM 1110-2-2902 Tab. 3-1 [p. 27] dá 2,5. O código usa 2,25
  (mínimo, a favor da segurança); `alfa_A` e `fonte="em2902"` são opções. Mostrar a classe com os dois.
- **Lacunas do corpus:** não há tabela de altura máxima de aterro por classe e DN (só no software da ABTC); veículo-tipo e projeção negativa não
  implementados; sobrecarga qm vem do usuário. O resultado sai rotulado "indicativo"; a classe final é de Estruturas e do fabricante.
- Teste de livro: EM 2902 p. 71-72, D0,01 = 57,0 N/m/mm resolvido (W_T = W_L + W_E, θ = 1/3); Bf 6,098 reproduz.

