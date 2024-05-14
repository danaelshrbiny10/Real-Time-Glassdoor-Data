"""
Real-Time Glassdoor Data Fetch and Database Integration Script

This Python script provides functionality to fetch real-time company data from the Glassdoor API and integrates it with a PostgreSQL database. It utilizes Flask for the web framework, SQLAlchemy for database management, and requests for making HTTP requests to the API. The script defines a Flask application with routes to fetch data from the Glassdoor API and save it to the database. The Company model is defined to represent the structure of the data, and the fetch-and-save-data route handles the process of fetching data from the API and saving it to the database. The script can be configured with environment variables to specify API credentials and database connection details.
"""

from flask import Blueprint
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
import os
import requests

load_dotenv()

# Initialize SQLAlchemy
db = SQLAlchemy()


def configure_db(app):
    """Configure the SQLAlchemy instance."""
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")


# Define Blueprint for database-related routes
app_db = Blueprint("database", __name__)


class Company(db.Model):
    """Define the Company model."""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    company_link = db.Column(db.String(255))
    rating = db.Column(db.Float)
    review_count = db.Column(db.Integer)
    salary_count = db.Column(db.Integer)
    job_count = db.Column(db.Integer)
    headquarters_location = db.Column(db.String(255))
    logo = db.Column(db.String(255))
    company_size = db.Column(db.String(255))
    company_size_category = db.Column(db.String(255))
    company_description = db.Column(db.Text)
    industry = db.Column(db.String(255))

    def __repr__(self):
        """Return a human-readable representation of the company."""
        return f"<Company {self.name}>"

    @classmethod
    def save_data(cls, companies):
        """Save data to the database."""
        for company_data in companies:
            """Create a new Company object from the company data."""
            company = cls(
                name=company_data["name"],
                industry=company_data["industry"],
                rating=(
                    float(company_data["rating"])
                    if company_data.get("rating")
                    else None
                ),
                review_count=company_data.get("review_count"),
                salary_count=company_data.get("salary_count"),
                job_count=company_data.get("job_count"),
                headquarters_location=company_data.get("headquarters_location"),
                logo=company_data.get("logo"),
                company_size=company_data.get("company_size"),
                company_size_category=company_data.get("company_size_category"),
                company_description=company_data.get("company_description"),
                company_link=company_data.get("company_link"),
            )
            db.session.add(company)
        db.session.commit()


@app_db.route("/fetch_and_save_data")
def fetch_and_save_data():
    """Fetch data from Glassdoor API and save it to the database."""
    url = os.getenv("GLASSDOOR_API_URL")
    headers = {
        "X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
        "X-RapidAPI-Host": os.getenv("X_RAPIDAPI_HOST"),
    }
    query_params = {
        "query": "goo",
        "limit": "10",
    }
    response = requests.get(url, headers=headers, params=query_params)
    data = response.json()

    if not data or "data" not in data:
        return "No valid data received from the Glassdoor API."

    companies = data["data"]
    if not companies:
        return "No companies found in the Glassdoor API response."

    # Save fetched data to the database
    Company.save_data(companies)
    return "Data fetched from Glassdoor API and saved to the database successfully."
