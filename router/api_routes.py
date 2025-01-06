from flask import jsonify, request
from datetime import datetime, timezone
from markdown import markdown
from model.Article import db, Article


def api_routes(app):

    # All articles
    @app.route('/api/articles', methods=['GET'])
    def get_articles():
        articles = Article.query.all()
        return jsonify({"message": "OK", "data": [article.to_dict() for article in articles]}), 200

    # Get article_id
    @app.route('/api/article/<int:article_id>', methods=['GET'])
    def get_article(article_id):
        article = Article.query.get(article_id)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        return jsonify({"message": "OK", "data": article.to_dict()})

    # create new article
    @app.route('/api/article', methods=['POST'])
    def create_article():
        data = request.get_json()

        if not data or 'title' not in data or 'content' not in data:
            return jsonify({"message": "Title and content are required"}), 400

        new_article = Article(
            title=data['title'],
            content=markdown(data['content']),
            type=data['type'],
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc)
        )

        db.session.add(new_article)
        db.session.commit()

        return jsonify({"message": "OK", "data": new_article.to_dict()}), 201

    # update article
    @app.route('/api/article/<int:article_id>', methods=['PUT'])
    def update_article(article_id):
        article = Article.query.get(article_id)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        data = request.get_json()

        # Update students data
        article.title = data.get('title', article.title)
        article.content = markdown(data.get('content', article.content))
        article.type = data.get('type', article.type)
        article.update_at = datetime.now(timezone.utc)

        db.session.commit()

        return jsonify({"message": "OK", "data": article.to_dict()}), 200

    # delete article
    @app.route('/api/article/<int:article_id>', methods=['DELETE'])
    def delete_article(article_id):
        article = Article.query.get(article_id)

        if article is None:
            return jsonify({"message": "article not found"}), 404

        db.session.delete(article)
        db.session.commit()

        return jsonify({"message": "OK", "data": article.to_dict()}), 200
