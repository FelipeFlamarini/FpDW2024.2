from flask import Flask, render_template, send_from_directory
from pathlib import Path
from tqdm import tqdm

# blueprints aulas
from aulas.au03.main import au03Blueprint

# blueprints atividades
from atividades.at01.main import at01Blueprint

app = Flask(__name__)


@app.get("/directories")
def directories():
    return {"dir": [str(dir) for dir in tqdm(Path(".").iterdir())]}


# blueprints aulas
app.register_blueprint(au03Blueprint)

# blueprints atividades
app.register_blueprint(at01Blueprint)

if __name__ == "__main__":
    app.run(debug=True)
