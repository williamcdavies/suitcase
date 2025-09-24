import asyncio
import json

from playwright.async_api import async_playwright

async def main() -> int:
        goto_response = input("goto: ")

        with open("config.json", "r") as f:
                config = json.load(f)
                
        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page = await browser.new_page()
                await page.goto(goto_response)

                continue_flag = ""
                while(continue_flag != "Y"):
                        continue_flag = (input("continue[y/n]: ").capitalize())

                anchors = page.locator("a")
                hrefs = await anchors.evaluate_all(
                        """
                        (anchors, filters) => {
                        return anchors
                                .map(a => a.href)
                                .filter(href => filters.some(f => new RegExp(f.replace('.', '\\.'), 'i').test(href)));
                        }
                        """,
                        config["filters"]
                )
                print(hrefs)
                
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())