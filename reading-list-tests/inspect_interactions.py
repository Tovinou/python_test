from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://tap-vt25-testverktyg.github.io/exam--reading-list/")
        
        print("--- Main Page ---")
        print(f"URL: {page.url}")
        
        # Click 'Lägg till bok'
        print("\n--- Clicking 'Lägg till bok' ---")
        page.get_by_test_id("add-book").click()
        print(f"URL: {page.url}")
        # Print inputs on this page
        inputs = page.locator("input").all()
        for i in inputs:
            print(f"Input found: id={i.get_attribute('id')}, testid={i.get_attribute('data-testid')}")
        
        # Print buttons on this page
        buttons = page.locator("button").all()
        for b in buttons:
             print(f"Button found: Text='{b.text_content()}'")

        # Go back to catalog (assuming 'Katalog' button works now)
        print("\n--- Clicking 'Katalog' ---")
        # Note: on main page, catalog was disabled. Let's see if it is enabled here.
        page.get_by_test_id("catalog").click()
        print(f"URL: {page.url}")

        # Click 'Mina böcker'
        print("\n--- Clicking 'Mina böcker' ---")
        page.get_by_test_id("favorites").click()
        print(f"URL: {page.url}")
        # Check content of favorites
        print(page.locator("main").text_content())

        browser.close()

if __name__ == "__main__":
    run()
