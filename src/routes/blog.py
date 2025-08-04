from flask import Blueprint, jsonify, request
from src.models.blog_post import BlogPost, db
from datetime import datetime

blog_bp = Blueprint('blog', __name__)

@blog_bp.route('/blog/posts', methods=['GET'])
def get_blog_posts():
    """Get all published blog posts with optional filtering"""
    category = request.args.get('category')
    limit = request.args.get('limit', type=int)
    
    query = BlogPost.query.filter_by(is_published=True)
    
    if category:
        query = query.filter_by(category=category)
    
    query = query.order_by(BlogPost.published_at.desc())
    
    if limit:
        query = query.limit(limit)
    
    posts = query.all()
    return jsonify([post.to_dict() for post in posts])

@blog_bp.route('/blog/posts/<slug>', methods=['GET'])
def get_blog_post_by_slug(slug):
    """Get a specific blog post by slug"""
    post = BlogPost.query.filter_by(slug=slug, is_published=True).first_or_404()
    return jsonify(post.to_dict())

@blog_bp.route('/blog/posts/<int:post_id>', methods=['GET'])
def get_blog_post(post_id):
    """Get a specific blog post by ID"""
    post = BlogPost.query.get_or_404(post_id)
    return jsonify(post.to_dict())

@blog_bp.route('/blog/posts', methods=['POST'])
def create_blog_post():
    """Create a new blog post"""
    data = request.json
    post = BlogPost(
        title=data['title'],
        slug=data['slug'],
        excerpt=data.get('excerpt'),
        content=data['content'],
        meta_title=data.get('meta_title'),
        meta_description=data.get('meta_description'),
        featured_image=data.get('featured_image'),
        category=data['category'],
        tags=','.join(data.get('tags', [])) if data.get('tags') else None,
        is_published=data.get('is_published', False),
        published_at=datetime.now() if data.get('is_published', False) else None
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(post.to_dict()), 201

@blog_bp.route('/blog/posts/<int:post_id>', methods=['PUT'])
def update_blog_post(post_id):
    """Update a blog post"""
    post = BlogPost.query.get_or_404(post_id)
    data = request.json
    
    # Handle tags separately
    if 'tags' in data:
        post.tags = ','.join(data['tags']) if data['tags'] else None
        del data['tags']
    
    # Handle published status
    if 'is_published' in data and data['is_published'] and not post.is_published:
        post.published_at = datetime.now()
    
    for key, value in data.items():
        if hasattr(post, key):
            setattr(post, key, value)
    
    db.session.commit()
    return jsonify(post.to_dict())

@blog_bp.route('/blog/posts/<int:post_id>', methods=['DELETE'])
def delete_blog_post(post_id):
    """Delete a blog post"""
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return '', 204

@blog_bp.route('/blog/categories', methods=['GET'])
def get_blog_categories():
    """Get all unique blog categories"""
    categories = db.session.query(BlogPost.category).distinct().all()
    return jsonify([cat[0] for cat in categories])

@blog_bp.route('/blog/search', methods=['GET'])
def search_blog_posts():
    """Search blog posts by title or content"""
    query = request.args.get('q', '')
    if not query:
        return jsonify([])
    
    posts = BlogPost.query.filter(
        db.or_(
            BlogPost.title.contains(query),
            BlogPost.content.contains(query)
        ),
        BlogPost.is_published == True
    ).order_by(BlogPost.published_at.desc()).all()
    
    return jsonify([post.to_dict() for post in posts])
