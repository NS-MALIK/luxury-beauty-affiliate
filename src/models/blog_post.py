# from flask_sqlalchemy import SQLAlchemy
# from src.models.user import db
from src.models import db
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)
    excerpt = db.Column(db.Text, nullable=True)
    content = db.Column(db.Text, nullable=False)
    meta_title = db.Column(db.String(60), nullable=True)
    meta_description = db.Column(db.String(160), nullable=True)
    featured_image = db.Column(db.String(500), nullable=True)
    category = db.Column(db.String(50), nullable=False)  # guide, review, trend, ingredient
    tags = db.Column(db.String(500), nullable=True)  # comma-separated tags
    is_published = db.Column(db.Boolean, default=False)
    published_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<BlogPost {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'slug': self.slug,
            'excerpt': self.excerpt,
            'content': self.content,
            'meta_title': self.meta_title,
            'meta_description': self.meta_description,
            'featured_image': self.featured_image,
            'category': self.category,
            'tags': self.tags.split(',') if self.tags else [],
            'is_published': self.is_published,
            'published_at': self.published_at.isoformat() if self.published_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
