from flask import Blueprint, render_template

at05Blueprint = Blueprint("at05", __name__, url_prefix="/at05")


@at05Blueprint.route("/")
def index():
    return render_template("au03/at05/index.html")


@at05Blueprint.route("/<nome>")
def get_curriculum(nome):
    return render_template(f"au03/at05/{nome}.html")
