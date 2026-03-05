from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

users = {}

@app.route("/")
def home():
    return "Zenith backend running"


@app.route("/register", methods=["POST"])
def register():

    data = request.json

    name = data["name"]
    email = data["email"]
    password = data["password"]

    users[email] = {
        "name": name,
        "password": password
    }

    return jsonify({"status": "registered"})


@app.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data["email"]
    password = data["password"]

    if email in users and users[email]["password"] == password:

        return jsonify({
            "status": "success"
        })

    return jsonify({
        "status": "wrong"})
