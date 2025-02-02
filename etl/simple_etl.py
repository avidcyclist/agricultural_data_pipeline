import sys
import os
import logging
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
from data_ingestion.fetch_crop_yield_data import fetch_crop_yield_data
from data_ingestion.fetch_weather_data import get_weather_data, city
from etl.data_cleaning import clean_crop_yield_data
from etl.data_transformation import transform_crop_yield_data
from etl.load_to_postgres import load_data_to_postgres
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up logging configuration
logging.basicConfig(level=logging.INFO)

def main():
    api_url = "https://quickstats.nass.usda.gov/api/api_GET/"

    # Step 1: Fetch Crop Yield Data (Extract)
    logging.info("Fetching crop yield data...")
    raw_crop_yield_data, crop_yield_data = fetch_crop_yield_data(api_url, "YIELD")
    logging.info("Crop yield data fetched successfully.")

    # Step 2: Fetch Area Harvested Data (Extract)
    logging.info("Fetching area harvested data...")
    raw_area_harvested_data, area_harvested_data = fetch_crop_yield_data(api_url, "AREA HARVESTED")
    logging.info("Area harvested data fetched successfully.")

    # Step 3: Clean Data (Transform)
    logging.info("Cleaning data...")
    cleaned_crop_yield_data = clean_crop_yield_data(crop_yield_data)
    cleaned_area_harvested_data = clean_crop_yield_data(area_harvested_data)
    logging.info("Data cleaned successfully.")

    # Step 4: Transform Data (Transform)
    logging.info("Transforming data...")
    transformed_data = transform_crop_yield_data(cleaned_crop_yield_data, cleaned_area_harvested_data)
    logging.info("Data transformed successfully.")

    # Step 5: Load Data (Load)
    logging.info("Loading crop yield data to PostgreSQL...")
    db_config = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD').strip(),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }
    load_data_to_postgres(transformed_data, 'crop_yield_data', db_config)
    logging.info("Crop yield data loaded to PostgreSQL successfully.")

    # Fetch and load weather data
    logging.info("Fetching weather data...")
    weather_data = get_weather_data(city)
    if weather_data:
        weather_data['utc_timestamp'] = datetime.utcnow()
        weather_data['local_timestamp'] = datetime.now()
        logging.info("Weather data fetched successfully.")
        logging.info("Loading weather data to PostgreSQL...")
        load_data_to_postgres(pd.DataFrame([weather_data]), 'weather_data', db_config)
        logging.info("Weather data loaded to PostgreSQL successfully.")

if __name__ == "__main__":
    main()