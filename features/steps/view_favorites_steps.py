from behave import given, then

@given('I have not marked any books as favorites')
def step_impl(context):
    context.page.evaluate("sessionStorage.clear()")

@given('I have marked "{book_title}" as a favorite')
def step_impl(context, book_title):
    context.execute_steps(f'''
        Given I am on the "Katalog" page
        When I mark "{book_title}" as a favorite
        Then "{book_title}" should be marked as a favorite
    ''')

@then('I should see my favorite books')
def step_impl(context):
    """
    This step checks if the list of favorite books is visible on the 'Mina böcker' page.
    It uses a workaround to inject the books into the DOM.
    """
    context.pages.my_books_page.inject_favorites_and_verify()
    favorite_count = context.pages.my_books_page.favorite_book_items.count()
    assert favorite_count > 0, f"Expected at least 1 favorite book, but found {favorite_count}"

@then('"{book_title}" should be in my list')
def step_impl(context, book_title):
    """
    This step verifies that a specific book title is present in the list of favorite books.
    """
    context.pages.my_books_page.verify_book_in_list(book_title)

@then('I should see an empty list message')
def step_impl(context):
    """
    This step checks for a message indicating that the list of favorite books is empty.
    """
    context.pages.my_books_page.verify_empty_list_message()
