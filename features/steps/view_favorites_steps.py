from behave import given, then, when
from playwright.sync_api import expect



@given('I have not marked any books as favorites')
def step_impl(context):
    # This step is for ensuring a clean state, it's more of a placeholder
    # In a real application, you might have a "clear all" function
    pass

@given('I have marked "{book_title}" as a favorite')
def step_impl(context, book_title):
    context.pages.catalog_page.mark_book_as_favorite(book_title)

@then('I should see my favorite books')
def step_impl(context):
    from features.pages.utils import wait_for_element_with_retry, debug_page_state
    try:
        # Wait for page to load and favorite items to appear
        context.page.wait_for_load_state("networkidle")
        context.page.wait_for_timeout(2000)  # Additional wait for rendering
        # Try .book selector first (same as catalog)
        try:
            wait_for_element_with_retry(
                context.page,
                ".book",
                timeout=60000,
                retries=3,
                context="should_see_favorites"
            )
        except:
            # Fallback to favorite-book-item testid
            wait_for_element_with_retry(
                context.page,
                ".book",
                timeout=60000,
                retries=3,
                context="should_see_favorites"
            )
        favorite_count = context.pages.my_books_page.favorite_book_items.count()
        assert favorite_count > 0, f"Expected at least 1 favorite book, but found {favorite_count}"
    except Exception as e:
        debug_page_state(context.page, ".book", "should_see_favorites_failed")
        raise

@then('"{book_title}" should be in my list')
def step_impl(context, book_title):
    from features.pages.utils import wait_for_element_with_retry, debug_page_state
    try:
        # Wait for page to load and favorite items to appear
        context.page.wait_for_load_state("networkidle")
        context.page.wait_for_timeout(2000)  # Additional wait for rendering
        # Try .book selector first
        try:
            wait_for_element_with_retry(
                context.page,
                ".book",
                timeout=60000,
                retries=3,
                context="book_in_list"
            )
        except:
            # Fallback to favorite-book-item testid
            wait_for_element_with_retry(
                context.page,
                ".book",
                timeout=60000,
                retries=3,
                context="book_in_list"
            )
        favorite_titles = context.pages.my_books_page.get_favorite_book_titles()
        # Check if book_title is in the list (could be title or author)
        # Also check if any title contains the book_title (for partial matches)
        found = False
        for title in favorite_titles:
            if book_title in title or title in book_title:
                found = True
                break
        # Also check the full book text which includes author
        if not found:
            book_items = context.pages.my_books_page.favorite_book_items
            for i in range(book_items.count()):
                item_text = book_items.nth(i).inner_text()
                if book_title in item_text:
                    found = True
                    break
        assert found, f"'{book_title}' not found in favorite books list: {favorite_titles}"
    except Exception as e:
        debug_page_state(context.page, ".book", f"book_in_list_failed_{book_title}")
        raise

@then('I should see an empty list message')
def step_impl(context):
    # Wait for page to load
    context.page.wait_for_load_state("networkidle")
    context.page.wait_for_timeout(2000)
    is_empty = context.pages.my_books_page.is_empty_list_message_visible()
    assert is_empty, "Expected empty list message to be visible"