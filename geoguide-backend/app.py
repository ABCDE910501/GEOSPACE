from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from routes import all_blueprints  # Import all blueprints from __init__.py

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enables CORS for frontend-backend communication
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')

# Register all routes dynamically
for bp in all_blueprints:
    app.register_blueprint(bp, url_prefix=f'/api/{bp.name}')

# Error Handling
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(error):
    return jsonify({"error": "Internal Server Error"}), 500

if __name__ == '__main__':
    app.run(debug=True)
