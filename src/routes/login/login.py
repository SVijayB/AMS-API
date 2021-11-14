from flask import Flask, jsonify, request, Blueprint
from src.routes.login.db_connection import connection

login_bp = Blueprint("logins", __name__, url_prefix="/login")


@login_bp.route("/", methods=["GET"])
def get_data():
    data = connection()
    return jsonify(data)


@login_bp.route("/<int:id>", methods=["GET"])
def get_id(id):
    data = connection()
    temp = 0
    for login in data:
        if login["id"] == id:
            temp = 1
            break
        else:
            temp = 0
    if temp == 1:
        login = jsonify(login)
        return login
    else:
        return "ERROR 404: CANNOT GET {}".format(request.path)
