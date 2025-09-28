import asyncio

from playwright.async_api       import async_playwright
from suitcase                   import config
from suitcase                   import scripts
from suitcase                   import session

async def main() -> int:
        url = input("__main__.py, url, [str]% ")

        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page    = await browser.new_page()
                
                await page.goto(url)

                handover = 1 if input("__main__.py, handover, [y/N]% ") == "y" else 0
                if(not handover):
                        await browser.close()
                        return 0
                
                anchors = page.locator("a")
                urls    = await anchors.evaluate_all(scripts.read("injection.js"), config.load()["filters"])
                path    = input("__main__.py, path, [Path]% ")
                
                await session.download(urls, path)
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())