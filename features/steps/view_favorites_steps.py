from behave import given, then, when
from playwright.sync_api import expect

@given('I have marked "{book_title}" as a favorite')
def step_impl(context, book_title):
    context.pages.catalog_page.mark_book_as_favorite(book_title)

@given('I have not marked any books as favorites')
def step_impl(context):
    # This step is for ensuring a clean state, it's more of a placeholder
    # In a real application, you might have a "clear all" function
    pass

@then('I should see my favorite books')
def step_impl(context):
    expect(context.pages.my_books_page.favorite_book_items).to_have_count_greater_than(0)

@then('"{book_title}" should be in my list')
def step_impl(context, book_title):
    favorite_titles = context.pages.my_books_page.get_favorite_book_titles()
    assert book_title in favorite_titles

@then('I should see an empty list message')
def step_impl(context):
    expect(context.pages.my_books_page.is_empty_list_message_visible()).to_be_true()