import pandas as pd
from sqlalchemy import create_engine

def clean_data(df):
    # Drop rows with missing values in key columns
    df = df.dropna(subset=["lpep_pickup_datetime", "lpep_dropoff_datetime", "fare_amount"])
    # Ensure datetime columns are proper type
    df["lpep_pickup_datetime"] = pd.to_datetime(df["lpep_pickup_datetime"])
    df["lpep_dropoff_datetime"] = pd.to_datetime(df["lpep_dropoff_datetime"])
    # Remove rows with negative fare amounts
    df = df[df["fare_amount"] >= 0]
    print(df.head())
    return df

def load_csv_to_db(csv_path, db_url):
    df = pd.read_csv(csv_path)
    df = clean_data(df)
    engine = create_engine(db_url)
    df.to_sql("nyc_taxi", engine, if_exists="replace", index=False)
    print("Data loaded successfully.")

if __name__ == "__main__":
    load_csv_to_db("./data/nyc_taxi_tripdata.csv", "sqlite:///./data/nyc_taxi.db")
