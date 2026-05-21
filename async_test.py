import asyncio
import aiohttp

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
    await asyncio.gather(get_joke(), get_fact())

asyncio.run(main())