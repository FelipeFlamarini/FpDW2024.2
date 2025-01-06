from flask import Blueprint, render_template

at02Blueprint = Blueprint("at02", __name__, url_prefix="/at02")

@at02Blueprint.route("/")
def index():
    return render_template("au03/at02/index.html")
