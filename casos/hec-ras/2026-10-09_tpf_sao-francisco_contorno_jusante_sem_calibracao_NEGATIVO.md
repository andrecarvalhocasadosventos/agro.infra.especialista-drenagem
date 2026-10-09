# Caso HR-03 — NEGATIVO: contorno de jusante sem curva-chave e modelo sem calibração (captação, TPF)

**Tipo:** negativo (premissa sem dado e divergência texto × arquivo; não é erro de cálculo comprovado).
`REL-FINAL`, `HR-SF` e `ACOMP-0811` (= `Acompanhamento_Ventos_da_Terra_2026.08.11.pptx.pdf`, id 1503) como nos casos anteriores. Marca A (lido), B (derivado); sem ✓h.

## Evidência
1. **Contorno de jusante por declividade.** REL-FINAL:41: "Como condição de contorno de jusante, foi utilizada a declividade média do rio, correspondente a 0,01 %". No arquivo, `sao_francisco_Q95/sao_francisco.u01` traz `Friction Slope=0.000093` nos dois contornos de saída ("saida 1" e "saida 2") e `Flow Hydrograph Slope= 0.000093` na entrada: **0,0093 %**, não 0,01 % (A; diferença de 7 %, igual nas pastas Q50 e QTR100). Efeito no NA: não avaliado; a profundidade normal imposta no contorno só vale se a seção de saída for uniforme e a declividade for a do leito local (HEC-RAS 2D UM 6.6, p. 144-145: "[Normal Depth] ... o usuário informa a friction slope").
2. **Sem calibração nem verificação.** O relatório não apresenta curva-chave, cota observada ou marca de cheia para comparar com o modelo. A premissa 9 do acompanhamento de 11/ago (ACOMP-0811:2) previa "avaliação das curvas-chave... e seleção da relação cota-vazão mais representativa" e a premissa 10 "verificação dos níveis calculados com as cotas operacionais de Sobradinho (elevação do IBGE = Sobradinho + 1,88 m)"; **não há registro dessa verificação no relatório** (A: nenhuma ocorrência nas p. 41-48 do REL-FINAL, páginas lidas).
3. **Sensibilidade de n não apresentada.** Um único n (0,035) para canal e planície; nenhuma rodada com n ±20 % (A: busca nas mesmas páginas).
4. **Cota inicial 382,4 m** (≈ 8 m abaixo do NA final) não é justificada (ver HR-02).

## O teste que revelaria
Rodar o Q95 com declividade 0,0001 e 0,000093 e comparar NA na seção da captação; rodar n = 0,028 e 0,042; comparar com marca de cota de Sobradinho (premissa 10 do ACOMP-0811). Sem esses três, o parecer deve registrar "NA sem calibração, ±incerteza não quantificada".

## Gabarito do caso negativo
O parecer correto reproduz o alerta: "NA 390,80 m (Q95) e 397,56 m (QTR100) são resultados de modelo sem calibração, com contorno de jusante por declividade (0,0093 % no arquivo × 0,01 % no texto) e rugosidade única; recomenda-se faixa de sensibilidade antes de fixar cota de captação". Número com ✓h: nenhum.
