import json
import csv
import os


class auth_functions:
    def login_validate(givenUsername, givePassword):
        """
        This function is used to validate the user credentials
        """
        result = {
            "status": "false",
            "message": "Login Failed",
            "type": "",
            "id": "",
            "name": "",
            "username": "",
            "CourseID": [],
            "CourseCredits": "",
        }
        with open("data/data.json") as json_file:
            complete_data = json.load(json_file)

        for student in complete_data["StudentData"]:
            if (
                student["StudentUserName"] == givenUsername
                and student["StudentPassword"] == givePassword
            ):
                result = auth_functions.get_data(complete_data, student, result)

        for prof in complete_data["ProfData"]:
            if (
                prof["ProfUserName"] == givenUsername
                and prof["ProfPassword"] == givePassword
            ):
                result = auth_functions.get_data(complete_data, prof, result)
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

        ProfID = len(data["ProfData"]) + 1
        for row in csvReader:
            row["ProfID"] = ProfID
            row.move_to_end("ProfID", last=False)
            data["ProfData"].append(row)
            ProfID += 1

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

    def get_data(data, user, result):
        if "StudentID" in user:
            result["status"] = "true"
            result["message"] = "Login Successful"
            result["type"] = "student"
            result["id"] = user["StudentID"]
            result["name"] = user["StudentName"]
            result["username"] = user["StudentUserName"]
            for course in data["CourseData"]:
                if user["StudentID"] in course["StudentIDList"]:
                    result["CourseID"].append(course["CourseID"])
                    result["CourseCredits"] = course["CourseCredits"]
        else:
            result["status"] = "true"
            result["message"] = "Login Successful"
            result["type"] = "prof"
            result["id"] = user["ProfID"]
            result["name"] = user["ProfName"]
            result["username"] = user["ProfUserName"]
            for course in data["CourseData"]:
                if user["ProfID"] in course["ProfIDList"]:
                    result["CourseID"].append(course["CourseID"])
                    result["CourseCredits"] = course["CourseCredits"]
        return result
