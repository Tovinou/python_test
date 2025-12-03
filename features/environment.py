from behave import *
from playwright.sync_api import sync_playwright, expect
import os

from features.pages.base_page import BasePage
from features.pages.add_book_page import AddBookPage
from features.pages.catalog_page import CatalogPage
from features.pages.my_books_page import MyBooksPage

# Define the base URL of the application to be tested
BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

def before_scenario(context, scenario):
    """
    Set up the browser and page objects before each scenario.
    """
    # Check for headless mode parameter from the command line
    headless = context.config.userdata.get("headless", "false").lower() == "true"
    
    playwright = sync_playwright().start()
    browser = playwright.chromium.launch(headless=headless)
    
    # Create a new browser context and page
    context.browser = browser.new_context()
    context.page = context.browser.new_page()
    
    # Set default timeout for all actions (60 seconds)
    context.page.set_default_timeout(60000)
    context.page.set_default_navigation_timeout(60000)
    
    # Navigate to the base URL before each scenario, waiting for the network to be idle
    context.page.goto(BASE_URL, wait_until="networkidle")
    # Additional wait to ensure JavaScript has fully loaded and rendered
    context.page.wait_for_load_state("domcontentloaded")
    # Give the page a moment for any dynamic content to render
    context.page.wait_for_timeout(2000)  # 2 second wait for SPA to initialize
    
    # Clear session storage before each scenario to ensure a clean state
    context.page.evaluate("() => sessionStorage.clear()")

    # Initialize page objects and attach them to the context
    context.pages = type('Pages', (), {})() # Create an empty object to hold page instances
    context.pages.base_page = BasePage(context.page)
    context.pages.add_book_page = AddBookPage(context.page)
    context.pages.catalog_page = CatalogPage(context.page)
    context.pages.my_books_page = MyBooksPage(context.page)
    
    # Store playwright instance for cleanup
    context.playwright = playwright

def after_scenario(context, scenario):
    """
    Clean up by closing the browser after each scenario.
    """
    if hasattr(context, 'page') and context.page:
        try:
            context.page.close()
        except Exception as e:
            print(f"Error closing page: {e}")
    
    if hasattr(context, 'browser') and context.browser:
        try:
            context.browser.close()
        except Exception as e:
            print(f"Error closing browser: {e}")
            
    if hasattr(context, 'playwright') and context.playwright:
        try:
            context.playwright.stop()
        except Exception as e:
            print(f"Error stopping playwright: {e}")