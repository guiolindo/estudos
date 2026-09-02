# 📚 Plano de Estudos — Concurso Prefeitura de Contagem/MG 2026

Sistema completo de estudos para o **Concurso Público da Prefeitura Municipal
de Contagem/MG — Edital PMC nº 01/2026**, com aulas, questões, simulados,
flashcards e cronograma personalizado. Todo o conteúdo segue fielmente o
**Anexo IV do edital oficial** (conteúdo programático).

- **Banca organizadora:** IBGP (Instituto Brasileiro de Gestão e Pesquisa)
- **Prova objetiva prevista para:** 24 de janeiro de 2027
- **Cargos cobertos:** 36 cargos de níveis médio, técnico e superior
- **Portal oficial:** [portal.contagem.mg.gov.br](https://portal.contagem.mg.gov.br/portal/editais/0/3/6171/)

---

## 🚀 Como usar

O sistema é **um único arquivo HTML** — não precisa instalar nada, não
depende de servidor, não coleta dados. Tudo roda no navegador e o progresso
fica salvo localmente (`localStorage`).

1. Baixe o arquivo `plano-estudos-contagem-2026.html`
2. Dê dois cliques nele — abre no navegador padrão
3. Escolha seu cargo na barra lateral
4. Comece a estudar

Funciona em desktop e celular. Layout responsivo, tema claro/escuro.

---

## ✨ O que o sistema tem

### 📖 Aulas
- Teoria densa por tópico, com seções longas (700-1200 palavras cada)
- Exemplos resolvidos, dicas práticas, resumos em bullets
- Palavras-chave e articulação com o edital
- Modo leitura tipográfico (fonte serifada, coluna estreita)

### ❓ Questões
- 10 questões por tópico, no padrão real da banca **IBGP**
- Múltipla escolha (5 alternativas)
- Texto-base em várias questões (imitando prova de verdade)
- Gabarito com explicação **alternativa por alternativa**
  (por que a certa está certa E por que cada errada está errada)
- Distribuição por dificuldade: 3 fáceis, 5 médias, 2 difíceis

### 📝 Simulados
- Monte simulados por cargo, disciplina e nº de questões
- Cronômetro, correção automática, análise por disciplina
- Histórico de tentativas com evolução visual
- Gabarito comentado no final

### 🃏 Flashcards
- Sistema de repetição espaçada (**SRS**) com intervalos de
  0/1/2/4/7/15/30 dias
- Cartões auto-populados a partir das aulas na seleção do cargo
- Revisão diária destacada no dashboard

### 📅 Cronograma
- Editor de blocos de estudo por dia da semana
- Sugestor automático baseado no peso de cada disciplina
- Metas diárias e semanais (minutos e tópicos)
- Timer Pomodoro integrado

### 📊 Dashboard e estatísticas
- Progresso por disciplina, tópicos concluídos, taxa de acerto
- Metas de estudo com barras de progresso
- Ranking de matérias mais/menos estudadas
- Gráficos (Chart.js) de evolução

### 🛠 Outros recursos
- **Backup/importação** de todo o progresso em JSON
- **Glossário** com 460+ termos técnicos das disciplinas
- **Resumão** de todas as aulas em uma tela só
- **Modo escuro** e responsividade mobile
- **Zero dependências externas** salvo Chart.js (via CDN)

---

## 📂 Estrutura do repositório

```
estudos/
├── plano-estudos-contagem-2026.html    ← o sistema (1 arquivo, ~1.7 MB)
├── README.md                            ← este arquivo
└── ferramentas/                         ← utilitários pra expandir conteúdo
    ├── README.md
    ├── prompts/         ← prompts prontos pra IA externa gerar aulas/questões
    ├── scripts/         ← integração automática dos JSONs no HTML
    └── referencia/      ← Anexo IV do edital + backups do conteúdo gerado
```

---

## 🧠 Como o conteúdo foi construído

O material é grande demais para ser escrito à mão. O fluxo usado:

1. **Extração do edital** — o Anexo IV oficial foi convertido em texto e
   os tópicos programáticos catalogados por disciplina e cargo.
2. **Geração de teoria e questões** — prompts detalhados são rodados em uma
   IA externa (DeepSeek, ChatGPT, etc.) para gerar aulas densas e questões
   no estilo IBGP. Ver `ferramentas/prompts/`.
3. **Integração automática** — scripts Python integram os JSONs de volta
   no HTML, substituindo aulas ou questões pontualmente. Ver
   `ferramentas/scripts/`.
4. **Validação** — antes de cada commit a sintaxe JS dos scripts inline é
   verificada e o sistema testado em headless browser (Playwright).

Instruções completas do fluxo no `ferramentas/README.md`.

---

## 📋 Cobertura do conteúdo programático

Extraído fielmente do **Anexo IV do Edital PMC 01/2026**:

### Comum a todos os cargos
- **Língua Portuguesa** — 19 tópicos (médio) + 4 adicionais (superior)
- **Raciocínio Lógico e Matemático** — conjuntos numéricos, operações,
  razões, porcentagem, equações, lógica proposicional, análise combinatória,
  probabilidade
- **Noções de Informática** — Windows 10/11, Microsoft 365, Google
  Workspace, redes, nuvem, segurança, backup, IA generativa
- **Conhecimentos Gerais do Município** — aspectos de Contagem, Lei
  Orgânica, Estatuto dos Servidores (Lei 2.160/1990), Plano de Cargos
  (Lei 105/2011)

### Conhecimentos Específicos
Um bloco de aulas por cargo, cobrindo desde Assistente Administrativo até
Analista de TI, Advogado, Médico, Enfermeiro, entre outros — total de
**36 cargos** mapeados.

---

## 🔒 Privacidade

- **Nenhum dado sai do seu navegador.** Progresso, respostas, flashcards,
  metas — tudo em `localStorage` local.
- **Sem cadastro, sem login, sem analytics.**
- Para backup, use o botão de exportar JSON dentro do sistema.

---

## ⚠️ Isenção

Este é um material de apoio ao estudo, **não oficial** e não afiliado à
Prefeitura de Contagem, ao IBGP ou a qualquer instituição. Sempre confirme
prazos, vagas e regras no [portal oficial](https://portal.contagem.mg.gov.br/portal/editais/0/3/6171/).

O conteúdo das aulas e questões foi gerado a partir do conteúdo programático
público do edital. Não substitui a leitura direta das leis citadas, da
Constituição Federal, da Lei Orgânica de Contagem, do Estatuto dos
Servidores nem de bibliografia complementar.

---

## 👤 Autoria

Sistema desenvolvido por **Guilherme Júnio**.

Repositório: [github.com/guiolindo/estudos](https://github.com/guiolindo/estudos)

---

## 📄 Licença

Uso livre para estudo pessoal. O conteúdo do edital é público. As aulas e
questões geradas são de autoria própria a partir do conteúdo programático
oficial.
