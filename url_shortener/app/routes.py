from flask import (
    Blueprint, jsonify, request, redirect, url_for, render_template
)
from app.models import ShortURL
from app import db, limiter
from app.utils import validate_url, generate_short_code

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET'])
def index():
    """Serve basic frontend interface"""
    return render_template('index.html')

@bp.route('/shorten', methods=['POST'])
@limiter.limit("10 per minute")  # Rate limiting
def shorten_url():
    """Endpoint for URL shortening"""
    data = request.get_json()
    if not data or 'long_url' not in data:
        return jsonify({'error': 'Missing long_url parameter'}), 400
    
    long_url = data['long_url'].strip()
    if not validate_url(long_url):
        return jsonify({'error': 'Invalid URL format'}), 400
    
    # Check for existing URL
    existing = ShortURL.query.filter_by(long_url=long_url).first()
    if existing:
        return jsonify({
            'short_url': url_for('main.redirect_url', 
                              short_code=existing.short_code, 
                              _external=True)
        })
    
    # Generate new short code
    short_code = generate_short_code(long_url)
    while ShortURL.query.filter_by(short_code=short_code).first():
        short_code = generate_short_code(long_url + str(datetime.now()))
    
    # Save to database
    new_url = ShortURL(long_url=long_url, short_code=short_code)
    db.session.add(new_url)
    db.session.commit()
    
    return jsonify({
        'short_url': url_for('main.redirect_url', 
                           short_code=short_code, 
                           _external=True)
    }), 201

@bp.route('/<short_code>', methods=['GET'])
def redirect_url(short_code):
    """Redirect to original URL using short code"""
    url_entry = ShortURL.query.filter_by(short_code=short_code).first_or_404()
    url_entry.visits += 1
    db.session.commit()
    return redirect(url_entry.long_url, code=302)


# @bp.route('/debug')
# def debug():
#     import os
#     from flask import current_app
#     template_path = os.path.join(current_app.root_path, 'templates')
#     return f"Templates path: {template_path}"

@bp.route('/urls', methods=['GET'])
def list_urls():
    """List all stored URLs"""
    urls = ShortURL.query.all()
    return render_template('urls.html', urls=urls)