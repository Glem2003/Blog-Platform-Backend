from flask import jsonify
from utils.file_operations import read_json
from config.config import ARTICLES_DATA_FILE


def api_routes(app):

    # All articles
    @app.route('/api/articles', methods=['GET'])
    def get_articles():
        articles = read_json(ARTICLES_DATA_FILE)
        return jsonify({"message": "OK", "data": articles}), 200

    # Get article_id
    @app.route('/api/article/<int:article_id>', methods=['GET'])
    def get_article(article_id):
        articles = read_json(ARTICLES_DATA_FILE)
        article = next(
            (article for article in articles if article['id'] == article_id), None)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        return jsonify({"message": "OK", "data": article})
