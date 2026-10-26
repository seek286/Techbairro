# Registro de testes da TechBairro

**Versão testada:** 3.3.2  
**Data:** 26/10/2026  
**Responsável:** Arthur de Souza Guedes  
**Sistema operacional:** Windows (versão a confirmar)  
**Versão do Python:** a confirmar

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar um cliente com todos os campos corretos. | Cliente cadastrado e exibido na consulta. | A preencher após executar o teste. | Pendente |
| CT02 | RF01 | Tentar salvar com Nome e Endereço vazios. | O sistema deve impedir o cadastro e informar os campos obrigatórios. | A preencher após executar o teste. | Pendente |
| CT03 | RF02 | Informar o telefone `61 9999 0000`. | O sistema deve validar o telefone conforme as regras implementadas. | A preencher após executar o teste. | Pendente |
| CT04 | RF03 | Informar o e-mail `ana@email`. | O sistema deve rejeitar o e-mail inválido. | A preencher após executar o teste. | Pendente |
| CT05 | RF05 | Editar um cliente, alterar o telefone e salvar. | O telefone atualizado deve ser salvo e exibido. | A preencher após executar o teste. | Pendente |
| CT06 | RF06 | Excluir um cliente, respondendo primeiro Não e depois Sim. | Ao responder Não, o cliente deve permanecer; ao responder Sim, deve ser excluído. | A preencher após executar o teste. | Pendente |

## Testes automáticos

**Comando:** `python testar_validacao.py`

**Saída:** A preencher após executar o teste.

## Defeitos encontrados

A preencher após executar os testes. Registrar os defeitos encontrados, suas correções e os respectivos commits, ou informar "nenhum" caso não ocorram defeitos.

## Testes automáticos

**Comando:** `python testar_validacao.py`

**Saída:**
```text
OK teste_cliente_valido
OK teste_endereco_vazio
OK teste_telefone_com_letras
OK teste_email_sem_ponto
OK teste_nome_e_telefone_vazios
OK teste_email_sem_usuario
Todos os testes passaram.
```

**Resultado:** 6 testes automáticos passaram.

ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT01	RF01	Cadastrar Bruno Lima com todos os campos preenchidos corretamente.	Cliente cadastrado e exibido na consulta.	Cliente Bruno Lima cadastrado com sucesso.	Passou

| ID | Requisito | Passos e dados | Esperado | Obtido | Status |
|---|---|---|---|---|---|
| CT01 | RF01 | Cadastrar Bruno Lima com todos os campos preenchidos corretamente. | Cliente cadastrado e exibido na consulta. | Cliente Bruno Lima cadastrado com sucesso. | Passou |
| CT02 | RF01 | Deixar Nome e Endereço vazios e tentar salvar. | O sistema deve impedir o cadastro e informar os campos obrigatórios. | A preencher após o teste. | Pendente |
| CT03 | RF02 | Informar o telefone `61 9999 0000`, com espaços. | O sistema deve validar o telefone conforme as regras implementadas. | A preencher após o teste. | Pendente |
| CT04 | RF03 | Informar o e-mail `ana@email`, sem ponto. | O sistema deve rejeitar o e-mail inválido. | A preencher após o teste. | Pendente |
| CT05 | RF05 | Editar um cliente, trocar o telefone e salvar. | O telefone atualizado deve ser salvo e exibido na consulta. | A preencher após o teste. | Pendente |
| CT06 | RF06 | Tentar excluir um cliente, responder Não e depois repetir a exclusão respondendo Sim. | Com Não, o cliente permanece. Com Sim, o cliente é excluído. | A preencher após o teste. | Pendente |

ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT02	RF01	Deixar Nome e Endereço vazios e tentar salvar.	O sistema deve impedir o cadastro e informar os campos obrigatórios.	Exibiu a mensagem: “Preencha campos nome e endereco”. O cadastro foi bloqueado.	Passou

ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT03	RF02	Informar o telefone 61 9999 0000, com espaços.	O sistema deve validar o telefone conforme as regras implementadas.	Passou

ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT04	RF03	Informar o e-mail ana@email, sem ponto.	O sistema deve rejeitar o e-mail inválido.	O sistema bloqueou o cadastro com o e-mail ana@email.	Passou

Coloque esta linha no docs/registro_de_testes.md:
ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT05	RF05	Editar Bruno Lima, trocar o telefone para 61987654322 e salvar.	O telefone atualizado deve ser salvo e exibido na consulta.	O telefone foi atualizado corretamente.	Passou

ID	Requisito	Passos e dados	Esperado	Obtido	Status
CT06	RF06	Tentar excluir Bruno Lima, responder Não e depois repetir a exclusão respondendo Sim.	Com Não, o cliente permanece. Com Sim, o cliente é excluído.	O cliente continuou cadastrado após responder Não e foi removido após responder Sim.	Passou

## Defeitos encontrados

Nenhum defeito identificado nos seis casos manuais executados.