"""Script to Run the Real-Time Glassdoor Project.
This script initializes and runs the Flask application for the Real-Time Glassdoor project. 
It serves as the main entry point for the project, allowing access to various routes and functionalities.
"""

from flask import Flask
from server.server import server_app
from model.preprocessing import preprocessing_app

app = Flask(__name__)

# Register blueprints
app.register_blueprint(server_app)
app.register_blueprint(preprocessing_app)


if __name__ == "__main__":
    """Create a simple web server that returns the data from Glassdoor API."""
    app.run(host="0.0.0.0", port=5000, debug=True)
