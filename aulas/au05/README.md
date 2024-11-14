## Aula 5 13/11/2024

## Regras do back-end
### 1. Não confie nos dados que chegam
É necessário validar os dados que chegam das requisições, onde a validação depende do tipo esperado do dado. Se o dado é esperado que seja do tipo int, valida-se se o dado é um int, etc.

### 2. Garantir integridade e consistência dos dados
Use um armazenamento consistente para guardar os dados.

### 3. Trabalha-se de forma assíncrona se as respostas são demoradas para serem retornadas, de forma síncrona se forem rápidas.

### 4. Tratar as excessões
Não deixe seu back-end morrer

## Atividades em aula
Criar rota renderizando um formulário com dois campos, usuário e senha
Criar uma aplicação web com uma rota para autenticação
Fazer a integração de autenticação do front-end e back-end
Acrescentar ao parâmetro "methods" da rota a lista methods=["POST"]

## Tarefas
### 1. Fazer as validações, no back-end, verificando se usuário e senha foram enviados ao servidor
### 2. Tratar exceções para evitar que seja exibida a mensagem "Method not allowed"
### 3. Garantir que o usuário possa tentar a autenticação novamente quando usuário e senha estiverem incorretos
### 4. Limitar em 2 tentativas de autenticação
### 5. Alterar todos os retornos das rotas utilizando dados formatados em JSON.