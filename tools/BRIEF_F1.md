# Brief F1 — manifesto de fontes do Especialista Drenagem

Preenchido a partir de `Agent Builder/modelos/BRIEF_FONTES.md` em 2026-10-07. Subagente: **1 Sonnet**. Custo ~US$ 1.

RAIZ = `08. AI Squad/Especialista Drenagem` (a pasta com `PACOTE.yaml`). Caminhos relativos à RAIZ.

## Diferença em relação ao modelo (decisões D1 e D8 do `PLANO.md`)

- O corpus principal é o do Hidráulico, por caminho: `../Especialista Hidraulica/referencias/_catalogo.yaml`. **Não
  repita** nenhuma obra que já esteja lá (confira por título e órgão com Grep, sem ler o catálogo inteiro).
- Meta reduzida: **15 a 40 itens abertos** de lacunas (não 60–140).
- Bloco separado `fontes_locais:` no mesmo YAML com os itens A/B da tabela §5.1 do `PLANO.md` (pasta
  `G:\Meu Drive\DRENAGEM`): campos `id`, `titulo`, `origem` (caminho completo), `tamanho_mb`, `escaneado` (sim/não/a
  conferir: só pelo tamanho e por `pdftotext -l 2` de 2 páginas, nunca ler o livro), `prioridade`, `licenca`
  (`uso-interno` para livros com direito autoral), `temas`. Não copie nada: a cópia é da F2.

## Leitura obrigatória (teto 40 KB)
1. `PLANO.md` (§1, §2, §5 e §5.1).
2. `PACOTE.yaml` e `LEIA-ME.md`.
3. `PENDENCIAS_DE_TREINAMENTO.md` §3 (fontes que faltam).
4. `../Especialista Hidraulica/NAO_ABERTOS.md` e `PENDENTES_DOWNLOAD_MANUAL.md` (só Grep por drenagem, DAEE, FAO 38, NBR 8890, ES 018, ES 021).

## Lacunas a procurar (prioridade sugerida)
- A: FAO Irrigation & Drainage Paper 38 (Drainage design factors), por capítulo HTML se for o único formato; DAEE-SP
  Manual de Cálculo das Vazões (1994); DNIT ES 018 e ES 021 (drenagem); FHWA HY-8 User Manual e HEC-12 (bocas de
  lobo/entradas em pista, só se aplicável a estradas de serviço); USBR Drainage Manual (edição vigente, se não estiver
  no corpus); critério de TR para bueiros e drenagem em perímetros irrigados (USBR Design Standards, Codevasf,
  DNOCS, ANA/PISF).
- B: manuais estaduais de drenagem rodoviária abertos (DER-SP, DERBA, DER-MG); NRCS NEH 650 cap. 14 se faltar;
  normas DNIT de dispositivos (ES 015 a 030) que o IPR-724 cita.
- Pelo menos 3 itens A para cada skill de disciplina nova: `drenagem-de-estradas-e-plataformas`,
  `canais-de-drenagem-e-macrodrenagem`, `drenagem-subsuperficial` (contando o corpus do Hidráulico e as fontes locais).

## O que escrever (só isso)
- `tools/fontes_candidatas.yaml` (itens abertos + bloco `fontes_locais:`).
- `NAO_ABERTOS.md` (NBR 8890:2020 e o que mais for fechado; como obter).
- `PENDENTES_DOWNLOAD_MANUAL.md` (só se houver).

Regras de conteúdo, formato da resposta e proibições: as do modelo `BRIEF_FONTES.md`, sem mudança.
