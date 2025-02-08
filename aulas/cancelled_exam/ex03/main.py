from werkzeug.utils import secure_filename
import os
from datetime import datetime
from flask import Blueprint, render_template, request, Response, current_app
from http import HTTPStatus

ex03Blueprint = Blueprint("ex03", __name__, url_prefix="/ex03")

uploaded_files = []
UPLOAD_FOLDER = "static/uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@ex03Blueprint.route("/")
def index():
    return render_template(
        "cancelled_exam/ex03/index.html", uploaded_files=uploaded_files
    )


@ex03Blueprint.route("/upload", methods=["POST"])
def upload_file():
    if request.method == "POST":
        if "file" not in request.files:
            return Response(
                {"message": "No file part"},
                status=400,
                mimetype="application/json",
            )
        file = request.files["file"]
        if file.filename == "":
            return Response(
                {"message": "No selected file"},
                status=400,
                mimetype="application/json",
            )
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            timestamp = datetime.now()
            uploaded_files.append(
                {"filename": filename, "filepath": filepath, "timestamp": timestamp}
            )
            print(filepath)
            return Response(
                {"message": "File successfully uploaded", "filepath": filepath},
                status=200,
                mimetype="application/json",
            )
        return Response(
            {"message": "File upload failed"},
            status=500,
            mimetype="application/json",
        )
    return Response(
        {"message": "Method not allowed"}, status=HTTPStatus.METHOD_NOT_ALLOWED
    )
