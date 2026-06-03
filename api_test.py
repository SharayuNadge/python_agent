import os
import requests
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt

load_dotenv()

api_key = os.getenv("API_KEY")

@retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(3)
)
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

get_weather("Dubai")