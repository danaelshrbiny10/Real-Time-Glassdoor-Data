# Real-Time Glassdoor Data API

This project aims to provide real-time access to data from Glassdoor, allowing users to search for companies and retrieve their reviews. The Flask API serves as a middleware to interact with the Glassdoor API and deliver the data to users.

## Model Building and Prediction

In addition to serving real-time data, the project includes a machine learning model for predicting company ratings based on various features such as review sentiment, employee satisfaction, etc. The model is trained on historical Glassdoor data and can be accessed through the /predict/ endpoint. Users can input relevant features to get predictions for a company's rating.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/danaelshrbiny10/Real-Time-Glassdoor-Data.git
```

2. Install dependencies:

```bash
pip install -r requirements/base.txt
```

## Usage

Start the Flask server, run the following command to start the Flask server:

```bash
python server.py
```

## Endpoints

Search for companies in Glassdoor:

- Endpoint: `/search/`
- Method: `GET`
- Parameters: `None`
- Returns: `JSON data of companies matching the search query`

## RapidAPI Link

Access the Real-Time Glassdoor Data API on RapidAPI:
[Real-Time Glassdoor Data](https://rapidapi.com/letscrape-6bRBa3QguO5/api/real-time-glassdoor-data/details)

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
