import json
import time
from geopy.geocoders import Nominatim
import os

import requests

import os

def get_list_of_cities():
    script_path = os.path.dirname(os.path.abspath(__file__))
    cities_json_path = os.path.join(script_path, 'cities.json')
    with open(cities_json_path, 'r') as file:
        data = json.load(file)
    return data


    # read the file cities.json and returns its content.
    # Example: this function should return ["Algiers", "Batna", "Tamanrasset"]

def get_lat_lon(city):
    geolocator = Nominatim(user_agent="MyApp")

    location = geolocator.geocode(city)
    # get latitude and longitude data of cities in Algeria 
    # using the API documented here: https://nominatim.org/release-docs/latest/api/Search/
    # Example: this function should return 36.6875, 3.125
    return location.latitude, location.longitude

def get_current_weather(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['hourly']['temperature_2m'][0]
        return temperature, data
    
    return None
    # get current weather data at (latitude, longitude)
    # using the API documented here: https://open-meteo.com/

def get_weather_all_cities(cities):
    data = dict()
    for city in cities:
        lat, lon = get_lat_lon(city)
        res = get_current_weather(lat, lon)
        data[city] = res
    return data

def save_output_data(data_):
    unix_timestamp = int(time.time())
    output_filename = f"raw_data_{unix_timestamp}.json"
    with open(output_filename, "w") as f:
        json.dump(data_, f)

def main():
    cities = get_list_of_cities()
    weather_data = get_weather_all_cities(cities)
    save_output_data(weather_data)

main()