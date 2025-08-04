from seed_data.seed_products import seed_products
from seed_data.seed_blog_posts import seed_blog_posts
from src.models import db

def seed_all_data():
    """Seeds all data by calling individual seed functions."""
    with db.session.begin():
        seed_products()
        seed_blog_posts()



 