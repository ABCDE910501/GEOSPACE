import googlemaps
import os

# Load Google Maps API Key
API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")
gmaps = googlemaps.Client(key=API_KEY)

def get_travel_time(origin, destination, mode="driving"):
    """
    Fetches estimated travel time between two locations using Google Maps API.
    """
    directions = gmaps.directions(origin, destination, mode=mode)
    if directions:
        return directions[0]["legs"][0]["duration"]["text"]
    return "Travel time unavailable"

def get_nearby_pois(location, radius=5000, place_type="tourist_attraction"):
    """
    Fetches nearby points of interest (POIs) from Google Maps API.
    """
    places = gmaps.places_nearby(location=location, radius=radius, type=place_type)
    return places.get("results", [])

# Example usage:
if __name__ == "__main__":
    print(get_travel_time("Eiffel Tower, Paris", "Louvre Museum, Paris"))
    print(get_nearby_pois("48.8584,2.2945"))  # Eiffel Tower location
