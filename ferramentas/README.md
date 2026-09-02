# Ferramentas do plano de estudos

Este diretório reúne os artefatos usados para gerar e atualizar o conteúdo do
arquivo principal `plano-estudos-contagem-2026.html`. É a "cozinha" do sistema:
o HTML é o produto final, aqui estão os prompts, scripts e material de
referência para reproduzir/expandir o conteúdo.

## Estrutura

```
ferramentas/
├── prompts/       # prompts prontos para colar em IA externa (DeepSeek etc)
├── scripts/       # scripts Python/Node para integrar o retorno das IAs no HTML
└── referencia/    # fontes: edital extraído, aulas já geradas, questões
```

## Fluxo de trabalho

Para expandir o conteúdo (novas aulas ou novas questões):

1. **Escolha o prompt em `prompts/`** conforme o que quer gerar:
   - `01-conteudo-denso-lp-info.txt` — aulas com teoria densa
   - `02-questoes-ibgp-real.txt` — questões IBGP-style com texto-base
2. **Rode em uma IA externa** (DeepSeek preferencialmente por ser gratuita),
   uma disciplina por thread limpa. Se a resposta for cortada, peça
   "continue de onde parou, mantendo o formato JSON exato, próximo tópico: X".
3. **Cole o JSON completo** num arquivo local.
4. **Integre no HTML** com o script apropriado:
   ```bash
   # Substitui todas as aulas da disciplina
   python3 ferramentas/scripts/integrar_aulas.py minha-fonte.json "Língua Portuguesa"

   # Substitui só o array `questoes` (mantém teoria)
   python3 ferramentas/scripts/integrar_questoes.py minhas-questoes.json "Língua Portuguesa"
   ```
5. **Valide a sintaxe JS** antes de commitar:
   ```bash
   NODE_PATH=/opt/node22/lib/node_modules node ferramentas/scripts/validar_html.js
   ```

## Referências

- `anexo-iv-edital-01-2026.txt` — extração texto do Anexo IV oficial
  (conteúdo programático). Fonte oficial:
  https://portal.contagem.mg.gov.br/portal/editais/0/3/6171/
- `lp-aulas-densas-fonte.json` — 23 aulas de Língua Portuguesa geradas para
  o material atual (backup consolidado).
- `lp-questoes-ibgp-primeiros-blocos.json` — primeiros blocos de questões
  IBGP-style (Compreensão e Gêneros de texto).

## Notas sobre o padrão IBGP

- Banca oficial do Edital 01/2026: **IBGP** (Instituto Brasileiro de Gestão
  e Pesquisa).
- Prova objetiva prevista para 24/01/2027.
- Estilo IBGP: múltipla escolha 5 alternativas, dificuldade moderada,
  literal na letra da lei, questões com texto-base.
- Distribuição por bloco de 10 questões: 3 fáceis, 5 médias, 2 difíceis.
- Legislação municipal citada explicitamente no edital:
  Lei Orgânica, Estatuto dos Servidores (Lei 2.160/1990), Plano de
  Cargos (Lei 105/2011).

## Autoria

Sistema desenvolvido por **Guilherme Júnio**.
