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
projeto-validador-lfaf/
│
├── README.md                 # Documentação principal do repositório (com instruções, equipe e rotas)
│
├── src/                      # Pasta contendo todo o código-fonte em Python
│   ├── __init__.py           # Torna a pasta src um pacote Python (opcional, mas boa prática)
│   ├── main.py               # Arquivo principal: O menu de escolha (IP ou URL)
│   ├── validador_ip.py       # Módulo do Autômato de IPv4
│   └── validador_url.py      # Módulo do Autômato de URL
│
├── docs/                     # Pasta opcional para guardar os arquivos do relatório
│   ├── relatorio.tex         # Relatório técnico em LaTeX (classe article)
│   ├── apresentacao.tex      # Slides de defesa em LaTeX (classe beamer)
│   └── imagens/              # Diagramas e grafos exportados (TikZ / PNG)
│
└── tests/                    # Pasta de testes automatizados (opcional, para garantir os asserts)
    └── test_validadores.py   # Testes unitários validando casos certos e errados
```

---

## 👥 Equipe e Divisão de Responsabilidades

Para atender aos requisitos da disciplina, todos os integrantes participam tanto da fundamentação teórica/documental quanto da implementação do código:

| Integrante | Responsabilidade Teórica / Documental | Responsabilidade na Programação (`src/`) |
| :--- | :--- | :--- |
| **Pedro** | Definição formal da quíntupla $M = (Q, \Sigma, \delta, q_0, F)$ e lógica inicial do diagrama de transições. | **`input_handler.py`**: Validação do alfabeto permitido ($\Sigma$) e inicialização do estado $q_0$. |
| **Gus** | Verificação das regras de transição ($\delta$) e validação de estados de aceitação e erro. | **`validator.py`**: Implementação do núcleo do AFD (tabela/regras de transição de estados). |
| **Guilherme** | Redação e compilação do Relatório Técnico em $\LaTeX$ (`amsmath`, `tikz` e `listings`). | **`tests.py`**: Criação da suíte de testes automatizados para validar a aceitação/rejeição de cadeias. |
| **Cauã** | Criação dos slides da apresentação em $\LaTeX$ (`beamer`) e roteiro da defesa oral. | **`main.py`**: Desenvolvimento da interface interativa no terminal (CLI) e integração dos módulos. |

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
