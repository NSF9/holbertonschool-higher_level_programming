#!/usr/bin/env python3
from flask import Flask, jsonify, request

App = Flask(__name__)

users = {}

@App.route("/")
def home():
    return jsonify({"message": "Welcome to the Flask API"})

@App.route("/data")
def get_username():
    return jsonify(list(users.keys()))

@App.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

@App.route("/status")
def status():
    return "OK"

@App.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict) or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201

if __name__ == "__main__":
    App.run()
