
print("Starting API")
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#Simple data storage(temporary)
students = []

#GET Endpoints
#Returns all students
@app.route("/students",methods=["GET"])
def get_students():
    return jsonify(students), 200

#POST Endpoint
#Adds a new student
@app.route("/students", methods=["POST"])
def add_students():
    data = request.get_json()
    student = {
        "name": data["name"],
        "age":data["age"],
        "skill":data["skill"]
    }

    students.append(student)

    return jsonify({
        "message":"Student added successfully!",
        "student":student
    }), 201

if __name__ == "__main__":
    app.run(debug=True)
