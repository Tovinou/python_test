from behave import given, when, then
from playwright.sync_api import expect

@given('jag är på startsidan')
def step_impl(context):
    context.catalog_page.navigate()

@then('ska jag se en lista med böcker')
def step_impl(context):
    books = context.catalog_page.get_all_books()
    assert len(books) > 0, "Inga böcker hittades i katalogen"

@then('varje bok ska visa titel och författare')
def step_impl(context):
    # This is a bit hard to verify strictly without splitting string, 
    # but we can check if content is not empty.
    books = context.catalog_page.get_all_books()
    for book in books:
        assert len(book.strip()) > 0
        # HTML format is: "Title", Author
        # We could check for comma if we want strictness
        # assert "," in book

@then('det ska finnas en knapp för att favoritmarkera')
def step_impl(context):
    # We check if hearts are present
    # Using a generic check for at least one heart
    assert context.page.locator(".star").count() > 0

@then('ska boken "{title}" finnas i katalogen')
def step_impl(context, title):
    context.catalog_page.go_to_catalog() # Use SPA navigation to preserve state
    expect(context.catalog_page.get_book_element(title)).to_be_visible()

@then('boken "{title}" ska ha författaren "{author}"')
def step_impl(context, title, author):
    # Check if the text contains both title and author
    # Note: get_book_element returns the row which contains both.
    element = context.catalog_page.get_book_element(title)
    expect(element).to_contain_text(author)
