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
    from features.pages.utils import wait_for_element_with_retry, debug_page_state
    try:
        # Wait for at least one book item to appear with retry
        wait_for_element_with_retry(
            context.page,
            ".book",
            timeout=60000,
            retries=3,
            context="should_see_books"
        )
        # Wait for network to be idle to ensure all books are loaded
        context.page.wait_for_load_state("networkidle")
        context.page.wait_for_timeout(2000)  # Additional wait for rendering
        # Check that there are book items (at least 1, typically 7 default books)
        book_count = context.pages.catalog_page.book_items.count()
        assert book_count > 0, f"Expected at least 1 book, but found {book_count}"
    except Exception as e:
        debug_page_state(context.page, ".book", "should_see_books_failed")
        raise