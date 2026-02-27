from behave import when, then
from playwright.sync_api import expect

def _map_link_text_to_testid(text):
    if text == "Lägg till bok":
        return "add-book"
    if text == "Mina böcker":
        return "favorites"
    if text == "Katalog":
        return "catalog"
    raise ValueError(f"Okänd länktext: {text}")

@when('jag klickar på navigation "{link_text}"')
def step_impl(context, link_text):
    testid = _map_link_text_to_testid(link_text)
    btn = context.page.get_by_test_id(testid)
    if not btn.is_disabled():
        btn.click()

@then('ska vyn visa "{expected_view}"')
def step_impl(context, expected_view):
    if expected_view == "Lägg till bok":
        expect(context.page.get_by_test_id("add-input-title")).to_be_visible()
        expect(context.page.get_by_test_id("add-input-author")).to_be_visible()
        expect(context.page.get_by_role("button", name="Lägg till ny bok")).to_be_visible()
        return
    if expected_view == "Mina böcker":
        expect(context.page.get_by_test_id("favorites")).to_be_disabled()
        return
    if expected_view == "Katalog":
        expect(context.page.locator(".book").first).to_be_visible()
        return
    raise ValueError(f"Okänd vy: {expected_view}")
