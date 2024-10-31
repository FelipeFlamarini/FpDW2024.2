from flask import Blueprint, render_template

au03Blueprint = Blueprint("au03", __name__, url_prefix="/au03")


@au03Blueprint.route("/contact")
def contact():
    return {
        "name": "Felipe Flamarini",
        "email": "felipeflamarini@hotmail,com",
        "phone": "+55 (67) 99999-9999",
        "city": "Três Lagoas",
        "state": "Mato Grosso do Sul",
        "country": "Brazil",
    }

@au03Blueprint.route("/")
def index():
    return render_template("contact.html")