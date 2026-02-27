from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://tap-vt25-testverktyg.github.io/exam--reading-list/")
        
        print(f"Title: {page.title()}")
        
        # Get all elements with data-testid
        testids = page.locator("[data-testid]").all()
        print("\nTest IDs found:")
        for t in testids:
            try:
                print(f" - {t.get_attribute('data-testid')} (Tag: {t.evaluate('el => el.tagName')})")
            except:
                pass
                
        # Get all buttons
        buttons = page.locator("button").all()
        print("\nButtons found:")
        for b in buttons:
             print(f" - Text: '{b.text_content().strip()}'")

        # Get all links
        links = page.locator("a").all()
        print("\nLinks found:")
        for l in links:
             print(f" - Text: '{l.text_content().strip()}', Href: {l.get_attribute('href')}")

        browser.close()

if __name__ == "__main__":
    run()
