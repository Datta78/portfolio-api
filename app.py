# Personal Portfolio API - Dattatray Bhosale
# Strong Backend Project for Recruiters

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# Sample Data
projects = [
    {
        "id": 1,
        "title": "Online Food Ordering System",
        "description": "Full-stack platform with admin panel and real-time tracking",
        "tech": ["PHP", "MySQL", "JavaScript"]
    },
    {
        "id": 2,
        "title": "Expense Manager",
        "description": "Finance tracker with budgeting and reports",
        "tech": ["PHP", "MySQL", "Chart.js"]
    }
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Dattatray Bhosale Portfolio API",
        "status": "running",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

@app.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

@app.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = {
        "id": len(projects) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "tech": data.get("tech")
    }
    projects.append(new_project)
    return jsonify({"message": "Project added", "project": new_project}), 201

if __name__ == '__main__':
    print("Portfolio API running on http://localhost:5000")
    app.run(debug=True)
