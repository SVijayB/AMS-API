from dotenv import load_dotenv
import psycopg2
import os
import json


def connection():
    conn = psycopg2.connect(os.getenv("DATABASE_URL"))
    cursor = conn.cursor()
    query = """SELECT * FROM eventreg_event"""
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()

    result = []

    for row in data:
        result.append(
            {
                "id": row[0],
                "AssignmentName": row[1],
                "AssignmentCaption": row[2],
                "AssignmentDescription": row[3],
                "eventVenue": row[4],
                "AssignmentDate": row[5],
                "AssignmentStartTime": row[6],
                "AssignmentEndTime": row[7],
                "AssignmentRegEndDate": row[8],
                "AssignmentRegEndTime": row[9],
                "AssignmentSpeaker": row[10],
                "AssignmentURL": row[11],
                "AssignmentDocumentation": row[12],
            }
        )

    result.sort(key=lambda x: x["id"])
    json_data = json.dumps(result, indent=4, default=str)
    return json.loads(json_data)
