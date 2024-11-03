from flask import Blueprint, render_template

at01Blueprint = Blueprint("at01", __name__, url_prefix="/at01")

@at01Blueprint.route("/")
def index():
    return render_template("at01/index.html")
