from flask import Blueprint, request, jsonify
from services.auth import authenticate_user, register_user
from utils.auth import generate_jwt

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    data = request.get_json()
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    user = register_user(data)  # Calls service function
    return jsonify({"message": "User registered successfully", "user_id": user.id}), 201

@user_bp.route('/login', methods=['POST'])
def login():
    """Authenticates a user and returns a JWT token."""
    data = request.get_json()
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    user = authenticate_user(data['email'], data['password'])  # Calls service function
    if user:
        token = generate_jwt(user.id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
