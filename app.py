from flask import Flask
from router.api_routes import api_routes

app = Flask(__name__)

api_routes(app)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
