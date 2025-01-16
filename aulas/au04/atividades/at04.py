from typing import List
from datetime import datetime
from http import HTTPStatus

from flask import Blueprint, request, render_template, Response
from pydantic import BaseModel


class Book(BaseModel):
    title: str
    description: str
    author: str
    genres: List[str]
    published_date: datetime


books: List[Book] = []

at04Blueprint = Blueprint("at04", __name__, url_prefix="/at04")


@at04Blueprint.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("/au04/at04/index.html")
    if request.method == "POST":
        global books
        request_data = {**request.form}
        genres = request_data.pop("genres", "").split(",")
        books.append(Book(**request_data, genres=genres))
        return Response(status=HTTPStatus.CREATED)
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)


@at04Blueprint.route("/<int:id>", methods=["GET"])
def get_book(id: int):
    global books
    try:
        return render_template(
            "au04/at04/book.html", book=books[id].model_dump(), id=id
        )
    except IndexError:
        return Response(status=HTTPStatus.NOT_FOUND)
