from behave import given, when, then
from playwright.sync_api import expect

@when('jag går till sidan för att lägga till bok')
def step_impl(context):
    context.catalog_page.go_to_add_book()

@when('jag anger titeln "{title}"')
def step_impl(context, title):
    context.add_book_page.enter_title(title)

@when('jag anger författaren "{author}"')
def step_impl(context, author):
    context.add_book_page.enter_author(author)

@when('jag sparar boken')
def step_impl(context):
    context.add_book_page.submit_book()
