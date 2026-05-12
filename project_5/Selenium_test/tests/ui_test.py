# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time


class UntitledTestCase(unittest.TestCase):

    def setUp(self):
        # Setup Chrome options for CI/headless environment
        options = webdriver.ChromeOptions()
        options.add_argument('--headless=new')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        
        # Start Chrome browser
        self.driver = webdriver.Chrome(options=options)
        
        # Maximize window is mostly for visible mode, but setting a standard size is safer for headless
        self.driver.set_window_size(1920, 1080)

        # Wait up to 30 seconds
        self.driver.implicitly_wait(30)

        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def tearDown(self):
        # Wait a moment so you can see final state
        time.sleep(2)
        # Close browser
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def highlight_and_click(self, element):
        """Highlights element in red, clicks it, then removes highlight"""
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(0.5)  # see the highlight
        element.click()
        time.sleep(0.5)  # see the click result
        self.driver.execute_script("arguments[0].style.border=''", element)

    def highlight_and_type(self, element, text):
        """Highlights element, clears it, types text"""
        self.driver.execute_script("arguments[0].style.border='3px solid red'", element)
        time.sleep(0.5)
        element.clear()
        element.send_keys(text)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].style.border=''", element)

    def test_untitled_test_case(self):
        driver = self.driver

        # Open SauceDemo website
        print("Opening website")
        driver.get("https://www.saucedemo.com/")
        time.sleep(1)  # let the page load visibly

        # Username field - using highlight method
        print("Entering username")
        username_field = driver.find_element(By.ID, "user-name")
        self.highlight_and_type(username_field, "komlam")

        # Password field
        print("Entering password")
        password_field = driver.find_element(By.ID, "password")
        self.highlight_and_type(password_field, "rrfcccxx")

        # Login button
        print("Clicking login button")
        login_btn = driver.find_element(By.ID, "login-button")
        self.highlight_and_click(login_btn)
        time.sleep(1)  # see login attempt result

        # Random clicks from original exported script
        print("Clicking random element")
        elem = driver.find_element(By.XPATH, "//div[@id='root']/div")
        self.highlight_and_click(elem)

        elem2 = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div[2]/div/div[2]")
        self.highlight_and_click(elem2)

        # Login credentials section
        print("Clicking login credentials element")
        cred_elem = driver.find_element(By.ID, "login_credentials")
        self.highlight_and_click(cred_elem)
        self.highlight_and_click(cred_elem)  # second click
        self.highlight_and_click(cred_elem)  # third click

        # Additional clicks
        print("Clicking additional element")
        add_elem = driver.find_element(By.XPATH, "//div[@id='root']/div/div")
        self.highlight_and_click(add_elem)

        print("Clicking login button")
        self.highlight_and_click(login_btn)
        self.highlight_and_click(login_btn)

        print("Clicking random element")
        rand_elem = driver.find_element(By.XPATH, "//div[@id='root']/div")
        self.highlight_and_click(rand_elem)

        # SVG icon clicks
        print("Clicking SVG icon element")
        svg1 = driver.find_element(
            By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][2]"
        )
        self.highlight_and_click(svg1)

        svg2 = driver.find_element(
            By.XPATH,
            "(.//*[normalize-space(text()) and normalize-space(.)='Swag Labs'])[2]/following::*[name()='svg'][1]"
        )
        self.highlight_and_click(svg2)

        # More interactions
        print("Clicking more element")
        more_elem = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div")
        self.highlight_and_click(more_elem)

        # Clear password
        print("Clearing password")
        self.highlight_and_type(password_field, "")  # empty string clears

        # Click page
        page_elem = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div")
        self.highlight_and_click(page_elem)

        # Clear username
        print("Clearing username")
        self.highlight_and_type(username_field, "")

        # Final clicks
        print("Clicking login credentials element")
        self.highlight_and_click(cred_elem)

        final_elem1 = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div[2]/div")
        self.highlight_and_click(final_elem1)

        final_elem2 = driver.find_element(By.XPATH, "//div[@id='root']/div/div[2]/div[2]/div/div[2]")
        self.highlight_and_click(final_elem2)

        print("Test finished - browser will close in 2 seconds")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to.alert
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True


if __name__ == "__main__":
    unittest.main()