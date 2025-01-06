# Aula 03 - 30/10/2024

## Explicando o conceito de uma aplicação *web*

*Requests* do cliente, *responses* do servidor

* * *

## Iniciando servidor *Flask*

Pelo CLI do *Flask*

```sh
flask run --debug
```

Pelo CLI do Python, desde que o script possua o *app.run(debug=True, host='0.0.0.0)*

```sh
python app.py
```

O argumento debug ativa o modo de desenvolvimento do Flask, fazendo com que o app reinicie sempre que um script do app é alterado

* * *

## Criando uma rota básica

O Flask oferece um decorador para cada método HTTP.
Utilizando o decorador *get* na rota "/" (*root*)

```python
@app.get("/")
def hello_world():
    return {"hello": "world"}
```

Utilizando o decorador *route*, que permite receber mais de um método de *request* na mesma rota

```python
from flask import request

@app.route("/todos", methods=["GET", "POST"])
def todos():
    if request.method === POST:
        db.add(request.values.get("todo"))
    elif request.method === GET:
        return db.get("todos")
```

Se o argumento *methods* está ausente, por padrão o único método aceitado será GET.
O objeto [*request*](https://flask.palletsprojects.com/en/stable/quickstart/#accessing-request-data) é necessário para acessar o método atual e o *body* de um método *POST* ou *PUT*.
Também é possível receber mais de um método de *request* na mesma rota utilizando os decoradores específicos para cada rota

```python
@app.get("/todos")
def todos_get():
    return db.get("todos")

from flask import request
@app.post("/todos")
def todos_post():
    return db.add(request.values.get("todo"))
```

Também é possível acessar o *body* pela propriedade [*form*](https://flask.palletsprojects.com/en/stable/api/#flask.Request.form). Na verdade, a propriedade [*values*](https://flask.palletsprojects.com/en/stable/api/#flask.Request.values) é baseada na propriedade *form*.

* * *

## Atividades

1. criar rota web html com a tag canvas onde o usuário pode deslocar uma foto para a esquerda e direita com as setas do teclado
2. criar rota web html que permite ao usuário tirar uma foto com webcam
3. criar uma rota web sem a tag table que exiba uma tabela com 997 linhas e 5 colunas
coluna 1: id
coluna 2: nome
coluna 3: sobrenome
coluna 4: email
coluna 5: ações

4. criar 3 rotas, uma para cada atividade anterior, "bonita"
5. criar 6 rotas, sendo todas "bonitas", cada uma contendo currículo de um integrate do grupo.
