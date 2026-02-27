from .base_page import BasePage

class AddBookPage(BasePage):
    def enter_title(self, title):
        self.page.get_by_test_id("add-input-title").fill(title)

    def enter_author(self, author):
        self.page.get_by_test_id("add-input-author").fill(author)

    def submit_book(self):
        # Based on inspection, button text is "Lägg till ny bok"
        # Or we can look for the button inside the form/main area.
        self.page.get_by_role("button", name="Lägg till ny bok").click()

    def add_new_book(self, title, author):
        self.enter_title(title)
        self.enter_author(author)
        self.submit_book()
