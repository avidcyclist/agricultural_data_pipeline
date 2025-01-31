import pandas as pd
from data_ingestion.fetch_crop_yield_data import fetch_crop_yield_data
from etl.data_cleaning import clean_crop_yield_data
from etl.data_transformation import transform_crop_yield_data


def main():
    api_url = "https://quickstats.nass.usda.gov/api/api_GET/"

    # Step 1: Fetch Crop Yield Data (Extract)
    print("Fetching crop yield data...")
    crop_yield_data = fetch_crop_yield_data(api_url, "YIELD")
    print("Crop yield data fetched successfully.")

    # Step 2: Fetch Area Harvested Data (Extract)
    print("Fetching area harvested data...")
    area_harvested_data = fetch_crop_yield_data(api_url, "AREA HARVESTED")
    print("Area harvested data fetched successfully.")

    # Step 3: Clean Data (Transform)
    print("Cleaning data...")
    cleaned_crop_yield_data = clean_crop_yield_data(crop_yield_data)
    cleaned_area_harvested_data = clean_crop_yield_data(area_harvested_data)
    print("Data cleaned successfully.")

    # Step 4: Transform Data (Transform)
    print("Transforming data...")
    transformed_data = transform_crop_yield_data(cleaned_crop_yield_data, cleaned_area_harvested_data)
    print("Data transformed successfully.")

    # Step 5: Load Data (Load)
    #print("Loading data to SQLite...")
    #load_crop_yield_data_to_sqlite(transformed_data)
    #print("Data loaded to SQLite successfully.")

if __name__ == "__main__":
    main()