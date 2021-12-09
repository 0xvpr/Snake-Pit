from flask import ( Blueprint,
                    request,
                    render_template )

from typing import Text

routes = Blueprint("routes", __name__)

@routes.route("/")
def index() -> Text:
    host = request.url_root
    return render_template("index.html", host=host)
