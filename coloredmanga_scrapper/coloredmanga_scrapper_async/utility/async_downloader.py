import aiohttp
import asyncio
import time
from copy import deepcopy
from pprint import pprint

from classes.c_utils.parser import Parser


async def get_pages(session: aiohttp.ClientSession, ch_name: str, ch_link: str) -> dict:
    async with session.get(ch_link) as resp:
        ch_html = await resp.text()
        parser = Parser(ch_html)
        pages = parser.parse_chapter_page()
        return {ch_name: pages}


async def get_vol_chapters(chapters: dict[str, str]) -> None:
    async with aiohttp.ClientSession() as session:
        tasks = []
        for ch_name, ch_link in chapters.items():
            tasks.append(asyncio.ensure_future(get_pages(session, ch_name, ch_link)))
        all_chapters = await asyncio.gather(*tasks)
        return all_chapters


def get_full_contents(manga_vols: dict[str, dict[str, str]]) -> dict[str, dict[str, list[str]]]:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    vols = deepcopy(manga_vols)
    for vol_name, vol_chapters in vols.items():
        tmp = asyncio.run(get_vol_chapters(vol_chapters))
        print(vol_name, tmp)
        # time.sleep(3)
