from flask import Flask
from flask_cors import CORS
from router.api_routes import api_routes
from model.Article import db

def blog_platform():
    # 建立 Flask 應用
    app = Flask(__name__)

    # 設定 SQLite 資料庫 URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 初始化 SQLAlchemy 與 CORS
    db.init_app(app)
    CORS(app)

    # RESTful API
    api_routes(app)

    return app


app = blog_platform()


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
