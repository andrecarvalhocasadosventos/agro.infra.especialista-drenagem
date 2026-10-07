# Período de retorno (TR) por tipo de obra: fontes e prática dos projetos do acervo

Este arquivo **só escolhe o TR**. A vazão para esse TR (método, Tc, IDF, CN) vem de `hidrologia-de-projeto-para-drenagem`;
o IDF e a chuva de projeto são de Climatologia (`[DELEGAR: climatologia]`). Páginas = marcador do `_texto`
(página física do PDF).

## 1. O que as fontes dizem

| Obra | TR (anos) | Fonte e página | Observação |
|---|---|---|---|
| Bueiro de rodovia | 10 a 20 ("geralmente") | [DNIT-HIDRO p. 23, §3] (IPR-715) | texto: "os períodos normalmente adotados no caso de bueiros são de 10 a 20 anos" |
| Bueiro: procedimento da IS-203 | dimensionar para a condição crítica com **TR 10**; verificar o nível d'água a montante com **TR 20 ou 25** | [DNIT-HIDRO p. 24] | se o nível inunda área marginal, ampliar a seção; considerar amortecimento pela área inundada |
| Ponte | 50 a 100 | [DNIT-HIDRO p. 23] | folga de 1,00 m sob a superestrutura (mais em rio navegável) |
| Bueiro de greide | "função do vulto econômico da obra" (sem número) | [DNIT-DREN p. 202, §3.9.3] | sem carga a montante sempre que possível |
| Sarjeta de corte | **TR 10**, duração de 5 min | [DNIT-DREN p. 171, §3.3.3] | intensidade da curva IDF do estudo hidrológico |
| Valeta de proteção de corte e de aterro | sem TR no capítulo; "chuva de projeto fixada no estudo hidrológico" | [DNIT-DREN p. 160, §3.1.3] | o TR é decisão do projeto |
| Ponte e pontilhão | "compatível com o porte, a vida útil, a importância da rodovia e o risco"; pontilhão em geral com TR inferior ao da ponte | [DNIT-DREN p. 135, §2.2] | sem número |
| Canal de beira de estrada, revestimento permanente | **5 ou 10** | [FHWA-HEC15 p. 33, §2.3.1] | revestimento de transição: vazão média anual (≈ TR 2) |
| Rodovia, pavimento (sarjeta e boca de lobo) | AEP 0,02 (TR 50, interestadual), 0,1 (TR 10, arterial e coletora), 0,2 (TR 5, rua local de baixo tráfego); verificação ("check storm") de TR 50 onde há empoçamento | [FHWA-HEC22 p. 70-71, Tabela 5.1 e §5.1.2] | também define o espalhamento permitido (acostamento, ½ faixa) |
| Rodovia da rede nacional dos EUA (NHS) | não galgar para a cheia de **50 anos** | [FHWA-HDS5 p. 152, §5.4.5] | |
| Cheia de verificação | maior que a de projeto, quando a norma exige (ex.: 100 anos para a planície regulatória) | [FHWA-HDS5 p. 64, §2.1.3; p. 72] | HDS-5 não fixa TR de projeto: é critério do órgão |
| Canalização e travessia, **zona rural** | **25** (mínimo); **100** em obra de maior porte ou importância, qualquer localização | [DAEE-IT-DPO11 p. 1, Tabela 1] | outorga no Estado de SP; referência fora de SP |
| Canalização e travessia, zona urbana ou de expansão | **100** (mínimo) | [DAEE-IT-DPO11 p. 1] | |
| Barramento (para comparar com extravasor) | 100 a 10.000, por altura e risco a jusante | [DAEE-IT-DPO11 p. 1-2, Tabela 2] | é do `vertedouros-e-dissipadores` |
| Microdrenagem urbana | 2 a 10 | [PMSP-DRENURB-V2 p. 30, Tabela 1.4] | |
| Macrodrenagem urbana | 25 a 50 | idem | |
| Grandes corredores de tráfego e áreas vitais | 100 | idem | |
| Perda de vidas em risco | 100 (mínimo) | idem | |
| Instalação estratégica (hospital, defesa civil) | 500 | idem | |
| Obras de pequenas bacias de controle de inundação | 5 a 50; canal em terra sugerido 10, depois revestido | [ABDER-APOSTILA p. 35-36] | texto de apostila, citando prof. Wilken; ponte 50 e 100 |
| Risco de excedência na vida útil | J = 1 − (1 − 1/TR)ⁿ | [DNIT-HIDRO p. 24]; [ABDER-APOSTILA p. 36] | usar para justificar TR (ex.: TR 25, vida 50 anos: J ≈ 87 %) |

Notas:
- O DNIT (IPR-715) cita bueiro 10 a 20 e ponte 50 a 100. Os projetos do acervo (irrigação) usam TR **maiores** que o piso
  rodoviário (§2). Hipótese, não declarada nas fontes: o bueiro sob canal principal arrisca o rompimento do canal e a
  interrupção da adução, e não só a estrada. Não citar como justificativa sem confirmar com o projetista.
- A tabela de TR do DAEE de SP é a **única** do corpus que dá um número único por localização (25 rural; 100 urbano). Aplica-se
  a outorga paulista; fora de SP é referência.
- Nenhuma fonte do corpus fixa o TR de **bueiro sob canal de irrigação** ou de **estrada de serviço de projeto de irrigação**.
  Isso é decisão do projeto, registrada no parecer com o risco (J) e a consequência de falha.

## 2. Prática dos projetos do acervo (`casos/drenagem_dissipadores/`)

| Projeto e obra | TR (anos) | Fonte do número | Ancoragem |
|---|---|---|---|
| Baixio de Irecê (PB 2008): bueiros sob canal e estrada | **25** (capacidade livre); **50** (verificação como orifício) | [670:119, 123, 126]; [896:1] | ✓ |
| Baixio de Irecê: drenos agrícolas e de proteção de canais | **5** | [670:119] | texto |
| CSB GEOHIDRO 2016: travessias (bueiros e overchutes) | **100** | [1341:45, 70] | ✓ |
| CSB GEOHIDRO 2016: valetas e canais de desvio | **50** (1341:45) ou 100 (1341:70 diz "todo o sistema") | divergência interna | ✓ (divergente) |
| CSB Salitre RC500-800: bueiros celulares | **100** | [1357:4, 98] | texto |
| Xingó Lote I: bueiros e aquedutos | **100** | [1419:26, 154] | texto |
| Vale do Iuiu 2002: drenos e dispositivos | **10** | [1051:316] | texto |
| Iuiu: bueiros sob canal / sob estrada | **50** / **25** | [1051:316, 331-332] | texto |
| Jaíba Etapas 3-4: sifão sob rodovia | Q = 2,44 m³/s sem TR impresso | [1182:57] | texto |

Padrão das obras maiores (CSB, Salitre, Xingó): bueiro de travessia sob canal principal com **TR 100**. Padrão das menores (Baixio,
Iuiu): **TR 25** em estrada e **TR 50** sob o canal. Os valores seguem um critério de risco que o projeto explicita; nenhum
cita DAEE ou DNIT como origem do número.

## 3. Recomendação operativa para o agente (anteprojeto, quando o usuário não definir o TR)

Registrar como **premissa adotada** (e delegar a decisão final):

| Obra | TR sugerido | Base |
|---|---|---|
| Valeta de proteção, canal de drenagem de pequena bacia, sarjeta | 10 (sarjeta) a 25 (valeta que protege canal) | DNIT-DREN p. 171; HEC-15 p. 33; prática Baixio (drenos TR 5) e Iuiu (drenos TR 10) |
| Bueiro de estrada de serviço (A < poucas dezenas de ha) | 25 | `hidraulica-fundamentos` §2; DNIT 10-20 + verificação 25; Baixio, Iuiu |
| Bueiro sob canal de irrigação principal ou adutor | 50 a 100, com verificação HW para 100 | CSB, Salitre, Xingó (100); Baixio, Iuiu (50) |
| Verificação de nível a montante | uma classe acima: TR 50 se projetou com 25; TR 100 se projetou com 50 | DNIT-HIDRO p. 24 (10 projeto, 20-25 verifica); Baixio (25 e 50) |
| Obra em zona urbana ou de expansão | 100 | DAEE p. 1; PMSP p. 30 |

Sempre declarar TR de projeto e TR de verificação, J na vida útil, e que a vazão de cada um vem da hidrologia. Mudar o TR
muda Q: devolver ao Climatologista/hidrólogo (`[DELEGAR: climatologia]`) e não "corrigir" Q por fator.
