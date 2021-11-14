from flask import request, Blueprint, flash, current_app
from pymongo import results
from werkzeug.utils import secure_filename
from dotenv import load_dotenv
import os
from src.routes.assignments.db_connection import *

load_dotenv()
UPLOAD_FOLDER = "back-end/temp"
ALLOWED_EXTENSIONS = {"csv"}
assignment_bp = Blueprint("eb", __name__, url_prefix="/assignment")


@assignment_bp.route("/", methods=["GET"])
def get_data():
    return "ASSIGNMENT DATA FROM MONGODB"


@assignment_bp.route("/uploadCSV", methods=["GET", "POST"])
def uploadFiles():
    current_app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    if request.method == "POST":
        key = request.args.get("key")
        if key == os.getenv("API_KEY"):
            pass
        else:
            return "<h2> Invalid Key</h2>"
        if "file" not in request.files:
            return "<h2> ERROR: File not found. Please upload a CSV file containing details </h2>"
        file = request.files["file"]
        filename = file.filename
        if filename == "":
            flash("No selected file")
            return "<h2> ERROR: File not found. Please upload a CSV file containing all assignment details </h2>"
        allowed_file = "." in filename and filename.rsplit(".", 1)[1].lower() in {"csv"}
        if file and allowed_file:
            filename = secure_filename(filename)
            file.save(os.path.join(current_app.config["UPLOAD_FOLDER"], filename))
            return "<h2>DATA UPLOADED SUCCESSFULLY</h2>"
        else:
            return (
                "<h2> ERROR: Make sure to upload a CSV file containing EB details </h2>"
            )
    return """
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    """
