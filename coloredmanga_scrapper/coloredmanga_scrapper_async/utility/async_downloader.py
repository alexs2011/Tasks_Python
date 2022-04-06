import aiohttp
import asyncio
import time


def get_full_contents(manga_vols: dict[str, dict[str, str]]) -> dict[str, dict[str, list[str]]]:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())


