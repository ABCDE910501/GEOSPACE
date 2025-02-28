import re

def validate_email(email):
    """Validates an email format using regex."""
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email) is not None

def format_response(success=True, message="", data=None):
    """Formats a standard API response."""
    return {
        "success": success,
        "message": message,
        "data": data
    }

def convert_str_to_int(value, default=0):
    """Converts a string to an integer safely, returns default if conversion fails."""
    try:
        return int(value)
    except ValueError:
        return default
