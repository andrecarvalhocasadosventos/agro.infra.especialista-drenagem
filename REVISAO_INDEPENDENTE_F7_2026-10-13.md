# Revisão independente do portão F7, Especialista Drenagem (pedido 2.B, 2026-10-13)

Revisor independente: não escreveu o pacote nem as recomendações. Escopo: os 20 critérios de `PARA_O_ANDRE_F7.md`, as
premissas HEC-RAS de `PARA_O_ANDRE.md`, a seção C (14 xfail), o dissipador (§D) e as perguntas 21–23. Nada foi editado
no pacote; somente este arquivo foi escrito. R0: nada aqui decide D-xx do Visão CDV.

**Como foi conferido.** Os `_texto` estão em `Especialista Drenagem/referencias/_texto` e
`Especialista Hidraulica/referencias/_texto`, por marcador `<!-- p. N -->`. As contas foram refeitas pela calculadora
`tools/dren` (venv squad), por import e com `PYTHONDONTWRITEBYTECODE`. A suíte roda com 291 passed e 14 xfailed:
o número cresceu desde os 273 citados no F7 porque entraram os testes de HEC-RAS, e os 14 xfail não mudaram.

**Classes:** (i) ok, baixa consequência; (ii) muda resultado ou calculadora; (iii) precisa de dado ou decisão do
Visão CDV (ou do André), não do treinamento.

---

## Achados que o André deveria saber antes de responder

1. **Item 19: o sinal está trocado.** Trocar a tabela do código pela Embrapa Tab. 3 [EMBRAPA-DREN-SUBT p. 14], com
   o μ médio, dá L de Glover-Dumm **−11 % (areia média/grossa), −8 % (franco) e +22 % (argila)**. O pacote escreveu
   +13/+8/−18 %, que é a razão inversa (código ÷ Embrapa). Refeito com `glover_dumm_espacamento`. Por isso a troca é
   **menos conservadora em argila**: μ menor resulta em L maior.
2. **Item 20: "Manning subestima ~1,8×" tem outra causa.** O fator vem quase todo da **integração com afluência
   uniforme ao longo do dreno**, e não da fórmula. Pelo FAO-62, Manning integrado com vazão linear (Eq. 12–15,
   p. 215–216) dá Q = √3 × Q_Manning(s = H/B), ou seja, 1,73×. Wesseling (89·d^2,714·s^0,571) é a fórmula do
   **tubo tecnicamente liso** [FAO-IDP62 p. 213–214]. Para o corrugado, o FAO usa Manning com Km da Tab. A20.3
   (p. 216), e para DN ≈ 300 mm de corrugação grande o Km fica entre **45 e 50** (n ≈ 0,020–0,022), pior que o
   n = 0,016 do código. No D-86 (d = 0,30 m, s = 10⁻⁴) isso dá:
   - Manning sem integração: 7,86 L/s;
   - Manning integrado com Km 46: **10,0 L/s**;
   - Manning integrado com Km 65: **14,2 L/s**;
   - Blasius com a = 0,77: 12,2 L/s;
   - Wesseling liso: **17,6 L/s**.

   Adotar Wesseling como padrão para o corrugado superestima a capacidade do tubo em até ~75 %.
3. **Item 21: a citação e o enquadramento estão imprecisos.** A faixa "1–2 mm/d" está na **Tab. 8 do FAO-62, p. 114**
   (e no ILRI-56, p. 42), não na p. 113. A p. 113 diz que, em clima árido, **2–4 mm/d** bastam para a lixiviação.
   Além disso, o próprio FAO manda usar a experiência local, e a experiência local do Submédio São Francisco no corpus
   é bem mais alta:
   - Embrapa Bebedouro: descarga normativa de 4 mm/d e picos de 13,6 mm/d [EMBRAPA-BEBEDOURO-1986];
   - Embrapa Maniçoba (sulcos): q de projeto de 8 mm/d e picos de 8–10 mm/d [EMBRAPA-MANICOBA-1988].

   Portanto 1,2 L/s/ha (= 10,4 mm/d) é alto, mas **não está "fora da faixa"** para irrigação por superfície no
   semiárido baiano.
4. **Item 13: h deve ser a lâmina, não a profundidade da valeta.** A fórmula f = √(46·h) (cm) é a forma da USBR
   F = √(C·y), com C = 1,5 ft ≈ 46 cm e y = **lâmina d'água**. A fonte é Chow (1959), §7 (borda livre), que está fora
   do corpus; isso é conhecimento do revisor e precisa ser conferido. Na leitura correta, f > y em canal raso é normal
   (borda livre de canal pequeno de terra), e a "estranheza física" registrada no pacote some. A legenda "h =
   profundidade da valeta" do DNIT-DREN p. 162 vale para f = 0,2·h. No topo da faixa (10 m³/s), a USBR usaria C maior
   que 1,5 ft, então o 46 fica levemente contra a segurança ali.
5. **Item 1: falta uma opção no quadro.** É a tabela da IS-203 [DNIT-IPR726 p. 258 e 463]:
   - bueiro tubular: TR 15 como canal e 25 como orifício;
   - bueiro celular: TR 25 como canal e 50 como orifício;
   - pontilhão: TR 50;
   - ponte: TR 100.

   A DAEE-IT-DPO11 p. 1 também pede **mínimo de 100 anos em travessia "de maior importância ou porte"**, e não só os
   25 da zona rural. A conta de risco usou 25 anos de vida útil. Para o canal adutor, com 50 anos de vida útil, o risco
   sobe: TR 50 = 64 % e TR 100 = 40 %.
6. **Dissipador (§D): o item já está decidido.** A R5 foi aprovada em 2026-10-09 (`DECISOES_2026-10-09.md`; D10 do
   `PLANO.md`; MATRIZ linha 34) e a skill do Hidráulico já foi corrigida (linha 28). O §D do F7 está desatualizado.
   Resta uma zona cinzenta:
   - o `PLANO.md` (linha 51) põe "dissipadores-tipo DNIT (seleção)" na Drenagem;
   - a skill `vertedouros-e-dissipadores` (linha 145) atribui DNIT-DREN/ES022 ("dissipador") à Drenagem.

   Convém fechar a fronteira assim: o dispositivo-tipo de descida ou sarjeta do Álbum fica com a Drenagem, que
   seleciona; o dissipador de saída de bueiro e de estrutura fica com a Hidráulica, que dimensiona.

---

## A. Critérios 1–20

### 1. TR de bueiro em perímetro irrigado
- **Fontes conferidas.** Todas as citações conferem:
  - USBR-DRAINAGE p. 57: dreno superficial de 5 a 15 anos; 25 "where relatively expensive structures are involved";
  - DNIT-HIDRO p. 23: bueiros de 10 a 20 anos;
  - DNIT-HIDRO p. 24: pela IS-203, projeto com TR 10 e verificação do NA com 20 ou 25;
  - DAEE-IT-DPO11 p. 1: 25 em zona rural, com nota que pede 100 em obra de maior importância.

  **Falta a opção da IPR-726 p. 258** (tubular 15/25; celular 25/50 como orifício; pontilhão 50).
- **Números.** 1 − (1 − 1/TR)^25 dá 64 %, 40 % e 22 % para TR 25, 50 e 100: confere. Com n = 50 anos, que é a vida
  útil natural do adutor, dá 87 %, 64 % e 40 %.
- **Recomendação.** Concordo no essencial e proponho tornar a verificação obrigatória e explícita:
  - estrada de serviço: TR 25;
  - sob o canal adutor: TR 50 no projeto, com **verificação obrigatória em TR 100** e o critério "NA de montante abaixo
    da crista do aterro do canal com folga, sem galgamento e sem entrada no canal".

  Hoje o pacote diz "100 só se a falha põe o adutor em risco", mas toda passagem sob aterro do adutor põe o adutor em
  risco quando é galgada.
- **Consequência.** Pode aumentar células ou DN nas travessias do adutor.
- **Classe (ii).** O TR final das obras do adutor é critério do contratante: (iii) no CDV.

### 2. Ke de alas paralelas (caixa)
- **Fontes conferidas.** HDS-5 p. 216 e HEC-13 p. 100 dão 0,7; DNIT-DREN p. 130 dá 0,2. A linha do DNIT parece fundir
  a do "side-tapered 0,2".
- **Números.** ΔHW = 0,5·V²/2g = 0,229 m com V = 3 m/s: confere.
- **Recomendação.** Concordo (0,7).
- **Classe (i).**

### 3. Limite de área do racional
- **Fontes conferidas.**
  - HDS-2 dá 200 ac (80 ha), linhas 3864 e 7563.
  - IPR-726 p. 259: racional até 4 km² e corrigido de 4 a 10 km². A mesma página tem também uma tabela com "< 10 km²:
    racional e racional corrigido", então a fonte é internamente inconsistente.
  - DNIT-HIDRO p. 131: coeficiente de distribuição para A > 1 km².
- **Números.** 2^−0,1 = 0,933 (−7 %) e 3,5^−0,1 = 0,882 (−12 %): confere.
- **Recomendação.** Concordo. Registrar que o Cd só se aplica acima de 1 km².
- **Classe (i).**

### 4. Tc mínimo de drenagem superficial
- **Fontes conferidas.**
  - IPR-726 p. 258: 5 min.
  - IPR-726 p. 463 (IS-239, vicinais): 10 min.
  - Álbum p. 214 (OCR): 6 min com TR 10, NBR 10844, para dispositivo linear.
- **Números.** O +12 a +19 % no L crítico depende da IDF, que não está no pacote; não foi refeito. É plausível para
  i = K/(t+b)^c com b de 10 a 20 min.
- **Recomendação.** Concordo (5 min, com sensibilidade a 10 min).
- **Classe (i).**

### 5. TR da drenagem superficial
- **Fontes conferidas.** IPR-726 p. 258 dá "5 a 10" (não só 10). LOC-IME p. 53 traz DNER 10 e ENGEFER 25.
- **Números.** 2,5^0,241 = 1,247 e 2,5^0,172 = 1,171: confere (+17 a +25 %).
- **Recomendação.** Concordo.
- **Classe (i).**

### 6. Declividade mínima de sarjeta e valeta
- **Fontes conferidas, com ressalva.**
  - DERPR-ES-DR-01 p. 10 é uma **especificação de execução**: abaixo de 0,5 % há demolição, "ressalvados casos
    justificados em projeto".
  - HEC-12 p. 19 dá 0,3 % para **sarjeta de pavimento com meio-fio** (0,2 % em terreno muito plano), não para valeta
    de terra.

  Nenhuma das duas é critério hidráulico de valeta de perímetro.
- **Números.** √(0,3/0,5) = 0,775 (−23 %): confere.
- **Recomendação.** Concordo com 0,5 % / 0,3 % / < 0,3 % revestida, e acrescentaria a checagem de velocidade mínima de
  autolimpeza (ver item 11) em vez de só a declividade. No Baixio, que é plano, isso pesa na escavação.
- **Classe (i).**

### 7. y/D máximo de tubo parcialmente cheio
- **Números.** Recalculei Q/Q pleno: 0,912 em 0,75 e 1,000 em 0,82 (9,7 %): confere.
- **Recomendação.** Concordo. Lembrete: para bueiro o critério que governa é HW/D (controle de entrada); o y/D vale
  para galeria e dreno em lâmina livre.
- **Classe (i).**

### 8. n do concreto em bueiro
- **Fontes conferidas.** HDS-5 p. 90 e linha 3542 (0,012); DNIT-DREN usa 0,015 nas declividades críticas.
- **Números.** "~8 % por degrau" vale de 0,012 para 0,013. **De 0,013 para 0,015 são 15 %.**
- **Recomendação.** Concordo (0,013). O n só pesa em controle de saída.
- **Classe (i).**

### 9. Fator de berço classe A
- **Fontes conferidas.** ABTC Tab. 4.1 p. 37 dá 2,25 a 3,4 "conforme execução e compactação"; EM 2902 p. 71 dá 2,5.
- **Números.** De 2,25 para 2,5 a carga admissível sobe 11 %.
- **Recomendação.** Concordo. A tabela é de **vala**: bueiro sob aterro de canal ou estrada é projeção positiva, e o
  fator de berço é outro. O parecer deve dizer qual instalação foi usada.
- **Classe (i).**

### 10. Carga de aterro sobre tubo
- **Recomendação.** Concordo: ABTC simplificada no anteprojeto; Spangler ou software antes do básico. Cuidado com
  aterros altos do adutor, onde λe independente de H pode errar mais.
- **Classe (i).**

### 11. Velocidade mínima em dreno a céu aberto
- **Fontes conferidas.** NRCS-CPS608-2023 p. 2: "Without site specific information, the minimum design velocity is
  1.4 ft/s" = 0,427 m/s.
- **Recomendação.** Concordo: 0,43 m/s na vazão de projeto quando o projeto não declarar. Aceitar 0,30 m/s (Salitre)
  só com justificativa de baixo aporte de sedimento e manutenção prevista. A falha do trecho Delmiro (0,29 m/s) fica
  como aviso.
- **Classe (ii).**

### 12. Folga de dreno
- **Fontes conferidas.** CPS 608 p. 2: "calculated freeboard, or a minimum of 0.5 feet" = 0,152 m.
- **Recomendação.** Concordo: max(25 % do tirante; 0,15 m). Para coerência com o item 13, considerar √(C·y) nos
  canais de drenagem maiores.
- **Classe (ii).**

### 13. Folga de valeta
- **Fontes conferidas.** IME p. 54 traz f = 0,2·h com "h = profundidade da valeta" e, para 0,3–10 m³/s, a EQ 4.7
  (radical perdido no texto). A imagem do DNIT-DREN p. 162 foi conferida pelo pacote.
- **Divergência.** Ver o achado 4: o h da fórmula com radical é a lâmina (origem USBR √(C·y)).
- **Recomendação ("outra").**
  - Terra até 0,3 m³/s: 0,2·h, com h = profundidade da valeta.
  - Terra de 0,3 a 10 m³/s: f = √(46·y), com y = lâmina em cm.
  - Concreto: Tab. 36 DNIT / Tab. 4.2 IME (20 cm acima de 2,8 m³/s).
  - Mínimo de 0,15 m em todos os casos.
- **Consequência.** Hoje a função dá `ValueError` nessa faixa.
- **Classe (ii).**

### 14. Faixa de Froude instável
- **Fontes conferidas.** HEC-11 p. 38 (0,89–1,13).
- **Recomendação.** Concordo.
- **Classe (i).**

### 15. Colmatação de grelha em ponto baixo
- **Fontes conferidas.** HEC-12 linha ~2978: "allow for 50% clogging".
- **Recomendação.** Concordo. Pouco uso em perímetro (plataformas de EB).
- **Classe (i).**

### 16. Coeficiente da onda cinemática
- **Números.** 0,938/0,933 = 1,005: confere.
- **Recomendação.** Concordo.
- **Classe (i).**

### 17. NERC e Bransby-Williams
- **Fontes conferidas.** Não há primário no corpus: correto.
- **Recomendação.** Concordo (só para reprodução). Acrescentar que a Kirpich também está fora de domínio acima de
  ~0,8 km² [DNIT-HIDRO p. 88]. Em bacia grande, conferir com o método de velocidades (NRCS) e declarar a dispersão:
  7,65 h × 4,92 h = 55 % no Tc.
- **Classe (i).**

### 18. Critério de filtro (Terzaghi)
- **Fontes conferidas.** DNIT-DREN p. 252: permeabilidade D15F ≥ 5·D15S e ≤ 5 % passando na #200.
- **Recomendação ("outra", ajuste).** "Retenção 4–5" não é um número único. Proponho:
  - retenção D15F ≤ 4·D85S, conservador e já implementado;
  - permeabilidade D15F ≥ 5·D15S (DNIT).

  Para o envoltório de dreno agrícola, valem os critérios do ILRI-56 (pp. 53–72) e não o Terzaghi isolado. O filtro
  real é decisão da Geotecnia.
- **Classe (ii).**

### 19. Porosidade drenável μ
- **Fontes conferidas.** EMBRAPA-DREN-SUBT Tab. 3 p. 14 (FAO 1980) confere. As classes não casam uma a uma com as do
  código ("areia" do código pode ser areia fina, 0,12–0,22, ou média/grossa, 0,22–0,35).
- **Números.** Errados no sinal; ver o achado 1. Valores corretos: −11 / −8 / +22 %.
- **Recomendação ("R com condição").** Trocar pela Embrapa, mapear as classes explicitamente e, sem medição, usar o
  **limite superior** de μ da classe, que é conservador porque dá L menor. Em argila, a troca aumenta L em 22 %.
- **Classe (ii).**

### 20. Wesseling para lateral e coletor corrugado
- **Fontes conferidas.** FAO-IDP62 p. 214 (tubo liso; coletor com mais de 5 laterais segue a mesma fórmula) e
  p. 215–216 (corrugado com Manning e Km da Tab. A20.3, até 65).
- **Números.** 7,86 / 11,43 / 17,63 L/s confere, e o C com a = 0,77 dá 61,7.
- **Recomendação ("outra").**
  - Wesseling só para tubo liso.
  - Para o corrugado, implementar o Manning integrado do FAO (Q = √3 × Q_Manning(s = H/B), com Km da Tab. A20.3 por
    DN e corrugação) e manter o Manning sem integração apenas para trecho com vazão concentrada.
  - Conferir os fatores de redução por colmatação do FAO-62 (seção que começa na p. 216).
- **Consequência.** No D-86 a capacidade vai a 10–14 L/s, e não aos 17,6 do Wesseling.
- **Classe (ii).** O DN final do D-86 é (iii).

---

## B. Perguntas 21–23

### 21. Origem do coeficiente de drenagem 1,2 L/s/ha
- **Números.** 1,2 × 8,64 = 10,37 mm/d: confere.
- **Correções.** A citação certa é FAO-62 **p. 114** (Tab. 8), e a p. 113 dá 2–4 mm/d para lixiviação. O semiárido
  baiano com chuva intensa se enquadra melhor em "irrigated areas with some rainfall, 2–4 mm/d" [ILRI-56 p. 42] e na
  experiência local Embrapa de 4–8 mm/d, com picos de 10–13,6. Ver o achado 3.
- **Recomendação.** Pedir a origem ao André, como o pacote faz. Enquanto não houver resposta:
  - não usar 1,2 L/s/ha como gabarito;
  - classificá-lo como provável coeficiente de **coletor ou pico (superficial + subterrâneo)**;
  - para o lateral subterrâneo, calcular q por balanço (perdas de percolação pelo método de irrigação + chuva), com a
    faixa local de 2–8 mm/d.
- **Classe (iii).**

### 22. Conferência humana (✓h) de números do acervo
- **Recomendação.** Concordo. Acrescentaria à lista o **memorial Delmiro 1492:105** (capacidade dos drenos
  DN170/DN230), porque sustenta o D-86 e é xfail estrito sem explicação.
- **Classe (iii)** (dado do André).

### 23. Enunciado dos cartões CDV P-108 e P-272
- **Recomendação.** Concordo. Sem o enunciado, a F10 só faz triagem.
- **Classe (iii).**

---

## C. As 14 divergências (xfail)

- **Legado × HDS-5 (Baixio): ok.** O −6 a −8 % usa a entrada **mais favorável hipotética** (alas de 30–75°); com
  outras entradas a diferença chega a −12 a −18 %. É caso negativo contra a segurança, e o parecer deve dizer que a
  entrada foi suposta.
- **Xingó, lâmina por energia: ok** (convenção).
- **Gabarito inconsistente: ok, com uma exceção de rótulo.** O CSB BTCC-N17 (−27 %) não está comprovadamente
  "errado": a hipótese é leitura errada da Tab. 4.7. Rotular como "não confirmado", não como "gabarito errado".
- **Dado não recuperável: ok.** Conferi a hipótese do Baixio HUT TR 25:
  - com P = 55,56 mm e S = 155,39 mm, a lâmina efetiva é 3,33 mm;
  - com o "Soma(p)" de 71,5 mm, sobe para 8,34 mm (2,5×);
  - o pico passaria de 2,70 para ~6,8 m³/s, contra 6,03 do projeto (+12 %).

  A causa é a chuva, não o método. Manter o xfail e registrar essa reconstrução.
- **Veredito: "C ok", com o reajuste de rótulo do CSB BTCC-N17.**
- **Classe (i).**

## Premissas HEC-RAS (`PARA_O_ANDRE.md`, 2026-10-10)

- **Estabilização dNA ≤ 0,01 m em 2 h.** Aceito como premissa para simulação com **vazão constante** (Q95 ou Q de
  projeto levada ao permanente). Em hidrograma de cheia o critério não se aplica: exigir que o pico tenha passado e a
  recessão começado no ponto de interesse.
- **Sensibilidade de n ±20 %.** A regra está no HRM p. 389, escrita para ruptura de barragem (confere).
- **Limiar de 0,3 m.** É arbitrário. Proponho:
  - ligar o limiar à folga que o NA governa, com limiar = min(0,3 m; 1/3 da folga exigida, por exemplo 1,00 m de
    ponte em DNIT-HIDRO p. 23);
  - quando o limiar for excedido, adotar o NA do cenário +20 %, e não uma "cota por faixa".
- **Erro de volume.** Não tem limiar no manual: fixar ≤ 1 % como premissa declarada.
- **Classe.** (i) para o critério de estabilização; (ii) para o limiar.
- **Itens de 2026-10-09.** Concordo com (b) não instalar até haver modelo próprio e com pedir à TPF os arquivos do rio
  Verde. A fronteira §11.3 já foi decidida pela sessão squad (MATRIZ linha 35).

## Dissipador (§D)

Já decidido (R5/D10, 2026-10-09): nada a responder. Só falta fechar a zona cinzenta dos dispositivos-tipo DNIT
(achado 6). **Classe (i).**

---

## Tabela-resumo

| Item | Pacote | Revisor | Concorda? | Classe |
|---|---|---|---|---|
| 1 TR bueiro | 25 estrada; 50 sob adutor; verif. TR seguinte; 100 se risco ao adutor | idem, mas **verificação TR 100 obrigatória** sob o adutor (sem galgar o aterro); citar IPR-726 p. 258 | parcial | (ii); TR do adutor (iii) |
| 2 Ke ala paralela | 0,7 | 0,7 | sim | (i) |
| 3 limite racional | ≤ 80–100 ha; ≤ 2 km² com Cd; 2–4 com HUT | idem (Cd só > 1 km²) | sim | (i) |
| 4 Tc mín. | 5 min | 5 min | sim | (i) |
| 5 TR superficial | 10 (25 se atinge adutor/EB) | idem | sim | (i) |
| 6 declividade mín. | 0,5 %; 0,3 % justif.; < 0,3 % revestida | idem + checar V mín. | sim | (i) |
| 7 y/D | 0,75 projeto; 0,82 teto | idem | sim | (i) |
| 8 n concreto | 0,013 | 0,013 (corrigir "8 %/degrau") | sim | (i) |
| 9 berço A | 2,25 | 2,25 (só vala) | sim | (i) |
| 10 carga aterro | ABTC; Spangler antes do básico | idem | sim | (i) |
| 11 V mín. dreno | 0,43 m/s | 0,43 m/s; 0,30 só justificado | sim | (ii) |
| 12 folga dreno | max(25 %; 0,15 m) | idem | sim | (ii) |
| 13 folga valeta | 0,2 h terra; tabela concreto; mín. 0,15; incluir √(46h) | incluir **√(46·y), y = lâmina** (origem USBR), não profundidade | parcial | (ii) |
| 14 Froude | 0,89–1,13 | idem | sim | (i) |
| 15 grelha | 50 % | 50 % | sim | (i) |
| 16 onda cinemática | 0,938 | 0,938 | sim | (i) |
| 17 NERC/B-W | só reprodução | idem + método de velocidades em bacia grande | sim | (i) |
| 18 filtro | retenção 4–5; permeab. ≥ 5 | **retenção ≤ 4; permeab. ≥ 5**; envoltório agrícola pelo ILRI-56 | parcial | (ii) |
| 19 μ | trocar pela Embrapa | trocar, **corrigir sinais (−11/−8/+22 %)**, μ no limite superior | parcial | (ii) |
| 20 Wesseling | incluir antes da F10 | **não** para corrugado: Manning integrado (√3) com Km da Tab. A20.3; Wesseling só liso | não | (ii); D-86 (iii) |
| 21 1,2 L/s/ha | perguntar; "fora de 1–2 mm/d" | perguntar; corrigir citação (p. 114) e faixa local 4–8 mm/d | parcial | (iii) |
| 22 ✓h | 3 casos | + Delmiro 1492:105 | sim | (iii) |
| 23 P-108/P-272 | pedir texto | idem | sim | (iii) |
| C 14 xfail | C ok | C ok; CSB N17 "não confirmado" | sim | (i) |
| HEC-RAS dNA | aceitar | aceitar (só Q constante) | sim | (i) |
| HEC-RAS n ±20 %/0,3 m | aceitar | ±20 % ok; limiar ligado à folga; NA +20 % se exceder; erro de volume ≤ 1 % | parcial | (ii) |
| D dissipador | aprovar diff | já decidido (R5); fechar dispositivos-tipo DNIT | — | (i) |

## Resposta sugerida (formato curto)

1 outra: R + verificação TR 100 obrigatória sob o adutor (sem galgar o aterro), citar IPR-726 p. 258; 2 R; 3 R;
4 R; 5 R; 6 R; 7 R; 8 R; 9 R; 10 R; 11 R; 12 R; 13 outra: incluir √(46·y) com y = lâmina d'água (USBR), conferir
na imagem; 14 R; 15 R; 16 R; 17 R; 18 outra: retenção ≤ 4·D85, permeabilidade ≥ 5·D15, envoltório agrícola pelo
ILRI-56; 19 R, corrigindo os efeitos para −11/−8/+22 % e usando μ no limite superior; 20 outra: Wesseling só para
tubo liso, corrugado por Manning integrado (√3) com Km da Tab. A20.3, recalcular o D-86; 21 [origem do 1,2]
+ corrigir a citação para FAO-62 p. 114 e considerar a faixa local da Embrapa; 22 R + Delmiro 1492:105;
23 [enviar os textos]; C ok (CSB N17 = "não confirmado"); HEC-RAS: dNA R (só Q constante), n ±20 % R, limiar
= min(0,3 m; folga/3) com NA +20 % se exceder, erro de volume ≤ 1 %; D: já decidido (R5), fechar os
dispositivos-tipo DNIT.
