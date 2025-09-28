import aiofiles
import aiohttp
import asyncio

from pathlib import Path

async def download(urls, root: Path):
        root.mkdir(exist_ok=True)

        async with aiohttp.ClientSession() as session:
                async def _download(url) -> Path:
                        path = root / url.split("/")[-1]
                        
                        async with session.get(url) as resp:
                                resp.raise_for_status()
                                
                                async with aiofiles.open(path, "wb") as wbf:
                                        async for chunk in resp.content.iter_any():
                                                await wbf.write(chunk)

                        return path
                
                futures = [_download(url) for url in urls]
                
                return await asyncio.gather(*futures)