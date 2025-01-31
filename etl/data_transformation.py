import pandas as pd

def transform_weather_data(weather_data):
    # Example transformation: Convert temperature from Kelvin to Celsius
    weather_data['temperature_celsius'] = weather_data['temperature'] - 273.15
    return weather_data[['date', 'temperature_celsius', 'humidity', 'precipitation']]

def transform_crop_yield_data(crop_yield_data, area_harvested_data):
    # Merge crop yield data with area harvested data
    merged_data = pd.merge(
        crop_yield_data,
        area_harvested_data,
        on=['crop_type', 'year', 'state', 'county'],
        suffixes=('_yield', '_area')
    )

    # Calculate yield per hectare
    merged_data['yield_per_hectare'] = merged_data['total_yield'] / (merged_data['area_harvested'] * 0.404686)
    return merged_data[['crop_type', 'year', 'state', 'county', 'yield_per_hectare']]

def main(weather_data, crop_yield_data, area_harvested_data):
    transformed_weather = transform_weather_data(weather_data)
    transformed_crop_yield = transform_crop_yield_data(crop_yield_data, area_harvested_data)
    return transformed_weather, transformed_crop_yield

# This file is intended to be imported as a module, so no execution code is included here.