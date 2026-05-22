import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")

def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url, timeout=5)
        data = response.json()

        if data['cod'] != 200:
            print(f"Error: {data['message']}")
            return

        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")

    except requests.exceptions.ConnectionError:
        print("Error: No internet connection")
    except requests.exceptions.Timeout:
        print("Error: Request timed out")

for i in range(10):
    print(f"Call {i+1}")
    get_weather("Dubai")