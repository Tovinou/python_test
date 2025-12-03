from playwright.sync_api import Page, expect
from .base_page import BasePage
from .utils import wait_for_element_with_retry, retry_with_fallback, debug_page_state

class AddBookPage(BasePage):
    """
    Page Object for the Add Book page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_input = page.locator("[data-testid='book-title-input']")
        self.author_input = page.locator("[data-testid='book-author-input']")
        self.submit_button = page.get_by_role("button", name="Lägg till ny bok")
        # A more robust selector for the success message
        self.success_message = page.locator("div:has-text('Boken har lagts till!')")

    def add_book(self, title: str, author: str):
        """
        Fill out the form and submit to add a new book.
        """
        try:
            # Wait for page to be ready
            self.page.wait_for_load_state("domcontentloaded")
            self.page.wait_for_timeout(2000)  # Wait for SPA to render
            
            # Wait for form elements with retry and fallback selectors
            title_input = retry_with_fallback(
                self.page,
                "[data-testid='book-title-input']",
                [
                    "input[name*='title']",
                    "input[placeholder*='title']",
                    "input[type='text']:first-of-type"
                ],
                lambda loc: loc,
                timeout=60000,
                context="title_input"
            )
            
            author_input = retry_with_fallback(
                self.page,
                "[data-testid='book-author-input']",
                [
                    "input[name*='author']",
                    "input[placeholder*='author']",
                    "input[type='text']:last-of-type"
                ],
                lambda loc: loc,
                timeout=60000,
                context="author_input"
            )
            
            if title:
                title_input.fill(title)
            author_input.fill(author)
            
            # Only click if the button is enabled
            if self.submit_button.is_enabled():
                self.submit_button.click()
                # Wait for network to be idle after submission
                self.page.wait_for_load_state("networkidle")
                self.page.wait_for_timeout(1000)  # Additional wait for UI update

        except Exception as e:
            debug_page_state(self.page, "[data-testid='book-title-input']", "add_book_error")
            raise

    def get_success_message_text(self) -> str:
        """
        Get the text of the success message after adding a book.
        """
        return self.success_message.inner_text()