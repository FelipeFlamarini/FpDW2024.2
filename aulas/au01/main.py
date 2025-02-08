from flask import Blueprint, render_template

au01Blueprint = Blueprint("au01", __name__, url_prefix="/au01")


@au01Blueprint.route("/")
def index():
    return render_template("au01/index.html")
