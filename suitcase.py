import asyncio

from playwright.async_api import async_playwright

async def main() -> int:
        url = input("goto?: ")
        
        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page = await browser.new_page()
                await page.goto(url)

                anchors = page.locator("a")
                hrefs = await anchors.evaluate_all(
                        "anchors => anchors.filter(anchor => anchor.hasAttribute('href')).map(anchor => anchor.href).filter(h => h.match(/.*\\.[^\\/]+$/i))"
                        )
                print(hrefs)
                
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())