@app.route('/trains', methods=['GET'])
def get_train_schedules():
    response = requests.get(f"{http://127.0.0.1:5000}/all-trains")
    train_data = response.json()

    # Process train_data to filter and sort as needed
    # ...

    return jsonify(sorted_train_data)
