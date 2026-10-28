# Registro de testes da TechBairro

**Versão testada:** 3.3.2  
**Data:** 26/10/2026  
**Responsável:** Arthur de Souza Guedes  
**Sistema operacional:** Windows (versão a confirmar)  
**Versão do Python:** preencher com o resultado de `python --version`

## Testes manuais

| ID | Requisito | Passos e dados | Resultado obtido | Status |
|---|---|---|---|---|
| CT01 | RF01 | Cadastrar Bruno Lima com todos os campos preenchidos. | Cliente cadastrado com sucesso. | Passou |
| CT02 | RF01 | Deixar Nome e Endereço vazios e tentar salvar. | O cadastro foi bloqueado e o sistema informou os campos obrigatórios. | Passou |
| CT03 | RF02 | Informar o telefone `61 9999 0000`, com espaços. |O sistema aceitou o telefone, permitindo espaços na formatação. | Passou |
| CT04 | RF03 | Informar o e-mail `ana@email`, sem ponto. | O sistema bloqueou o cadastro com o e-mail inválido. | Passou |
| CT05 | RF05 | Editar Bruno Lima e trocar o telefone para `61987654322`. | O telefone foi atualizado corretamente. | Passou |
| CT06 | RF06 | Tentar excluir Bruno Lima, responder Não e depois repetir a exclusão respondendo Sim. | O cliente permaneceu cadastrado após Não e foi removido após Sim. | Passou |

## Testes automatizados

**Comando:** `python testar_validacao.py`

**Resultado:** 6 testes automatizados passaram.

```text
OK teste_cliente_valido
OK teste_endereco_vazio
OK teste_telefone_com_letras
OK teste_email_sem_ponto
OK teste_nome_e_telefone_vazios
OK teste_email_sem_usuario
Todos os testes passaram.
```

## Defeitos encontrados

Nenhum defeito identificado nos seis casos manuais executados.

## Teste do pacote de entrega

O arquivo `TechBairro-3.3.2.zip` foi extraído em outra pasta e a aplicação foi iniciada com sucesso. O pacote contém os arquivos principais do projeto, a documentação e os scripts auxiliares.
