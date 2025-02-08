from flask import Blueprint, render_template
from aulas.au04.atividades.at01 import at01Blueprint
from aulas.au04.atividades.at04 import at04Blueprint
from aulas.au04.atividades.at06 import at06Blueprint

au04Blueprint = Blueprint("au04", __name__, url_prefix="/au04")


@au04Blueprint.route("/")
def index():
    return render_template("au04/index.html")


au04Blueprint.register_blueprint(at01Blueprint)
au04Blueprint.register_blueprint(at04Blueprint)
au04Blueprint.register_blueprint(at06Blueprint)
