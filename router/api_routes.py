from flask import jsonify, request
from utils.file_operations import read_json, write_json
from datetime import datetime, timezone
from markdown import markdown
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
            # article_id | None
            (article for article in articles if article['id'] == article_id), None)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        return jsonify({"message": "OK", "data": article})

    # create new article
    @app.route('/api/article', methods=['POST'])
    def create_article():
        articles = read_json(ARTICLES_DATA_FILE)
        data = request.get_json()

        new_id = max([article['id'] for article in articles], default=0)+1
        now = datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S")  # format is ISO

        new_article = {
            "id": new_id,
            "title": data.get('title', 'Untitled'),
            "content": markdown(data.get('content', '')),
            "created_at": now,
            "updated_at": now
        }

        articles.append(new_article)
        write_json(ARTICLES_DATA_FILE, articles)
        return jsonify({"message": "OK", "data": new_article}), 201

    # update article
    @app.route('/api/article/<int:article_id>', methods=['PUT'])
    def update_article(article_id):
        articles = read_json(ARTICLES_DATA_FILE)
        article = next(
            (article for article in articles if article['id'] == article_id), None)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        data = request.get_json()
        now = datetime.now(timezone.utc).strftime(
            "%Y-%m-%dT%H:%M:%S")  # format is ISO

        # Update students data
        article['title'] = data.get('title', article['title'])
        article['content'] = markdown(data.get('content', ''))
        article['updated_at'] = now

        # save data in Json
        write_json(ARTICLES_DATA_FILE, articles)

        return jsonify({"message": "OK", "data": article}), 200

    # delete article
    @app.route('/api/article/<int:article_id>', methods=['DELETE'])
    def delete_article(article_id):
        articles = read_json(ARTICLES_DATA_FILE)
        article = next(
            # article_id | None
            (article for article in articles if article['id'] == article_id), None)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        articles.remove(article)

        try:
            write_json(ARTICLES_DATA_FILE, articles)
        except Exception as e:
            # <class exception> transform <class str>
            return jsonify({"error": f"Failed to update student data: {str(e)}"}), 500

        return jsonify({"message": "OK", "data": article}), 200
