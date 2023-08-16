from flask import Flask, request, jsonify
import requests

app = Flask('app.run()')

BASE_URL = "http://20.244.56.144/train"

@app.route('/register', methods=['POST'])
def register_company():
    data = {
        "companyName": "Train Central",
        "ownerName": "Ram",
        "rollNo": "1",
        "ownerEmail": "ram@abc.edu",
        "accessCode": "FKDLig"
    }
    response = requests.post(f"{http://127.0.0.1:5000}/register", json=data)
    
    if response.status_code == 200:
        return "Company registered successfully!"
    else:
        return "Company registration failed."
