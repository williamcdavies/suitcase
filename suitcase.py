import asyncio

from playwright.async_api import async_playwright

async def main() -> int:
        str = input("stdin: ")
        
        async with async_playwright() as p:
                browser = await p.firefox.launch(headless=False)
                page = await browser.new_page()
                await page.goto(str)
                print(await page.title())
                await browser.close()

        return 0

if __name__ == '__main__':
        asyncio.run(main())