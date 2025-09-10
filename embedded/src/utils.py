import json
import datetime

def log(message):
    """Print log with timestamp."""
    print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")

def to_json(data):
    """Convert Python dict to JSON string."""
    return json.dumps(data)

def from_json(data):
    """Convert JSON string to Python dict."""
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        log("Invalid JSON received")
        return {}
