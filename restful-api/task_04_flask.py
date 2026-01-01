#!/usr/bin/env python3

from flask import Flask, jsonify, request

# Create the Flask app
App = Flask(__name__)

# Sample user data stored in memory
users = {}

@App.route("/")
def home():
    """
    Home endpoint.
    Returns a welcome message.
    """
    return "Welcome to the Flask API"

@App.route("/data")
def get_username():
    """
    Returns a list of all usernames.
    """
    return jsonify(list(users.keys()))

@App.route("/users/<username>")
def get_user(username):
    """
    Returns full user data for a given username.
    If the user doesn't exist, returns 404 error.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "user not found"}), 404

@App.route("/add_user", methods=["POST"])
def add_user():
    """
    Adds a new user to the dictionary.
    Validates input JSON and handles duplicate or missing usernames.
    """
    try:
        data = request.get_json()
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    if not data or "username" not in data:
        return jsonify({"error": "username is required"}), 400

    username = data["username"]

    if username in users:
        return jsonify({"error": "username already exists"}), 409

    users[username] = data
    return jsonify({"message": "user added", "user": data}), 201

if __name__ == "__main__":
    App.run()
