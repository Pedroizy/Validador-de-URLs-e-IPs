# 🔍 Validador de IPs e URLs via Autômatos Finitos

Projeto prático desenvolvido para a disciplina de **Linguagens Formais e Autômatos Finitos (LFAF)**, com o objetivo de aplicar os conceitos teóricos de expressões regulares e autômatos finitos determinísticos (AFD) na modelagem e validação de cadeias de texto (endereços IP e URLs).

---

## 📋 Sobre o Projeto

Este trabalho consiste na especificação matemática formal e na implementação computacional de um reconhecedor léxico baseado em Autômatos Finitos. O sistema é capaz de processar cadeias de entrada e determinar se elas pertencem ou não à linguagem formal definida para formatos válidos de endereços IP e URLs.

### Objetivos Principais:
1. **Definição Formal:** Especificação matemática completa do autômato $M = (Q, \Sigma, \delta, q_0, F)$.
2. **Modelagem Visual:** Representação gráfica do diagrama de transições utilizando vetores no pacote `tikz` do $\LaTeX$.
3. **Minimização:** Aplicação do algoritmo de redução de estados equivalentes (Tabela de Distinção) para otimização do AFD.
4. **Simulação Computacional:** Implementação modular em Python para validar entradas em tempo real.
5. **Documentação Científica:** Relatório técnico e slides de apresentação construídos inteiramente em $\LaTeX$ (classes `article` e `beamer`).

---

## 📁 Estrutura do Repositório

```text
validador-ip-url-lfaf/
│
├── src/                        # Código-fonte do simulador em Python
│   ├── main.py                 # Menu interativo (CLI) que direciona para IP ou URL
│   ├── validador_ip.py         # Módulo do Autômato de IPv4 (núcleo e transições)
│   ├── validador_url.py        # Módulo do Autômato de URL (núcleo e transições)
│   ├── input_handler.py        # Validação do alfabeto (Σ) e leitura inicial
│   └── tests.py                # Bateria de testes automatizados (válidos e inválidos)
│
├── docs/                       # Documentação acadêmica em LaTeX
│   ├── relatorio/              # Relatório técnico (article / SBC)
│   │   ├── main.tex            # Arquivo principal com pacotes amsmath, tikz e listings
│   │   └── diagramas.tex       # Código vetorial TikZ do autômato
│   │
│   └── apresentacao/           # Slides da defesa do projeto (Beamer)
│       └── slides.tex          # Apresentação de 10-15 minutos
│
├── .gitignore                  # Arquivos temporários ignorados (Python e compilações LaTeX)
└── README.md                   # Documentação geral do repositório
```

---

## 👥 Equipe e Divisão de Responsabilidades

Para atender aos requisitos da disciplina, todos os integrantes participam tanto da fundamentação teórica/documental quanto da implementação do código:

| Integrante | Módulo / Arquivo Responsável | Descrição das Atividades |
| :--- | :--- | :--- |
| **Pedro** | `src/validator_ip.py` & Modelagem Matemática | • Definição formal da quíntupla matemática do autômato ($M$) e do diagrama de transições do IPv4[cite: 40, 191].<br>• Implementação do núcleo de transição de estados para a validação de endereços IPv4. |
| **Gus** | `src/input_handler.py` | • Desenvolvimento da função de leitura e tratamento de entradas.<br>• Validação prévia do alfabeto permitido ($\Sigma$)[cite: 4] antes de enviar a cadeia para os autômatos. |
| **Guilherme** | `src/validator_url.py` & `docs/relatorio/` | • Implementação do autômato voltado para a validação sintática de URLs.<br>• Produção do relatório técnico completo em LaTeX (`article` / SBC)[cite: 192]. |
| **Cauã** | `src/main.py`, `src/tests.py` & `docs/apresentacao/` | • Desenvolvimento do menu interativo no terminal (CLI)[cite: 191].<br>• Criação da bateria de testes automatizados (`tests.py`) e dos slides em Beamer[cite: 192]. |

---

## 🚀 Como Executar o Simulador

### Pré-requisitos
* **Python 3.8+** instalado na máquina.
* Distribuição $\LaTeX$ (como TeX Live, MiKTeX ou via **Overleaf**) para compilar os arquivos da pasta `docs/`.

### Rodando o Validador
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/validador-ip-url-lfaf.git
   cd validador-ip-url-lfaf
   ```

2. Execute o programa principal:
   ```bash
   python src/main.py
   ```

3. Para rodar a bateria de testes automatizados:
   ```bash
   python src/tests.py
   ```

---

## 📐 Formalismo Matemático (Resumo)

O reconhecedor opera sobre o modelo de Autômato Finito Determinístico:

$$M = (Q, \Sigma, \delta, q_0, F)$$

* **$Q$**: Conjunto finito de estados internos da máquina.
* **$\Sigma$**: Alfabeto de entrada composto pelos caracteres válidos para IPs e URLs (ex: dígitos `0-9`, letras `a-z`, `.`, `/`, `:`, `-`).
* **$\delta$**: Função de transição $\delta: Q \times \Sigma \rightarrow Q$.
* **$q_0$**: Estado inicial de processamento ($q_0 \in Q$).
* **$F$**: Subconjunto de estados finais ou de aceitação ($F \subseteq Q$).

---

## 📄 Licença

Este projeto foi desenvolvido exclusivamente para fins acadêmicos na disciplina de Linguagens Formais e Autômatos Finitos.
