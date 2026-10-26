# TechBairro

A TechBairro é um sistema de cadastro de clientes para a associação de moradores. Ele permite cadastrar, consultar, alterar e excluir clientes por meio de uma janela simples.

**Versão atual:** 3.3.1 · Histórico de mudanças no [CHANGELOG](CHANGELOG.md)

## Funcionalidades

- Cadastrar clientes com nome, telefone, e-mail e endereço.
- Consultar os cadastros em ordem alfabética.
- Alterar os dados de um cliente e excluir cadastros com confirmação.
- Conferir o preenchimento dos campos antes de salvar.

## Requisitos para execução

| Item | Requisito |
|---|---|
| Sistema operacional | Windows, Linux ou macOS com ambiente gráfico |
| Python | Python 3 (versão registrada como testada no projeto: 3.12) |
| Tkinter | Necessário para abrir as janelas; no Windows normalmente acompanha o Python. No Linux pode precisar ser instalado separadamente |
| Bibliotecas externas | Nenhuma; o projeto usa módulos da biblioteca padrão |
| Internet | Necessária para baixar o projeto; não é necessária para usar o sistema depois de instalado |

> Antes de instalar, confira a versão disponível no computador com `python --version`. O projeto registra testes com Python 3.12; se a versão do computador for diferente, confirme a compatibilidade com o responsável pela instalação.

## Instalação

### Opção A — baixar com Git

É necessário ter o Git e o Python 3 instalados.

1. Abra o terminal ou PowerShell.
2. Baixe o repositório:

   ```bash
   git clone https://github.com/seek286/Techbairro.git
   ```

3. Entre na pasta do projeto:

   ```bash
   cd Techbairro
   ```

4. Confira o Python e teste se o Tkinter abre uma pequena janela:

   ```bash
   python --version
   python -m tkinter
   ```

   Se o teste do Tkinter abrir uma janela de demonstração, feche-a para continuar.

5. Confira as dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

   O arquivo `requirements.txt` informa que não há pacotes externos para instalar. O comando pode terminar sem instalar nenhum pacote.

6. Execute o programa:

   ```bash
   python techbairro.py
   ```

### Opção B — baixar pelo site do GitHub (Download ZIP)

1. Acesse o [repositório TechBairro](https://github.com/seek286/Techbairro).
2. Clique em **Code** e depois em **Download ZIP**.
3. Extraia o arquivo ZIP. A pasta extraída normalmente se chama `Techbairro-main`.
4. Abra o terminal ou PowerShell dentro dessa pasta. No Windows, você pode abrir a pasta no Explorador de Arquivos, clicar na barra de endereço, digitar `powershell` e pressionar Enter.
5. Confira o Python e o Tkinter:

   ```bash
   python --version
   python -m tkinter
   ```

   Feche a pequena janela de demonstração do Tkinter.

6. Confira o arquivo de dependências:

   ```bash
   python -m pip install -r requirements.txt
   ```

7. Inicie o sistema:

   ```bash
   python techbairro.py
   ```

### Como saber se abriu corretamente

Deve aparecer a janela **TechBairro — Cadastro de Cliente**. No terminal, deve aparecer uma linha começando com:

```text
Banco em uso:
```

Ela informa o caminho completo do arquivo de dados que o programa está utilizando. Se o comando `python` não funcionar no Windows, tente usar `py` no lugar de `python` nos comandos acima.

## Configuração do banco de dados

A TechBairro utiliza SQLite. Na primeira execução, o arquivo `techbairro.db` é criado automaticamente na mesma pasta de `techbairro.py`. Os clientes cadastrados ficam gravados nesse arquivo e continuam disponíveis quando o programa é fechado e aberto novamente.

Para confirmar qual arquivo está em uso, confira no terminal a mensagem `Banco em uso:`. Antes de fazer uma cópia de segurança, feche a TechBairro e copie o arquivo `techbairro.db` para outra pasta segura ou para uma unidade externa. Guarde a cópia em local protegido, pois ela contém dados pessoais.

O arquivo `techbairro.db` não deve ser enviado ao GitHub: ele pode conter nomes, telefones, e-mails e endereços de pessoas. O repositório deve conter o código, não os dados reais dos clientes. Não compartilhe cópias do banco sem autorização.

## Como usar

O passo a passo está no [Manual de uso](docs/manual_de_uso.md).

## Estrutura do projeto

- `techbairro.py` — abre a janela e coordena as ações do usuário.
- `cliente.py` — representa os dados de um cliente.
- `banco.py` — grava, consulta, altera e exclui os dados no SQLite.
- `validacao.py` — confere se os dados preenchidos seguem as regras do sistema.
- `testar_validacao.py` — testa as regras de preenchimento sem abrir a janela.
- `scripts/` — reúne scripts auxiliares do projeto.
- `docs/` — guarda a documentação para instalação e uso.
- `requirements.txt` — registra as dependências externas; neste projeto, nenhuma é necessária.
- `CHANGELOG.md` — registra as mudanças entre versões.
- `.gitignore` — evita que arquivos locais e dados gerados sejam enviados ao repositório.

## Autor

Arthur de Souza Guedes  
Técnico em Desenvolvimento de Sistemas — Senac DF
