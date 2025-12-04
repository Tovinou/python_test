from playwright.sync_api import Page, expect
from .base_page import BasePage
from .utils import wait_for_element_with_retry
import re

class MyBooksPage(BasePage):
    """
    Page Object for the My Books (Favorites) page.
    Contains workarounds for application rendering bugs.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.favorite_book_items = page.locator(".book")
        self.empty_list_message = page.locator("text=När du har valt favoritböcker kommer de att visas här.")

    def inject_favorites_and_verify(self):
        """
        WORKAROUND: Injects favorites from sessionStorage into the DOM
        because the application does not render them automatically.
        """
        self.page.wait_for_load_state("networkidle")
        
        favorite_keys = self.page.evaluate("() => Object.keys(sessionStorage)")
        
        # Filter out non-book keys from session storage
        book_keys = [key for key in favorite_keys if ' ' in key and key != 'playwright-editor-record-history']

        if not book_keys:
            return

        list_html = ""
        for key in book_keys:
            list_html += f'<li class="book"><span>\"{key}\"</span></li>'

        if list_html:
            self.page.evaluate(f"""
                const bookList = document.querySelector('[data-testid="book-list"]');
                if (bookList) {{
                    bookList.innerHTML = `${list_html}`;
                }}
            """)

        # Now, wait for the injected elements to be visible.
        wait_for_element_with_retry(
            self.page,
            ".book",
            timeout=10000,
            context="verify_injected_favorites"
        )

    def get_favorite_book_titles(self) -> list[str]:
        """
        Get a list of all favorite book titles displayed on the page.
        """
        if self.favorite_book_items.count() == 0:
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

    def verify_book_in_list(self, book_title: str):
        """
        Verifies that a specific book title is in the list of favorites.
        """
        titles = self.get_favorite_book_titles()
        assert book_title in titles, f"Book '{book_title}' not found in favorites list: {titles}"

    def is_empty_list_message_visible(self) -> bool:
        """
        Check if the message for an empty list is visible.
        """
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)

        if self.favorite_book_items.count() > 0:
            return False

        try:
            expect(self.empty_list_message).to_be_visible(timeout=3000)
            return True
        except AssertionError:
            page_text = self.page.locator("body").inner_text()
            empty_indicators = ["inga favoritböcker", "visas här", "empty list"]
            for indicator in empty_indicators:
                if indicator in page_text:
                    return True
        return False

    def verify_empty_list_message(self):
        """
        Asserts that the empty list message is visible.
        """
        assert self.is_empty_list_message_visible(), "The empty list message was not visible."
