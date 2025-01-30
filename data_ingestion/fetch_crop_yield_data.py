import requests
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

CROP_YIELD_API_KEY = os.getenv('CROP_YIELD_API_KEY')

def fetch_crop_yield_data(api_url):
    params = {
        'key': CROP_YIELD_API_KEY,
        'commodity_desc': 'CORN',
        'year__GE': '2020',
        'state_alpha': 'IL',
        'format': 'JSON'
    }
    response = requests.get(api_url, params=params)
    if response.status_code == 200:
        crop_yield_data = response.json()
        return crop_yield_data
    else:
        raise Exception(f"Error fetching crop yield data: {response.status_code}")

def process_crop_yield_data(data):
    # Process the data as needed
    processed_data = []
    for item in data['data']:
        yield_value = item['Value'].strip()
        if yield_value in ['(D)', '(Z)']:
            yield_value = None  # Handle special values
        processed_data.append({
            'crop': item['commodity_desc'],
            'yield': yield_value,
            'year': item['year'],
            'state': item['state_name'],
            'county': item['county_name'] if 'county_name' in item else None
        })
    return processed_data

if __name__ == "__main__":
    api_url = "https://quickstats.nass.usda.gov/api/api_GET/"  # Base API URL
    try:
        raw_data = fetch_crop_yield_data(api_url)
        processed_data = process_crop_yield_data(raw_data)
        print(json.dumps(processed_data, indent=4))
    except Exception as e:
        print(e)