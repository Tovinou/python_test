from playwright.sync_api import expect

BASE_URL = "https://tap-vt25-testverktyg.github.io/exam--reading-list/"

def test_navigation_clicks_and_dom(page):
    page.goto(BASE_URL)
    page.get_by_test_id("add-book").click()
    expect(page.get_by_test_id("add-input-title")).to_be_visible()
    expect(page.get_by_test_id("add-input-author")).to_be_visible()
    expect(page.get_by_role("button", name="Lägg till ny bok")).to_be_visible()
    page.get_by_test_id("favorites").click()
    expect(page.get_by_test_id("favorites")).to_be_disabled()
    page.get_by_test_id("catalog").click()
    expect(page.locator(".book").first).to_be_visible()
