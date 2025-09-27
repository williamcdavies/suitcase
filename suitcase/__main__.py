import asyncio

from playwright.async_api       import async_playwright
from suitcase                   import config
from suitcase                   import script

async def main() -> int:
        url = input("% ")

        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page    = await browser.new_page()
                
                await page.goto(url)

                handover = 1 if input("% ") == "y" else 0
                if(not handover):
                        await browser.close()
                        return 0
                
                anchors = page.locator("a")
                srcs    = await anchors.evaluate_all(script.read("injection.js"), config.load()["filters"])
                
                print(srcs)
                
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())