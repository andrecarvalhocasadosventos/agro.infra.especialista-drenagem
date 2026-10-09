# Pontos abertos e padrões provisórios (decisão F7 do André)

Movido do perfil do agente em 2026-10-09 (teto de 20 KB). Atualizar quando o André decidir.


Escolha entre fontes ou critério **não é decisão do agente** (só o André decide). Em
todo parecer em que o ponto aparecer: (1) usar o padrão provisório da calculadora/skill, rotulado "padrão provisório,
decisão F7"; (2) mostrar a alternativa com fonte e o efeito no resultado; (3) listar o ponto em Pendências.

| Ponto aberto | Padrão provisório (rotular) | Alternativa a mostrar (fonte) |
|---|---|---|
| TR de bueiro de perímetro irrigado | o TR da tabela `tr-por-tipo-de-obra`, sempre com o risco R = 1 − (1 − 1/TR)^N | USBR 5 a 15 anos × prática do acervo 25 e 50 |
| Ke de alas paralelas | 0,7 (o código; HDS-5/HEC-13) | 0,2 (DNIT) |
| Limite de área do racional | `limite_km2` declarado na entrada; sem ele, o aviso da calculadora (2 km²) | 80 ha (HDS-2), 2 km² (DAEE), 3 km² (PMSP), 50 ha a 3,5 km² (projetos do acervo) |
| Tc mínimo de drenagem superficial | 5 min, TR 10 | 6 ou 10 min (projetos) |
| y/D do tubo; folga de canal; folga/hmax de valeta | y/D ≤ 0,75; ≥ 25 % do tirante normal; hmax = 0,8 h (0,2 h, IME p. 54) | critério do acervo; folga do projeto; Tab. 4.2 IME (concreto), 0,15 m (WSDOT) |
| Faixa de Fr instável | 0,89–1,13 (HEC-11 p. 38) | 0,9–1,1 (bueiros, antes) |
| n do concreto do bueiro | 0,013 em projeto; 0,012 só para reproduzir o HDS-5 | 0,012 (HDS-5 p. 90) ou 0,015 (prática DNIT) |
| Onda cinemática; NERC e Bransby-Williams | 0,938; NERC e Bransby só para reproduzir o caso (em projeto novo, Kirpich modificada ou DNOS) | 0,933 ou 0,93; constante do caso, sem primário no corpus |
| Berço classe A; carga do solo no tubo; colmatação de grelha | 2,25 em anteprojeto; forma simplificada do TUBOS; 50 % em ponto baixo | 2,5 a 3,4; equação completa de Spangler; sem colmatação |

Lista completa: `tools/dren/DIVERGENCIAS.md` ("Decisões do André"); o que a tabela não cobrir segue a mesma regra.

