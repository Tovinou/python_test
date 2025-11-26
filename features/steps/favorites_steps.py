from behave import given, then, when
from playwright.sync_api import expect

@when('I mark "{book_title}" as a favorite')
def step_impl(context, book_title):
    context.pages.catalog_page.mark_book_as_favorite(book_title)

@then('"{book_title}" should be marked as a favorite')
def step_impl(context, book_title):
    assert context.pages.catalog_page.is_book_marked_as_favorite(book_title)

@given('"{book_title}" is marked as a favorite')
def step_impl(context, book_title):
    if not context.pages.catalog_page.is_book_marked_as_favorite(book_title):
        context.pages.catalog_page.mark_book_as_favorite(book_title)

@then('"{book_title}" should not be marked as a favorite')
def step_impl(context, book_title):
    assert not context.pages.catalog_page.is_book_marked_as_favorite(book_title)