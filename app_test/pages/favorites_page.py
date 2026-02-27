from .base_page import BasePage

class FavoritesPage(BasePage):
    def get_favorite_books(self):
        # Similar to catalog, but in favorites view.
        # We can reuse logic or check for specific elements.
        # Assuming the structure is similar (list of .book)
        return self.page.locator(".book").all_text_contents()

    def is_book_in_favorites(self, title):
        # Check if the title is visible in the list
        # We might want to ensure we are strictly in the favorites list.
        # Since it's a SPA, the DOM might just change content of main.
        return self.page.get_by_text(title).is_visible()
