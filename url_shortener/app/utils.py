import re
import string
import hashlib
from urllib.parse import urlparse

def validate_url(url):
    """Validate URL format and scheme"""
    pattern = re.compile(
        r'^(https?://)'  # http:// or https://
        r'([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}'  # Domain
        r'(:[0-9]+)?'  # Port
        r'(/[^\s]*)?$'  # Path
    )
    return pattern.match(url) is not None

def generate_short_code(url, length=6):
    """Generate unique short code using hash and base62 encoding"""
    # Create hash digest
    sha256 = hashlib.sha256(url.encode()).hexdigest()
    
    # Convert to base62
    chars = string.digits + string.ascii_letters
    base = len(chars)
    hash_int = int(sha256[:8], 16)
    
    code = []
    for _ in range(length):
        hash_int, rem = divmod(hash_int, base)
        code.append(chars[rem])
    
    return ''.join(code)