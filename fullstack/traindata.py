# Create a simplified mock train data
mock_train_data = [
    {
        "departure_time": "2023-08-16 10:00:00",
        "price": 50,
        "availability": 10
    },
    {
        "departure_time": "2023-08-16 11:30:00",
        "price": 70,
        "availability": 5
    },
    {
        "departure_time": "2023-08-16 13:15:00",
        "price": 60,
        "availability": 8
    }
]

# ...

@app.route('/trains', methods=['GET'])
def get_train_schedules():
    access_code = request.headers.get('Access-Code')
    if access_code != app.config['ACCESS_CODE']:
        return jsonify({'error': 'Authentication failed'}), 401

    # Simulate fetching data from a mock API
    train_data = mock_train_data  # Replace with actual API response

    # ... rest of the code ...

if __name__ == '__main__':
    app.run(debug=True)
