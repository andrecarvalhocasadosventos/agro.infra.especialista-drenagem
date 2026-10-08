---
pacote: drenagem                      # id do PACOTE.yaml
agente: engenheiro-de-drenagem@<versao>   # name do agente + versão do PACOTE.yaml
data: <AAAA-MM-DD>
modo: direto                          # direto | squad | cdv
pedido: <uma frase, como veio>        # vira o `prompt` do caso em evals/casos_reais.yaml
solicitante: <pessoa ou "Gestor CDV / CT-xx">
skills: []                            # skills de disciplina carregadas (o núcleo não conta) -> `esperado`
calculadoras: []                      # <módulo.função@versão>
delegacoes_emitidas: []               # ids dos blocos [DELEGAR] emitidos -> `delegacoes` esperadas
delegacoes_recebidas: []              # ids de quem pediu este parecer, se veio de [DELEGAR]
licoes_aplicadas: []                  # [L-nnn] que mudaram a resposta
licoes_propostas: 0                   # nº de linhas propostas para LICOES.md
modelo: sonnet
nivel: anteprojeto                    # anteprojeto | basico | executivo-conferencia
---

<!-- Este bloco abre todo pareceres/<AAAA-MM-DD>-<slug>/parecer.md (PADRAO_DO_PACOTE §6).
     tools/registro.py --resumir lê estes campos e gera evals/casos_reais.yaml. Corpo do parecer segue o formato do agente. -->
