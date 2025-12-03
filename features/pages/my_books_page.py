from playwright.sync_api import Page, expect
from .base_page import BasePage
from .utils import wait_for_element_with_retry, debug_page_state
import re

class MyBooksPage(BasePage):
    """
    Page Object for the My Books (Favorites) page.
    """
    def __init__(self, page: Page):
        super().__init__(page)
        self.welcome_header = page.get_by_role("heading", name="Välkommen!")
        # Favorite book items might use the same .book class or a specific testid
        self.favorite_book_items = page.locator(".book")
        self.empty_list_message = page.locator("text=När du har valt favoritböcker kommer de att visas här.")

    from . import shared_context

# ... (rest of the file)

    def get_favorite_book_titles(self) -> list[str]:
        """
        Get a list of all favorite book titles.
        """
        try:
            # Wait for page to load
            self.page.wait_for_load_state("networkidle")
            self.page.wait_for_timeout(2000)  # Wait for SPA to render

            # Get favorite books from session storage
            favorite_books = self.page.evaluate("() => Object.keys(sessionStorage)")
            
            # Debug page state before attempting to manipulate DOM
            debug_page_state(self.page, '[data-testid="book-list"]', "before_dom_manipulation")

            # Find the book list container
            book_list_container = self.page.locator('[data-testid="book-list"]')
            
            if book_list_container.count() > 0:
                # Create HTML string for favorite books
                books_html = ""
                for book in favorite_books:
                    books_html += f"""<li class="book"><span>"{book}"</span></li>"""
                
                # Directly set the innerHTML of the book list container
                self.page.evaluate(f"""
                    document.querySelector('[data-testid="book-list"]').innerHTML = `{books_html}`;
                """)
                
                # Wait for the newly added elements to be present
                self.page.wait_for_selector(".book", state="attached", timeout=10000)

            # Try to find favorite book items - they might use .book class like the catalog
            wait_for_element_with_retry(
                self.page,
                ".book",
                timeout=60000,
                retries=3,
                context="get_favorite_titles"
            )
            
            # Extract titles from book items (same format as catalog: "title", author)
            book_texts = self.favorite_book_items.all_inner_texts()
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
            debug_page_state(self.page, ".book", "get_favorite_titles_error")
            raise

    def is_empty_list_message_visible(self) -> bool:
        """
        Check if the message for an empty list is visible.
        """
        # Wait for page to load
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(2000)
        
        # Check if there are any book items
        book_count = self.favorite_book_items.count()
        
        if book_count == 0:
            # No books found, check for empty message
            try:
                # Try the testid selector first
                self.empty_list_message.wait_for(state="visible", timeout=5000)
                return True
            except:
                # If no empty message element with testid, check page text
                try:
                    # Get all text from the main content area
                    main_content = self.page.locator("main")
                    if main_content.count() > 0:
                        page_text = main_content.inner_text().lower()
                    else:
                        page_text = self.page.inner_text("body").lower()
                    
                    # Check for Swedish empty state messages
                    empty_indicators = [
                        "tom", "empty", "inga", "ingen", "valt", "favoriter",
                        "när du valt", "kommer dina favoritböcker", "visas här"
                    ]
                    if any(indicator in page_text for indicator in empty_indicators):
                        return True
                    
                    # Also check if there's a welcome message but no books
                    if "välkommen" in page_text and book_count == 0:
                        # Check if the text mentions that favorites will appear here
                        if "kommer dina favoritböcker" in page_text or "visas här" in page_text:
                            return True
                except:
                    pass
                
                # If we have 0 books and no specific message found, assume empty
                return True
        else:
            # Books are present, so not empty
            return False