from flask import Blueprint, render_template, session

au05Blueprint = Blueprint("aula05", __name__)


@au05Blueprint.route("/aula05")
def index():
    return render_template("au05/index.html", session=session)
