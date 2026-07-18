# Portfolio API - Dattatray Bhosale

from flask import Flask, jsonify
from datetime import datetime
from models import projects, skills
from routes import routes
from extensions import init_extensions

app = Flask(__name__)
init_extensions(app)
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
    app.run(debug=True)
