from flask import render_template, request, Response, Blueprint
from datetime import datetime
from http import HTTPStatus

from pydantic import BaseModel


class LoginAttempt(BaseModel):
    username: str
    success: bool
    timestamp: datetime


ex02Blueprint = Blueprint("ex02", __name__, url_prefix="/ex02")


users = {"admin": "admin"}


login_attempts = []


@ex02Blueprint.route("/")
def login_page():
    login_attempts_dicts = [attempt.model_dump() for attempt in login_attempts]
    return render_template(
        "cancelled_exam/ex02/index.html", loginAttempts=login_attempts_dicts
    )


@ex02Blueprint.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        timestamp = datetime.now()

        if username in users and users[username] == password:
            login_attempts.append(
                LoginAttempt(username=username, success=True, timestamp=timestamp)
            )
            return Response(status=HTTPStatus.OK)
        else:
            login_attempts.append(
                LoginAttempt(username=username, success=False, timestamp=timestamp)
            )
            return Response(status=HTTPStatus.UNAUTHORIZED)
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)
