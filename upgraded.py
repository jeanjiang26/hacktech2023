import requests
import json

# read input cities from file
with open('cities.txt', 'r') as file:
    cities = file.read().splitlines()

# open output file for writing
with open('output.txt', 'w') as file:
    # loop through cities and get carbon footprint info from OpenEI API
    for city in cities:
        # set API endpoint URL
        url = f"https://api.openei.org/utility_rates?version=latest&format=json&api_key=NUlAemEybPtThidgm3mpPLnSpv6Cvp2YakXxztTY&sector=Residential&lat=40.7128&lon=-74.0060"

        # make API request
        response = requests.get(url)

        # check if API request was successful
        if response.status_code == 200:
            # parse JSON response
            data = json.loads(response.text)

            # write carbon footprint info to output file
            file.write(f"City: {city}\n")
            file.write(f"Electricity carbon intensity: {data['electricity_carbon_intensity']}\n")
            file.write(f"Natural gas carbon intensity: {data['natural_gas_carbon_intensity']}\n")
            file.write(f"Total carbon intensity: {data['total_carbon_intensity']}\n\n")
        else:
            print(f"Failed to get carbon footprint data for {city}")

