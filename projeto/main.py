from flask_openapi3 import OpenAPI, Info, APIBlueprint

info = Info(title="projeto", version="0.1")
app = OpenAPI(__name__, info=info)
api = APIBlueprint("/api", __name__, url_prefix="/api")


@api.get("/teste")
def hello_world():
    return {"hello": "world"}


app.register_api(api)

if __name__ == "__main__":
    app.run(debug=True)
