from flask import Blueprint
from aulas.au04.atividades.at01 import at01Blueprint
from aulas.au04.atividades.at04 import at04Blueprint

au04Blueprint = Blueprint("au04", __name__, url_prefix="/au04")

au04Blueprint.register_blueprint(at01Blueprint)
au04Blueprint.register_blueprint(at04Blueprint)
