#!/usr/bin/python3
from flask import Flask, request, jsonify, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token, jwt_required, JWTManager, get_jwt_identity, get_jwt
import os

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "secret"
jwt = JWTManager(app)
basic_auth = HTTPBasicAuth()

users = {
    "user1": {
        "username": "user1", "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1", "password": generate_password_hash("password"),
        "role": "admin"
        }
}

@basic_auth.verify_password
def verify_password(username, password):
    user_data = users.get(username)
    if user_data and check_password_hash(user_data["password"], password):
        return username
    return None

@jwt.unauthorized_loader
def handle_unauthorized_error(callback):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(callback):
    return jsonify({"error": "Signature verification failed"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(callback):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(callback):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(callback):
    return jsonify({"error": "Fresh token required"}), 401

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
    'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
@basic_auth.login_required
def basic_protected():
    return "Hello, {}!".format(basic_auth.current_user())

@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username, additional_claims={"role": user["role"]})
    return jsonify(access_token=access_token)

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    current_user_claims = get_jwt()
    if current_user_claims["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == '__main__':
    app.run()
