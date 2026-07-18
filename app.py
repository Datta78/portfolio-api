# Portfolio API - Dattatray Bhosale
# Strong Backend Project for Recruiters

from flask import Flask, jsonify, request
from models import projects, skills
from routes import routes
from datetime import datetime

app = Flask(__name__)
app.register_blueprint(routes)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Dattatray Bhosale Portfolio API",
        "status": "running",
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "endpoints": {
            "/projects": "GET - List all projects",
            "/skills": "GET - List all skills",
            "/projects": "POST - Add new project"
        }
    })

if __name__ == '__main__':
    print("🚀 Portfolio API running on http://localhost:5000")
    print("Visit http://localhost:5000 in browser")
    app.run(debug=True)
