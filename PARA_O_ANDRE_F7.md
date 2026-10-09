# Para o André: decisões da F7 (Especialista Drenagem), 2026-10-09

Treinamento pausado aqui por decisão de processo: a F7 tem portão seu, e a F10 (aceitação com o CDV) usa estes
critérios. Tudo abaixo já está implementado com um **padrão provisório** declarado nos pareceres. Nada é erro de
fórmula: as revisões Opus (F5 e F7) conferiram ~170 afirmações no primário e não acharam erro numérico de calculadora.
Detalhe e páginas: `tools/dren/DIVERGENCIAS.md` (seções "Revisão de fórmula F5" e "Revisão técnica F7").

Responda por número, por exemplo "1 R, 2 R, 3 outra: …". R = aceito a recomendação.

## A. Critérios de projeto (escolha entre fontes)

| # | Decisão | Alternativas (fonte) | Efeito | Recomendação |
|---|---|---|---|---|
| 1 | TR de bueiro em perímetro irrigado | USBR 5–15 (dreno superficial) e 25 (estrutura cara) [USBR-DRAINAGE p. 57]; DNIT 10–20 projeto, 20–25 verificação [DNIT-HIDRO p. 23–24]; DAEE 25 rural [IT-DPO11 p. 1]; acervo 20/50, 25/50, 25, 100 | risco em 25 anos: TR 25 = 64 %, 50 = 40 %, 100 = 22 % | **25 na estrada de serviço; 50 sob o canal adutor; verificar com o TR seguinte; 100 só se a falha põe o adutor em risco** |
| 2 | Ke de alas paralelas (caixa) | 0,7 [HDS-5 p. 216; HEC-13 p. 100] × 0,2 [DNIT-DREN Tab. 30 p. 130] | ΔHW de saída 0,23 m com V = 3 m/s; nulo se a entrada governa | **0,7**; 0,2 só para reproduzir projeto DNIT |
| 3 | Limite de área do racional | 80 ha (HDS-2); 2 km² (DAEE, só SP); 4 km² e corrigido até 10 km² [IPR-726 p. 259]; acervo 50 ha a 3,5 km² | Cd = A^−0,10: −7 % em 2 km², −12 % em 3,5 km² | **racional puro até 80–100 ha; até 2 km² com Cd e conferência McMath/SCS; 2–4 km² só com HUT de comparação** (aviso passa a citar o IPR-726) |
| 4 | Tc mínimo de drenagem superficial | 5 min [IPR-726 p. 258]; 6 min (Álbum, só canaleta pré-fabricada) [p. 214]; 10 min (vicinal) [IPR-726 p. 463] | L crítico +12 a +19 % de 5 para 10 min | **5 min**, com sensibilidade a 10 min no parecer |
| 5 | TR da drenagem superficial (sarjeta, valeta) | 10 [IPR-726 p. 258]; 25 (ENGEFER, IME p. 53); 50 em ponto baixo (WSDOT) | 10 → 25: +17 a +25 % na vazão | **10**; 25 quando a falha atinge o adutor ou a plataforma da EB |
| 6 | Declividade mínima de sarjeta e valeta | 0,5 % [DER-PR ES-DR-01 p. 10] × 0,3 % [HEC-12 p. 19] | 0,3 % tem 23 % menos capacidade | **0,5 %**; 0,3 % com justificativa; < 0,3 % só revestida |
| 7 | y/D máximo de tubo parcialmente cheio | 0,75 (Delmiro) × 0,82 (Jaíba) | 9,7 % de capacidade | **0,75 no projeto; 0,82 como teto na verificação** |
| 8 | n do concreto em bueiro | 0,012 [HDS-5 p. 90] × 0,013 × 0,015 (prática DNIT/acervo) | ~8 % por degrau | **0,013 em projeto**; 0,012 só para reproduzir o HDS-5 |
| 9 | Fator de berço classe A em vala | 2,25 [ABTC TUBOS Tab. 4.1 p. 37] × 2,5 [EM 2902 p. 71] × até 3,4 | proporcional à carga admissível | **2,25 em anteprojeto**; 2,5 só com berço fiscalizado |
| 10 | Carga de aterro sobre tubo | forma simplificada ABTC (El Debs) × Spangler completa | não quantificado | **anteprojeto com a ABTC; conferir no software da ABTC antes do básico** |
| 11 | Velocidade mínima em dreno a céu aberto | sem piso (hoje) × 0,43 m/s [NRCS CPS 608 p. 2] × 0,30 m/s (Salitre) | Delmiro: 1 trecho (0,29 m/s) falha com qualquer piso | **0,43 m/s quando o projeto não declarar** |
| 12 | Folga de dreno | 25 % do tirante (Delmiro) × 0,15 m [CPS 608 p. 2; HEC-15 p. 34] | Delmiro DS-1.1/C: 0,108 → 0,15 m | **max(25 % do tirante; 0,15 m)** |
| 13 | Folga de valeta | 0,2 h em terra [IME p. 54]; Tab. 4.2 IME/Tab. 36 DNIT em concreto (20 cm acima de 2,8 m³/s); √(46·h) cm em terra para 0,3–10 m³/s [DNIT-DREN p. 162] | — | **0,2 h em terra e tabela em concreto, mínimo 0,15 m**; incluir a fórmula do DNIT (falta saber se h é lâmina ou profundidade: eu confiro na imagem) |
| 14 | Faixa de Froude instável | 0,9–1,1 (bueiros) × 0,89–1,13 [HEC-11 p. 38] | só aviso | **unificar em 0,89–1,13** |
| 15 | Colmatação de grelha em ponto baixo | 0 × 50 % [HEC-12 Ex. 14] | capacidade ÷ 2 | **50 %** |
| 16 | Coeficiente da onda cinemática (Tc em lâmina) | 0,938 (dedução, McCuen) × 0,933 (planilhas) × 0,93 (HDS-2) | 0,5 % | **0,938** |
| 17 | NERC e Bransby-Williams (Tc) | usar só para reproduzir o Delmiro × buscar o primário (TRRL/FSR, ARR) × não usar | Delmiro: 7,65 h (NERC) × 4,92 h (Kirpich) | **só reprodução; projeto novo com Kirpich modificada ou DNOS** |
| 18 | Critério de filtro (Terzaghi) | fator único 4 (código) × 5 nas duas razões [DNIT-DREN p. 252–253] × retenção 4–5 e permeabilidade 5 | o 4 é menos exigente na permeabilidade | **separar: retenção 4–5, permeabilidade ≥ 5** |
| 19 | Porosidade drenável μ por textura | tabela sem página (código) × Embrapa Tab. 3 [EMBRAPA-DREN-SUBT p. 14] | L de Glover-Dumm +13 % areia, +8 % franco, −18 % argila | **trocar pela Embrapa** |
| 20 | Wesseling para lateral e coletor corrugado | incluir Q = 89·d^2,714·s^0,571 [FAO-62 p. 214] × manter só Manning | Manning subestima ~1,8× o lateral; pesa no **D-86** (tubo de 300 mm) | **incluir antes da F10** |

## B. Informação que só você tem

| # | Pergunta | Por quê |
|---|---|---|
| 21 | De onde vem o coeficiente de drenagem 1,2 L/s/ha (casos herdados dsub-03/04)? | 1,2 L/s/ha = 10,4 mm/d, fora da faixa de irrigado árido (1–2 mm/d, FAO-62 p. 113). Pode ser coletor com escoamento superficial. Sem fonte, não vira gabarito. |
| 22 | Pode conferir (✓h) alguns números de caso do acervo? | Nenhum dos 26 casos tem ✓h, então nada do acervo é gabarito. Sugestão mínima: Xingó VPC-1 (1419:64–66), Delmiro BHD1 (1494:64), Salitre DT 4.1.6/A (1585). 15 min cada no PDF. |
| 23 | Enunciado dos cartões CDV P-108 e P-272 | Não há texto deles no pacote. Sem isso, a F10 só faz a triagem. |

## C. As 14 divergências > 5 % (xfail) com o acervo

Nenhuma pede mudança de fórmula. Proposta de veredito por grupo; basta "C ok" ou apontar a exceção.

| Grupo | Testes | Veredito proposto |
|---|---|---|
| Método legado × HDS-5 (Baixio BU-CP0-13/15/18: −6 a −8 % no HW) | 3 | **convenção**: o legado (orifício) subestima HW; fica como caso negativo de treinamento |
| Lâmina por energia × Manning normal (Xingó BU-01/06/24) | 3 | **convenção**: o projeto usa perfil de energia, não escoamento uniforme; teste fica documentando a diferença |
| Gabarito do projeto inconsistente (Baixio folga ao TN; CSB BTCC-N17 −27 %; Delmiro DN170 6,9× e DN230 4,7×; CSB 2DN150) | 5 | **gabarito errado ou ilegível**: casos negativos; não corrigir a calculadora |
| Dado não recuperável do acervo (Baixio HUT TR25; Delmiro BHD1 +5,3 %; Iuiu DP11 McMath) | 3 | **sem gabarito**: o hietograma ou o S da bacia não está no documento; manter xfail estrito |

Também proponho tornar estritos (`strict=True`) os 6 xfail que hoje não são. Nenhum número muda.

## D. Fronteira com o Hidráulico (para a sessão /treinar squad)

A skill `vertedouros-e-dissipadores` do Hidráulico (linha ~31 e V12) manda o dissipador de saída de bueiro para o
Drenagem, contra a D3. A sessão squad concordou e registrou o diff para você aprovar (PARA_O_ANDRE §3c dela).

## E. Fontes

- NBR 8890:2020, 15645 e 16085 continuam fechadas. A Target bloqueou o acesso (CF-403), e a ficha da 8890 feita pela
  sessão squad foi descartada por conter conteúdo inventado. O pacote usa a ABTC (classe de tubo indicativa).
- FDOT Drainage Manual: o servidor entrega o PDF truncado (`PENDENTES_DOWNLOAD_MANUAL.md`). Baixa prioridade.
- Slides Robson I–IV sem OCR (521 páginas, prioridade B, ~45 min de máquina). Só se o IPR-724 não bastar.

## Depois da sua resposta

Eu aplico as decisões (calculadoras, skills, `pontos-abertos.md`), rodo testes e evals, e sigo para a F10
(13 pareceres do CDV, sem escrever no CDV) e a F11 (instalação). Os dois têm portão seu.

## F. Infraestrutura (aviso de 2026-10-09)

A sessão /treinar squad está migrando C:\bibtec, C:\bibhid e C:\bibdren para `08. AI Squad/_infra/`, por causa do
servidor novo, e vai renomear os originais. Autorizei a renomeação porque o Drenagem não os usa até o seu portão.
Antes da F10 vou atualizar os caminhos em `PACOTE.yaml`, no núcleo e no agente.
Atualização: migração concluída. A cópia está em `_infra/` e os originais viraram `C:\bib*_MIGRADO_2026-10-09`. Pela
sua decisão (`Agent Builder/DECISOES_2026-10-09.md`), os caminhos novos só valem na 1ª sessão no servidor, com os
bancos copiados para disco local curto (sugestão `D:\bib*`), nunca lidos direto do Drive. Até lá, nesta máquina, o
acervo e o `corpus.sqlite` estão indisponíveis. A F10 deve rodar no servidor, depois de ajustar `PACOTE.yaml`, o
núcleo e o agente para o caminho local de lá.
