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
    <h2>/api/assign:</h2>
    <p>
        <ul>
            <li><b>/api/assign/course</b>: POST username and GET all assignments </li>
            <li><b>/api/assign/create_assignment: POST courseID with form to create new assignments</li>
            <li><b>/api/assign/file_upload: POST form-data to save assignment file on the server</li>
            <li><b>/api/assign/get-pdf/<fileID>: GET request to obtain the file saved on the server.</li>
        </ul>
    </p>
    """
    return content
