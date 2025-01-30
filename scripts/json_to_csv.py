import boto3
import json
import csv
import sys
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

AWS_REGION = os.getenv('AWS_REGION')
S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
AWS_PROFILE_NAME = os.getenv('AWS_PROFILE_NAME')

def download_from_s3(bucket_name, object_name, download_path, profile_name):
    session = boto3.Session(profile_name=profile_name)
    s3_client = session.client('s3', region_name=AWS_REGION)
    response = s3_client.get_object(Bucket=bucket_name, Key=object_name)
    data = response['Body'].read().decode('utf-8')
    with open(download_path, 'w') as jsonfile:
        jsonfile.write(data)

def json_to_csv(json_file_path, csv_file_path, filter_no_county=False):
    with open(json_file_path, 'r') as jsonfile:
        json_data = json.load(jsonfile)
    
    # Debugging: Print the JSON data structure
    print(json.dumps(json_data, indent=4))
    
    # Check if the JSON data is a dictionary with a key 'data'
    if isinstance(json_data, dict) and 'data' in json_data:
        json_data = json_data['data']
    
    # Check if the JSON data is a list
    if isinstance(json_data, list):
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = json_data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in json_data:
                # Normalize the yield value based on the unit or type of data
                yield_value = row['yield']
                if 'unit_desc' in row and row['unit_desc'] == 'BUSHELS':
                    yield_value = int(yield_value.replace(',', ''))  # Convert to integer
                
                # Filter out rows without county information if specified
                if filter_no_county and not row.get('county'):
                    continue
                
                writer.writerow({
                    'crop': row['crop'],
                    'yield': yield_value,
                    'year': row['year'],
                    'state': row['state'],
                    'county': row.get('county', '')
                })
    elif isinstance(json_data, dict):
        with open(csv_file_path, 'w', newline='') as csvfile:
            fieldnames = json_data.keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerow(json_data)
    else:
        print("Error: JSON data is not a list or dictionary")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python json_to_csv.py <s3_object_name> <output_csv_file> [--filter-no-county]")
        sys.exit(1)
    
    s3_object_name = sys.argv[1]
    output_csv_file = os.path.join('data', sys.argv[2])
    filter_no_county = '--filter-no-county' in sys.argv
    
    # Create the data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Download JSON file from S3
    json_file_path = os.path.join('data', s3_object_name)
    download_from_s3(S3_BUCKET_NAME, s3_object_name, json_file_path, AWS_PROFILE_NAME)
    print(f"Downloaded {s3_object_name} from S3 to {json_file_path}")
    
    # Convert JSON to CSV
    json_to_csv(json_file_path, output_csv_file, filter_no_county)
    print(f"Converted {json_file_path} to {output_csv_file}")