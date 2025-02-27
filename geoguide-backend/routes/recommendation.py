from flask import Blueprint, request, jsonify
from services.recommendation import get_recommendations

recommendation_bp = Blueprint('recommendation', __name__)

@recommendation_bp.route('/recommend', methods=['GET'])
def get_recommendation():
    """Fetches AI-powered travel recommendations for a user."""
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "Missing user_id parameter"}), 400

    recommendations = get_recommendations(user_id)  # Calls service function
    return jsonify(recommendations), 200
