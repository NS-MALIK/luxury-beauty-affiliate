from src.models import db
from datetime import datetime

class Wishlist(db.Model):
    __tablename__ = 'wishlists'
    
    id = db.Column(db.Integer, primary_key=True)
    session_id = db.Column(db.String(255), nullable=False, index=True)  # For anonymous users
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to product
    product = db.relationship('Product', backref='wishlist_items')
    
    # Unique constraint to prevent duplicate entries
    __table_args__ = (db.UniqueConstraint('session_id', 'product_id', name='unique_session_product'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'session_id': self.session_id,
            'product_id': self.product_id,
            'product': self.product.to_dict() if self.product else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }
    
    @classmethod
    def add_to_wishlist(cls, session_id, product_id):
        """Add a product to wishlist for a session"""
        try:
            # Check if already exists
            existing = cls.query.filter_by(session_id=session_id, product_id=product_id).first()
            if existing:
                return existing
            
            # Create new wishlist item
            wishlist_item = cls(session_id=session_id, product_id=product_id)
            db.session.add(wishlist_item)
            db.session.commit()
            return wishlist_item
        except Exception as e:
            db.session.rollback()
            raise e
    
    @classmethod
    def remove_from_wishlist(cls, session_id, product_id):
        """Remove a product from wishlist for a session"""
        try:
            wishlist_item = cls.query.filter_by(session_id=session_id, product_id=product_id).first()
            if wishlist_item:
                db.session.delete(wishlist_item)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise e
    
    @classmethod
    def get_wishlist(cls, session_id):
        """Get all wishlist items for a session"""
        return cls.query.filter_by(session_id=session_id).order_by(cls.created_at.desc()).all()
    
    @classmethod
    def is_in_wishlist(cls, session_id, product_id):
        """Check if a product is in wishlist for a session"""
        return cls.query.filter_by(session_id=session_id, product_id=product_id).first() is not None
    
    @classmethod
    def get_wishlist_count(cls, session_id):
        """Get count of items in wishlist for a session"""
        return cls.query.filter_by(session_id=session_id).count()