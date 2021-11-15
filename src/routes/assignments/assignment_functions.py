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


def create_assignment(data):
    given_CourseID = data["CourseID"]
    with open("data/data.json") as json_file:
        complete_data = json.load(json_file)
    new_assignment = {}
    if given_CourseID in complete_data["AssignmentData"]:
        new_assignment = {
            "AssignmentID": complete_data["AssignmentData"][given_CourseID][-1][
                "AssignmentID"
            ]
            + 1,
            "AssignmentName": data["AssignmentName"],
            "AssignmentDescription": data["AssignmentDescription"],
            "AssignmentDueDate": data["AssignmentDueDate"],
            "AssignmentMaxScore": data["AssignmentMaxScore"],
            "AssignmentCompleted": {},
        }
        complete_data["AssignmentData"][given_CourseID].append(new_assignment)
    else:
        complete_data["AssignmentData"][given_CourseID] = [new_assignment]

    with open("data/data.json", "w") as json_file:
        json.dump(complete_data, json_file, indent=4, separators=(",", ": "))
    return {"status": "true", "message": "Assignment created successfully"}
