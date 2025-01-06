from flask import Flask, render_template

# blueprints aulas
from aulas.au03.main import au03Blueprint
from aulas.au05.main import au05Blueprint
from aulas.au05.login import login

app = Flask(__name__)
app.secret_key = "verysecretkey"


@app.route("/")
def index():
    return render_template("index.html")


# blueprints aulas
app.register_blueprint(au03Blueprint)
app.register_blueprint(au05Blueprint)
app.register_blueprint(login)


if __name__ == "__main__":
    app.run(debug=True)
