from flask import Blueprint, request, Response
from pydantic import BaseModel, ValidationError

at06Blueprint = Blueprint("at06", __name__, url_prefix="/at06")


class Person(BaseModel):
    username: str
    password: str


users_db = {"john_doe": "securepassword123", "jane_smith": "password456"}


def authenticate(pessoa: Person) -> bool:
    stored_password = users_db.get(pessoa.username)
    return stored_password == pessoa.password


@at06Blueprint.route("/", methods=["POST"])
def login():
    try:
        pessoa = Person(**request.form)
    except ValidationError as e:
        return Response({"error": e.errors()}, status=400)

    if authenticate(pessoa):
        return Response({"message": "Authentication successful"}, status=200)
    else:
        return Response({"message": "Invalid credentials"}, status=401)
