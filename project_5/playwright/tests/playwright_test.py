# -*- coding: utf-8 -*-
import os
import time
from playwright.sync_api import sync_playwright

class UntitledPlaywrightTest:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None

    def setup(self):
        self.playwright = sync_playwright().start()
        is_ci = os.environ.get("CI", "").lower() == "true"
        self.browser = self.playwright.chromium.launch(headless=is_ci)
        self.page = self.browser.new_page()
        self.page.set_viewport_size({"width": 1280, "height": 720})
        self.page.set_default_timeout(30000)

    def teardown(self):
        keep_open_seconds = float(os.getenv("UI_KEEP_OPEN_SECONDS", "2"))
        time.sleep(keep_open_seconds)
        self.browser.close()
        self.playwright.stop()

    def highlight_and_click(self, locator):
        try:
            locator.evaluate("el => el.style.border='3px solid red'")
            time.sleep(0.5)
            locator.click()
            time.sleep(0.5)
            locator.evaluate("el => el.style.border=''")
        except Exception as e:
            print(f"  ⚠️ Could not click element: {e}")

    def highlight_and_type(self, locator, text):
        try:
            locator.evaluate("el => el.style.border='3px solid red'")
            time.sleep(0.5)
            locator.fill(text)
            time.sleep(0.5)
            locator.evaluate("el => el.style.border=''")
        except Exception as e:
            print(f"  ⚠️ Could not type in element: {e}")

    def test_untitled_test_case(self):
        print("Opening website")
        self.page.goto("https://www.saucedemo.com/")
        time.sleep(1)

        # Username field
        print("Entering username")
        username = self.page.locator("#user-name")
        self.highlight_and_type(username, "komlam")

        # Password field
        print("Entering password")
        password = self.page.locator("#password")
        self.highlight_and_type(password, "rrfcccxx")

        # Login button
        print("Clicking login button")
        login_btn = self.page.locator("#login-button")
        self.highlight_and_click(login_btn)
        time.sleep(1)

        # Random clicks – add .first and xpath= prefix
        print("Clicking random element")
        elem1 = self.page.locator("xpath=//div[@id='root']/div").first
        self.highlight_and_click(elem1)

        elem2 = self.page.locator("xpath=//div[@id='root']/div/div[2]/div[2]/div/div[2]").first
        self.highlight_and_click(elem2)

        # Login credentials section
        print("Clicking login credentials element")
        cred_elem = self.page.locator("#login_credentials")
        self.highlight_and_click(cred_elem)
        self.highlight_and_click(cred_elem)
        self.highlight_and_click(cred_elem)

        # Additional clicks
        print("Clicking additional element")
        add_elem = self.page.locator("xpath=//div[@id='root']/div/div").first
        self.highlight_and_click(add_elem)

        print("Clicking login button")
        self.highlight_and_click(login_btn)
        self.highlight_and_click(login_btn)

        print("Clicking random element")
        rand_elem = self.page.locator("xpath=//div[@id='root']/div").first
        self.highlight_and_click(rand_elem)

        # SVG icon clicks – fixed with xpath= prefix
        print("Clicking SVG icon element")
        svg1 = self.page.locator(
            "xpath=(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][2]"
        ).first
        self.highlight_and_click(svg1)

        svg2 = self.page.locator(
            "xpath=(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][1]"
        ).first
        self.highlight_and_click(svg2)

        # More interactions
        print("Clicking more element")
        more_elem = self.page.locator("xpath=//div[@id='root']/div/div[2]/div").first
        self.highlight_and_click(more_elem)

        # Clear password
        print("Clearing password")
        self.highlight_and_type(password, "")

        # Click page
        page_elem = self.page.locator("xpath=//div[@id='root']/div/div[2]/div").first
        self.highlight_and_click(page_elem)

        # Clear username
        print("Clearing username")
        self.highlight_and_type(username, "")

        # Final clicks
        print("Clicking login credentials element")
        self.highlight_and_click(cred_elem)

        final_elem1 = self.page.locator("xpath=//div[@id='root']/div/div[2]/div[2]/div").first
        self.highlight_and_click(final_elem1)

        final_elem2 = self.page.locator("xpath=//div[@id='root']/div/div[2]/div[2]/div/div[2]").first
        self.highlight_and_click(final_elem2)

        print("Test finished – browser closes in 2 seconds")

if __name__ == "__main__":
    test = UntitledPlaywrightTest()
    test.setup()
    try:
        test.test_untitled_test_case()
    finally:
        test.teardown()
