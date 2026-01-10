from playwright.sync_api import Page
from .base_page import BasePage
import re


class MyBooksPage(BasePage):
    """
    Page Object for the My Books (Favorites) page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        # The page uses "Välkommen!" as heading, but shows "Dina favoriter:" when there are favorites
        self.header = page.locator("text=Dina favoriter:").or_(page.get_by_role("heading", name="Välkommen!"))
        self.favorite_book_items = page.locator(".book")
        # The actual empty message text is slightly different
        self.empty_list_message = page.locator("text=När du valt, kommer dina favoritböcker att visas här.")

    def get_favorite_book_titles(self) -> list[str]:
        """
        Get a list of all favorite book titles displayed on the page.
        """
        if not self.favorite_book_items.first.is_visible():
            return []

        book_elements = self.favorite_book_items.all()
        titles = []
        for book_element in book_elements:
            text_content = book_element.inner_text()
            match = re.search(r'"(.*?)"', text_content)
            if match:
                titles.append(match.group(1))
            else:
                titles.append(text_content.strip())
        return titles

    def is_empty_message_visible(self) -> bool:
        """
        Check if the message for an empty favorites list is visible.
        """
        return self.empty_list_message.is_visible()
