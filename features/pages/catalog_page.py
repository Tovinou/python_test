from playwright.sync_api import Page, Locator
from .base_page import BasePage
import re


class CatalogPage(BasePage):
    """
    Page Object for the Book Catalog page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_header = page.get_by_role("heading", name="Välkommen!")
        self.book_items = page.locator(".book")

    def get_book_titles(self) -> list[str]:
        """
        Get a list of all book titles currently displayed in the catalog.
        """
        book_texts = self.book_items.all_inner_texts()
        titles = []
        for text in book_texts:
            match = re.search(r'"(.*?)"', text)
            if match:
                titles.append(match.group(1))
            else:
                titles.append(text.replace('❤', '').replace('⭐', '').replace('\ufe0f', '').strip())
        return titles

    def _find_book_item(self, book_identifier: str) -> Locator:
        """
        Finds the book item locator that contains the given text.
        """
        return self.book_items.filter(has_text=book_identifier).first

    def mark_book_as_favorite(self, book_identifier: str):
        """
        Mark a specific book as a favorite by clicking its star button.
        """
        book_item = self._find_book_item(book_identifier)
        favorite_button = book_item.locator("[data-testid^='star-']")
        favorite_button.click()

    def is_book_marked_as_favorite(self, book_identifier: str) -> bool:
        """
        Check if a specific book is marked as a favorite by checking if
        the star button has the 'selected' class.
        """
        book_item = self._find_book_item(book_identifier)
        favorite_button = book_item.locator("[data-testid^='star-']")
        class_attr = favorite_button.get_attribute("class") or ""
        return "selected" in class_attr

