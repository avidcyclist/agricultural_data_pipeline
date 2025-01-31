import requests
import pandas as pd
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CROP_YIELD_API_KEY = os.getenv('CROP_YIELD_API_KEY')

def fetch_crop_yield_data(api_url, statisticcat_desc):
    params = {
        'key': CROP_YIELD_API_KEY,
        'commodity_desc': 'CORN',
        'year__GE': '2020',
        'state_alpha': 'IL',
        'statisticcat_desc': statisticcat_desc,
        'format': 'JSON'
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        crop_yield_data = response.json()
        return process_crop_yield_data(crop_yield_data, statisticcat_desc)
    else:
        raise Exception(f"Error fetching crop yield data: {response.status_code}")

def process_crop_yield_data(data, statisticcat_desc):
    # Process the data as needed
    processed_data = []
    for item in data['data']:
        value = item['Value'].strip().replace(',', '')
        if value in ['(D)', '(Z)'] or not item.get('county_name'):
            continue  # Skip entries with special values or without county name
        processed_data.append({
            'crop_type': item['commodity_desc'],
            'total_yield' if statisticcat_desc == 'YIELD' else 'area_harvested': float(value),
            'year': int(item['year']),
            'state': item['state_name'],
            'county': item['county_name']
        })
    return pd.DataFrame(processed_data)

if __name__ == "__main__":
    api_url = "https://quickstats.nass.usda.gov/api/api_GET/"  # Base API URL
    try:
        raw_data = fetch_crop_yield_data(api_url, "YIELD")
        print(raw_data.head())  # Print the first few rows of the DataFrame
    except Exception as e:
        print(e)