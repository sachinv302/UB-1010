import pickle
import os

# Load trained ML model
model_path = os.path.join("models", "urgency_model.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)


def calculate_priority(description, category, location):

    # Predict urgency using ML model
    urgency = model.predict([description])[0]

    urgency_scores = {
        "Critical": 10,
        "High": 8,
        "Medium": 5,
        "Low": 2
    }

    category_weights = {
        "Electricity": 9,
        "Water": 7,
        "Road": 6,
        "Garbage": 4,
        "Drainage": 6,
        "Street Light": 5,
        "Public Safety": 10,
        "Traffic": 7,
        "Infrastructure": 6
    }

    urgency_score = urgency_scores.get(urgency, 2)
    category_weight = category_weights.get(category, 5)

    # SMART LOCATION DETECTION
    location = location.lower()

    if "hospital" in location:
        location_weight = 4
    elif "school" in location:
        location_weight = 3
    elif "market" in location:
        location_weight = 3
    elif "bus stand" in location:
        location_weight = 3
    elif "railway" in location:
        location_weight = 4
    elif "highway" in location:
        location_weight = 4
    elif "industrial" in location:
        location_weight = 3
    else:
        location_weight = 1

    priority_score = (
        urgency_score * 0.6 +
        category_weight * 0.3 +
        location_weight * 0.1
    )

    return urgency, round(priority_score, 2)