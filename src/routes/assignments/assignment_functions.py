import json


def get_assignments_init(data):
    given_CourseID = data["CourseID"]
    with open("data/data.json") as json_file:
        complete_data = json.load(json_file)
    if given_CourseID in complete_data["AssignmentData"]:
        return complete_data["AssignmentData"][given_CourseID]
    else:
        return "No Courses"


def create_assignment(data):
    given_CourseID = data["CourseID"]
    with open("data/data.json") as json_file:
        complete_data = json.load(json_file)
    AssigmentID = 1
    try:
        AssigmentID = (
            complete_data["AssignmentData"][given_CourseID][-1]["AssignmentID"] + 1
        )
    except:
        pass
    new_assignment = {
        "AssignmentID": AssigmentID,
        "AssignmentName": data["AssignmentName"],
        "AssignmentDescription": data["AssignmentDescription"],
        "AssignmentDueDate": data["AssignmentDueDate"],
        "AssignmentMaxScore": data["AssignmentMaxScore"],
        "AssignmentCompleted": {},
    }
    if given_CourseID in complete_data["AssignmentData"]:
        complete_data["AssignmentData"][given_CourseID].append(new_assignment)
    else:
        complete_data["AssignmentData"][given_CourseID] = [new_assignment]

    with open("data/data.json", "w") as json_file:
        json.dump(complete_data, json_file, indent=4, separators=(",", ": "))
    return {"status": "true", "message": "Assignment created successfully"}


def after_upload(studentId, courseId, assignmentId):
    with open("data/data.json") as json_file:
        complete_data = json.load(json_file)

    print(assignmentId)
    for assignments in complete_data["AssignmentData"][courseId]:
        if assignments["AssignmentName"] == assignmentId:
            assignments["AssignmentCompleted"][studentId] = "NA"

    with open("data/data.json", "w") as json_file:
        json.dump(complete_data, json_file, indent=4, separators=(",", ": "))
    return "Data updated successfully"
