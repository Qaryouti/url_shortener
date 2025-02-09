from datetime import datetime
from app import db

class ShortURL(db.Model):
    """Stores URL mappings with generated short codes"""
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(2048), nullable=False)
    short_code = db.Column(db.String(16), unique=True, index=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    visits = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<ShortURL {self.short_code} -> {self.long_url}>'