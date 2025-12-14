from playwright.sync_api import Page
from .base_page import BasePage


class AddBookPage(BasePage):
    """
    Page Object for the Add Book page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_input = page.locator("[data-testid='book-title-input']")
        self.author_input = page.locator("[data-testid='book-author-input']")
        self.submit_button = page.get_by_role("button", name="Lägg till ny bok")
        self.success_message = page.locator("div:has-text('Boken har lagts till!')")

    def add_book(self, title: str, author: str):
        """
        Fill out the form and submit to add a new book.
        """
        if title:
            self.title_input.fill(title)
        self.author_input.fill(author)
        self.submit_button.click()

    def get_success_message_text(self) -> str:
        """
        Get the text of the success message after adding a book.
        """
        return self.success_message.inner_text()
