from playwright.sync_api import sync_playwright
from pages.catalog_page import CatalogPage
from pages.add_book_page import AddBookPage
from pages.favorites_page import FavoritesPage

def before_all(context):
    context.playwright = sync_playwright().start()
    headless_opt = str(context.config.userdata.get("headless", "true")).lower() in ("true", "1", "yes")
    slowmo_val = int(context.config.userdata.get("slowmo", "0"))
    keep_open_opt = str(context.config.userdata.get("keep_open", "false")).lower() in ("true", "1", "yes")
    context.keep_open = keep_open_opt
    context.browser = context.playwright.chromium.launch(headless=headless_opt, slow_mo=slowmo_val)

def after_all(context):
    if not getattr(context, "keep_open", False):
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
    if not getattr(context, "keep_open", False):
        context.browser_context.close()
