import datetime
from geopy.distance import geodesic
from services.recommendation import get_recommendation_with_live_data

def generate_itinerary(user_id, start_location, days=3):
    """
    Generates an AI-powered itinerary based on user preferences and geospatial data.
    """
    recommendations = get_recommendation_with_live_data(user_id).split("\n")  # Convert to list
    itinerary = []
    current_location = start_location

    for day in range(1, days + 1):
        daily_plan = {"day": day, "places": []}

        for place in recommendations[:5]:  # Select top 5 recommended places per day
            daily_plan["places"].append(place)
        
        itinerary.append(daily_plan)

    return itinerary
