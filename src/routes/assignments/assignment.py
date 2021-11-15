from dotenv.main import load_dotenv
from flask import Flask, jsonify, request, Blueprint, current_app, redirect, url_for
from werkzeug.utils import secure_filename
from src.routes.assignments.assignment_functions import *
import os

assign_bp = Blueprint("assignments", __name__, url_prefix="/assign")
load_dotenv()


@assign_bp.route("/course", methods=["GET", "POST"])
def getAssignments():
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2>Invalid Key, To obtain access to the key contact Project Lead.</h2>"
        data = request.get_json()
        result = get_assignments_init(data)
        print(result)
        return jsonify(result)
    if request.method == "GET":
        result = """<h3>POST Json data of CourseID to get assignments created</h3></br>
        <pre>
        JSON Data format:
        {
            "CourseID": "CSE1005"
        }
        </pre>
        """
        return result


@assign_bp.route("/create_assignment", methods=["GET", "POST"])
def createAssignment():
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2>Invalid Key, To obtain access to the key contact Project Lead.</h2>"
        data = request.get_json()
        result = create_assignment(data)
        return result
    if request.method == "GET":
        result = """<h3>POST Json data of CourseID, AssignmentName, AssignmentDescription,
        AssignmentDueDate to create assignment</h3></br>
        <pre>
        JSON Data format example:
        {
            "CourseID": "CSE1005",
            "AssignmentName": "Assignment1",
            "AssignmentDescription": "Assignment1",
            "AssignmentDueDate": "2020-01-01",
            "AssignmentMaxScore": "100"
        }
        </pre>
        """
        return result


@assign_bp.route("/file_upload", methods=["GET", "POST"])
def uploadFile():
    current_app.config["UPLOAD_FOLDER"] = "file_upload"
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2> Invalid Key </h2>"
        file = request.files["file"]
        filename = file.filename
        if filename == "":
            return "<h2> ERROR: File not found. </h2>"
        allowed_file = "." in filename and filename.rsplit(".", 1)[1].lower() in {"pdf"}
        if file and allowed_file:
            folder = current_app.config["UPLOAD_FOLDER"]
            filename = secure_filename(filename)
        try:
            file.save(os.path.join(folder, filename))
            result = {"status": "true", "message": "File uploaded successfully!"}
        except:
            result = {"status": "false", "message": "Please upload a valid file"}
        return result
    if request.method == "GET":
        return """
        <!doctype html>
        <title>Upload new File</title>
        <h1>Upload new File</h1>
        <form method=post enctype=multipart/form-data>
        <input type=file name=file>
        <input type=submit value=Upload>
        </form>
        """
