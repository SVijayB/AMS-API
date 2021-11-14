import json


def login_validate(givenUsername, givePassword):
    """
    This function is used to validate the user credentials
    """
    with open("data/data.json") as json_file:
        data = json.load(json_file)

    result = {
        "status": "false",
        "message": "Login Failed",
        "type": "",
        "ID": "",
        "name": "",
        "username": "",
    }

    for student in data["StudentData"]:
        if (
            student["StudentUserName"] == givenUsername
            and student["StudentPassword"] == givePassword
        ):
            result["status"] = "true"
            result["message"] = "Login Successful"
            result["type"] = "student"
            result["ID"] = student["StudentID"]
            result["name"] = student["StudentName"]
            result["username"] = student["StudentUserName"]

    for prof in data["ProfData"]:
        if (
            prof["ProfUserName"] == givenUsername
            and prof["ProfPassword"] == givePassword
        ):
            result["status"] = "true"
            result["message"] = "Login Successful"
            result["type"] = "prof"
            result["ID"] = prof["ProfID"]
            result["name"] = prof["ProfName"]
            result["username"] = prof["ProfUserName"]

    return result
