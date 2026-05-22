import os
from dotenv import load_dotenv
from tenacity import retry, wait_exponential, stop_after_attempt
import asyncio
import aiohttp

load_dotenv()

api_key = os.getenv("API_KEY")

@retry(
    wait=wait_exponential(multiplier=1, min=2, max=10),
    stop=stop_after_attempt(3)
)
async def get_weather(city):
    try:
        async with aiohttp.ClientSession() as session:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
            async with session.get(url) as r:
                data = await r.json()

            if data['cod'] != 200:
                print(f"Error: {data['message']}")
                return

            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Weather: {data['weather'][0]['description']}")

    except aiohttp.ClientConnectionError:
        print("Error: No internet connection")
    except asyncio.TimeoutError:
        print("Error: Request timed out")

async def get_joke():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://official-joke-api.appspot.com/random_joke") as r:
            data = await r.json()
            print(f"Joke: {data['setup']} ... {data['punchline']}")

async def get_fact():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://uselessfacts.jsph.pl/api/v2/facts/random") as r:
            data = await r.json()
            print(f"Fact: {data['text']}")

async def main():
    await asyncio.gather(get_joke(), get_fact(), get_weather("Dubai"))

asyncio.run(main())