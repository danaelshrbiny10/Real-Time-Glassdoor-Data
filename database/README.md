# Database Initialization Guide

This guide provides step-by-step instructions on how to create the database tables for the Real-Time Glassdoor project.

## Prerequisites

- Python installed on your system.
- Flask and SQLAlchemy installed in your Python environment.
- PostgreSQL installed and running on your machine.
- Required environment variables set up (e.g., SQLALCHEMY_DATABASE_URI).

## Steps

1. Set Flask Application

- Set the FLASK_APP environment variable to point to your Flask application file (server.py).

```bash
export FLASK_APP=server.py
```

2. Start Flask Shell

- Start the Flask shell to interact with your application.

```bash
flask shell
```

3. Import Dependencies

- Inside the Flask shell, import the necessary dependencies.

```bash
from flask import Flask
from database.models import db
import os
```

4. Configure SQLAlchemy with the Flask application.

```bash
db.init_app(app)
```

5. Create Database Tables

- Within the Flask application context, create the database tables.

```bash
with app.app_context():
    db.create_all()
```

6. Exit Flask Shell

- Exit the Flask shell.

```bash
exit()
```

## Load CSV Data into the Database

Once the database tables are created, you can copy actual API data into the tables using the `COPY` command in PostgreSQL.

1. Ensure your CSV file path is correct and accessible.
2. Run the following command to copy data from the CSV file into the `Company` table:

```bash
COPY company(id, name, company_link, rating, review_count, salary_count, job_count, headquarters_location, logo, company_size, company_size_category, company_description, industry)
FROM 'F:\DataScience\code\Real-Time-Glassdoor-Data\data\glassdoor_company.csv'
DELIMITER ','
CSV HEADER;
```
This command assumes that your CSV file is located at `F:\DataScience\code\Real-Time-Glassdoor-Data\data\glassdoor_company.csv`. Ensure the file path is correct and replace it with the actual path if different.
