"""Script to Run the Real-Time Glassdoor Project.
This script initializes and runs the Flask application for the Real-Time Glassdoor project. 
It serves as the main entry point for the project, allowing access to various routes and functionalities.
"""

from flask import Flask
from api.search import search_app
# from model.preprocessing import preprocessing_app
from database.models import app_db, configure_db



app = Flask(__name__)

# Register blueprints
app.register_blueprint(search_app)
# app.register_blueprint(preprocessing_app)
app.register_blueprint(app_db)

# Configure SQLAlchemy
configure_db(app)


if __name__ == "__main__":
    """Create a simple web server that returns the data from Glassdoor API."""
    app.run(host="0.0.0.0", port=5000, debug=True)
