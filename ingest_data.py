import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

from constants import (DATABASE_HOST, DATABASE_NAME, DATABASE_PORT,
                       TAXI_TRIPS_DATA_URL, TAXI_ZONES_DATA_URL,
                       TRIPS_TABLE_NAME, ZONES_TABLE_NAME)


def main():
    load_dotenv()

    postgres_engine = get_postgres_engine()

    taxi_zones = pd.read_csv(TAXI_ZONES_DATA_URL)
    taxi_zones.to_sql(ZONES_TABLE_NAME, postgres_engine, if_exists="replace")

    if_trips_exist = "replace"
    taxi_trip_batches = pd.read_csv(TAXI_TRIPS_DATA_URL, parse_dates=[1, 2],
                                    iterator=True, chunksize=40000)

    for taxi_trip_batch in taxi_trip_batches:
        taxi_trip_batch.to_sql(TRIPS_TABLE_NAME, postgres_engine, if_exists=if_trips_exist)

        # Append to the table created after first iteration
        if_trips_exist = "append"


def get_postgres_engine():
    database_username = os.getenv("HOMEWORK_POSTGRES_USER")
    database_password = os.getenv("HOMEWORK_POSTGRES_PASS")

    return create_engine(f"postgresql://{database_username}:{database_password}@"
                         f"{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}")


main()
