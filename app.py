from flask import Flask
from router.api_routes import api_routes


def blog_platform():
    app = Flask(__name__)

    # RESTful API
    api_routes(app)

    return app


if __name__ == '__main__':
    app = blog_platform()
    app.run(port=5000, debug=True)
