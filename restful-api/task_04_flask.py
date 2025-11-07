#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {}

@app.route("/")
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

@app.route('/status')
def status():
    return 'OK'

@app.route('/users/<username>')
def get_user_data(username):
    user = users.get(username)
    if user:

        user_with_username = user.copy()
        user_with_username['username'] = username
        return jsonify(user_with_username)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        new_user_data = request.get_json(silent=True)
        if new_user_data is None:
            return jsonify({"error": "Invalid JSON"}), 400

    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    if not isinstance(new_user_data, dict):
        return jsonify({"error": "Invalid user data"}), 400

    if 'username' not in new_user_data:
        return jsonify({"error": "Username is required"}), 400

    username = new_user_data['username']

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user
    user_details = {k: v for k, v in new_user_data.items() if k != 'username'}
    users[username] = user_details
    return jsonify({"message": "User added successfully", "user": new_user_data}), 201



if __name__ == '__main__':
    app.run(debug=True)
