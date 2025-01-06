from flask import (
    Blueprint,
    render_template,
    request,
    Response,
    session,
    redirect,
    url_for,
)

login = Blueprint("login", __name__)

fake_db = {
    "users": [
        {"username": "admin", "password": "admin"},
        {"username": "user", "password": "user"},
    ]
}


@login.route("/auth", methods=["POST"])
def login_route():
    if request.method == "POST":
        body = request.form

        for user in fake_db["users"]:
            if user["username"] == body["username"]:
                if user["password"] == body["password"]:
                    session["username"] = body["username"]
                    return Response(status=204)
                return Response(status=401)
        return Response(status=401)
    return Response(status=500)


@login.route("/logout")
def logout():
    session.pop("username", None)
    return Response(status=204)
