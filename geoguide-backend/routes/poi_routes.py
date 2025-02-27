from flask import Blueprint, request, jsonify
from services.poi_service import get_pois, add_poi

poi_bp = Blueprint('poi', __name__)

@poi_bp.route('/pois', methods=['GET'])
def list_pois():
    """Fetches all POIs from the database."""
    pois = get_pois()
    return jsonify(pois), 200

@poi_bp.route('/pois', methods=['POST'])
def create_poi():
    """Adds a new POI to the database."""
    data = request.get_json()
    if not data or "name" not in data or "location" not in data:
        return jsonify({"error": "Missing required fields"}), 400

    poi = add_poi(data)  # Calls service function
    return jsonify({"message": "POI added successfully", "poi_id": poi.id}), 201
