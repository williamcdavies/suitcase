import asyncio

from .                    import *
from pathlib              import Path
from playwright.async_api import async_playwright

async def main() -> int:
        """suitcase.main
        """
        
        url = input("__main__.py, url, [Any]% ")
        
        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page    = await browser.new_page()
                
                await page.goto(url, wait_until="domcontentloaded")

                handover = input("__main__.py, handover, [y/N]% ") == "y"
                
                if(not handover):
                        await browser.close()
                        
                        return -1
 
                await session.download(await page.locator("a").evaluate_all(scripts.read("injection.js"), config.load()["filters"]), Path("common"), verbose=True)
                await browser.close()
        
        return 0

if __name__ == '__main__':
        asyncio.run(main())