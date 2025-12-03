from behave import given, then, when
from playwright.sync_api import expect

@given('I am on the "Lägg till bok" page')
def step_impl(context):
    # Navigate using the navigation button instead of direct URL to avoid 404 errors
    # The page should already be on the root URL from environment.py
    context.pages.base_page.navigate_to("Lägg till bok")
    # Wait for the page to be ready
    context.page.wait_for_load_state("networkidle")
    context.page.wait_for_timeout(2000)  # Wait for SPA to render
    
    # Verify we're on the add-book page by checking for form elements
    # Try multiple selectors since SPA might not change URL
    from features.pages.utils import retry_with_fallback
    
    try:
        # Try the testid selector first
        retry_with_fallback(
            context.page,
            "[data-testid='book-title-input']",
            [
                "input[name*='title']",
                "input[placeholder*='title']",
                "input[placeholder*='Titel']",
                "input[type='text']:first-of-type",
                "label:has-text('Titel') + input",
            ],
            lambda loc: loc.wait_for(state="visible", timeout=10000),
            timeout=15000,
            context="add_book_page_title_input"
        )
    except:
        # If testid fails, try finding by label text and nearby input
        try:
            title_label = context.page.get_by_text("Titel", exact=False)
            if title_label.count() > 0:
                # Find input near the label
                context.page.wait_for_selector("input[type='text']", timeout=5000)
        except:
            # Last resort: check for submit button to confirm we're on add-book page
            submit_btn = context.page.get_by_role("button", name="Lägg till ny bok")
            submit_btn.wait_for(state="visible", timeout=5000)

@when('I add a new book with title "{title}" and author "{author}"')
def step_impl(context, title, author):
    # If the title is "<EMPTY>", treat it as an empty string
    effective_title = "" if title == "<EMPTY>" else title
    context.pages.add_book_page.add_book(effective_title, author)
    context.added_book = {"title": effective_title, "author": author}



@then('the "Lägg till ny bok" button should be disabled')
def step_impl(context):
    expect(context.pages.add_book_page.submit_button).to_be_disabled()


@then('the book should be added to the catalog')
def step_impl(context):
    from features.pages.utils import wait_for_element_with_retry, debug_page_state
    # Navigate to the catalog to verify
    context.pages.base_page.navigate_to("Katalog")
    try:
        # Wait for book items to be visible before getting titles with retry
        wait_for_element_with_retry(
            context.page,
            ".book",
            timeout=60000,
            retries=3,
            context="book_added_to_catalog"
        )
        context.page.wait_for_load_state("networkidle")
        context.page.wait_for_timeout(2000)  # Additional wait for rendering
        catalog_titles = context.pages.catalog_page.get_book_titles()
        assert context.added_book["title"] in catalog_titles
    except Exception as e:
        debug_page_state(context.page, ".book", "book_added_to_catalog_failed")
        raise

@then('the book should not be added to the catalog')
def step_impl(context):
    from features.pages.utils import wait_for_element_with_retry, debug_page_state
    # Navigate to the catalog to verify
    context.pages.base_page.navigate_to("Katalog")
    try:
        # Wait for book items to be visible before getting titles with retry
        wait_for_element_with_retry(
            context.page,
            ".book",
            timeout=60000,
            retries=3,
            context="book_not_added_to_catalog"
        )
        context.page.wait_for_load_state("networkidle")
        context.page.wait_for_timeout(2000)  # Additional wait for rendering
        catalog_titles = context.pages.catalog_page.get_book_titles()
        # The book with an empty title should not be there
        assert "" not in catalog_titles
    except Exception as e:
        debug_page_state(context.page, ".book", "book_not_added_to_catalog_failed")
        raise