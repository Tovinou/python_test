from playwright.sync_api import Page, expect
from .base_page import BasePage

class CatalogPage(BasePage):
    """
    Page Object for the Book Catalog page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_header = page.get_by_role("heading", name="Välkommen!")
        self.book_items = page.locator("[data-testid='book-item']")

    def get_book_titles(self) -> list[str]:
        """
        Get a list of all book titles currently displayed in the catalog.
        """
        # This selector assumes each book item has a title element with a testid
        title_locators = self.book_items.locator("[data-testid='book-title']")
        return title_locators.all_inner_texts()

    def mark_book_as_favorite(self, book_title: str):
        """
        Mark a specific book as a favorite.
        """
        # Find the book item by its title and then click its favorite button
        book_item = self.book_items.filter(has_text=book_title)
        favorite_button = book_item.locator("[data-testid='favorite-button']")
        favorite_button.click()

    def is_book_marked_as_favorite(self, book_title: str) -> bool:
        """
        Check if a specific book is marked as a favorite.
        """
        book_item = self.book_items.filter(has_text=book_title)
        favorite_button = book_item.locator("[data-testid='favorite-button']")
        # This assumes the button has an attribute or class that changes when favorited.
        # For this example, let's assume it gets an 'aria-pressed="true"' attribute.
        return favorite_button.get_attribute("aria-pressed") == "true"
