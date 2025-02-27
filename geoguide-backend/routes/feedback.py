from flask import Blueprint, request, jsonify
from services.feedback_service import submit_feedback, get_feedback, update_feedback

feedback_bp = Blueprint('feedback', __name__)

@feedback_bp.route('/submit', methods=['POST'])
def submit():
    """Allows users to submit feedback for a POI."""
    data = request.get_json()
    if not data or "user_id" not in data or "poi_id" not in data or "rating" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    response = submit_feedback(data)  # Calls service function
    return jsonify(response), 201

@feedback_bp.route('/get', methods=['GET'])
def get():
    """Fetches feedback for a given POI."""
    poi_id = request.args.get("poi_id")
    if not poi_id:
        return jsonify({"error": "Missing poi_id parameter"}), 400

    feedback = get_feedback(poi_id)  # Calls service function
    return jsonify(feedback), 200

@feedback_bp.route('/update', methods=['PUT'])
def update():
    """Allows users to update their feedback for a POI."""
    data = request.get_json()
    if not data or "feedback_id" not in data or "rating" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    response = update_feedback(data)  # Calls service function
    return jsonify(response), 200
