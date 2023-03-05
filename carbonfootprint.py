import requests

# replace YOUR_API_KEY with your actual API key
api_key = "NUlAemEybPtThidgm3mpPLnSpv6Cvp2YakXxztTY"

# read the list of cities from the input file
with open("input.txt", "r") as input_file:
    cities = [line.strip() for line in input_file]

# open the output file in write mode
with open("output.txt", "w") as output_file:
    # loop through the cities and retrieve data for each city
    for city in cities:
        # construct the API URL
        url = f"https://api.openei.org/utility_rates?version=latest&format=json&sector=Residential&lat=40.7128&lon=-74.0060"

        # make the API request
        response = requests.get(url)

        # check if the request was successful
        if response.status_code == 200:
            # extract the data from the response
            data = response.json()

            # write the data to the output file
            output_file.write(f"Data for {city}:\n")
            output_file.write(f"------------------------\n")
            for item in data:
                output_file.write(f"{item}: {data[item]}\n")
            output_file.write("\n\n")
        else:
            output_file.write(f"Failed to retrieve data for {city}.\n")
