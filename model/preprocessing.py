"""This Script Performs Data Preprocessing.

This script defines routes for preprocessing data before analysis. It includes methods for reading data from CSV files and performing initial preprocessing steps.

Usage:
    This script is intended to be run as part of a Flask application. It provides routes for preprocessing data before analysis.

Attributes:
    app: Flask application instance.
    preprocessing_routes: Blueprint containing routes for data preprocessing.
"""

from flask import Blueprint, render_template
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

preprocessing_app = Blueprint("preprocessing", __name__)


@preprocessing_app.route("/data/")
def read_csv() -> str:
    """
    This function reads a CSV file and returns the data.

    Parameters:
    None

    Returns:
    str: The data read from the CSV file in the form of a pandas DataFrame.

    Raises:
    FileNotFoundError: If the specified CSV file does not exist.
    pd.errors.EmptyDataError: If the CSV file is empty.
    pd.errors.ParserError: If there is a parsing error in the CSV file.

    Usage:
    data = read_csv()
    print(data.head())
    """

    data = pd.read_csv("data/glassdoor_company.csv")

    # info = data.info()
    # info_str = str(info)
    # print("data info:", info_str)
    
    cols = data.columns.tolist()
    rows = data.values.tolist()
    description_index = cols.index("company_description")
    return render_template(
        "tables.html", cols=cols, rows=rows, description_index=description_index
    )
