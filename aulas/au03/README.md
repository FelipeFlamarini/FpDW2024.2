# Aula 03 - 30/10/2024

### Explicando o conceito de uma aplicação *web*
*Requests* do cliente, *responses* do servidor
* * *
### Iniciando servidor *Flask*
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
### Criando uma rota básica
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
Se o argumento *methods* 
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
### Renderizando uma página HTML
Por padrão, o Flask procura o arquivo na pasta *templates*.
```python
from flask import render_template

@app.route("/")
def index():
    return render_template("index.html")
```