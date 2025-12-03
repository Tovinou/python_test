from playwright.sync_api import Page, expect
from .utils import debug_page_state

class BasePage:
    """
    Base class for all page objects. Contains common elements and methods.
    """
    def __init__(self, page: Page):
        self.page = page
        # Define common navigation selectors - these are buttons, not links
        self.nav_katalog = page.locator("[data-testid='catalog']")
        self.nav_lagg_till_bok = page.locator("[data-testid='add-book']")
        self.nav_mina_bocker = page.locator("[data-testid='favorites']")

    def navigate_to(self, page_name: str):
        """
        Navigate to a specific page using the navigation bar.
        """
        # Wait for page to be ready
        self.page.wait_for_load_state("domcontentloaded")
        self.page.wait_for_timeout(1000)  # Brief wait for SPA to be ready
        
        if page_name == "Katalog":
            # Navigation buttons use data-testid attributes
            try:
                self.nav_katalog.wait_for(state="visible", timeout=10000)
                # Check if button is disabled (we're already on this page)
                is_disabled = self.nav_katalog.get_attribute("disabled")
                if is_disabled is None:
                    # Button is not disabled, click it
                    self.nav_katalog.click()
            except:
                # Fallback: try finding by text content
                try:
                    katalog_btn = self.page.get_by_role("button", name="Katalog")
                    katalog_btn.wait_for(state="visible", timeout=10000)
                    is_disabled = katalog_btn.get_attribute("disabled")
                    if is_disabled is None:
                        katalog_btn.click()
                except:
                    # Last resort: try by text filter
                    katalog_btn = self.page.locator("button").filter(has_text="Katalog")
                    if katalog_btn.count() > 0:
                        is_disabled = katalog_btn.first.get_attribute("disabled")
                        if is_disabled is None:
                            katalog_btn.first.click()
        elif page_name == "Lägg till bok":
            try:
                self.nav_lagg_till_bok.wait_for(state="visible", timeout=10000)
                self.nav_lagg_till_bok.click()
            except:
                try:
                    lagg_till_btn = self.page.get_by_role("button", name="Lägg till bok")
                    lagg_till_btn.wait_for(state="visible", timeout=10000)
                    lagg_till_btn.click()
                except:
                    lagg_till_btn = self.page.locator("button").filter(has_text="Lägg till bok")
                    lagg_till_btn.first.click()
        elif page_name == "Mina böcker":
            try:
                self.nav_mina_bocker.wait_for(state="visible", timeout=10000)
                self.nav_mina_bocker.click()
            except:
                try:
                    mina_bocker_btn = self.page.get_by_role("button", name="Mina böcker")
                    mina_bocker_btn.wait_for(state="visible", timeout=10000)
                    mina_bocker_btn.click()
                except:
                    mina_bocker_btn = self.page.locator("button").filter(has_text="Mina böcker")
                    mina_bocker_btn.first.click()
        else:
            raise ValueError(f"Unknown page name: {page_name}")
        
        # Wait for navigation to complete (for all paths)
        self.page.wait_for_load_state("networkidle")
        self.page.wait_for_timeout(1000)  # Wait for SPA to render new page