import aiohttp
import asyncio
import aiofiles

import utility.utils as utils
from classes.page import Page


async def get_page(session: aiohttp.ClientSession, page: Page) -> None:
    async with session.get(page.url) as resp:
        # if resp.status == 200:
        #     f = await aiofiles.open(page.path, mode='wb')
        #     await f.write(await resp.read())
        #     await f.close()
        with open(page.path, 'wb') as fd:
            async for chunk in resp.content.iter_chunked(1024 * 8):
                fd.write(chunk)
        print(f"[+] {page.path}")


async def process_pages(pages: list[Page]) -> None:
    # устанавливаем небольшое число одновременных соединений, чтобы не нагружать сервер.
    connector = aiohttp.TCPConnector(limit=20)

    timeout = aiohttp.ClientTimeout(total=60 * 60 * 12)  # устанавливаем максимальное время работы сессии на 12 часов.

    session = aiohttp.ClientSession(headers=utils.headers, connector=connector, timeout=timeout)
    tasks = []
    for page in pages:
        tasks.append(asyncio.ensure_future(get_page(session, page)))
    tasks_done = await asyncio.gather(*tasks)
    await session.close()


def download_pages(pages: list) -> None:
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(process_pages(pages))
