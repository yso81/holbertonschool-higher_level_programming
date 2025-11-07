#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

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
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/data/users', methods=['POST'])
def add_user():
    new_user = request.json

    if new_user and 'username' in new_user and new_user['username'] not in users:

        username = new_user['username']
        user_details = {k: v for k, v in new_user.items() if k != 'username'}
        users[username] = user_details
        return jsonify({"message": "User added successfully", "user": new_user}), 201

    elif new_user and 'username' in new_user and new_user['username'] in users:
        return jsonify({"error": "User with this username already exists"}), 409
        
    else:
        return jsonify({"error": "Invalid user data"}), 400



if __name__ == '__main__':
    app.run(debug=True)
