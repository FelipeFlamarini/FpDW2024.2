from flask import Blueprint, render_template

at04Blueprint = Blueprint("at04", __name__, url_prefix="/at04")


@at04Blueprint.route("/")
def index():
    return render_template("au03/at04/index.html")


@at04Blueprint.route("/<n>")
def number_template(n):
    print(n)
    return render_template(
        f"au03/at04/at04_{n}.html",
    )
