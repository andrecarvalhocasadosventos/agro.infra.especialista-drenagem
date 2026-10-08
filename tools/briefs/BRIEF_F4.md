# Brief F4 — casos reais do Especialista Drenagem (2026-10-08)

Base: `../Agent Builder/modelos/BRIEF_CASOS.md` (leia-o; vale integralmente). Este arquivo só fixa o que muda.

RAIZ = `08. AI Squad/Especialista Drenagem` (pasta com `PACOTE.yaml`). Acervo: `dependencias_externas.acervo_projetos`
(`../../03. Infraestrutura/Projetos de Referência/_BIBLIOTECA_TECNICA`), **somente via** `02_PIPELINE/consultar.py`
(rode `python consultar.py --help` primeiro; a skill `consultar-acervo` descreve o protocolo). Protocolo de ancoragem:
seção correspondente do `MAPA.md` do acervo.

Leitura obrigatória extra: `PLANO.md` §1, §2, §6; `casos/drenagem/_INDICE_original_completo.md` e os nomes dos 10 casos
existentes em `casos/drenagem/` (não repetir); `PENDENCIAS_DE_TREINAMENTO.md` §4 (lições negativas já conhecidas).

Onde escrever: `casos/drenagem/2026-10-08_<projeto>_<assunto>.md`. **Não edite** `_INDICE*.md` (há outros agentes em
paralelo): devolva na resposta, além do resumo, as linhas de índice no formato `| slug | projeto (doc) | o que resolve | qualidade A/B/C | positivo/negativo |`.

Lotes (cada agente faz só o seu):
- **L1 canais de drenagem e macrodrenagem** (meta 3–4 casos): canal de drenagem natural/desviado, revestimento,
  velocidade admissível, deságue, talvegues interceptados pela faixa do canal de adução (CDV D-56, D-85). Também
  `G:\Meu Drive\DRENAGEM\01. ESTUDOS\RETROANÁLISE CANAL GABIÃO.xlsx` (fonte local D8; leia com openpyxl, só as abas
  relevantes) como caso possível.
- **L2 estradas de serviço e hidrologia** (meta 4–5 casos): sarjeta, valeta de crista/pé, descida d'água, bueiro de
  estrada de serviço (Baixio, CAC, Jaíba, Salitre); hidrologia: Tc, racional, SCS, HU com fórmulas e limites
  diferentes entre projetos (Baixio HUT, Iuiu, CSB, CAC).
- **L3 bueiros e subsuperficial** (meta 3 casos): +2 bueiros sob canal (projetos não cobertos ou obras diferentes das
  já extraídas, preferindo celular e tubular com controle de entrada aplicável) e +1 dreno subsuperficial/agrícola ou
  dreno de fundo (espaçamento Hooghoudt/Glover-Dumm, se algum projeto tiver).

Pelo menos 1 caso negativo por lote. Resposta ≤ 20 linhas.
