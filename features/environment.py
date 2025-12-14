from playwright.sync_api import sync_playwright

from features.pages.base_page import BasePage
from features.pages.add_book_page import AddBookPage
from features.pages.catalog_page import CatalogPage
from features.pages.my_books_page import MyBooksPage

# Define the base URL of the application to be tested
BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"


def before_all(context):
    """
    Launch the browser and create a context once for all scenarios.
    """
    headless = context.config.userdata.get("headless", "false").lower() == "true"
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)
    context.browser_context = context.browser.new_context()


def after_all(context):
    """
    Close the browser and stop Playwright after all scenarios are done.
    """
    if hasattr(context, 'browser_context') and context.browser_context:
        context.browser_context.close()
    if hasattr(context, 'playwright') and context.playwright:
        context.playwright.stop()


def before_scenario(context, scenario):
    """
    Create a new page for each scenario and navigate to the base URL.
    This is much faster than creating a new browser for each scenario.
    """
    context.page = context.browser_context.new_page()
    context.page.goto(BASE_URL)

    # Initialize page objects and attach them to the context
    context.pages = type('Pages', (), {})()
    context.pages.base_page = BasePage(context.page)
    context.pages.add_book_page = AddBookPage(context.page)
    context.pages.catalog_page = CatalogPage(context.page)
    context.pages.my_books_page = MyBooksPage(context.page)


def after_scenario(context, scenario):
    """
    Clean up by closing the page after each scenario.
    """
    if hasattr(context, 'page') and context.page:
        context.page.close()
