from fastapi import FastAPI
from sqlalchemy import create_engine
import pandas as pd
app = FastAPI()
engine = create_engine("sqlite:///./data/nyc_taxi.db")

@app.get("/trips/count")
def trips_count():
    df = pd.read_sql("SELECT COUNT(*) as trip_count FROM nyc_taxi", engine)
    return df.to_dict(orient="records")[0]

@app.get("/trips/average_fare")
def average_fare():
    df = pd.read_sql("SELECT AVG(fare_amount) as avg_fare FROM nyc_taxi", engine)
    return df.to_dict(orient="records")[0]

@app.get("/trips/date/{date}")
def trips_by_date(date: str):
    query = f"SELECT * FROM nyc_taxi WHERE DATE(pickup_datetime)='{date}'"
    df = pd.read_sql(query, engine)
    return df.to_dict(orient="records")

# Run: uvicorn src.api:app --reload

