from models.user import User
from werkzeug.security import check_password_hash, generate_password_hash

def register_user(data):
    """Registers a new user with hashed password."""
    email = data.get("email")
    password = data.get("password")

    # Check if user already exists
    if User.get_by_email(email):
        return None  # User already exists
    
    hashed_password = generate_password_hash(password)  # Hash password
    user_data = {"email": email, "password": hashed_password}
    return User.create(user_data)  # Save user to database

def authenticate_user(email, password):
    """Authenticates user by verifying email and password."""
    user = User.get_by_email(email)
    if user and check_password_hash(user.password, password):
        return user  # Valid credentials
    return None  # Invalid credentials
