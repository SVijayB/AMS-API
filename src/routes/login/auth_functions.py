import json
import csv
import os


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


def validate_signup(name, username, password):
    """
    This function is used to register the user to the network
    """
    with open("data/data.json") as json_file:
        data = json.load(json_file)

    studentID = len(data["StudentData"]) + 1

    for check in data["StudentData"]:
        if check["StudentUserName"] == username:
            return {
                "status": "false",
                "message": "Username already exists",
            }

    obtained_data = {
        "StudentID": studentID,
        "StudentName": name,
        "StudentUserName": username,
        "StudentPassword": password,
    }

    data["StudentData"].append(obtained_data)

    with open("data/data.json", "w") as json_file:
        json.dump(data, json_file, indent=4, separators=(",", ": "))

    result = {"status": "true", "message": "Signup Successful"}
    return result


def validate_prof_signup(csvFile):
    with open(csvFile, encoding="utf-8") as f:
        csvReader = list(csv.DictReader(f))

    with open("data/data.json") as json_file:
        data = json.load(json_file)

    existingProf = []
    for check in data["ProfData"]:
        for row in csvReader:
            if check["ProfUserName"] == row["ProfUserName"]:
                existingProf.append(row["ProfUserName"])
                csvReader.remove(row)

    for row in csvReader:
        data["ProfData"].append(row)

    with open("data/data.json", "w") as json_file:
        json.dump(data, json_file, indent=4, separators=(",", ": "))
    os.remove(csvFile)

    if len(existingProf) > 0:
        return str(
            "<h3>Professors with the following usernames already exist: </h3> \n<pre>"
            + str(existingProf)
            + "</pre> However, rest of the data has been added.",
        )
    else:
        return "<h3>Professors added successfully to the networks</h3>"
