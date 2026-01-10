from behave import given, then, when
from playwright.sync_api import expect


@given('I have not marked any books as favorites')
def step_impl(context):
    """
    Ensures a clean state by navigating to the favorites page.
    The test framework clears the browser state before each scenario.
    """
    context.pages.base_page.navigate_to("Mina böcker")


@given('I have marked "{book_title}" as a favorite')
def step_impl(context, book_title):
    """
    Sets up the test state by marking a specific book as a favorite.
    """
    # First, ensure we are on the catalog page to see the books
    context.pages.base_page.navigate_to("Katalog")
    # Now, find the specific book and mark it as a favorite
    context.pages.catalog_page.mark_book_as_favorite(book_title)


@then('I should see my favorite books')
def step_impl(context):
    """
    Verifies that the list of favorite books is not empty.
    """
    favorite_titles = context.pages.my_books_page.get_favorite_book_titles()
    assert len(favorite_titles) > 0, "Expected to see at least one favorite book, but the list was empty."


@then('"{book_title}" should be in my list of favorites')
def step_impl(context, book_title):
    """
    Verifies that a specific book title is present in the list of favorite books.
    """
    favorite_titles = context.pages.my_books_page.get_favorite_book_titles()
    assert book_title in favorite_titles, \
        f"Expected '{book_title}' to be in the favorites list, but it was not. Found: {favorite_titles}"


@then('I should see an empty favorites list message')
def step_impl(context):
    """
    Verifies that the empty list message is visible.
    """
    expect(context.pages.my_books_page.empty_list_message).to_be_visible()
