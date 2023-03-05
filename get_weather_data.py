import requests

# replace YOUR_API_KEY with your actual API key
api_key = "6d0c7ec3fb617dc3d67c92f6d4f938ee"

# define a function to retrieve weather data for a given city
def get_weather_data(city):
    # construct the API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    # make the API request
    response = requests.get(url)

    # check if the request was successful
    if response.status_code == 200:
        # extract the weather data from the response
        data = response.json()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        # return the weather data as a string
        return f"{city}: Temperature={temperature}, Humidity={humidity}, WindSpeed={wind_speed}"
    else:
        return f"Failed to retrieve weather data for {city}."


# read in the list of cities from a text file
with open("cities.txt", "r") as f:
    cities = [line.strip() for line in f]

# retrieve weather data for each city and save it to a text file
with open("weather_data.txt", "w") as f:
    for city in cities:
        weather_data = get_weather_data(city)
        f.write(weather_data + "\n")
