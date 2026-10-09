# Armadilhas transversais (casos negativos)

Tabela movida do `SKILL.md` §9 na revisão F7 (2026-10-08) para manter o núcleo abaixo de 25 KB. A regra mestra continua no
`SKILL.md` §9: apontar a divergência com evidência e consequência, nunca corrigir o projeto em silêncio.

| Armadilha | Onde ocorreu | Como detectar |
|---|---|---|
| Bueiro verificado só por orifício ou Manning plena; HW 6 a 18 % abaixo do HDS-5. Salitre BTCC 7 e BTCC 1 dariam HW/D ≈ 2,25 e 1,78 pelo controle de entrada (entrada hipotética alas 30-75°; recalculado na F7) | Baixio, CSB, Xingó, Salitre | `comparar_legado_hds5`; o maior HW (entrada × saída) governa |
| Limite do racional e fórmula de Tc diferentes em cada projeto (50, 100, 350 ha, 2 km², 3,5 km²) | acervo todo | declarar o limite usado e a faixa de validade de cada Tc; não "uniformizar" |
| Rótulo trocado: NERC chamada Kirpich, km/h sob m/s, declividade 0,0618 × 0,0043 | Delmiro Gouveia (`..._tc_rotulos_velocidade_declividade`) | reproduzir o Tc pela fórmula com a unidade da fonte |
| P (mm) usada como i (mm/h): vazão 12 vezes menor | CAC Castanhão, valas da estrada | conferir a dimensão da intensidade |
| Froude com y em seção trapezoidal (0,197 com y × 0,254 com A/T) | Baixio de Irecê, canal CS2 (doc 894; lição nº 23 de `casos-de-referencia/references/licoes-do-acervo.md` do Hidráulico) | Fr = V/√(gA/T) |
| Coluna "OK" em planilha com folga negativa; seção ZTT01 menor que o tirante; folga < 25 % em 43 % dos trechos | Baixio; Delmiro Gouveia | recalcular folga = h − y; `verificar_trechos` |
| Extensão total que não fecha com a soma das parcelas; dois limites de velocidade no mesmo documento | Salitre Etapa 2 | `reconciliar_extensoes`; `verificar_limites_alternativos` |
| Cota do rasto incoerente no quadro de bueiros | CAC Trecho 1 (B31) | monotonia do perfil |
| Capacidade de tubo dreno do memorial 4,7 a 6,9 vezes menor que Manning parcial; razão entre DN que não segue D^(8/3) | Delmiro, dreno de fundo; CSB 2DN150 | `capacidade_tubo_parcial`; pedir S e n usados |
| Fórmula legada embutida (Xingó: 33,5·D^2,67·i^0,5 equivale a n ≈ 0,0093; com n 0,012 a 0,013 a capacidade cai 22 a 28 %) | Xingó, tubo dreno | converter para n equivalente antes de comparar |
| Hietograma por polinômio não recuperável: pico do HUT +5,3 % sobre o do projeto | Delmiro BHD1 | declarar que o gabarito não é reproduzível |
| IDF emprestada de outra região (Wilken, SP, num perímetro semiárido) ou sem faixa de duração | vários | sinais de `delegar-climatologia.md` §3; `[DELEGAR: clima]` |
| Gabarito do próprio manual depende de n não informado (HDS-5 p. 280: 6,47 m/s com n 0,012; 6,07 com n 0,013) | HDS-5 | declarar o n adotado |
