from flask import Blueprint, request, jsonify
from src.models.blog_post import  BlogPost,db
from src.models.product import Product, db

search_bp = Blueprint('search', __name__)

@search_bp.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('q', '').lower()
    if not query:
        return jsonify({"products": [], "articles": []})

    # Search for products
    products = Product.query.filter(
        Product.name.ilike(f'%{query}%') |
        Product.description.ilike(f'%{query}%') |
        Product.brand.ilike(f'%{query}%')
    ).limit(5).all()

    # Search for blog posts
    articles = BlogPost.query.filter(
        BlogPost.title.ilike(f'%{query}%') |
        BlogPost.content.ilike(f'%{query}%') |
        BlogPost.tags.ilike(f'%{query}%')
    ).limit(5).all()

    product_results = [{
        "id": p.id, 
        "name": p.name,
        "category": p.category
    } for p in products]

    article_results = [{
        "id": a.id, 
        "title": a.title, 
        "slug": a.slug
    } for a in articles]

    return jsonify({"products": product_results, "articles": article_results})