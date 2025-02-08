from flask import Blueprint, request, Response, jsonify
from pydantic import BaseModel, ValidationError

at06Blueprint = Blueprint("at06", __name__, url_prefix="/at06")


class Person(BaseModel):
    username: str
    password: str


users_db = [
    Person(username="john_doe", password="securepassword123"),
    Person(username="jane_smith", password="password456"),
]


def authenticate(pessoa: Person) -> bool:
    for user in users_db:
        if user.username == pessoa.username and user.password == pessoa.password:
            return True
    return False


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
