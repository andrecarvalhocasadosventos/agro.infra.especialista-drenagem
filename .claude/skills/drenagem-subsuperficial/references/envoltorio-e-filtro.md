# Envoltório e filtro: critério hidráulico (Drenagem) × filtro real (Geotecnia)

Fronteira (MATRIZ §3.3 e D-86 do CDV): a Drenagem especifica o **critério** (razões granulométricas, necessidade,
gradiente de saída) e a vazão; a Geotecnia decide o **filtro real**, a granulometria do material disponível, o
geotêxtil e o risco de piping. Toda saída das funções abaixo é **indicativa**. Bloco `[DELEGAR: geotecnia]` em
`delegar-irrigacao-e-geotecnia.md`.

## 1. Precisa de envoltório? (fluxograma do ILRI-56)

`necessidade_envoltorio_ilri56` [ILRI-56 p. 46-47, Fig. 7; p. 165-171]:

1. Argila > 40 %: provavelmente **sem** envoltório filtrante (a recomendação segura é > 25 % no nível do dreno; a
   experiência holandesa dá 17,5 %). O envoltório ainda pode reduzir a resistência de entrada.
2. SAR e CE da água de rega com dispersão de argila possível (observado até 40 % de argila): seguir o método HFG.
3. Argila > 25-30 %, PI > 12 ou Cu > 15: critérios indicam não requerido; conferir por HFG.
4. Demais: **HFG = exp(0,332 − 0,132 K + 1,07 ln PI)** (K = Ks ou K calculado do d15, m/d). Gradiente de saída sem
   envoltório i_x = q1max/(Ks Apu), Apu = Ap/2 (água entra pela metade inferior do tubo); q1max = vazão máxima por
   m de dreno, com o lençol na superfície (mesma equação de espaçamento) [ILRI-56 p. 43, 47]. **i_x > HFG → envoltório
   necessário** (ou volumoso, para reduzir a resistência de entrada).
Os limiares são faixas: a função devolve `indicadores`, não decisão dura.

## 2. Critério granulométrico de Terzaghi (`criterio_de_filtro_hidraulico`)

DNIT-DREN p. 252-253 (Terzaghi, SCS, USBR; geotêxtil: método do Comitê Francês) [DNIT-DREN p. 252-253]:
- permeabilidade: D15f ≥ 5 D15s (máx. 5 % passando na peneira nº 200);
- retenção: D15f ≤ 5 D85s; D15f ≤ 40 D15s; D50f ≤ 25 D50s;
- tubo: D85f ≥ diâmetro do furo do tubo; uniformidade: 2 ≤ D60f/D10f ≤ 20.

A calculadora usa **um só** fator (padrão 4) para as duas razões e avalia só D15f/D85s e D15f/D15s, mais um aviso
(não reprovação) para D15f/D15s > 40. **Não** verifica D50, uniformidade nem o furo do tubo (lacuna). O ILRI-56 observa
que o D15 do filtro é, na prática, um tamanho de poro O85-O95, e que a **ponte (bridging)** permite razões de 4 a 7
[ILRI-56 p. 63, Box 10].

**Atenção (revisão F7):** o fator 4 é conservador **só na retenção** (D15f ≤ 4 D85s é mais exigente que ≤ 5). Na
**permeabilidade** ele é **menos** exigente que o DNIT: D15f ≥ 4 D15s aprova filtros com razão 4 a 5 que o DNIT
reprova (D15f ≥ 5 D15s, p. 252). No parecer: rodar com `fator=5` para comparar com o DNIT, ou conferir a razão de
permeabilidade à mão contra 5. Registrado em `tools/dren/DIVERGENCIAS.md` (F7, Lote B).

## 3. Pontos de controle do envoltório granular (`envoltorio_granular_pontos_controle`)

[ILRI-56 p. 66-68; PDF = impr. + 20]. Subíndices c (grosso) e f (fino) são as fronteiras da faixa do envoltório:

| Ponto | Regra | Natureza |
|---|---|---|
| 1 | D15c ≤ 7 d85f (fronteira fina do solo-base; razão > 9 sempre falhou, Sherard) | retenção |
| 2 | D50c = 5 D15c (Cu ≈ 6) | guia de gradação |
| 3 | D100c ≤ 9,5 mm | segregação |
| 4a | D15f ≥ 4 d15c (fronteira grossa do solo-base) | hidráulico |
| 4b | D15f = D15c/5 | guia de faixa |
| 5 | D5f > 0,074 mm | hidráulico |
| 6 | D60f = D60c/5 | guia de faixa |
| 7 | D85 > abertura do furo do tubo (em geral D85 > 2 mm) | retenção/ponte |

O livro chama 2, 4b e 6 de **guias**, não de critérios; o projetista decide. Usar 4a se a faixa for praticável e Cu > 2;
se Cu < 2 usar 4b ou algo entre 4a e 4b [ILRI-56 p. 68]. Se 4a > ponto 1, não há faixa viável em D15: relaxar um critério.
d15c > 0,09 mm: o ponto 4a funciona mal. Cobertura mínima dos furos: 75 mm (construção) [ILRI-56 p. 69]; brita britada
com K < 300 m/d, sem partículas lamelares (fator 2) e com peneiramento completo (21 peneiras) [ILRI-56 p. 69]. Sem
exemplo numérico completo no livro (só Figs. 11-12, p. 71-72): o teste da calculadora é de consistência aritmética.

## 4. Outras espessuras e materiais citados (para não perder)

Embrapa: seixo rolado como padrão, ≥ 5 cm de espessura; palha de arroz decompõe em clima quente; manilha cerâmica de
30 cm × 10 cm de diâmetro interno; concreto > 15 cm [EMBRAPA-DREN-SUBT p. 21-22]. NEH 624: envoltório mínimo 3 pol.
[NRCS-NEH624-CH04 p. 87]. Geotêxtil: retenção, hidráulica e anti-colmatação [ILRI-56 p. 76-88]: `[DELEGAR: geotecnia]`.
DNIT-ES015/016/017 especificam o material e a execução do dreno e do filtro de manta (p. 3-7), não o dimensionamento.

## 5. O que o parecer diz

"Critério hidráulico de envoltório (indicativo): [comando]. Dados: d15, d85 (solo-base), PI, argila %, SAR, Ks, q1max.
Resultado: [necessário/não/indicadores]. Filtro real, geotêxtil e risco de piping: `[DELEGAR: geotecnia]`. Premissa
provisória: envoltório de brita ≥ 5 cm, sujeito a Geotecnia."
