# NYC Taxi Data Pipeline & RESTful API

This project demonstrates an end-to-end data engineering and backend workflow for NYC taxi data. It features an ETL pipeline for data cleaning and ingestion using pandas and SQLAlchemy, with a FastAPI-powered RESTful API for querying data insights.

## Project Structure

nyc_taxi_pipeline/
├── data/
│   └── sample_nyc_taxi.csv
├── src/
│   ├── pipeline.py
│   └── api.py
├── requirements.txt
└── README.md

## Features

- Cleans and loads NYC taxi CSV data into SQLite.
- Provides API endpoints for:
  - Trip count
  - Average fare
  - Querying trips by date

## Setup

1. Clone this repo and install dependencies:

    ```
    pip install -r requirements.txt
    ```

2. Place your NYC taxi trip CSV into `data/sample_nyc_taxi.csv`.

3. Run the ETL pipeline to preprocess and load data:

    ```
    python src/pipeline.py
    ```

4. Start the API server:

    ```
    uvicorn src.api:app --reload
    ```

5. Test endpoints:

    - `GET /trips/count`
    - `GET /trips/average_fare`
    - `GET /trips/date/{YYYY-MM-DD}`

## Technologies

- Python (pandas, FastAPI, SQLAlchemy, SQLite)
- RESTful API best practices

