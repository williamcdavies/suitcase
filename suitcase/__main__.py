import asyncio
import json

from playwright.async_api       import async_playwright
from suitcase                   import cfg        

async def main() -> int:
        cfg.init()

        goto_response = input("goto: ")

        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page = await browser.new_page()
                await page.goto(goto_response)

                continue_flag = input("continue[y/n]: ").capitalize()
                if(continue_flag != "Y"):
                        await browser.close()
                        return 0

                anchors = page.locator("a")
                srcs = await anchors.evaluate_all(
                        """
                        (anchors, filters) => {
                        return anchors
                                .map(a => a.href)
                                .filter(href => filters.some(f => new RegExp(f.replace('.', '\\.'), 'i').test(href)));
                        }
                        """,
                        cfg.load()["filters"]
                )
                print(srcs)
                
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())