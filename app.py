from flask import Flask
from router.api_routes import api_routes


def blog_platform():
    app = Flask(__name__)

    # RESTful API
    api_routes(app)

    return app

app = blog_platform()
