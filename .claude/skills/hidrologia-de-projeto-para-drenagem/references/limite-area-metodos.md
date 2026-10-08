# Qual método por tamanho de bacia: divergência entre fontes e projetos

Ponto aberto para a F7 (limite de área do racional): **padrão provisório, decisão F7**. Não decidir; mostrar as alternativas com fonte e declarar o limite adotado no parecer. Páginas = física do PDF.

| Fonte | Racional até | Acima |
|---|---|---|
| FHWA HDS-2 | < 200 acres (≈ 81 ha), "geralmente" [FHWA-HDS2 p. 90-91, 181]; HEC-22 repete 80 ha [FHWA-HEC22 p. 57] | Hidrograma unitário |
| Eslamian cap. 16 | "menor que 80 ha" [LOC-ESLAMIAN-HANDBOOK-HYDROLOGY p. 352] | — |
| NRCS EFH cap. 2 (gráfico) | método de pico válido de 1 a 2.000 acres (0,4 a 810 ha) [NRCS-NEH650-CH02 p. 11] | TR-55 ou TR-20 |
| DAEE-SP IT DPO 11 | 2 km² [DAEE-IT-DPO11 p. 1] | Não define o método |
| PMSP-V2 | < 3 km² ou tc < 1 h [PMSP-DRENURB-V2 p. 53] | — |
| ABDER | ≤ 4 km² (C de Peltier); 4 a 10 km² racional com coeficiente de retardo φ = 1/(100·A)^(1/n), n = 4, 5, 6 conforme a declividade; > 10 km² HU triangular [ABDER-APOSTILA p. 53-55, 59] | HUT |
| DNIT IPR-715 | Sem teto; "de preferência bacias pequenas", aplicável a maiores com fator de distribuição A^-0,10 [DNIT-HIDRO p. 129, 131]; para pontes e bueiros sem fluviometria indica o HU sintético [DNIT-HIDRO p. 57] | — |
| Acervo, Iuiu 2002 | 50 ha racional; 50 a 400 ha média de McMath e CN (ignora valor menor que o racional); > 400 ha CN [doc 1051:316] | CN |
| Acervo, Baixio | 100 ha | HUT |
| Acervo, CSB | 350 ha; 350 a 2.000 ha HUT de uma ordenada; > 2.000 ha 11 ordenadas [doc 1341:46] | HUT |
| Acervo, Xingó | A < 2 km² ou Tc < 1 h [doc 1419:26] | HUT |
| Acervo, CAC Trecho 1 | A < 3,5 km² (cita o Manual DNIT 2005, que não traz teto) [doc 1139:227]; 428 de 448 bacias | HUT com CN 85 |
| Acervo, Delmiro Gouveia | bacia de 36 km² por HUT (BHD1) [doc 1494:31-33] | — |

Nenhum dos limites do acervo é derivado de Tc ou de C: é regra de prática. O agente cita o limite do projeto, não impõe um.

## Regra operativa do agente (decisão desta skill, não norma)

- Racional puro até 80 a 100 ha.
- De 100 ha a 2 km²: racional com Cd = A^-0,10 (`coef_distribuicao`) e conferência por McMath ou SCS-CN.
- De 2 a 3,5 km²: só com justificativa e comparação com o HUT-SCS (o CAC usa racional até 3,5 km²).
- Acima de 3,5 km² ou Tc > 1 h: SCS-CN com HUT.
- Mostrar a vazão por dois métodos e adotar a maior com justificativa; diferença > 30 % entre métodos exige explicação.
- A função `racional` avisa acima de `limite_km2` (padrão 2): para reproduzir um projeto, passar o limite dele (`LIMITES_RACIONAL_ACERVO_KM2`: Iuiu 0,5; Baixio 1,0; CSB 3,5; Xingó 2,0 km²; CAC 3,5 km² deve ser passado à mão).
