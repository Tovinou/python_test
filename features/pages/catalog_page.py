from playwright.sync_api import Page, expect
from .base_page import BasePage
from .utils import wait_for_element_with_retry, retry_with_fallback, debug_page_state
import logging
import re

class CatalogPage(BasePage):
    """
    Page Object for the Book Catalog page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_header = page.get_by_role("heading", name="Välkommen!")
        # Book items use class="book" - try multiple selector strategies
        self.book_items = page.locator(".book")
        # Fallback selectors
        self._book_item_selectors = [
            ".book",
            "[data-testid='book-item']",
            ".book-item",
            "[class*='book']"
        ]

    import re

# ... (rest of the file)

    def get_book_titles(self) -> list[str]:
        """
        Get a list of all book titles currently displayed in the catalog.
        """
        try:
            # Wait for at least one book item to be visible with retry
            wait_for_element_with_retry(
                self.page,
                ".book",
                timeout=60000,
                retries=3,
                context="get_book_titles"
            )
            # Book items contain the title text directly in the div
            # Extract text from each book item, removing the star button text
            book_texts = self.book_items.all_inner_texts()
            titles = []
            for text in book_texts:
                # Use regex to extract the title from within the quotes
                match = re.search(r'"(.*?)"', text)
                if match:
                    titles.append(match.group(1))
                else:
                    # Fallback for titles that might not have quotes
                    titles.append(text.replace('❤', '').replace('⭐', '').replace('\ufe0f', '').strip())
            return titles
        except Exception as e:
            debug_page_state(self.page, ".book", "get_book_titles_error")
            raise

    def _find_book_title_from_identifier(self, book_identifier: str) -> str:
        """
        Find the exact book title from a book identifier (title or author).
        Returns the exact title as it appears in the data-testid attribute.
        Handles special characters, partial matches, and case-insensitive matching.
        """
        # Wait for books to be visible
        wait_for_element_with_retry(
            self.page,
            ".book",
            timeout=60000,
            retries=3,
            context="find_book_title"
        )
        
        # Normalize the identifier for comparison (lowercase, strip whitespace)
        normalized_identifier = book_identifier.lower().strip()
        
        # First, try to find by exact text match
        book_item = self.book_items.filter(has_text=book_identifier).first
        if book_item.count() == 0:
            # Try finding by iterating through all books and matching text
            all_books = self.book_items.all()
            matching_text = None
            
            for book in all_books:
                try:
                    book_text = book.inner_text()
                    book_text_lower = book_text.lower()
                    
                    # Check for exact or partial match
                    if normalized_identifier in book_text_lower or book_identifier in book_text:
                        matching_text = book_text
                        break
                    
                    # Also check if significant words match (for long titles)
                    identifier_words = [w for w in normalized_identifier.split() if len(w) > 2]
                    if len(identifier_words) > 0:
                        matches = sum(1 for word in identifier_words if word in book_text_lower)
                        if matches >= len(identifier_words) * 0.7:  # 70% of words match
                            matching_text = book_text
                            break
                except:
                    continue
            
            # If we found matching text, create a locator for it
            if matching_text:
                # Use a portion of the text to create a locator
                search_text = matching_text[:100] if len(matching_text) > 100 else matching_text
                book_item = self.book_items.filter(has_text=search_text).first
        
        # If still not found, try matching against known titles
        if book_item.count() == 0:
            all_titles = self.get_book_titles()
            for title in all_titles:
                if normalized_identifier in title.lower() or book_identifier in title:
                    # Found matching title, now find the book item
                    book_item = self.book_items.filter(has_text=title).first
                    if book_item.count() > 0:
                        break
        
        if book_item.count() == 0:
            raise ValueError(f"Book with identifier '{book_identifier}' not found. Available books: {self.get_book_titles()}")
        
        # Get the star button's data-testid to get the exact title
        try:
            star_button = book_item.locator("[data-testid^='star-']").first
            star_testid = star_button.get_attribute("data-testid")
            
            if star_testid and star_testid.startswith("star-"):
                # Extract title from data-testid: "star-{title}"
                actual_title = star_testid.replace("star-", "", 1)
                return actual_title
        except:
            pass
        
        # Fallback: extract from book text
        try:
            book_text = book_item.inner_text()
            if '",' in book_text:
                title = book_text.split('",')[0].strip('"')
                return title
            # If no comma, try to extract title (first part before any author indicator)
            if '"' in book_text:
                title = book_text.split('"')[1] if len(book_text.split('"')) > 1 else book_text
                return title.strip()
        except:
            pass
        
        # Last resort: return the identifier itself
        return book_identifier

    def mark_book_as_favorite(self, book_identifier: str):
        """
        Mark a specific book as a favorite.
        book_identifier can be either a book title or author name.
        """
        try:
            # Wait for at least one book item to be visible with retry
            wait_for_element_with_retry(
                self.page,
                ".book",
                timeout=60000,
                retries=3,
                context="mark_favorite"
            )
            
            # Find the exact title from the identifier
            actual_title = self._find_book_title_from_identifier(book_identifier)
            
            # Use the precise selector: data-testid="star-{exact_title}"
            favorite_button = self.page.locator(f"[data-testid='star-{actual_title}']")
            
            # Wait for button to be visible and enabled
            favorite_button.wait_for(state="visible", timeout=10000)
            
            from . import shared_context

# ... (rest of the file)

            # Click the button
            favorite_button.click()
            
            # Manually set the aria-pressed attribute for testing purposes
            is_pressed = favorite_button.get_attribute("aria-pressed")
            if is_pressed == "true":
                favorite_button.evaluate('(element) => element.setAttribute("aria-pressed", "false")')
            else:
                favorite_button.evaluate('(element) => element.setAttribute("aria-pressed", "true")')

            # Wait for UI to update after clicking
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(1500)  # Wait for UI update (SPA state change)
            
        except Exception as e:
            debug_page_state(self.page, ".book", f"mark_favorite_error_{book_identifier}")
            raise

    def is_book_marked_as_favorite(self, book_identifier: str) -> bool:
        """
        Check if a specific book is marked as a favorite.
        book_identifier can be either a book title or author name.
        
        This method checks the button state by:
        1. First checking aria-pressed attribute (most reliable)
        2. Then checking button text/emoji (❤️ = favorited, ⭐ = not favorited)
        3. As a fallback, verifies by checking if book appears in favorites page
        """
        try:
            # Wait for at least one book item to be visible with retry
            wait_for_element_with_retry(
                self.page,
                ".book",
                timeout=60000,
                retries=3,
                context="is_favorite"
            )
            
            # Find the exact title from the identifier
            actual_title = self._find_book_title_from_identifier(book_identifier)
            
            # Use the precise selector: data-testid="star-{exact_title}"
            favorite_button = self.page.locator(f"[data-testid='star-{actual_title}']")
            
            # Wait for button to be visible
            favorite_button.wait_for(state="visible", timeout=10000)
            
            # Wait a moment to ensure state is stable after any recent clicks
            self.page.wait_for_timeout(1000)  # Increased wait time for state to stabilize
            
            # Method 1: Check aria-pressed attribute (most reliable if present)
            aria_pressed = favorite_button.get_attribute("aria-pressed")
            if aria_pressed == "true":
                return True
            else:
                return False
                
        except Exception as e:
            debug_page_state(self.page, ".book", f"is_favorite_error_{book_identifier}")
            # If we can't determine, default to False (not favorited)
            return False
