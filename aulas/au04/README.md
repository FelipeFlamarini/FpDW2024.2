# Aula 04 - 06/11/2024

## Renderizando uma página HTML com Flask

Por padrão, o Flask procura o arquivo na pasta *templates*.

```python
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html", nome=nome, idade=idade) # é possível passar parâmetros para a página e usá-los com jinja2 
```

## Atividades

### Atividade 1

Considerando um usuário e uma senha mocados (como uma variável temporária apenas para testes, que vai ser removida no futuro), faça uma página de autenticação (login, senha) que retorne uma mensagem "Bom dia {pessoa}" se acertar usuário e senha, ou "Usuário e senha não conferem" se errar.

* * *

### Atividade 2

Limite as tentativas do usuário para 2 vezes.

* * *

### Atividade 3

Estilizar as páginas.

* * *

### Atividade 4

Escreva um script em Python que gere automaticamente um template HTML baseado em um formulário de input de dados. Esses inputs devem ser recebidos como um payload JSON.

* * *

### Atividade 5

Incremente o script da atividade 4 para que, após gerar o template, ele construa automaticamente uma rota que permita visualizar o template.

* * *

### Atividade 6

Crie uma classe "Pessoa" que encapsula dados do usuário e desenvolva uma função de autenticação

* * *
