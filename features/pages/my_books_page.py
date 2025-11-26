from playwright.sync_api import Page, expect
from .base_page import BasePage

class MyBooksPage(BasePage):
    """
    Page Object for the My Books (Favorites) page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_header = page.get_by_role("heading", name="Välkommen!")
        self.favorite_book_items = page.locator("[data-testid='favorite-book-item']")
        self.empty_list_message = page.locator("[data-testid='empty-list-message']")

    def get_favorite_book_titles(self) -> list[str]:
        """
        Get a list of all favorite book titles.
        """
        title_locators = self.favorite_book_items.locator("[data-testid='book-title']")
        return title_locators.all_inner_texts()

    def is_empty_list_message_visible(self) -> bool:
        """
        Check if the message for an empty list is visible.
        """
        return self.empty_list_message.is_visible()