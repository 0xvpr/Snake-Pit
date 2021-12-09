from flask import Flask
from .routes import routes

def create_app() -> Flask:
    app = Flask(__name__)
    app.debug = False
    app.register_blueprint(routes, url_prefix="/")

    return app
