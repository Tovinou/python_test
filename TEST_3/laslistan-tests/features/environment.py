from playwright.sync_api import sync_playwright
from features.pages.catalog_page import CatalogPage
from features.pages.add_book_page import AddBookPage
from features.pages.favorites_page import MyBooksPage

BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

def before_all(context):
    headless = context.config.userdata.get("headless", "false").lower() == "true"
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(headless=headless)
    context.ctx = context.browser.new_context()
    context.page = context.ctx.new_page()
    context.page.set_default_timeout(1000)
    context.page.set_default_navigation_timeout(2000)
    context.page.goto(BASE_URL)

def after_all(context):
    try:
        context.page.close()
        context.ctx.close()
        context.browser.close()
    finally:
        context.playwright.stop()

def before_scenario(context, scenario):
    context.page.goto(BASE_URL)

    context.base_url = BASE_URL
    context.catalog_page = CatalogPage(context.page, BASE_URL)
    context.add_book_page = AddBookPage(context.page, BASE_URL)
    my_books = MyBooksPage(context.page)
    context.my_books_page = my_books
    context.favorites_page = my_books

def after_scenario(context, scenario):
    pass
