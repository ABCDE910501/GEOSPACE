from flask import Blueprint, request, jsonify
from services.auth import authenticate_user, register_user
from utils.auth import generate_jwt

user_bp = Blueprint('user', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    """Registers a new user."""
    try:
        data = request.get_json()
        if not data or "email" not in data or "password" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        user = register_user(data)  # Calls service function

        if not user:  # If user creation fails
            return jsonify({"error": "User already exists or registration failed"}), 400

        return jsonify({"message": "User registered successfully", "user_id": user.id}), 201

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500

@user_bp.route('/login', methods=['POST'])
def login():
    """Authenticates a user and returns a JWT token."""
    try:
        data = request.get_json()
        if not data or "email" not in data or "password" not in data:
            return jsonify({"error": "Missing required fields"}), 400

        user = authenticate_user(data['email'], data['password'])  # Calls service function

        if not user:
            return jsonify({"error": "Invalid email or password"}), 401

        token = generate_jwt(user.id)  # Generate JWT token
        return jsonify({"token": token}), 200

    except Exception as e:
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
