
# import os
# import sys

# # DON'T CHANGE THIS !!! This is for path setup.
# sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# from flask import Flask, send_from_directory, abort, jsonify
# from flask_cors import CORS
# from flask_migrate import Migrate

# # Import the single, central db instance
# from src.models import db

# # Import your route blueprints
# from src.routes.user import user_bp
# from src.routes.product import product_bp
# from src.routes.blog import blog_bp
# from src.routes.seo import seo_bp
# from src.routes.wishlist import wishlist_bp
# from src.routes.subscription import subscription_bp
# from src.routes.search import search_bp

# # Initialize extensions without an app for now
# migrate = Migrate()

# def create_app():
#     app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
#     app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'

#     CORS(app, supports_credentials=True)

#     app.register_blueprint(user_bp, url_prefix='/api')
#     app.register_blueprint(product_bp, url_prefix='/api')
#     app.register_blueprint(blog_bp, url_prefix='/api')
#     app.register_blueprint(seo_bp)
#     app.register_blueprint(wishlist_bp, url_prefix='/api')
#     app.register_blueprint(subscription_bp)
#     app.register_blueprint(search_bp)
    
#     app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     # Initialize extensions with the app instance
#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     return app

# # Create the app instance
# app = create_app()

# @app.route('/', defaults={'path': ''})
# @app.route('/<path:path>')
# def serve_react_app(path):
#     requested_file_path = os.path.join(app.static_folder, path)
#     if path != "" and os.path.exists(requested_file_path):
#         return send_from_directory(app.static_folder, path)
#     else:
#         index_path = os.path.join(app.static_folder, 'index.html')
#         if os.path.exists(index_path):
#             return send_from_directory(app.static_folder, 'index.html')
#         else:
#             return "index.html not found in static folder.", 404

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
# import os
# import sys

# # This is for path setup. Don't change this.
# sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

# from flask import Flask, send_from_directory
# from flask_cors import CORS
# from flask_migrate import Migrate
# from src.routes.user import user_bp
# from src.routes.product import product_bp
# from src.routes.blog import blog_bp
# from src.routes.seo import seo_bp
# from src.routes.wishlist import wishlist_bp
# from src.routes.subscription import subscription_bp
# from src.routes.search import search_bp
# from src.models import db
# from src.models.product import Product
# from src.models.blog_post import BlogPost
# from src.models.user import User
# from src.models.wishlist import Wishlist
# from src.seed_data.seed_products import seed_products
# from src.seed_data.seed_blog_posts import seed_blog_posts
# from datetime import datetime
# import uuid

# migrate = Migrate()

# def create_app():
#     app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
#     app.config['SECRET_KEY'] = 'asdf#FGSgvasgf$5$WGT'
#     CORS(app, supports_credentials=True)
#     app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)
#     migrate.init_app(app, db)
    
#     # Register your blueprints
#     app.register_blueprint(user_bp, url_prefix='/api')
#     app.register_blueprint(product_bp, url_prefix='/api')
#     app.register_blueprint(blog_bp, url_prefix='/api')
#     app.register_blueprint(seo_bp)
#     app.register_blueprint(wishlist_bp, url_prefix='/api')
#     app.register_blueprint(subscription_bp)
#     app.register_blueprint(search_bp)
    
#     @app.route('/', defaults={'path': ''})
#     @app.route('/<path:path>')
#     def serve_react_app(path):
#         requested_file_path = os.path.join(app.static_folder, path)
#         if path != "" and os.path.exists(requested_file_path):
#             return send_from_directory(app.static_folder, path)
#         else:
#             index_path = os.path.join(app.static_folder, 'index.html')
#             if os.path.exists(index_path):
#                 return send_from_directory(app.static_folder, 'index.html')
#             else:
#                 return "index.html not found in static folder.", 404

#     return app

# app = create_app()

# @app.cli.command("seed-data")
# def seed_data_command():
#     """Load sample data into the database."""
#     with app.app_context():
#         # Clear existing data to prevent duplicates
#         print("Clearing existing data...")
#         db.session.query(Product).delete()
#         db.session.query(BlogPost).delete()
#         db.session.query(Wishlist).delete()
#         db.session.query(User).delete()
#         db.session.commit()
#         print("Data cleared.")

#         print("Loading data from seed_data.py...")
#         seed_products()
#         seed_blog_posts()
#         print("Data loaded successfully.")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000, debug=True)
import os
import sys

# This is for path setup. Don't change this.
# sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from flask import Flask, send_from_directory
from flask_cors import CORS
from flask_migrate import Migrate
from src.routes.user import user_bp
from src.routes.product import product_bp
from src.routes.blog import blog_bp
from src.routes.seo import seo_bp
from src.routes.wishlist import wishlist_bp
from src.routes.subscription import subscription_bp
from src.routes.search import search_bp
from src.models import db
from src.models.product import Product
from src.models.blog_post import BlogPost
from src.models.user import User
from src.models.wishlist import Wishlist
from src.seed_data.seed_products import seed_products
from src.seed_data.seed_blog_posts import seed_blog_posts

# Initialize Flask-Migrate outside the function
migrate = Migrate()

def create_app():
    # app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))
    # The static folder is now the 'static' directory inside the 'src' folder
    app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'), static_url_path='/')
    
    # Use environment variables for sensitive information
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your_default_secret_key')
    
    # Enable CORS
    CORS(app, supports_credentials=True)
    
    # Use environment variable for database URI
    database_path = os.path.join(os.path.dirname(__file__), 'database', 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', f"sqlite:///{database_path}")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register your blueprints
    app.register_blueprint(user_bp, url_prefix='/api')
    app.register_blueprint(product_bp, url_prefix='/api')
    app.register_blueprint(blog_bp, url_prefix='/api')
    app.register_blueprint(seo_bp)
    app.register_blueprint(wishlist_bp, url_prefix='/api')
    app.register_blueprint(subscription_bp)
    app.register_blueprint(search_bp)
    
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve_react_app(path):
        requested_file_path = os.path.join(app.static_folder, path)
        if path != "" and os.path.exists(requested_file_path):
            return send_from_directory(app.static_folder, path)
        else:
            index_path = os.path.join(app.static_folder, 'index.html')
            if os.path.exists(index_path):
                return send_from_directory(app.static_folder, 'index.html')
            else:
                return "index.html not found in static folder.", 404

    return app

app = create_app()

@app.cli.command("seed-data")
def seed_data_command():
    """Load sample data into the database."""
    with app.app_context():
        # Clear existing data to prevent duplicates
        print("Clearing existing data...")
        db.session.query(Product).delete()
        db.session.query(BlogPost).delete()
        db.session.query(Wishlist).delete()
        db.session.query(User).delete()
        db.session.commit()
        print("Data cleared.")

        print("Loading data from seed_data.py...")
        # Note: You can add seeding logic for users and wishlists here if you create the seed functions.
        seed_products()
        seed_blog_posts()
        print("Data loaded successfully.")

if __name__ == '__main__':
    # Use environment variables for host and port
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host=host, port=port, debug=debug_mode)