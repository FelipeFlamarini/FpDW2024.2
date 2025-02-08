from flask import Blueprint, render_template

from aulas.cancelled_exam.ex01.main import ex01Blueprint
from aulas.cancelled_exam.ex02.main import ex02Blueprint
from aulas.cancelled_exam.ex03.main import ex03Blueprint

cancelled_examBlueprint = Blueprint("cancelled_exam", __name__, url_prefix="/exam")
cancelled_examBlueprint.register_blueprint(ex01Blueprint)
cancelled_examBlueprint.register_blueprint(ex02Blueprint)
cancelled_examBlueprint.register_blueprint(ex03Blueprint)


@cancelled_examBlueprint.route("/")
def index():
    return render_template("cancelled_exam/index.html")
