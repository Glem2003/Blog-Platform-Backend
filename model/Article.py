from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Article(db.Model):
    __tablename__ = 'articles'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    type = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, onupdate=datetime.now(timezone.utc))

    def __repr__(self):
        return f'<Article {self.id} - {self.title} created at {self.created_at}>'

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "type": self.type,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat()
        }
