from dotenv.main import load_dotenv
from flask import Flask, jsonify, request, Blueprint
from src.routes.login.db_connection import *
import os

login_bp = Blueprint("logins", __name__, url_prefix="/auth")
load_dotenv()


@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2>Invalid Key</h2>"
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        result = login_validate(username, password)
        return jsonify(result)

    if request.method == "GET":
        result = """<h3>POST Json data of username and password to get validated</h3></br>
        <pre>
        JSON Data format:
        {
            "username": "username",
            "password": "password"
        }
        </pre>
        """
        return result


@login_bp.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2>Invalid Key</h2>"
        data = request.get_json()
        name = data["name"]
        username = data["username"]
        password = data["password"]
        result = validate_signup(name, username, password)
        return jsonify(result)

    if request.method == "GET":
        result = """<h3>POST Json data of name, username and password to register yourself(student) to the network</h3></br>
        <pre>
        JSON Data format:
        {
            "name": "name",
            "username": "username",
            "password": "password"
        }
        </pre>
        """
        return result
