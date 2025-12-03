from behave import given, then, when
from playwright.sync_api import expect

@when('I mark "{book_title}" as a favorite')
def step_impl(context, book_title):
    context.pages.catalog_page.mark_book_as_favorite(book_title)

@then('"{book_title}" should be marked as a favorite')
def step_impl(context, book_title):
    is_favorite = context.pages.catalog_page.is_book_marked_as_favorite(book_title)
    assert is_favorite, f"Expected '{book_title}' to be marked as favorite, but it is not"

@given('"{book_title}" is marked as a favorite')
def step_impl(context, book_title):
    if not context.pages.catalog_page.is_book_marked_as_favorite(book_title):
        context.pages.catalog_page.mark_book_as_favorite(book_title)

@then('"{book_title}" should not be marked as a favorite')
def step_impl(context, book_title):
    is_favorite = context.pages.catalog_page.is_book_marked_as_favorite(book_title)
    assert not is_favorite, f"Expected '{book_title}' to NOT be marked as favorite, but it is marked as favorite"

@when('I mark "{book_title}" as a favorite again')
def step_impl(context, book_title):
    # Toggle the favorite status (click again to unmark)
    context.pages.catalog_page.mark_book_as_favorite(book_title)