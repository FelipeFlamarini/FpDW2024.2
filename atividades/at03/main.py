from flask import Blueprint, render_template

at03Blueprint = Blueprint("at03", __name__, url_prefix="/at03")

@at03Blueprint.route("/")
def index():
    return render_template("at03/index.html")
