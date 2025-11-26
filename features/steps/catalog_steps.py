from behave import given, then, when
from playwright.sync_api import expect

@given('I am on the "Katalog" page')
def step_impl(context):
    # The page is already on the catalog by default from environment.py
    # This step is now just for declarative purposes.
    pass

@then('I should see a welcome header')
def step_impl(context):
    expect(context.pages.catalog_page.welcome_header).to_be_visible()

@then('I should see a list of books')
def step_impl(context):
    # Check that there is at least one book item
    expect(context.pages.catalog_page.book_items).to_have_count(5) # Assuming there are 5 default books