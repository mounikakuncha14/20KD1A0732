from flask import Flask, jsonify
import requests
import datetime
import time
app = Flask(__name__)
AUTH_TOKEN = "your_auth_token"
API_BASE_URL = "https://api.johndoerailways.com"
current_timestamp = int(time.time())
twelve_hours_later = current_timestamp + 12 * 3600

def get_train_data():
    url = f"{API_BASE_URL}/trains"
    headers = {"Authorization": f"Bearer {AUTH_TOKEN}"}
    params = {
        "start_timestamp": current_timestamp,
        "end_timestamp": twelve_hours_later
    }
    
    response = requests.get(url, headers=headers, params=params)
    train_data = response.json()
    return train_data
def sort_trains(trains):
    sorted_trains = sorted(
        trains,
        key=lambda train: (
            train['price'],
            -train['seats_available'],
            -train['departure_time']
        )
    )
    return sorted_trains
@app.route("/get_train_schedule", methods=["GET"])
def get_train_schedule():
    train_data = get_train_data()
    sorted_trains = sort_trains(train_data)
    return jsonify(sorted_trains)

if __name__ == "__main__":
    app.run(debug=True)
