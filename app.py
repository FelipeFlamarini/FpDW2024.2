import os
from flask import Flask, render_template

from aulas.au01.main import au01Blueprint
from aulas.au02.main import au02Blueprint
from aulas.au03.main import au03Blueprint
from aulas.au04.main import au04Blueprint
from aulas.au05.main import au05Blueprint
from aulas.cancelled_exam.main import cancelled_examBlueprint

app = Flask(__name__)
app.secret_key = "verysecretkey"

UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route("/")
def index():
    return render_template("index.html")


app.register_blueprint(au01Blueprint)
app.register_blueprint(au02Blueprint)
app.register_blueprint(au03Blueprint)
app.register_blueprint(au04Blueprint)
app.register_blueprint(au05Blueprint)

app.register_blueprint(cancelled_examBlueprint)

if __name__ == "__main__":
    app.run(debug=True)
