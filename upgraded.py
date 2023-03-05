import requests
import json
import sys
import sqlite3

# API keys
open_ei_key = "NUlAemEybPtThidgm3mpPLnSpv6Cvp2YakXxztTY"
airnow_key = "7697BBD5-B9C9-4BD0-94D1-86BC378944B7"

# Input parameters
cities_file = sys.argv[1]
output_file = sys.argv[2]

# Connect to SQLite database
conn = sqlite3.connect(output_file)
c = conn.cursor()

# Create table to store data
c.execute('''CREATE TABLE IF NOT EXISTS carbon_footprint 
             (city text, state text, country text, 
             energy_consumption real, waste_generated real, air_quality_index real)''')

# OpenEI API URL
open_ei_url = "https://api.openei.org/utility_rates?version=latest&format=json&lat={lat}&lon={lon}&api_key={key}"

# AirNow API URL
airnow_url = "https://www.airnowapi.org/aq/observation/latLong/current/?format=application/json&latitude={lat}&longitude={lon}&distance=25&API_KEY={key}"

# Read cities from input file
with open(cities_file, "r") as f:
    cities = f.read().splitlines()

# Loop over cities and retrieve data from APIs
for city in cities:
    print(f"Retrieving data for {city}...")

    # Get latitude and longitude for city
    geo_url = f"https://nominatim.openstreetmap.org/search?q={city}&format=json"
    response = requests.get(geo_url)
    data = json.loads(response.text)
    lat = data[0]["lat"]
    lon = data[0]["lon"]

    # Retrieve energy consumption and waste generation data from OpenEI API
    open_ei_request = open_ei_url.format(lat=lat, lon=lon, key=open_ei_key)
    response = requests.get(open_ei_request)
    data = json.loads(response.text)
    energy_consumption = data["items"][0]["total_energy"]
    waste_generated = data["items"][0]["waste_generation_rate"]

    # Retrieve air quality data from AirNow API
    airnow_request = airnow_url.format(lat=lat, lon=lon, key=airnow_key)
    response = requests.get(airnow_request)
    data = json.loads(response.text)
    air_quality_index = data[0]["AQI"]

    # Add data to database
    city_data = (city.split(",")[0], city.split(",")[1], "USA", energy_consumption, waste_generated, air_quality_index)
    c.execute("INSERT INTO carbon_footprint VALUES (?, ?, ?, ?, ?, ?)", city_data)

# Commit changes and close connection
conn.commit()
conn.close()
