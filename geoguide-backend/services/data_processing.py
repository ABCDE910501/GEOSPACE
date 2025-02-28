import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_user_data(user_data):
    """
    Standardizes user preference data for AI models.
    """
    df = pd.DataFrame(user_data)
    scaler = StandardScaler()
    df_scaled = scaler.fit_transform(df)
    return df_scaled

def clean_poi_data(poi_data):
    """
    Cleans and processes POI data for better recommendations.
    """
    df = pd.DataFrame(poi_data)
    df.dropna(inplace=True)
    df = df[df["rating"] > 3.5]  # Filter top-rated places
    return df.to_dict(orient="records")

# Example usage:
if __name__ == "__main__":
    sample_pois = [
        {"name": "Eiffel Tower", "rating": 4.8, "latitude": 48.8584, "longitude": 2.2945},
        {"name": "Unknown Place", "rating": 3.0, "latitude": 10.0, "longitude": 10.0},
    ]
    print(clean_poi_data(sample_pois))
