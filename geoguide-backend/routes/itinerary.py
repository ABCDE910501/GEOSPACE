from flask import Blueprint, request, jsonify
from services.itinerary_planner import generate_itinerary

itinerary_bp = Blueprint('itinerary', __name__)

@itinerary_bp.route('/generate', methods=['POST'])
def create_itinerary():
    """Generates an AI-powered itinerary based on user input."""
    data = request.get_json()
    if not data or "user_id" not in data or "preferences" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    itinerary = generate_itinerary(data)  # Calls service function
    return jsonify(itinerary), 200
