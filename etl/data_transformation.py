import pandas as pd

def transform_weather_data(weather_data):
    # Example transformation: Convert temperature from Kelvin to Celsius
    weather_data['temperature_celsius'] = weather_data['temperature'] - 273.15
    return weather_data[['date', 'temperature_celsius', 'humidity', 'precipitation']]

def transform_crop_yield_data(crop_yield_data):
    # Example transformation: Calculate yield per hectare
    crop_yield_data['yield_per_hectare'] = crop_yield_data['total_yield'] / crop_yield_data['area_hectares']
    return crop_yield_data[['crop_type', 'year', 'yield_per_hectare']]

def main(weather_data, crop_yield_data):
    transformed_weather = transform_weather_data(weather_data)
    transformed_crop_yield = transform_crop_yield_data(crop_yield_data)
    return transformed_weather, transformed_crop_yield

# This file is intended to be imported as a module, so no execution code is included here.