from flask import Blueprint, render_template

from aulas.au03.atividades import at01, at02, at03, at04, at05

au03Blueprint = Blueprint("au03", __name__, url_prefix="/au03")


@au03Blueprint.route("/contact")
def contact():
    return {
        "name": "Felipe Flamarini",
        "email": "felipeflamarini@hotmail.com",
        "phone": "+55 (67) 99999-9999",
        "city": "Três Lagoas",
        "state": "Mato Grosso do Sul",
        "country": "Brazil",
    }


@au03Blueprint.route("/")
def index():
    return render_template("au03/contact.html")


au03Blueprint.register_blueprint(at01.at01Blueprint)
au03Blueprint.register_blueprint(at02.at02Blueprint)
au03Blueprint.register_blueprint(at03.at03Blueprint)
au03Blueprint.register_blueprint(at04.at04Blueprint)
au03Blueprint.register_blueprint(at05.at05Blueprint)
