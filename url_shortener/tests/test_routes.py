import pytest
from app import create_app, db
from app.models import ShortURL

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.drop_all()

def test_shorten_url(client):
    # Test valid URL
    response = client.post('/shorten', json={
        'long_url': 'https://example.com'
    })
    assert response.status_code == 201
    assert 'short_url' in response.json
    
    # Test duplicate URL
    response = client.post('/shorten', json={
        'long_url': 'https://example.com'
    })
    assert response.status_code == 200
    
    # Test invalid URL
    response = client.post('/shorten', json={
        'long_url': 'invalid-url'
    })
    assert response.status_code == 400

def test_redirect(client):
    # Create test entry
    with client.application.app_context():
        url = ShortURL(
            long_url='https://example.com',
            short_code='test123'
        )
        db.session.add(url)
        db.session.commit()
    
    # Test valid redirect
    response = client.get('/test123')
    assert response.status_code == 302
    
    # Test invalid code
    response = client.get('/invalid')
    assert response.status_code == 404