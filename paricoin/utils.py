import hashlib
import json

def hash(data: dict) -> str:
    """
    Takes a dicstionary and retruns its SHA-256 has string
    """
    raw=json.dumps(data, sort_keys=True).encode()
    return hashlib.sha256(raw).hexdigest()