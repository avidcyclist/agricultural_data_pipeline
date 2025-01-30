import requests
import json
import os
import logging
from dotenv import load_dotenv
from datetime import datetime
import pytz

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load environment variables from .env file
load_dotenv()

API_KEY = os.getenv('WEATHER_API_KEY')  # Set your API key in the environment variable

# Bloomington city details
city = {
    'name': 'Bloomington',
    'lat': 40.4842,
    'lon': -88.9937,
    'timezone': 'America/Chicago'
}

def get_weather_data(city):
    try:
        # Fetch weather data from external API
        url = f'https://api.openweathermap.org/data/3.0/onecall?lat={city["lat"]}&lon={city["lon"]}&exclude=minutely&units=metric&appid={API_KEY}'
        logging.debug(f"Fetching weather data from URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()
        logging.debug(f"Weather data received: {weather_data}")

        current_weather = weather_data['current']
        daily_weather = weather_data['daily'][0]
        weather_desc = current_weather['weather'][0]['description']
        temp_c = current_weather['temp']
        temp_f = round((temp_c * 9/5) + 32, 1)
        feels_like_c = current_weather['feels_like']
        feels_like_f = round((feels_like_c * 9/5) + 32, 1)
        wind_speed_mps = current_weather['wind_speed']
        wind_speed_mph = round(wind_speed_mps * 2.23694, 1)  # Corrected line
        wind_direction = current_weather['wind_deg']
        humidity = current_weather['humidity']
        pressure = current_weather['pressure']
        dew_point_c = current_weather['dew_point']
        dew_point_f = round((dew_point_c * 9/5) + 32, 1)
        uv_index = current_weather['uvi']
        visibility_m = current_weather['visibility']
        visibility_km = round(visibility_m / 1000, 1)
        precipitation = daily_weather.get('rain', 0)  # in mm
        solar_radiation = daily_weather.get('solar_radiation', None)  # if available
        temp_min_c = daily_weather['temp']['min']
        temp_max_c = daily_weather['temp']['max']
        temp_min_f = round((temp_min_c * 9/5) + 32, 2)
        temp_max_f = round((temp_max_c * 9/5) + 32, 2)

        # Convert UTC timestamp to local time
        utc_timestamp = datetime.utcfromtimestamp(current_weather['dt'])
        local_timezone = pytz.timezone(city['timezone'])
        local_timestamp = utc_timestamp.replace(tzinfo=pytz.utc).astimezone(local_timezone)

        weather = {
            'city': city['name'],
            'weather_desc': weather_desc,
            'temp_c': temp_c,
            'temp_f': temp_f,
            'feels_like_c': feels_like_c,
            'feels_like_f': feels_like_f,
            'wind_speed_mph': wind_speed_mph,
            'wind_direction': wind_direction,
            'humidity': humidity,
            'pressure': pressure,
            'dew_point_c': dew_point_c,
            'dew_point_f': dew_point_f,
            'uv_index': uv_index,
            'visibility_km': visibility_km,
            'precipitation_mm': precipitation,
            'solar_radiation': solar_radiation,
            'temp_min_c': temp_min_c,
            'temp_max_c': temp_max_c,
            'temp_min_f': temp_min_f,
            'temp_max_f': temp_max_f,
            'utc_timestamp': utc_timestamp.isoformat(),
            'local_timestamp': local_timestamp.isoformat()
        }
        logging.debug(f"Weather data fetched for {city['name']}: {weather}")
        return weather
    except Exception as e:
        logging.error(f"Error fetching weather data: {e}", exc_info=True)
        return None

if __name__ == "__main__":
    weather_data = get_weather_data(city)
    if weather_data:
        print(json.dumps(weather_data, indent=4))