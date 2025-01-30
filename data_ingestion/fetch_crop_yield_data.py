import requests
import json

def fetch_crop_yield_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        crop_yield_data = response.json()
        return crop_yield_data
    else:
        raise Exception(f"Error fetching crop yield data: {response.status_code}")

def process_crop_yield_data(data):
    # Process the data as needed
    processed_data = []
    for item in data:
        processed_data.append({
            'crop': item['crop'],
            'yield': item['yield'],
            'year': item['year']
        })
    return processed_data

if __name__ == "__main__":
    api_url = "https://api.example.com/crop_yield"  # Replace with the actual API URL
    try:
        raw_data = fetch_crop_yield_data(api_url)
        processed_data = process_crop_yield_data(raw_data)
        print(json.dumps(processed_data, indent=4))
    except Exception as e:
        print(e)