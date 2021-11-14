from flask import Blueprint
from src.routes.events import event
from src.routes.assignments import eb

api_blueprint = Blueprint("API", __name__, url_prefix="/api/")
api_blueprint.register_blueprint(event.event_bp)
api_blueprint.register_blueprint(eb.eb_bp)


@api_blueprint.route("/", methods=["GET"])
def get_data():
    content = """
    <h1>ASM-API</h1>
    <h2>/api/login:</h2>
    <p>
        <ul>
            <li><b>/api/login/</b>: POST Login details and GET JSONIFIED data </li>
            <li><b>/api/login/create: POST New credentials to be stored in DB</li>
            <li><b>/api/login/update</b>: POST update current data</li>
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