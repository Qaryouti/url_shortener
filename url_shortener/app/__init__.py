from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from app.config import Config

db = SQLAlchemy()
limiter = Limiter(key_func=get_remote_address)

def create_app(config_class=Config):
    app = Flask(__name__,template_folder='../templates')
    app.config.from_object(config_class)

    db.init_app(app)
    limiter.init_app(app)

    with app.app_context():
        from .routes import bp  # Import the blueprint
        app.register_blueprint(bp)  # Register the blueprint
        db.create_all()
        
    return app