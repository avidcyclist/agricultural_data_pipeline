import pandas as pd

def clean_weather_data(df):
    df = df.dropna()  # Remove rows with missing values
    df['date'] = pd.to_datetime(df['date'])  # Convert date column to datetime
    df = df[df['temperature'] >= -50]  # Filter out unrealistic temperature values
    return df

def clean_crop_yield_data(df):
    df = df.dropna()  # Remove rows with missing values
    df['year'] = df['year'].astype(int)  # Ensure year is an integer
    df = df[df['yield'] >= 0]  # Filter out negative yield values
    return df

def preprocess_data(weather_data, crop_yield_data):
    cleaned_weather_data = clean_weather_data(weather_data)
    cleaned_crop_yield_data = clean_crop_yield_data(crop_yield_data)
    return cleaned_weather_data, cleaned_crop_yield_data