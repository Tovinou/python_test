from playwright.sync_api import sync_playwright
from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage
from pages.favorites_page import FavoritesPage

def before_all(context):
    context.playwright = sync_playwright().start()
    # Launch browser once. Use headless=True for speed.
    context.browser = context.playwright.chromium.launch(headless=True)

def after_all(context):
    context.browser.close()
    context.playwright.stop()

def before_scenario(context, scenario):
    # Create a new context and page for each scenario to ensure isolation
    context.browser_context = context.browser.new_context()
    context.page = context.browser_context.new_page()
    
    # Initialize Page Objects
    context.catalog_page = CatalogPage(context.page)
    context.add_book_page = AddBookPage(context.page)
    context.favorites_page = FavoritesPage(context.page)
    
    # Default navigation to base page could be done here if needed
    # context.catalog_page.navigate()

def after_scenario(context, scenario):
    context.browser_context.close()
