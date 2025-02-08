from flask import Blueprint, render_template

au02Blueprint = Blueprint("au02", __name__, url_prefix="/au02")


@au02Blueprint.route("/")
def index():
    return render_template("au02/index.html")
