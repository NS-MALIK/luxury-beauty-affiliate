from flask import Blueprint, jsonify, request, Response
from src.models.product import Product
from src.models.blog_post import BlogPost
from datetime import datetime
import xml.etree.ElementTree as ET

seo_bp = Blueprint('seo', __name__)

@seo_bp.route('/sitemap.xml', methods=['GET'])
def generate_sitemap():
    """Generate XML sitemap for SEO"""
    # Create root element
    urlset = ET.Element('urlset')
    urlset.set('xmlns', 'http://www.sitemaps.org/schemas/sitemap/0.9')
    
    # Add homepage
    url = ET.SubElement(urlset, 'url')
    ET.SubElement(url, 'loc').text = request.url_root
    ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
    ET.SubElement(url, 'changefreq').text = 'daily'
    ET.SubElement(url, 'priority').text = '1.0'
    
    # Add product pages
    products = Product.query.filter_by(is_active=True).all()
    for product in products:
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = f"{request.url_root}products/{product.id}"
        ET.SubElement(url, 'lastmod').text = product.updated_at.strftime('%Y-%m-%d') if product.updated_at else datetime.now().strftime('%Y-%m-%d')
        ET.SubElement(url, 'changefreq').text = 'weekly'
        ET.SubElement(url, 'priority').text = '0.8'
    
    # Add blog posts
    blog_posts = BlogPost.query.filter_by(is_published=True).all()
    for post in blog_posts:
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = f"{request.url_root}blog/{post.slug}"
        ET.SubElement(url, 'lastmod').text = post.updated_at.strftime('%Y-%m-%d') if post.updated_at else datetime.now().strftime('%Y-%m-%d')
        ET.SubElement(url, 'changefreq').text = 'monthly'
        ET.SubElement(url, 'priority').text = '0.6'
    
    # Add category pages
    categories = ['skincare', 'makeup', 'fragrance']
    for category in categories:
        url = ET.SubElement(urlset, 'url')
        ET.SubElement(url, 'loc').text = f"{request.url_root}category/{category}"
        ET.SubElement(url, 'lastmod').text = datetime.now().strftime('%Y-%m-%d')
        ET.SubElement(url, 'changefreq').text = 'weekly'
        ET.SubElement(url, 'priority').text = '0.7'
    
    # Convert to string
    xml_str = ET.tostring(urlset, encoding='unicode')
    
    return Response(xml_str, mimetype='application/xml')

@seo_bp.route('/robots.txt', methods=['GET'])
def robots_txt():
    """Generate robots.txt for SEO"""
    robots_content = f"""User-agent: *
Allow: /

Sitemap: {request.url_root}sitemap.xml
"""
    return Response(robots_content, mimetype='text/plain')

@seo_bp.route('/api/seo/meta/<path:page_path>', methods=['GET'])
def get_page_meta(page_path):
    """Get SEO metadata for a specific page"""
    meta_data = {
        'title': 'Luxury Beauty Hub - Premium Beauty Products',
        'description': 'Discover the finest luxury beauty products, from premium skincare to high-end makeup and exquisite fragrances.',
        'keywords': 'luxury beauty, premium skincare, high-end makeup, luxury fragrances, beauty products',
        'og_title': 'Luxury Beauty Hub - Premium Beauty Products',
        'og_description': 'Discover the finest luxury beauty products, from premium skincare to high-end makeup and exquisite fragrances.',
        'og_image': '/images/luxury-beauty-og.jpg',
        'canonical_url': f"{request.url_root}{page_path}"
    }
    
    # Customize meta data based on page path
    if page_path.startswith('products/'):
        try:
            product_id = int(page_path.split('/')[-1])
            product = Product.query.get(product_id)
            if product:
                meta_data.update({
                    'title': f"{product.name} by {product.brand} - Luxury Beauty Hub",
                    'description': f"{product.description[:150]}...",
                    'keywords': f"{product.brand}, {product.name}, {product.category}, luxury beauty",
                    'og_title': f"{product.name} by {product.brand}",
                    'og_description': f"{product.description[:150]}...",
                    'og_image': product.image_url or '/images/luxury-beauty-og.jpg'
                })
        except (ValueError, IndexError):
            pass
    
    elif page_path.startswith('blog/'):
        slug = page_path.split('/')[-1]
        post = BlogPost.query.filter_by(slug=slug, is_published=True).first()
        if post:
            meta_data.update({
                'title': post.meta_title or f"{post.title} - Luxury Beauty Hub",
                'description': post.meta_description or post.excerpt or f"{post.content[:150]}...",
                'keywords': f"{post.tags}, luxury beauty, beauty guide" if post.tags else "luxury beauty, beauty guide",
                'og_title': post.title,
                'og_description': post.excerpt or f"{post.content[:150]}...",
                'og_image': post.featured_image or '/images/luxury-beauty-og.jpg'
            })
    
    elif page_path.startswith('category/'):
        category = page_path.split('/')[-1]
        category_titles = {
            'skincare': 'Luxury Skincare Products',
            'makeup': 'Premium Makeup Collection',
            'fragrance': 'Exquisite Fragrances'
        }
        if category in category_titles:
            meta_data.update({
                'title': f"{category_titles[category]} - Luxury Beauty Hub",
                'description': f"Explore our curated collection of {category_titles[category].lower()} from the world's most prestigious brands.",
                'keywords': f"luxury {category}, premium {category}, high-end {category}",
                'og_title': category_titles[category],
                'og_description': f"Explore our curated collection of {category_titles[category].lower()} from the world's most prestigious brands."
            })
    
    return jsonify(meta_data)