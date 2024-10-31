# Aula 02 - 23/10/2024

## Gerenciando um ambiente virtual (*venv*)
### Ativando o *venv*
```sh
source .venv/bin/activate
```
* * *
### Instalando *Flask*, *SQLAlchemy* e *tqdm*
```sh
pip install -U flask Flask-SQLAlchemy tqdm
```
* * *

### Criando a lista de dependências
```sh
pip freeze > requirements.txt
```
O *requirements.txt* também vai guardar todas as versões das dependências instaladas, de forma que qualquer usuário que instale as dependências a partir do *requirements.txt* receba as versões corretas das dependências.
* * *

### Instalando dependências a partir do arquivo *requirements.txt*
```sh
pip install -r requirements.txt
```
* * *

## Definindo o tema e grupo do projeto
Meu grupo: sistema de chamada por câmeras