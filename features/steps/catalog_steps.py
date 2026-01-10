from behave import given, then, when
from playwright.sync_api import expect


@given('I am on the "Katalog" page')
def step_impl(context):
    """
    Declarative step to state that tests start on the catalog page.
    The actual navigation is handled in environment.py.
    """
    # To be certain, we can verify the welcome header is visible.
    expect(context.pages.catalog_page.welcome_header).to_be_visible()


@then('I should see a welcome header')
def step_impl(context):
    """
    Verifies that the main welcome header is visible.
    """
    expect(context.pages.catalog_page.welcome_header).to_be_visible()


@then('I should see a list of books')
def step_impl(context):
    """
    Verifies that at least one book item is visible on the page.
    """
    # We expect the first element with class "book" to be visible.
    # Playwright's expect will auto-wait for it to appear.
    expect(context.pages.catalog_page.book_items.first).to_be_visible()