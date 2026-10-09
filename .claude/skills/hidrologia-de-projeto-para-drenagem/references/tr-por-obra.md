# Tempo de retorno (TR) por tipo de obra e risco hidrológico

Páginas = página física do PDF. TR é decisão de projeto: o corpus dá recomendações de órgãos rodoviários, de outorga e de drenagem urbana, **nenhuma específica de perímetro irrigado**, exceto o Drainage Manual do USBR. A escolha final vai ao parecer como premissa, com o risco da seção 3.

## 1. Tabela de TR por obra

| Obra | DNIT / rodovias | DAEE-SP | Outras fontes | Prática do acervo (rastro) |
|---|---|---|---|---|
| Drenagem superficial (valeta, sarjeta, dreno de parcela) | 5 a 10 anos; sarjeta de corte com chuva de 5 min e TR 10 [ABDER-APOSTILA p. 38; DNIT-DREN p. 171] | — | USBR: drenos de superfície de 5 a 15 anos [USBR-DRAINAGE p. 57]; PMSP microdrenagem 2 a 10 [PMSP-DRENURB-V2 p. 30]; AASHTO via HDS-2: via rural local 5 a 10 [FHWA-HDS2 p. 37] | Baixio de Irecê: drenos 5 (doc 670:119); Iuiu: drenos e demais dispositivos 10 (doc 1051:316); CSB: valetas e canais de desvio 50 (1341:45; o mesmo memorial diz 100 em 1341:70) |
| Drenagem profunda | 1 ano [ABDER-APOSTILA p. 38] | — | — | — |
| Bueiro tubular (grota) | 10 (como canal) e 25 (como orifício); IS-203: dimensionar com TR 10 e verificar o nível a montante com 20 ou 25 [ABDER-APOSTILA p. 38; DNIT-HIDRO p. 23-24] | Zona rural 25; "obra de maior importância ou porte", 100 [DAEE-IT-DPO11 p. 1] | DNIT: bueiros de 10 a 20 anos como prática geral [DNIT-HIDRO p. 23]; AASHTO: coletora rural maior 25, menor 10 [FHWA-HDS2 p. 37]; GOINFRA: A < 1 km² TR 10 (orifício 25); 1 a 5 km² TR 25 (orifício 50) [ABDER-APOSTILA p. 38] | Baixio: bueiros 25, verificação como orifício 50 (doc 670:119); Iuiu: sob estrada 25 (1051:316); **Delmiro Gouveia: TR 5 e 20 para obras da estrada de serviço** (1492:157; BUC sob canal TR 20 e 50, caso `delmiro_gouveia_bueiros_tubulares_sob_canal_principal`); Iuiu 2018: TR 25 em 91 bueiros sob canal |
| Bueiro celular (galeria) | 25 (canal) e 50 (orifício) [ABDER-APOSTILA p. 38]; DER-MG idem [p. 39] | Idem acima | GOINFRA: 5 a 10 km² TR 50 [ABDER-APOSTILA p. 38] | Salitre RC500-800 e CSB: 100; **CAC Trecho 1: 100 (vazões para 2, 5, 10, 25, 50 e 100 no Quadro 4.19, doc 1139:228)** |
| Travessia e overchute **sob canal** adutor (OAC) | Sem valor específico; pontilhão 50, ponte 100 [ABDER-APOSTILA p. 38] | 25 rural; 100 se importância ou porte maior [DAEE-IT-DPO11 p. 1] | PMSP: macrodrenagem 25 a 50; 100 para áreas vitais ou risco de vida [PMSP-DRENURB-V2 p. 30]; PMSP-V1: 100 para macrodrenagem [PMSP-DRENURB-V1 p. 33] | CSB: 100 (1341:45); Xingó: 100 (1419:26); Iuiu: sob canal 50 (1051:316) |
| Pontilhão | 50 [ABDER-APOSTILA p. 38] | — | — | — |
| Ponte | 100; 50 a 100 conforme o tipo e a importância [DNIT-HIDRO p. 23] | — | AASHTO: arterial rural 50; coletora 25 [FHWA-HDS2 p. 37]; ferrovia ≥ 200 com análise de risco [ABDER-APOSTILA p. 39] | — |
| Canal de drenagem aberto (coletor principal) | Corta-rio: "tempo de recorrência compatível com o custo econômico da obra" [DNIT-DREN p. 217] | 25 rural, 100 urbano [DAEE-IT-DPO11 p. 1] | PMSP: macrodrenagem 25 a 50 [PMSP-DRENURB-V2 p. 30]; USBR: 25 se a estrutura for cara ou o dano puder exigir projeto mais conservador [USBR-DRAINAGE p. 57] | — |
| Barramento e vertedouro | — | H ≤ 5 m: 100 (sem risco a jusante) e 500 (com risco); 5 < H ≤ 10: 500 e 1.000; H > 10: 1.000 e 10.000 [DAEE-IT-DPO11 p. 1-2] | Fora do escopo desta skill | → `reservatorios-e-pequenas-barragens`, `vertedouros-e-dissipadores` |

Observações:
- O TR da obra e o TR da verificação são dois números (bueiro: dimensionar com um, verificar o nível a montante com o outro, "como canal" e "como orifício"). O parecer declara os dois.
- A AASHTO (via HDS-2) está em AEP: 0,02 = 50 anos; 0,04 = 25; 0,1 = 10; 0,2 = 5 [FHWA-HDS2 p. 37].
- Os valores do DNIT são de rodovia. O DAEE-SP é norma paulista de outorga (valores mínimos). Nenhum vale por si no perímetro: a escolha cabe ao projetista (D2-Hid) e ao contratante, com o critério de risco abaixo.
- **TR de bueiro de perímetro irrigado é ponto aberto para a F7 (padrão provisório, decisão F7):** USBR, drenos de superfície 5 a 15 anos [USBR-DRAINAGE p. 57] × acervo 25/50 (Baixio, Iuiu) e 100 (CSB, Salitre, CAC). Não decidir: mostrar as duas faixas e o risco J de cada uma.
- Valores que o corpus não traz: TR de dreno parcelar em irrigação, de canal coletor de perímetro, de OAC sob canal em Codevasf. A prática do acervo (coluna da direita) é o rastro disponível; é preciso dado do contratante.

## 2. Divergências entre fontes sobre o mesmo item

| Item | Valores | Como tratar |
|---|---|---|
| Bueiro tubular rural | 10 a 20 (DNIT-HIDRO), 10 canal/25 orifício (ABDER, citando DNIT), 25 (DAEE) | Dimensionar com 25 e declarar. Se adotar 10, mostrar a verificação com 25 |
| Bueiro celular | 25/50 (DNIT, via ABDER) × 100 (CSB, Salitre) | A prática do acervo é mais conservadora que o DNIT; justificar pela importância do canal |
| Macrodrenagem | 25 a 50 (PMSP-V2) × 100 (PMSP-V1) | Mesmo órgão, dois volumes; citar o volume |
| Valeta do CSB | 50 × 100 no mesmo memorial | Registrar a inconsistência; não escolher por conta própria |
| Vão de ponte e bueiro | "TR 10 dimensiona, TR 20-25 verifica" × "TR 25 dimensiona" | Declarar o par TR de projeto e de verificação |

## 3. Risco hidrológico (vida útil × TR)

J = 1 − (1 − 1/TR)^n, probabilidade de ocorrer ao menos uma vez, em n anos, uma vazão igual ou maior que a de TR [DNIT-HIDRO p. 24; ABDER-APOSTILA p. 37-38; PMSP-DRENURB-V2 p. 29, eq. 1.7]. Valores calculados (conferem com a Tab. 1 da ABDER, p. 38, e com o exemplo TR 200 e n = 25 → 11,8 %, p. 37):

| TR (anos) | n = 10 | n = 20 | n = 25 | n = 50 |
|---|---|---|---|---|
| 5 | 89 % | 99 % | 100 % | 100 % |
| 10 | 65 % | 88 % | 93 % | 99 % |
| 25 | 34 % | 56 % | 64 % | 87 % |
| 50 | 18 % | 33 % | 40 % | 64 % |
| 100 | 10 % | 18 % | 22 % | 39 % |
| 200 | 5 % | 10 % | 12 % | 22 % |
| 500 | 2 % | 4 % | 5 % | 10 % |

TR para um risco admitido J em n anos: TR = 1/(1 − (1 − J)^(1/n)). Exemplos: J = 10 % em 25 anos → TR ≈ 238; J = 20 % em 25 anos → TR ≈ 113; J = 50 % em 25 anos → TR ≈ 37.

Uso:
- Risco de **ser excedida**, não de colapso. A ABDER lembra que J = 87 % para TR 25 e n = 50 não significa que a obra colapse [ABDER-APOSTILA p. 37].
- A obra de vida útil de 50 anos com TR 25 tem 87 % de chance de ver uma chuva maior. Isso não é erro de projeto, mas o parecer deve dizer a consequência (HW acima do admitido, transbordamento, erosão) e se há folga para esse evento.
- Escolha por risco e custo: o PMSP trata a escolha como "risco aceitável" balanceado com o custo [PMSP-DRENURB-V2 p. 29]. O DNIT pede folga de 1,00 m em pontes e permite carga a montante em bueiro [DNIT-HIDRO p. 23-24].
- Calculadora: `risco_hidrologico(TR, vida_util)` e `tr_para_risco(J, n)` (CLI `tools.dren.hidrologia`; teste `test_risco_hidrologico_e_tr_para_risco`). Ex.: TR 25, n = 25 → 64 %; TR 50, n = 25 → 40 %; J = 10 % em 25 anos → TR 238. Mostrar o comando e a saída no parecer (V1).
