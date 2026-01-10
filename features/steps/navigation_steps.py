from behave import given, then, when
from playwright.sync_api import expect


@given('I am on the start page')
def step_impl(context):
    # The before_scenario hook already navigates to the start page.
    # This step is just for readability.
    pass


@when('I navigate to the "{page_name}" page')
def step_impl(context, page_name):
    """
    Navigates to the specified page using the main navigation.
    """
    context.pages.base_page.navigate_to(page_name)


@then('I should be on the "Katalog" page')
def step_impl(context):
    expect(context.pages.catalog_page.welcome_header).to_be_visible()


@then('I should be on the "Lägg till bok" page')
def step_impl(context):
    expect(context.pages.add_book_page.title_input).to_be_visible()


@then('I should be on the "Mina böcker" page')
def step_impl(context):
    # The page shows "Välkommen!" heading, which is also on catalog page
    # But we can verify we're on the right page by checking the navigation button is disabled
    expect(context.pages.base_page.nav_mina_bocker).to_be_disabled()
