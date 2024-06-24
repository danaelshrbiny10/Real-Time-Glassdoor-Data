"""Script to Run the Real-Time Glassdoor Project.
This script initializes and runs the Flask application for the Real-Time Glassdoor project. 
It serves as the main entry point for the project, allowing access to various routes and functionalities.
"""

from flask import Flask, jsonify, request
import joblib
import pandas as pd
from api.search import search_app
from database.models import app_db, configure_db


app = Flask(__name__)

# Register blueprints
app.register_blueprint(search_app)
app.register_blueprint(app_db)

# Configure SQLAlchemy
configure_db(app)

# Load the trained model
model = joblib.load("model/saved_model/company_rating_model.pkl")


def preprocess_input(input_data):
    """
    Preprocesses input data to match the format expected by the machine learning model.
    Converts categorical variables 'company_size' and 'industry' into one-hot encoded format.
    """
    expected_company_sizes = ["1 to 50 Employees", "201 to 500 Employees"]
    expected_industries = [
        "Architectural & Engineering Services",
        "Enterprise Software & Network Solutions",
    ]

    # Convert company_size and industry to categorical variables
    input_data["company_size"] = pd.Categorical(
        input_data["company_size"], categories=expected_company_sizes
    )
    input_data["industry"] = pd.Categorical(
        input_data["industry"], categories=expected_industries
    )

    input_data = pd.get_dummies(input_data, columns=["company_size", "industry"])

    for col in [
        "company_size_1 to 50 Employees",
        "company_size_201 to 500 Employees",
        "industry_Architectural & Engineering Services",
        "industry_Enterprise Software & Network Solutions",
    ]:
        if col not in input_data.columns:
            input_data[col] = 0

    input_data = input_data[
        [
            "review_count",
            "salary_count",
            "job_count",
            "company_size_1 to 50 Employees",
            "company_size_201 to 500 Employees",
            "industry_Architectural & Engineering Services",
            "industry_Enterprise Software & Network Solutions",
        ]
    ]

    return input_data


@app.route("/predict/", methods=["POST"])
def predict():
    """
    Endpoint to predict company rating based on input data.
    Expects JSON input with fields matching the model's training data features.
    """
    if request.method == "POST":
        """"""
        try:
            input_data = request.json

            input_df = pd.DataFrame([input_data])
            input_df_processed = preprocess_input(input_df)

            # Make predictions
            predictions = model.predict(input_df_processed)

            response = {"predicted_rating": predictions[0]}

            return jsonify(response)
        except Exception as e:
            return jsonify({"error": str(e)}), 500
    else:
        return jsonify({"error": "Method not allowed"}), 405


if __name__ == "__main__":
    """Create a simple web server that returns the data from Glassdoor API."""
    app.run(host="0.0.0.0", port=5000, debug=True)
