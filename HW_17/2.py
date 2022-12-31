import requests
import asyncio
import aiohttp
from time import time

URL = "https://pokeapi.co/api/v2/"


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        finish = time()
        print(f"execution time {finish - start}")
        return res

    return wrapper


@time_decorator
def simple_print():
    resp = requests.get(f"{URL}/pokemon")
    data = resp.json()["results"]
    print(data)


async def print_pokemon(session, name):
    resp = await session.get("https://pokeapi.co/api/v2/pokemon/" + name)
    resp_json = await resp.json()
    print(
        f"Pokemon ",
        {name},
        "have a weight",
        {resp_json["weight"]},
        "g and height",
        {resp_json["height"]},
        "sm",
    )


async def main():
    simple_print()
    start = time()
    resp = requests.get(f"{URL}/pokemon")
    data = resp.json()["results"]
    new_pocemons = []
    for i in range(len(data)):
        new_pocemons.append(data[i]["name"])
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[print_pokemon(session, name) for name in new_pocemons])
    print(f"{round((time() - start), 3)} seconds")


asyncio.run(main())
