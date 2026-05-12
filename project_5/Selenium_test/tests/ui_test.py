# -*- coding: utf-8 -*-
import os
import time
import unittest

from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

LOGIN_URL = "https://www.saucedemo.com/"
ERROR_BANNER = (By.CSS_SELECTOR, "[data-test='error']")


class SauceDemoLoginTests(unittest.TestCase):
    """Automatiserade testfall för inloggning på Sauce Demo.

    Fält och knapp markeras kort med röd ram innan interaktion (bra vid manuell
    körning). I CI är pausen 0 så testerna inte sakta ned; sätt UI_HIGHLIGHT_DELAY
    om du vill tvinga paus även där.
    """

    def setUp(self):
        self.is_ci = os.environ.get("CI", "").lower() == "true"
        self.keep_open_seconds = float(os.getenv("UI_KEEP_OPEN_SECONDS", "0"))
        default_highlight = "0" if self.is_ci else "0.5"
        self.highlight_pause = float(os.getenv("UI_HIGHLIGHT_DELAY", default_highlight))

        options = Options()
        if self.is_ci:
            options.add_argument("--headless=new")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")

        self.driver = webdriver.Chrome(options=options)
        self.driver.set_window_size(1920, 1080)
        self.wait = WebDriverWait(self.driver, 15)

    def tearDown(self):
        if self.keep_open_seconds > 0:
            time.sleep(self.keep_open_seconds)
        self.driver.quit()

    def _sleep_highlight(self):
        if self.highlight_pause > 0:
            time.sleep(self.highlight_pause)

    def highlight_and_click(self, element):
        """Röd ram, klick, kort paus, återställ ram."""
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        self._sleep_highlight()
        element.click()
        self._sleep_highlight()
        try:
            self.driver.execute_script("arguments[0].style.border=''", element)
        except StaleElementReferenceException:
            # T.ex. lyckad inloggning byter sida innan ramen hinner tas bort.
            pass

    def highlight_and_type(self, element, text):
        """Röd ram, rensa, skriv text, kort paus, återställ ram."""
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        self._sleep_highlight()
        element.clear()
        element.send_keys(text)
        self._sleep_highlight()
        self.driver.execute_script("arguments[0].style.border=''", element)

    def _open_login_page(self):
        self.driver.get(LOGIN_URL)
        self.wait.until(EC.visibility_of_element_located((By.ID, "user-name")))

    def _submit_login(self, username, password):
        user_field = self.driver.find_element(By.ID, "user-name")
        self.highlight_and_type(user_field, username)
        password_field = self.driver.find_element(By.ID, "password")
        self.highlight_and_type(password_field, password)
        login_btn = self.driver.find_element(By.ID, "login-button")
        self.highlight_and_click(login_btn)

    def test_successful_login_goes_to_inventory(self):
        self._open_login_page()
        self._submit_login("standard_user", "secret_sauce")

        self.wait.until(EC.url_contains("inventory"))
        inventory_list = self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "inventory_list"))
        )

        self.assertIn("inventory", self.driver.current_url)
        self.assertTrue(inventory_list.is_displayed())

    def test_wrong_username_shows_error_message(self):
        self._open_login_page()
        self._submit_login("not_a_real_user", "secret_sauce")

        error = self.wait.until(EC.visibility_of_element_located(ERROR_BANNER))
        self.assertTrue(error.is_displayed())
        self.assertGreater(len(error.text.strip()), 0)

    def test_wrong_password_shows_error_message(self):
        self._open_login_page()
        self._submit_login("standard_user", "wrong_password")

        error = self.wait.until(EC.visibility_of_element_located(ERROR_BANNER))
        self.assertTrue(error.is_displayed())
        self.assertGreater(len(error.text.strip()), 0)


if __name__ == "__main__":
    unittest.main()
