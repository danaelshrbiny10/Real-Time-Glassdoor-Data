from flask import Flask
import requests
import os
import csv
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

url = os.getenv("URL")


headers = {
    "X-RapidAPI-Key": os.getenv("X_RAPIDAPI_KEY"),
    "X-RapidAPI-Host": os.getenv("X_RAPIDAPI_HOST"),
}


@app.route("/search/")
def company_search():
    """Return the data from Glassdoor API company search."""
    querystring = {"query": "goo", "limit": "10"}
    response = requests.get(url, headers=headers, params=querystring)
    data = response.json()

    # Define the file path
    folder_name = "data"
    file_name = "glassdoor_company.csv"
    file_path = os.path.join(folder_name, file_name)

    if not data or "data" not in data:
        """Create an empty CSV file when there is no valid data to write into it."""
        return "No valid data received from the Glassdoor API."

    companies = data["data"]
    if not companies:
        """Return an empty list if no companies are found for a given query."""
        return "No companies found in the Glassdoor API response."

    with open(file_path, mode="w", newline="") as file:
        """Write the data to a CSV file and return it as an HTTP response."""
        writer = csv.DictWriter(file, fieldnames=companies[0].keys())
        writer.writeheader()

        for row in companies:
            """Write each dictionary item (row) to the CSV file."""
            writer.writerow(row)

    return response.json()


if __name__ == "__main__":
    """Create a simple web server that returns the data from Glassdoor API."""
    app.run()
    debug = True