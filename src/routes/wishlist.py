from flask import Blueprint, jsonify, request, session
from src.models.wishlist import Wishlist
from src.models.product import Product
from src.models.user import db
import uuid

wishlist_bp = Blueprint('wishlist', __name__)

def get_session_id():
    """Get or create a session ID for anonymous users"""
    if 'session_id' not in session:
        session['session_id'] = str(uuid.uuid4())
    return session['session_id']

@wishlist_bp.route('/wishlist', methods=['GET'])
def get_wishlist():
    """Get all items in user's wishlist"""
    try:
        session_id = get_session_id()
        wishlist_items = Wishlist.get_wishlist(session_id)
        
        return jsonify({
            'items': [item.to_dict() for item in wishlist_items],
            'count': len(wishlist_items)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@wishlist_bp.route('/wishlist/add', methods=['POST'])
def add_to_wishlist():
    """Add a product to wishlist"""
    try:
        data = request.json
        product_id = data.get('product_id')
        
        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400
        
        # Check if product exists
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        session_id = get_session_id()
        wishlist_item = Wishlist.add_to_wishlist(session_id, product_id)
        
        return jsonify({
            'message': 'Product added to wishlist',
            'item': wishlist_item.to_dict(),
            'count': Wishlist.get_wishlist_count(session_id)
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@wishlist_bp.route('/wishlist/remove', methods=['POST'])
def remove_from_wishlist():
    """Remove a product from wishlist"""
    try:
        data = request.json
        product_id = data.get('product_id')
        
        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400
        
        session_id = get_session_id()
        removed = Wishlist.remove_from_wishlist(session_id, product_id)
        
        if removed:
            return jsonify({
                'message': 'Product removed from wishlist',
                'count': Wishlist.get_wishlist_count(session_id)
            })
        else:
            return jsonify({'error': 'Product not found in wishlist'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@wishlist_bp.route('/wishlist/toggle', methods=['POST'])
def toggle_wishlist():
    """Toggle a product in/out of wishlist"""
    try:
        data = request.json
        product_id = data.get('product_id')
        
        if not product_id:
            return jsonify({'error': 'Product ID is required'}), 400
        
        # Check if product exists
        product = Product.query.get(product_id)
        if not product:
            return jsonify({'error': 'Product not found'}), 404
        
        session_id = get_session_id()
        
        # Check if already in wishlist
        if Wishlist.is_in_wishlist(session_id, product_id):
            # Remove from wishlist
            Wishlist.remove_from_wishlist(session_id, product_id)
            in_wishlist = False
            message = 'Product removed from wishlist'
        else:
            # Add to wishlist
            Wishlist.add_to_wishlist(session_id, product_id)
            in_wishlist = True
            message = 'Product added to wishlist'
        
        return jsonify({
            'message': message,
            'in_wishlist': in_wishlist,
            'count': Wishlist.get_wishlist_count(session_id)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@wishlist_bp.route('/wishlist/check/<int:product_id>', methods=['GET'])
def check_wishlist_status(product_id):
    """Check if a product is in wishlist"""
    try:
        session_id = get_session_id()
        in_wishlist = Wishlist.is_in_wishlist(session_id, product_id)
        
        return jsonify({
            'product_id': product_id,
            'in_wishlist': in_wishlist,
            'count': Wishlist.get_wishlist_count(session_id)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@wishlist_bp.route('/wishlist/count', methods=['GET'])
def get_wishlist_count():
    """Get count of items in wishlist"""
    try:
        session_id = get_session_id()
        count = Wishlist.get_wishlist_count(session_id)
        
        return jsonify({'count': count})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@wishlist_bp.route('/wishlist/clear', methods=['POST'])
def clear_wishlist():
    """Clear all items from wishlist"""
    try:
        session_id = get_session_id()
        
        # Delete all wishlist items for this session
        Wishlist.query.filter_by(session_id=session_id).delete()
        db.session.commit()
        
        return jsonify({
            'message': 'Wishlist cleared',
            'count': 0
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500