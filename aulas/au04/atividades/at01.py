from flask import Blueprint, request, Response, session, render_template

at01Blueprint = Blueprint("at01", __name__, url_prefix="/at01")

fake_db = {
    "users": [
        {"username": "admin", "password": "admin"},
        {"username": "user", "password": "user"},
    ]
}

MAX_ATTEMPTS = 2


@at01Blueprint.route("/")
def index():
    return render_template("au04/at01/index.html")


@at01Blueprint.route("/auth", methods=["POST"])
def login_route():
    if request.method == "POST":
        if session.get("attempts", 0) >= MAX_ATTEMPTS:
            return Response(status=403)

        body = request.form

        for user in fake_db["users"]:
            if user["username"] == body["username"]:
                if user["password"] == body["password"]:
                    session["username"] = body["username"]
                    session.pop("attempts", None)
                    return Response(status=204)
                session["attempts"] = session.get("attempts", 0) + 1
                return Response(status=401)

        session["attempts"] = session.get("attempts", 0) + 1
        return Response(status=401)
    return Response(status=500)


@at01Blueprint.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("attempts", None)
    return Response(status=204)
