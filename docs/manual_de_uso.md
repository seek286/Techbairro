# Manual de uso da TechBairro

Este manual explica como cadastrar e administrar os clientes da associação.

## A tela principal

A janela tem o título **TechBairro — Cadastro de Cliente** e apresenta quatro campos: **Nome**, **Telefone**, **E-mail** e **Endereço**. Abaixo aparecem uma mensagem de situação, a quantidade de clientes cadastrados e os botões **Salvar**, **Cancelar** e **Consultar**. A versão aparece no canto inferior direito.

A mensagem de situação ajuda a entender o resultado da última ação. O contador mostra quantos clientes estão cadastrados.

## Cadastrar um cliente

1. Abra a TechBairro.
2. Preencha os campos **Nome**, **Telefone**, **E-mail** e **Endereço**.
3. Confira se todos os dados estão corretos. No telefone, digite somente números.
4. Clique em **Salvar**.
5. Confira a mensagem que aparece abaixo dos campos. Se o cadastro for aceito, aparecerá uma mensagem informando que o cliente foi salvo com sucesso.
6. Os campos serão limpos para permitir um novo cadastro.

## Consultar os clientes cadastrados

1. Na janela principal, clique em **Consultar**.
2. Uma janela com a lista de clientes cadastrados será aberta. Os nomes aparecem em ordem alfabética.
3. Clique uma vez no cliente que deseja consultar.
4. Para voltar à tela principal, feche a janela de consulta.

Se ainda não houver clientes, a lista informará que não há cadastros disponíveis.

## Alterar os dados de um cliente

1. Na janela principal, clique em **Consultar**.
2. Na lista, clique no cliente que deseja alterar.
3. Clique em **Editar selecionado**. Você também pode dar dois cliques na linha do cliente.
4. A janela de consulta será fechada e os dados do cliente aparecerão nos campos da tela principal.
5. Faça as alterações necessárias.
6. Clique em **Salvar edição**.
7. Confira a mensagem de confirmação. Se desistir, clique em **Cancelar**; a mensagem será **Edição cancelada. Nada foi alterado.**

## Excluir um cliente

1. Na janela principal, clique em **Consultar**.
2. Selecione o cliente que deseja excluir.
3. Clique em **Excluir selecionado**.
4. Leia a pergunta de confirmação. A janela informa: **Tem certeza que deseja excluir o cadastro de [nome]? Essa ação não pode ser desfeita.**
5. Clique em **Sim** somente se tiver certeza. Para manter o cadastro, clique em **Não**.
6. Depois da exclusão, confira a mensagem na tela principal: **Cliente '[nome]' excluído com sucesso!**

A exclusão não pode ser desfeita pelo programa. Confira o nome antes de confirmar.

## Regras de preenchimento

| Campo | Obrigatório? | Regra |
|---|---|---|
| Nome | Sim | Não pode ficar vazio. |
| Telefone | Sim | Preencha usando somente números, sem espaços, parênteses, hífen ou sinal de +. |
| E-mail | Sim | Deve conter `@`, um nome antes dele e um domínio com ponto, como `ana@exemplo.com`. |
| Endereço | Sim | Não pode ficar vazio. |

## Mensagens do sistema

| Mensagem | O que significa | O que fazer |
|---|---|---|
| `Nenhum cliente cadastrado ainda` | Ainda não há clientes salvos. | Preencha os campos para cadastrar o primeiro cliente. |
| `Preencha o(s) campo(s): ...` | Um ou mais campos obrigatórios estão vazios. | Preencha os campos indicados na mensagem. |
| `Telefone inválido: use somente números.` | O telefone contém letras, espaços ou símbolos. | Digite apenas números. |
| `E-mail inválido: use o formato nome@dominio.com` | O e-mail não passou pela conferência do sistema. | Confira se há um nome, `@` e um domínio com ponto. |
| `Cliente '[nome]' salvo com sucesso!` | O novo cadastro foi gravado. | Confira os dados e continue ou faça outro cadastro. |
| `Cliente '[nome]' atualizado com sucesso!` | As alterações foram gravadas. | Continue usando o sistema. |
| `Cliente '[nome]' excluído com sucesso!` | O cadastro foi excluído. | Confira se selecionou a pessoa certa antes da confirmação. |
| `Formulário limpo` | Os campos foram apagados. | Preencha novamente se quiser cadastrar um cliente. |
| `Selecione um cliente antes de editar.` | Você tentou editar sem selecionar um cliente. | Volte à lista, selecione uma linha e tente novamente. |
| `Selecione um cliente antes de excluir.` | Você tentou excluir sem selecionar um cliente. | Volte à lista, selecione uma linha e tente novamente. |
| `Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado.` | O cadastro não está mais disponível para alteração. | Clique em **Consultar** novamente e confira a lista atualizada. |
| `Erro ao salvar no banco: ...` | O programa encontrou um problema ao gravar os dados. | Anote a mensagem completa e peça ajuda ao responsável pela instalação. |

## Dúvidas frequentes

**Fechei o programa. Perdi os clientes cadastrados?**

Não. Os clientes ficam gravados no arquivo `techbairro.db`. Ao abrir o programa novamente, os dados devem continuar lá, desde que o arquivo não tenha sido apagado ou movido.

**O que faço se o telefone for recusado?**

Apague o conteúdo do campo e digite somente os números do telefone, sem espaços, traços, parênteses ou sinal de mais.

**Como sei onde os dados estão guardados?**

Confira no terminal a mensagem `Banco em uso:`. Ela mostra o caminho completo do arquivo utilizado pelo programa.

**Posso apagar um cliente por engano?**

A TechBairro pede confirmação antes de excluir. Leia o nome com atenção e escolha **Não** se não tiver certeza. Para recuperar dados de uma exclusão, será necessário usar uma cópia de segurança.

**O que faço se o programa não abrir?**

Confirme se o Python 3 está instalado e se o Tkinter funciona. Se o problema continuar, anote a mensagem exibida no terminal e peça ajuda ao responsável pela instalação.

## Cuidados com os dados

Os cadastros podem conter dados pessoais. Use o sistema somente para a finalidade da associação, não compartilhe os dados sem autorização e mantenha cópias de segurança em local protegido. Nunca envie o arquivo `techbairro.db` para um repositório público.
