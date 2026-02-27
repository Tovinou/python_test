from .base_page import BasePage

class CatalogPage(BasePage):
    def get_book_element(self, title):
        # We find the book div that contains the title.
        # Based on HTML: <div class="book">... "Title", Author ...</div>
        # But wait, the star has a testid: "star-Title"
        # We can use that to find the specific book row/card if needed.
        # Or just verify text is visible.
        return self.page.get_by_text(title)

    def is_book_visible(self, title):
        return self.get_book_element(title).is_visible()

    def toggle_favorite(self, title):
        # testid is "star-Title"
        # We need to be careful with exact title matching in testid
        self.page.get_by_test_id(f"star-{title}").click()

    def get_all_books(self):
        return self.page.locator(".book").all_text_contents()
