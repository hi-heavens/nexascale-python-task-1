# import credentials
from dotenv import load_dotenv
import requests
# import json
import os

def configure():
    load_dotenv()

def get_weather_data(city):
    # Load the environment variables into the script
    configure()

    # Using the credentials.py file
    # API_KEY = credentials.API_KEY

    API_KEY = os.getenv("API_KEY")
    endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(endpoint)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        condition = data['weather'][0]['description']
        # print(json.dumps(data, indent=4))
        print(f"Weather in {city}: Temperature: {temperature}°C Condition: {condition} Humidity: {humidity}%")
    else:
        print(f"Error fetching weather data for {city} with code {response.status_code}")

# Install the dotenv package
# pip install python-dotenv

if __name__ == '__main__':
    cities = input("Enter the city name(s) separated by commas: ")
    cities = [city.strip() for city in cities.split(',')]
    # print(cities)
    for city in cities:
        get_weather_data(city)