from flask import Flask
from flask_cors import CORS
from router.api_routes import api_routes


def blog_platform():
    app = Flask(__name__)
    CORS(app)

    # RESTful API
    api_routes(app)

    return app


app = blog_platform()
