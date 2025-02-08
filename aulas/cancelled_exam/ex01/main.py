from flask import Blueprint, render_template, request, redirect, url_for, Response
from datetime import datetime
from http import HTTPStatus

ex01Blueprint = Blueprint("ex01", __name__, url_prefix="/ex01")

posts = []


@ex01Blueprint.route("/")
def index():
    sorted_posts = sorted(posts, key=lambda x: x["date"], reverse=True)
    return render_template("cancelled_exam/ex01/index.html", posts=sorted_posts)


@ex01Blueprint.route("/add", methods=["POST"])
def add_post():
    if request.method == "POST":
        content = request.form["content"]
        date = datetime.now()
        posts.append({"content": content, "date": date})
        return redirect(url_for("index"))
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)
