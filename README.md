# TechBairro

Cadastro de clientes da associação, feito em Python com Tkinter e SQLite.

**Versão atual:** 3.3.1 (veja o [CHANGELOG](CHANGELOG.md))

## O que faz

- Cadastra clientes (nome, telefone, e-mail e endereço) com validação dos campos.
- Consulta os clientes em ordem alfabética.
- Edita um cliente pelo botão **Editar selecionado** ou com **duplo clique** na linha. Durante a edição, o botão principal mostra **Salvar edição**.
- Exclui um cliente com confirmação. O sistema confere a resposta do banco e avisa se o cliente já não existe mais.

## Como executar

```
python techbairro.py
```

Mais detalhes em [COMO_EXECUTAR.txt](COMO_EXECUTAR.txt). Os dados ficam em `techbairro.db`, na mesma pasta do programa.

## Organização do código

| Arquivo | Responsabilidade |
|---|---|
| `techbairro.py` | A janela (Tkinter): telas, botões e mensagens |
| `cliente.py` | Modelo: a classe `Cliente` |
| `banco.py` | Dados: toda a comunicação com o SQLite |
| `validacao.py` | Regras de negócio: a classe `ValidadorCliente` |
| `testar_validacao.py` | Testa as regras sem janela e sem banco: `python testar_validacao.py` |

## Scripts (pasta `scripts/`)

| Script | Para que serve |
|---|---|
| `gerar_pacote.py` | Gera o `.zip` da versão em `dist/`, sem o banco de dados |
| `verificar_banco.py` | Lê o banco direto e roda consultas de auditoria |
| `importar_banco.py` | Importa clientes da planilha antiga (grava direto no banco) |
| `travar_banco.py` | Segura uma trava no banco para testar o erro "database is locked" |
