# Blocos `[DELEGAR]` desta skill (Irrigação, Geotecnia, Hidráulica, Orçamento)

Formato e regras do protocolo: `drenagem-fundamentos` §4. O especialista **solicita**; o Gestor aprova o roteamento.
Destinatário que ainda não existe: o bloco vira pendência para a equipe humana e a premissa provisória vale rotulada,
com o impacto de mudar. Ids válidos: `irrigacao`, `geotecnia`, `hidraulica`, `orcamento`, `clima`.

## 1. Irrigação (D5: recarga, salinidade, lençol admissível)

```
[DELEGAR: irrigacao]
pedido:      recarga de projeto q (m/d), lençol admissível (profundidade mínima no meio do vão) e exigência de salinidade
entrego:     espaçamento e profundidade de dreno por Hooghoudt/Ernst/Glover-Dumm (tools.dren.drenos), vazão por linha
preciso de:  lâmina bruta e eficiência por setor (m/d), percolação profunda, turno de rega e intermitência (para escolher
             permanente × transitório), cultura e profundidade radicular (m), classe de salinidade da água e do solo,
             fração de lixiviação, nível de anteprojeto
premissa provisória: q = 2 a 4 mm/d (irrigado com alguma chuva, ILRI-56 p. 42) ou 1 a 2 mm/d (árido); lençol 0,8 a 0,9 m
             em culturas anuais e 1,0 a 1,2 m em fruteiras (FAO-IDP62 p. 113); regime permanente
impacto se mudar: o espaçamento é muito sensível a h, K e q (ILRI-56 p. 45): q dobrado reduz L em cerca de 30 %;
             regime transitório troca Hooghoudt por Glover-Dumm; salinidade pode exigir dreno mais fundo
urgência:    bloqueia a resposta (sem q e lençol a resposta é só ordem de grandeza)
```

Notas: (a) a Irrigação entrega recarga, não q "de dreno"; q = recarga que chega ao lençol (lâmina × (1 − eficiência) +
chuva efetiva − escoamento superficial); (b) o rebaixamento entre regas sai de μ e do turno [FAO-IDP62 p. 114, Fig. 35];
(c) salinidade, lixiviação e descarga de sal (FAO-IDP62 Anexos 6 e 7, p. 153-170) são da Irrigação.

## 2. Geotecnia (K, camadas, barreira, filtro real, piping)

```
[DELEGAR: geotecnia]
pedido:      K por camada, profundidade da camada impermeável abaixo do dreno, filtro/envoltório real e risco de piping
entrego:     critério hidráulico de envoltório (HFG, i_x, razões D15/D85 de Terzaghi, pontos de controle do ILRI-56),
             gradiente de saída, vazão máxima por metro de dreno (q1max), k adotado como premissa
preciso de:  K horizontal (e vertical, se Ernst) por camada em m/d (furo de trado ou Porchet), perfil com espessuras,
             cota da barreira, granulometria do solo-base (D10, D15, D50, D60, D85, % argila, PI, SAR) e do material de
             envoltório disponível, risco de dispersão
premissa provisória: K por textura (ILRI-56 Tab. 14, p. 175, faixa larga, usar média geométrica quando houver medidas);
             D como hipótese; envoltório de brita ≥ 5 cm (EMBRAPA-DREN-SUBT p. 22)
impacto se mudar: K varia por três ordens de grandeza na faixa por textura e muda L na mesma proporção (raiz de K);
             D pesa pouco se D > L/4; envoltório muda a resistência de entrada e o r efetivo
urgência:    bloqueia a resposta | refina a resposta (depende da fase)
```

Para dreno de fundo/subpressão: pedir também K sob o revestimento, freático (cenários cheio/vazio), perfil de corte/aterro,
estabilidade do revestimento sob subpressão (limite do CSB: 0,5 mca, 1341:77).

## 3. Hidráulica (canal revestido, deságue, poço)

```
[DELEGAR: hidraulica]
pedido:      geometria e NA do canal revestido, cota do deságue do dreno de fundo/coletor, decisão canal × sifão
entrego:     vazão de subpressão por critério (CSB, Delmiro, Xingó), DN e comprimento até a saída
preciso de:  estaca, seção (b, talude, tirante), cotas do fundo, NA do canal e do coletor/talvegue receptor, taxa de
             enchimento e esvaziamento
premissa provisória: cota de descarga ≥ 10 cm acima do espelho do coletor (EMBRAPA-DREN-SUBT p. 20)
impacto se mudar: carga H, comprimento até a saída e Q por tubo
urgência:    refina a resposta
```

Poço vertical de drenagem e bombeamento de drenagem (NEH 624 cap. 7; FAO-IDP62 Anexo 22, p. 229-234): fora do escopo
desta skill, pedir à Hidráulica (`pocos-tubulares`, `estacoes-elevatorias-e-bombas`).

## 4. Orçamento (custo por alternativa)

```
[DELEGAR: orcamento]
pedido:      custo por alternativa de dreno (DN, espaçamento, envoltório, profundidade)
entrego:     m de dreno por DN, m³ de escavação de vala, m³ de envoltório, nº de PIL/caixas, extensão de coletor
preciso de:  custo por alternativa, referência e data-base
premissa provisória: sem preço (só quantitativos)
impacto se mudar: escolha entre dreno mais fundo e espaçado × raso e denso (FAO-IDP62 p. 111: no Egito, dreno 20 cm mais
             raso, com 50 m em vez de 80 m, custou cerca de 60 % mais) e entre DN maior e mais linhas
urgência:    refina a resposta
```

A alternativa com custo relevante vai ao `orcamento` **antes** da recomendação final (núcleo §3, passo 5).
