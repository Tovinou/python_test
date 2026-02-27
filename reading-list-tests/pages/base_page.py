from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate(self):
        # We assume base URL is handled or we pass it. 
        # But for simplicity, we can hardcode or pass in constructor.
        # Since it is a SPA, we might just navigate to root.
        self.page.goto("https://tap-vt25-testverktyg.github.io/exam--reading-list/")

    def get_nav_button(self, name):
        # name can be 'catalog', 'add-book', 'favorites'
        return self.page.get_by_test_id(name)

    def go_to_catalog(self):
        btn = self.get_nav_button("catalog")
        if not btn.is_disabled():
            btn.click()

    def go_to_add_book(self):
        btn = self.get_nav_button("add-book")
        if not btn.is_disabled():
            btn.click()

    def go_to_favorites(self):
        btn = self.get_nav_button("favorites")
        if not btn.is_disabled():
            btn.click()
