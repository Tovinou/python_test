from behave import given, then, when
from playwright.sync_api import expect

@given('I am on the "Lägg till bok" page')
def step_impl(context):
    add_book_url = "https://tap-vt25-testverktyg.github.io/exam--reading-list/add-book"
    context.page.goto(add_book_url)
    expect(context.page).to_have_url(add_book_url)

@when('I add a new book with title "{title}" and author "{author}"')
def step_impl(context, title, author):
    context.pages.add_book_page.add_book(title, author)
    # Store the book details to check later
    context.added_book = {"title": title, "author": author}

@then('I should see a success message')
def step_impl(context):
    expect(context.pages.add_book_page.success_message).to_be_visible()
    expect(context.pages.add_book_page.success_message).to_contain_text("Boken har lagts till!")

@then('the book should be added to the catalog')
def step_impl(context):
    # Navigate to the catalog to verify
    context.pages.base_page.navigate_to("Katalog")
    catalog_titles = context.pages.catalog_page.get_book_titles()
    assert context.added_book["title"] in catalog_titles

@then('the book should not be added to the catalog')
def step_impl(context):
    # Navigate to the catalog to verify
    context.pages.base_page.navigate_to("Katalog")
    catalog_titles = context.pages.catalog_page.get_book_titles()
    # The book with an empty title should not be there
    assert "" not in catalog_titles