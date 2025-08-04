from flask import Blueprint, jsonify, request
from src.models.product import Product, db

product_bp = Blueprint('product', __name__)

@product_bp.route('/products', methods=['GET'])
def get_products():
    """Get all active products with optional filtering"""
    category = request.args.get('category')
    subcategory = request.args.get('subcategory')
    featured = request.args.get('featured')
    limit = request.args.get('limit', type=int)
    
    query = Product.query.filter_by(is_active=True)
    
    if category:
        query = query.filter_by(category=category)
    if subcategory:
        query = query.filter_by(subcategory=subcategory)
    if featured:
        query = query.filter_by(is_featured=True)
    
    if limit:
        query = query.limit(limit)
    
    products = query.all()
    return jsonify([product.to_dict() for product in products])

@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """Get a specific product by ID"""
    product = Product.query.get_or_404(product_id)
    return jsonify(product.to_dict())

@product_bp.route('/products', methods=['POST'])
def create_product():
    """Create a new product"""
    data = request.json
    product = Product(
        name=data['name'],
        brand=data['brand'],
        category=data['category'],
        subcategory=data.get('subcategory'),
        description=data['description'],
        price=data['price'],
        amazon_url=data['amazon_url'],
        image_url=data.get('image_url'),
        rating=data.get('rating'),
        review_count=data.get('review_count'),
        ingredients=data.get('ingredients'),
        benefits=data.get('benefits'),
        usage_instructions=data.get('usage_instructions'),
        is_featured=data.get('is_featured', False)
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(product.to_dict()), 201

@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    """Update a product"""
    product = Product.query.get_or_404(product_id)
    data = request.json
    
    for key, value in data.items():
        if hasattr(product, key):
            setattr(product, key, value)
    
    db.session.commit()
    return jsonify(product.to_dict())

@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    """Delete a product (soft delete by setting is_active to False)"""
    product = Product.query.get_or_404(product_id)
    product.is_active = False
    db.session.commit()
    return '', 204

@product_bp.route('/products/categories', methods=['GET'])
def get_categories():
    """Get all unique categories"""
    categories = db.session.query(Product.category).distinct().all()
    return jsonify([cat[0] for cat in categories])

@product_bp.route('/products/search', methods=['GET'])
def search_products():
    """Search products by name or brand"""
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    products = Product.query.filter(
        db.or_(
            Product.name.contains(query),
            Product.brand.contains(query)
        ),
        Product.is_active == True
    ).all()
    
    return jsonify([product.to_dict() for product in products])
