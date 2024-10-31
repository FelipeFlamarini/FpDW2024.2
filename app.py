from flask import Flask, render_template
from pathlib import Path
from tqdm import tqdm
from aulas.au03.main import au03Blueprint

app = Flask(__name__)


@app.get("/directories")
def directories():
    return {"dir": [str(dir) for dir in tqdm(Path(".").iterdir())]}

app.register_blueprint(au03Blueprint)


if __name__ == "__main__":
    app.run(debug=True)
