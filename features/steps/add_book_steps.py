from behave import given, then, when
from playwright.sync_api import expect


@given('I am on the "Lägg till bok" page')
def step_impl(context):
    context.pages.base_page.navigate_to("Lägg till bok")
    expect(context.pages.add_book_page.title_input).to_be_visible()


@when('I try to add a new book with title "{title}" and author "{author}"')
def step_impl(context, title, author):
    effective_title = "" if title == "<EMPTY>" else title
    context.pages.add_book_page.add_book(effective_title, author)
    context.added_book = {"title": effective_title, "author": author}


@when('I add a new book with title "{title}" and author "{author}"')
def step_impl(context, title, author):
    context.pages.add_book_page.add_book(title, author)
    context.added_book = {"title": title, "author": author}


@then('the "Lägg till ny bok" button should be disabled')
def step_impl(context):
    expect(context.pages.add_book_page.submit_button).to_be_disabled()


@then('the book should be added to my books')
def step_impl(context):
    # After adding a book, it appears in the catalog
    # To see it in "Mina böcker", we need to mark it as favorite first
    context.pages.base_page.navigate_to("Katalog")
    book_title = context.added_book["title"]
    # Mark the book as favorite
    context.pages.catalog_page.mark_book_as_favorite(book_title)
    # Now navigate to "Mina böcker" and verify it's there
    context.pages.base_page.navigate_to("Mina böcker")
    # The book should appear in the favorites list
    expect(context.page.locator(f"text={book_title}")).to_be_visible()


@then('the book should not be added to my books')
def step_impl(context):
    context.pages.base_page.navigate_to("Mina böcker")
    book_title = context.added_book["title"]
    expect(context.page.locator(f"//h3[text()='{book_title}']")).not_to_be_visible()
