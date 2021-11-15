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
        return result
    if request.method == "GET":
        result = """<h3>POST Json data of user-type and CourseID to get assignments created</h3></br>
        <pre>
        JSON Data format:
        {
            "type": "student/prof",
            "UserID": "student/prof ID" <int>,
            "CourseID": "CSE1005"
        }
        </pre>
        """
        return result
