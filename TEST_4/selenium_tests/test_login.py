import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Run in headless mode for CI/CD environments
    options.add_argument("--headless") 
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_successful_login(driver):
    """
    Test case 1 (G): Successful login with correct credentials.
    """
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    # Verify we are on the inventory page
    assert "inventory.html" in driver.current_url
    assert driver.find_element(By.CLASS_NAME, "title").text == "Products"

def test_invalid_username(driver):
    """
    Test case 2 (VG): Invalid username shows error message.
    """
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("wrong_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message

def test_invalid_password(driver):
    """
    Test case 3 (VG): Invalid password shows error message.
    """
    driver.get("https://www.saucedemo.com/")
    
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("wrong_pass")
    driver.find_element(By.ID, "login-button").click()
    
    error_message = driver.find_element(By.CSS_SELECTOR, "[data-test='error']").text
    assert "Epic sadface: Username and password do not match any user in this service" in error_message
