from flask import Blueprint, render_template, request, Response

login = Blueprint("login", __name__)

fake_db = {"users": [{"username": "admin", "password": "admin"}]}


@login.route("/login", methods=["POST"])
def login_route():
    if request.method == "POST":
        body = request.get_json(force=True)

        for user in fake_db["users"]:
            if user["username"] == body["username"]:
                if user["password"] == body["password"]:
                    return Response(status=204)
            return Response(status=401)
        return Response(status=401)
    return Response(status=500)


@login.route("/login_template")
def login_template():
    return render_template("login.html")
