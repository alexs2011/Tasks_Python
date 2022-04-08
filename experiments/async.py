import aiohttp
import asyncio
import time

import requests


async def async_func_1():
    async with aiohttp.ClientSession() as session:
        for i in range(1, 151):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json()
                print(i, pokemon['name'])


def sync_func():
    for i in range(1, 151):
        url = f'https://pokeapi.co/api/v2/pokemon/{i}'
        resp = requests.get(url)
        pokemon = resp.json()
        print(i, pokemon['name'])


async def get_pokemon(session, url, i):
    async with session.get(url) as resp:
        pokemon = await resp.json()
        n = pokemon['name']
        print(i, n)
        return n


async def async_func_2():
    async with aiohttp.ClientSession() as session:
        tasks = []
        for i in range(1, 151):
            url = f'https://pokeapi.co/api/v2/pokemon/{i}'
            tasks.append(asyncio.ensure_future(get_pokemon(session, url, i)))

        original_pokemon = await asyncio.gather(*tasks)
        for pokemon in original_pokemon:
            print(pokemon)


def main():
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    # start = time.time()
    # sync_func()
    # end_1 = time.time() - start
    #
    # start = time.time()
    # asyncio.run(async_func_1())
    # end_2 = time.time() - start

    start = time.time()
    asyncio.run(async_func_2())
    end_3 = time.time() - start

    print(end_3)


if __name__ == '__main__':
    main()
