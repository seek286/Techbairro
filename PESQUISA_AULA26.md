# Aula 26 — Parte 1: Pesquisa

## P1 — O que é um arquivo README? Onde ele precisa ficar?

O README é o arquivo de apresentação de um projeto. Ele explica o objetivo, os requisitos, a instalação e o uso do programa. Para o GitHub exibi-lo na página inicial do repositório, o arquivo deve se chamar `README.md` e ficar na pasta principal do projeto.

Fonte: https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/about-the-readme

## P2 — Como escrever elementos básicos em Markdown?

- **Título:** `# Título principal`
- **Subtítulo:** `## Subtítulo`
- **Lista numerada:** `1. Primeiro item` e `2. Segundo item`
- **Negrito:** `**texto em negrito**`
- **Link para outro arquivo:** `[Manual de uso](docs/manual_de_uso.md)`
- **Tabela:** `| Campo | Regra |` e uma linha separadora `|---|---|`, seguida das linhas de conteúdo.
- **Bloco de código:** três acentos graves antes e depois do código, por exemplo:
  ````markdown
  ```python
  print("Olá")
  ```
  ````

Fonte: https://docs.github.com/pt/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax

## P3 — Seções de dois projetos reais em Python

**Requests:** no README do projeto, os títulos incluem “Requests”, “Installing Requests”, “Supported Features & Best–Practices”, “API Reference”, “Community”, “Development”, “Running the Tests” e “License”. “Requests” apresenta a biblioteca; “Installing Requests” explica como instalar; os exemplos e a “API Reference” ajudam a entender como usar.

**Flask:** no README do projeto, os títulos incluem “Flask”, “What is Flask?”, “Installing”, “A Simple Example”, “User’s Guide”, “Donate”, “Contributing” e “License”. “What is Flask?” explica o que é; “Installing” explica a instalação; “A Simple Example” mostra um uso inicial. Os títulos podem mudar com novas versões dos projetos.

Fontes:
- https://github.com/psf/requests
- https://github.com/pallets/flask

## P4 — O que é requirements.txt? Por que tkinter e sqlite3 não entram?

O `requirements.txt` é um arquivo que lista os pacotes externos necessários para executar um projeto Python. O comando `pip install -r requirements.txt` lê esse arquivo e instala os pacotes listados. `tkinter` e `sqlite3` não são listados como pacotes externos porque fazem parte da biblioteca padrão do Python, embora em algumas distribuições Linux o Tkinter possa precisar de instalação pelo gerenciador de pacotes do sistema.

Fontes:
- https://pip.pypa.io/en/stable/reference/requirements-file-format/
- https://docs.python.org/pt-br/3/library/

## P5 — Como ver a versão do Python e testar o Tkinter?

O comando `python --version` mostra a versão do Python. Para testar o Tkinter, execute `python -m tkinter`. Se estiver funcionando, uma pequena janela de demonstração do Tkinter será aberta. A versão do Python instalada e utilizada nos testes do projeto foi a 3.12.0.

Fonte: https://docs.python.org/pt-br/3/library/tkinter.html

## P6 — O que é SQLite, o que é dado pessoal e por que não publicar techbairro.db?

SQLite é um sistema de banco de dados que guarda os dados em um arquivo local, sem precisar de um servidor separado. Na TechBairro, o arquivo `techbairro.db` fica na pasta do projeto e armazena os cadastros. Pela LGPD, dado pessoal é uma informação relacionada a uma pessoa natural identificada ou identificável. Nome, telefone, e-mail e endereço podem identificar alguém; por isso, o banco real não deve ser enviado ao GitHub público. O `.gitignore` ajuda a impedir que arquivos locais sejam adicionados por engano, mas é preciso conferir o que será enviado.

Fontes:
- https://www.sqlite.org/about.html
- https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm
- Arquivo `.gitignore` do projeto: https://github.com/seek286/Techbairro/blob/main/.gitignore

## P7 — Diferença entre manual do usuário e documentação técnica

O manual do usuário ensina a pessoa a realizar tarefas no programa. A documentação técnica explica como o programa foi construído, como o código está organizado e como mantê-lo.

Três cuidados ao escrever um manual para quem não sabe programar:
1. Usar palavras simples e explicar uma tarefa por vez.
2. Usar os nomes exatos dos botões e das mensagens que aparecem na tela.
3. Numerar os passos, dizer o que a pessoa deve esperar e explicar como agir quando aparece um erro.

Fontes:
- https://docs.python-guide.org/writing/documentation/
- https://www.gov.uk/service-manual/helping-people-to-use-your-service
