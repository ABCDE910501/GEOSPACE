import json
import ollama
import googlemaps
import os
from database.connection import get_db_connection

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize Google Maps API
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

def get_user_preferences(user_id):
    """Fetch user preferences and visited places from PostgreSQL."""
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "SELECT preferences, visited_places FROM users WHERE user_id = %s;"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    if result:
        preferences, visited_places = result
        return json.loads(preferences), json.loads(visited_places)
    return None, None

def get_recommendation(user_id):
    """Generate personalized travel recommendations using Ollama."""
    preferences, visited_places = get_user_preferences(user_id)

    if not preferences:
        return "No preferences found. Please update your profile."

    user_prompt = f"""The user enjoys {', '.join(preferences)} 
    and has already visited {', '.join(visited_places)}.
    Suggest 3 new travel destinations that match their interests."""

    response = ollama.chat(model="llama2", messages=[{"role": "user", "content": user_prompt}])
    return response['message']['content']

def get_live_poi_info(place_name):
    """Fetch live data like popularity and ratings for a recommended place."""
    result = gmaps.places(query=place_name)

    if result and "results" in result and len(result["results"]) > 0:
        place = result["results"][0]
        return {
            "name": place["name"],
            "rating": place.get("rating", "No rating"),
            "address": place.get("formatted_address", "Address not found")
        }
    return None

def get_recommendation_with_live_data(user_id):
    """Generate recommendations and enhance them with Google Maps data."""
    recommendations = get_recommendation(user_id).split("\n")  # Get list of places
    enhanced_recommendations = []

    for place in recommendations:
        place_info = get_live_poi_info(place)
        if place_info:
            enhanced_recommendations.append(
                f"{place_info['name']} - Rating: {place_info['rating']}, Address: {place_info['address']}"
            )
        else:
            enhanced_recommendations.append(place)

    return "\n".join(enhanced_recommendations)
