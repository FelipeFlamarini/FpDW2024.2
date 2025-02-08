from flask import Blueprint, render_template

au05Blueprint = Blueprint("au05", __name__, url_prefix="/au05")


@au05Blueprint.route("/")
def index():
    return render_template("au05/index.html")
