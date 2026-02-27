from behave import given, when, then
from playwright.sync_api import expect

@when('jag klickar på hjärtat för boken "{title}"')
def step_impl(context, title):
    context.catalog_page.toggle_favorite(title)

@then('ska boken "{title}" finnas under "Mina böcker"')
def step_impl(context, title):
    context.catalog_page.go_to_favorites()
    expect(context.page.get_by_text(title)).to_be_visible()

@given('jag har lagt till boken "{title}" som favorit')
def step_impl(context, title):
    context.catalog_page.navigate()
    context.catalog_page.toggle_favorite(title)

@given('boken "{title}" är inte favorit')
def step_impl(context, title):
    context.catalog_page.navigate()
    # Vi antar att startläget är att den inte är favorit. 
    # Om vi ville vara säkra kunde vi kolla om den finns i favoriter först och ta bort den.
    # Men eftersom varje scenario körs i en ny kontext (browser context) är state återställt.
    pass

@when('jag tar bort favoriten "{title}"')
def step_impl(context, title):
    context.catalog_page.go_to_catalog()
    context.catalog_page.toggle_favorite(title)

@then('ska boken "{title}" inte finnas under "Mina böcker"')
def step_impl(context, title):
    context.catalog_page.go_to_favorites()
    expect(context.page.get_by_text(title)).not_to_be_visible()

@when('jag går till "Mina böcker"')
def step_impl(context):
    context.catalog_page.go_to_favorites()

@then('ska jag se boken "{title}" i listan')
def step_impl(context, title):
    expect(context.page.get_by_text(title)).to_be_visible()
