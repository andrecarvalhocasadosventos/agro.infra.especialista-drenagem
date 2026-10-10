# Caso HR-05 — NEGATIVO: premissas sem dado no 2D dos riachos Recife e Ferreira (TPF)

**Tipo:** negativo (premissas e omissões; nenhum erro aritmético provado). `REL-FINAL` (id 1709) e `HR-RF` como em HR-04; marcas A e B; sem ✓h.

## Evidências
1. **Malha de 50 m** para riachos de calha estreita (REL-FINAL:57). Sem estudo de sensibilidade de malha nem breaklines nas margens declarados (A: nenhuma menção nas p. 55-62). Para fins de mancha em planície larga, 50 m pode bastar; para a lâmina em calha, não (o manual do 2D recomenda refinar a calha com breaklines: [USACE-HECRAS-2DUM-66 p. 53]).
2. **n único = 0,040** (REL-FINAL:57), contra 0,035 no rio Verde e no São Francisco no mesmo relatório (REL-FINAL:41, 52, 54). Sem justificativa da diferença nem uso de mapa de uso do solo.
3. **Contorno de jusante por declividade (0,012 %)** sem descrição da seção de saída nem do que existe a jusante dos riachos (REL-FINAL:55-57). A profundidade normal imposta só vale para seção uniforme com a declividade do leito local; arquivo `.u01` dos riachos não conferido para esse valor (só a declividade de 0,002 nos contornos de entrada foi lida).
4. **Sem ARF.** Sub-bacia Recife-SB1 tem 932,21 km² e usa a IDF pontual sem redução por área (REL-FINAL:56-57; A: nenhuma menção a ARF). Para bacias dessa ordem, o ARF costuma ser < 1 e o Q de pico SCS tende a ser superestimado; sem número, não quantificado. Premissa de treinamento: ARF é entrega do Clima (`chuvas-intensas-e-idf`).
5. **Sem calibração** (nenhuma marca de cheia, curva-chave ou imagem de evento no texto).
6. **Hidrograma na travessia (589,69 m³/s) sem origem** (ver HR-04) e sem checagem do volume: o pico de Recife-SB1 sozinho é 1.701,99 m³/s para TR 100 (REL-FINAL:57).
7. **TR 2, 10, 25 e 100** foram simulados (REL-FINAL:56); o critério de TR do sifão sob o riacho Recife (obra enterrada) não é declarado.
8. **SB7 do rio Verde** (caso HR-06) tem Tc de Kirpich 7,5 % acima do informado; no mesmo relatório.

## O teste que revelaria
Rodar o TR 100 com malha 25 m na calha e n = 0,035 e 0,050; rodar com ARF do Clima; comparar lâmina na seção do sifão. Se a lâmina variar > 0,3 m, a cota de projeto do sifão não pode vir do modelo atual.

## Gabarito do caso negativo
O parecer correto lista os 6 itens acima como "premissa sem dado", marca o resultado como "indicativo de mancha" (nunca cota de projeto) e delega ARF ao Clima.
