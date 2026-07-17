# Routes - Portfolio API

from flask import Blueprint, jsonify, request
from models import projects, skills

routes = Blueprint('routes', __name__)

@routes.route('/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

@routes.route('/skills', methods=['GET'])
def get_skills():
    return jsonify(skills)

@routes.route('/projects', methods=['POST'])
def add_project():
    data = request.get_json()
    new_project = {
        "id": len(projects) + 1,
        "title": data.get("title"),
        "description": data.get("description"),
        "tech": data.get("tech", []),
        "status": "In Progress"
    }
    projects.append(new_project)
    return jsonify({"message": "Project added", "project": new_project}), 201
