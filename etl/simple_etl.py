import pandas as pd
from data_ingestion.fetch_crop_yield_data import fetch_crop_yield_data
from etl.data_cleaning import clean_crop_yield_data
from etl.data_transformation import transform_crop_yield_data

def main():
    # Step 1: Fetch Data (Extract)
    print("Fetching data...")
    api_url = "https://quickstats.nass.usda.gov/api/api_GET/"
    data = fetch_crop_yield_data(api_url)
    print("Data fetched successfully.")

    # Step 2: Clean Data (Transform)
    print("Cleaning data...")
    cleaned_data = clean_crop_yield_data(data)
    print("Data cleaned successfully.")

    # Step 3: Transform Data (Transform)
    print("Transforming data...")
    transformed_data = transform_crop_yield_data(cleaned_data)
    print("Data transformed successfully.")

    # Step 4: Load Data (Load)
    # Here you would load the transformed data into a database or another destination
    # For example: load_crop_yield_data_to_postgres(transformed_data)
    print("Data loading step would go here.")

if __name__ == "__main__":
    main()