from flask import Blueprint, render_template, request, Response

create_template = Blueprint("create_template", __name__)

template_counter = 1


def create_html(data: dict):
    global template_counter
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{data["name"]}</title>
        <script src="https://cdn.tailwindcss.com"></script>
    </head>
    <body class="bg-gray-200">
        <div id="main-container" class="my-8 grid grid-cols-2 gap-4 max-w-2xl mx-auto">
            <div id="info" class="bg-blue-600 text-white p-8 rounded">
                <h2>{data["name"]}</h2>
                <p>{data["age"]} anos</p>
                <p>{data["about"]}</p>
            </div>
            <div id="contatos" class="bg-white text-black p-8 rounded">
                <h2>Contatos</h2>
                <p>Email: {data["email"]}</p>
                <p>GitHub: {data["github"]}</p>
            </div>
        </div>
    </body>
    </html>
    """
    with open(f"templates/temp/{template_counter}.html", "w") as file:
        template_counter += 1
        file.write(html)
        file.close()


@create_template.route("/template", methods=["POST"])
def post_template():
    if request.method == "POST":
        create_html(request.get_json(force=True))
        return Response({"message": "Página 1"}, status=201)
    return Response(status=500)

@create_template.route("/template/<template_id>")
def get_template(template_id: int):
    return render_template(f"temp/{template_id}.html")