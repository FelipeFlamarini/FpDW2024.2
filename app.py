from flask import Flask, render_template, send_from_directory
from pathlib import Path
from tqdm import tqdm

# blueprints aulas
from aulas.au03.main import au03Blueprint
from aulas.au05.main import au05Blueprint

# blueprints atividades
from atividades.at01.main import at01Blueprint
from atividades.at02.main import at02Blueprint
from atividades.at03.main import at03Blueprint
from atividades.at04.main import at04Blueprint
from atividades.at05.main import at05Blueprint

from atividades.login import login
from atividades.create_template import create_template

app = Flask(__name__)
app.secret_key = "verysecretkey"


@app.get("/directories")
def directories():
    return {"dir": [str(dir) for dir in tqdm(Path(".").iterdir())]}


# blueprints aulas
app.register_blueprint(au03Blueprint)
app.register_blueprint(au05Blueprint)

# blueprints atividades
app.register_blueprint(at01Blueprint)
app.register_blueprint(at02Blueprint)
app.register_blueprint(at03Blueprint)
app.register_blueprint(at04Blueprint)
app.register_blueprint(at05Blueprint)
app.register_blueprint(login)
app.register_blueprint(create_template)

if __name__ == "__main__":
    app.run(debug=True)
