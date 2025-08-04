# src/models/subscription.py
from datetime import datetime
# Import db from the new central location
from src.models import db

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    subscribed_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<Subscriber {self.email}>'

# IMPORTANT: Remove this line if it exists in your model file: `db = SQLAlchemy()`
# The db instance is now centralized in `src/models/__init__.py`