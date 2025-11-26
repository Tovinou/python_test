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
    
    # Navigate to the base URL before each scenario, waiting for the network to be idle
    context.page.goto(BASE_URL, wait_until="networkidle")
    
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
    context.page.close()
    context.browser.close()
    context.playwright.stop()