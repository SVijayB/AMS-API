import json


def get_assignments_init(data):
    given_CourseID = data["CourseID"]
    with open("data/data.json") as json_file:
        complete_data = json.load(json_file)
    result = {}
    if given_CourseID in complete_data["AssignmentData"]:
        result["CourseID"] = complete_data["AssignmentData"][given_CourseID]
    else:
        result["status"] = "false"
        result["message"] = "No assignments found for this course"
    return result
