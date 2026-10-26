# Changelog da TechBairro

## v3.3.2 (Aula 27)

### Adicionado
- Registro dos testes manuais em `docs/registro_de_testes.md`.
- Atualização da documentação para a entrega final da TechBairro.

## v3.3.1 (Aula 25)

### Adicionado
- Código publicado no GitHub, com histórico de versões.

## v3.3.1 (Aula 21)

### Alterado
- Reorganizei o código em quatro arquivos, cada um com uma responsabilidade: `cliente.py` (a classe `Cliente`), `banco.py` (o `GerenciadorClientes` e todo o SQL), `validacao.py` (as regras de negócio) e `techbairro.py` (a janela). Para quem usa o sistema, nada mudou.
- O `salvar()` agora pergunta ao `ValidadorCliente` se o cliente é válido e só mostra a mensagem; a função `email_parece_valido()` saiu do `techbairro.py` e virou método do validador, então a regra existe em um único lugar.

### Adicionado
- Classe `ValidadorCliente` (`validacao.py`) com as regras RF01 a RF03: campos vazios, telefone só com números e formato do e-mail.
- Arquivo `testar_validacao.py`, que testa as regras de negócio sem abrir a janela e sem usar o banco.

## v3.3.0 (Aula 20)

### Adicionado
- Modo de edição visível: ao editar um cliente, o botão **Salvar** passa a mostrar **Salvar edição** e volta a **Salvar** quando a edição termina (salvando ou cancelando).
- Mensagem **"Edição cancelada. Nada foi alterado."** ao clicar em Cancelar durante uma edição; sem edição, continua **"Formulário limpo"**.
- Duplo clique numa linha da Consulta abre a edição do cliente, igual ao botão **Editar selecionado**.
- Aviso **"Cliente não encontrado"** quando o cliente que se tenta excluir já foi excluído por outra Consulta; a lista é recarregada em seguida.
- Aviso **"Cliente não encontrado: ele pode ter sido excluído. Nada foi alterado."** quando se salva a edição de um cliente que já não existe no banco.

### Corrigido
- **Excluir selecionado** e **Editar selecionado** passaram a usar o cliente que está na tela (e não uma nova busca no banco pela posição), então a confirmação mostra sempre o nome do cliente que foi clicado, mesmo se a lista da Consulta estiver desatualizada.
- Salvar uma edição não diz mais "atualizado com sucesso" quando o cliente já foi excluído: o resultado do `atualizar()` agora é conferido.
- Excluir não diz mais "excluído com sucesso" quando o cliente já tinha sido removido: o resultado do `remover()` agora é conferido.
- Selecionar a linha de aviso "Nenhum cliente cadastrado" e clicar em Editar ou Excluir não gera mais erro (`IndexError`) no terminal; agora aparece o aviso "Selecione um cliente antes de editar/excluir."

## v3.2.1 (Aula 18)

### Alterado
- O número da versão passou a ficar em uma única constante no arquivo `techbairro.py`.

### Adicionado
- Script `scripts/gerar_pacote.py`, que gera o pacote da versão para publicação.
- Arquivo `COMO_EXECUTAR.txt`, com instruções para executar o sistema.

## v3.2 (Aula 16)

### Alterado
- Alterei o caminho do banco para ele abrir sempre na pasta do projeto, usando `os.path` e `__file__`, mesmo se o programa for executado de outro lugar.

### Adicionado
- Adicionei a mensagem "banco em uso" no terminal, mostrando qual arquivo do banco está sendo utilizado.

## v3.1 (Aula 15)

### Corrigido
- Corrigi o método `atualizar()`, que não estava fazendo o `commit()` corretamente.
- Corrigi a edição e a exclusão para usarem o `id` do banco, evitando problemas com índices.
- Corrigi a validação do telefone para não aceitar caracteres que não sejam números.
- Corrigi os casos em que o endereço estava vazio e causava erros.
- Corrigi a ordenação e a contagem dos clientes para ficarem iguais aos resultados mostrados pelo banco.

## v3.0 (Aula 14)

### Alterado
- Troquei a lista em memória pelo banco SQLite `techbairro.db`, fazendo os clientes continuarem salvos mesmo depois de fechar o programa.
