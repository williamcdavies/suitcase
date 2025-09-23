import asyncio

from playwright.async_api import async_playwright

async def main() -> int:
        goto_response = input("goto: ")
        
        async with async_playwright() as p:
                browser = await p.chromium.launch(headless=False)
                page = await browser.new_page()
                await page.goto(goto_response)

                f = ""
                while(f != "Y"):
                        f = (input("continue?[y/n]: ").capitalize())

                anchors = page.locator("a")
                hrefs = await anchors.evaluate_all(
                        """anchors => {
                                return anchors
                                .filter(anchor => anchor.hasAttribute('href'))
                                .map(anchor => anchor.href)
                                .filter(h => h.match(/.*\\.[^\\/]+$/i))
                        } """
                        )
                print(hrefs)
                
                await browser.close()
        return 0

if __name__ == '__main__':
        asyncio.run(main())