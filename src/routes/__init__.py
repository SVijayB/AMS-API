from flask import Blueprint
from src.routes.login import login
from src.routes.assignments import assignment

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(login.login_bp)
api_blueprint.register_blueprint(assignment.assign_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    content = """
    <h1>ASM-API</h1>
    <h2>/api/auth:</h2>
    <p>
        <ul>
            <li><b>/api/auth/login</b>: POST Login details.</li>
            <li><b>/api/auth/signup: POST New credentials to be stored in DB</li>
            <li><b>/api/auth/prof-signup</b>: POST request: Upload CSV File to add professors</li>
        </ul>
    </p>
    <h2>/api/assignment:</h2>
    <p>
        <ul>
            <li><b>/api/assignment</b>: POST username and GET all assignments </li>
            <li><b>/api/assignment/<int:assignmentID>: POST assignment ID to get details on specific assignment</li>
        </ul>
    </p>
    """
    return content
