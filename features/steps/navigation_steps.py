from behave import then, when
from playwright.sync_api import expect

@when('I navigate to the "{page_name}" page')
def step_impl(context, page_name):
    context.pages.base_page.navigate_to(page_name)

@then('the URL should contain "{url_fragment}"')
def step_impl(context, url_fragment):
    expect(context.page).to_have_url(url_fragment)