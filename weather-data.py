import credentials
import requests
import json

API_KEY = credentials.API_KEY
city = "Lagos"
endpoint = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
response = requests.get(endpoint)

if response.status_code == 200:
    data = response.json()
    # temperature = data['main']['temp']
    # humidity = data['main']['humidity']
    # condition = data['weather'][0]['description']
    print(json.dumps(data, indent=4))
    print(data)
    # print(f"Weather in {city}: Temperature: {temperature}°C Condition: {condition} Humidity: {humidity}%")
else:
    print("Error")

# if __name__ == '__main__':
#    main()