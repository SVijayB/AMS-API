from dotenv.main import load_dotenv
from flask import Flask, jsonify, request, Blueprint, current_app, redirect, url_for
from werkzeug.utils import secure_filename
from src.routes.login.auth_functions import auth_functions
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
            return "<h2>Invalid Key, To obtain access to the key contact Project Lead.</h2>"
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        result = auth_functions.login_validate(username, password)
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
            return "<h2>Invalid Key, To obtain access to the key contact Project Lead.</h2>"
        data = request.get_json()
        try:
            name = data["name"]
            username = data["username"]
            password = data["password"]
            result = auth_functions.validate_signup(name, username, password)
            return jsonify(result)
        except:
            return redirect(url_for("API.logins.signup"))

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


@login_bp.route("/prof-signup", methods=["GET", "POST"])
def prof_signup():
    current_app.config["UPLOAD_FOLDER"] = "file_upload"
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2> Invalid Key, To obtain access to the key contact Project Lead. </h2>"
        if "file" not in request.files:
            return "<h2> ERROR: File not found. Please upload a CSV file containing details </h2>"
        file = request.files["file"]
        filename = file.filename
        if filename == "":
            return "<h2> ERROR: File not found. Please upload a CSV file containing EB details </h2>"
        allowed_file = "." in filename and filename.rsplit(".", 1)[1].lower() in {"csv"}
        folder = current_app.config["UPLOAD_FOLDER"]
        if file and allowed_file:
            filename = secure_filename(filename)
            file.save(os.path.join(folder, filename))
            try:
                result = auth_functions.validate_prof_signup(f"{folder}/{filename}")
            except:
                return "<h2> ERROR: Make sure to follow exact structure as provided in examples/ebDetails.csv </h2>"
            return result
        else:
            return (
                "<h2> ERROR: Make sure to upload a CSV file containing EB details </h2>"
            )
    if request.method == "GET":
        result = """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload a CSV File containing Professor details</h1>
        <form method=post enctype=multipart/form-data>
            <input type=file name=file>
            <input type=submit value=Upload>
        </form>
        </br>
        ⚠️⚠️ Note: CSV Column names should strictly be limited to:
        ProfName,ProfUserName,ProfPassword ⚠️⚠️
        """
        return result
