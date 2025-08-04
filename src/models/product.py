# from flask_sqlalchemy import SQLAlchemy
# from src.models.user import db
from src.models import db
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # skincare, makeup, fragrance
    subcategory = db.Column(db.String(50), nullable=True)  # anti-aging, foundation, perfume
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    amazon_url = db.Column(db.String(500), nullable=False)
    image_url = db.Column(db.String(500), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    review_count = db.Column(db.Integer, nullable=True)
    ingredients = db.Column(db.Text, nullable=True)
    benefits = db.Column(db.Text, nullable=True)
    usage_instructions = db.Column(db.Text, nullable=True)
    is_featured = db.Column(db.Boolean, default=False)
    is_active = db.Column(db.Boolean, default=True)



    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __repr__(self):
        return f'<Product {self.name} by {self.brand}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'brand': self.brand,
            'category': self.category,
            'subcategory': self.subcategory,
            'description': self.description,
            'price': self.price,
            'amazon_url': self.amazon_url,
            'image_url': self.image_url,
            'rating': self.rating,
            'review_count': self.review_count,
            'ingredients': self.ingredients,
            'benefits': self.benefits,
            'usage_instructions': self.usage_instructions,
            'is_featured': self.is_featured,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
