import asyncio

from pathlib                    import Path
from playwright.async_api       import async_playwright
from suitcase                   import config
from suitcase                   import scripts
from suitcase                   import session

async def main() -> int:
        url     = input("__main__.py, url% ")

        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page    = await browser.new_page()
                
                await page.goto(url)

                handover        = 1 if input("__main__.py, handover% ") == "y" else 0
                
                if(not handover):
                        await browser.close()
                        return 0
                
                anchors         = page.locator("a")
                expression      = scripts.read("injection.js")
                arg             = config.load()["filters"]
                urls            = await anchors.evaluate_all(expression, arg)
                path            = Path(input("__main__.py, path% "))
                
                await session.download(urls, path)
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())