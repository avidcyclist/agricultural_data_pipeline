import boto3
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_PROFILE_NAME = os.getenv('AWS_PROFILE_NAME')
CROP_YIELD_API_KEY = os.getenv('CROP_YIELD_API_KEY')

def upload_to_s3(data, bucket_name, object_name, profile_name):
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3', region_name=AWS_REGION)
    s3_client.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=object_name)

if __name__ == "__main__":
    from fetch_weather_data import get_weather_data, city
    from fetch_crop_yield_data import fetch_crop_yield_data, process_crop_yield_data

    weather_data = get_weather_data(city)
    if weather_data:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        object_name = f"weather_data_{timestamp}.json"  # Use your configured profile name
        upload_to_s3(weather_data, S3_BUCKET_NAME, object_name, AWS_PROFILE_NAME)
        print(f"Weather data uploaded to S3 bucket {S3_BUCKET_NAME} as {object_name}")
    
    # Fetch and upload crop yield data
    
    crop_yield_api_url = "https://quickstats.nass.usda.gov/api/api_GET/"  # Base API URL
    crop_yield_data = fetch_crop_yield_data(crop_yield_api_url)
    if crop_yield_data:
        processed_crop_yield_data = process_crop_yield_data(crop_yield_data)
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        crop_yield_object_name = f"crop_yield_data_{timestamp}.json"
        upload_to_s3(processed_crop_yield_data, S3_BUCKET_NAME, crop_yield_object_name, AWS_PROFILE_NAME)
        print(f"Crop yield data uploaded to S3 bucket {S3_BUCKET_NAME} as {crop_yield_object_name}")