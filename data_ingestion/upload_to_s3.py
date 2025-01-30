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

def upload_to_s3(data, bucket_name, object_name, profile_name):
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3', region_name=AWS_REGION)
    s3_client.put_object(Body=json.dumps(data), Bucket=bucket_name, Key=object_name)

if __name__ == "__main__":
    from fetch_weather_data import get_weather_data, city

    weather_data = get_weather_data(city)
    if weather_data:
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        object_name = f"weather_data_{timestamp}.json"  # Use your configured profile name
        upload_to_s3(weather_data, S3_BUCKET_NAME, object_name, AWS_PROFILE_NAME)
        print(f"Weather data uploaded to S3 bucket {S3_BUCKET_NAME} as {object_name}")