# Entrega final da TechBairro

**Aluno:** Arthur de Souza Guedes  
**Versão entregue:** 3.3.2  
**Data:** 26/10/2026

## 1. Repositório

- **GitHub:** https://github.com/seek286/Techbairro

## 2. Justificativa da versão

A versão 3.3.2 foi escolhida porque as alterações foram principalmente de documentação e correções. O projeto recebeu o README, o manual de uso, o registro de testes e melhorias no gerador do pacote ZIP.

## 3. Registro de evidências

| # | Item | Evidência |
|---|---|---|
| 1 | A aplicação funciona e os seis casos de teste foram executados | `docs/registro_de_testes.md` |
| 2 | A versão aparece na janela e corresponde ao CHANGELOG e ao README | `techbairro.py`, `CHANGELOG.md` e `README.md` |
| 3 | O pacote foi testado em uma pasta limpa | `TechBairro-3.3.2.zip`, extraído e executado em outra pasta |
| 4 | Tag e Release publicadas, com o ZIP anexado | https://github.com/seek286/Techbairro/releases/tag/v3.3.2 |
| 5 | O repositório não contém banco de dados, `__pycache__` nem `dist` | `.gitignore` e arquivos publicados no GitHub |
| 6 | O histórico possui commits com mensagens claras | https://github.com/seek286/Techbairro/commits/main/ |
| 7 | README, manual de uso e requirements.txt estão no repositório | https://github.com/seek286/Techbairro |
| 8 | A Issue "Teste do README" está fechada | https://github.com/seek286/Techbairro/issues/1 — verificar e fechar antes da entrega |
| 9 | O vídeo está publicado e pode ser acessado sem login | PENDENTE: inserir o link do vídeo publicado |

## 4. Roteiro do vídeo

| Bloco | Tempo | O que vou mostrar ou dizer |
|---|---|---|
| 1. Problema e solução | 30 segundos | Apresentar a necessidade da associação e explicar que a TechBairro permite cadastrar e gerenciar clientes. |
| 2. Demonstração | 1 minuto e 30 segundos | Mostrar cadastro, consulta, edição, exclusão e uma validação impedindo um dado inválido. |
| 3. Como foi construída | 30 segundos | Apresentar a interface, a organização dos arquivos, o banco SQLite, os testes e o GitHub. |
| 4. Aprendizado | 30 segundos | Explicar uma dificuldade enfrentada, como foi resolvida e o que aprendi durante o desenvolvimento. |

## 5. Perguntas por escrito

**Pergunta 1: Por que o arquivo `techbairro.db` não está no GitHub?**

Porque ele armazena os dados dos clientes e é criado automaticamente pelo programa. Ele pode conter dados pessoais, por isso não deve ser publicado no GitHub.

**Pergunta 2: Qual caso de teste pegou um defeito de verdade? Qual era o defeito?**

Na Aula 21, o teste do telefone com espaços encontrou um defeito na validação. O sistema aceitava somente números sem espaços. A correção foi feita em `validacao.py`, permitindo tratar espaços, hífens e parênteses. A correção foi registrada no commit `0a79ccf`.

**Pergunta 3: Se o voluntário da associação tiver só o link do repositório, como ele instala e executa a TechBairro?**

Ele deve baixar ou clonar o repositório, instalar o Python e conferir as dependências do `requirements.txt`. Depois, deve executar `python techbairro.py` no terminal, seguindo as instruções do README e do manual de uso.

## 6. Autoavaliação

Meu vídeo ficou bom porque consegui apresentar as principais partes do projeto. Eu melhoraria a organização da apresentação e treinaria mais a fala. Aprendi a organizar o código em arquivos separados, utilizar o banco SQLite, criar testes automatizados e publicar um projeto no GitHub.
