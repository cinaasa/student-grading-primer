from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """
    # TODO: replace with your implementation. This is a mock response
    # return jsonify([
    #     {'course': 'COMP1531', 'id': 1, 'mark': 85, 'name': 'Alice Zhang'},
    #     {'course': 'COMP1531', 'id': 2, 'mark': 72, 'name': 'Bob Smith'}
    # ]), 200

    students = db.get_all_students()
    return jsonify(students), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    # Getting the request body - replace with your implementation
    # student_data = request.json

    student_data = request.json
    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")

    ## Checking for Name + Course
    if not name or not course:
        return jsonify({"error": "Name and Course are mandatory"}), 404
    
    new_student = db.insert_student(name, course, mark)

    return jsonify(new_student), 200



@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """
    student_data = request.json
    name = student_data.get("name")
    course = student_data.get("course")
    mark = student_data.get("mark")

    updated_student = db.update_student(student_id, name, course, mark)

    ## Student Existing Check
    if updated_student is None:
        return jsonify({"error": "Student does not exist!"}), 404

    return jsonify(updated_student), 200

@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Route to delete student by id
    return: The deleted student
    """

    deleted_student = db.delete_student(student_id)

    ## Success Check
    if deleted_student is None:
        return jsonify({"error": "Student not found!"}), 404

    return jsonify(deleted_student), 200


@app.route("/stats")
def get_stats():
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """

    students = db.get_all_students()
    
    # EDGE CASE: Database is empty then return 0
    if not students:
        return jsonify({"count": 0, "average": 0, "min": 0, "max": 0}), 200

    # Get Mark List
    marks = []
    for s in students:
        if s["mark"] is not None:
            marks.append(s["mark"])

    return jsonify({
        "count": len(students), 
        "average": sum(marks) / len(marks),
        "min": min(marks),
        "max": max(marks)
    }), 200


@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
