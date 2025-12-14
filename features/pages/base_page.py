from playwright.sync_api import Page


class BasePage:
    """
    Base class for all page objects. Contains common elements and methods.
    """
    def __init__(self, page: Page):
        self.page = page
        self.nav_katalog = page.locator("[data-testid='catalog']")
        self.nav_lagg_till_bok = page.locator("[data-testid='add-book']")
        self.nav_mina_bocker = page.locator("[data-testid='favorites']")

    def navigate_to(self, page_name: str):
        """
        Navigate to a specific page using the navigation bar.
        """
        target_locator = None
        if page_name == "Katalog":
            target_locator = self.nav_katalog
        elif page_name == "Lägg till bok":
            target_locator = self.nav_lagg_till_bok
        elif page_name == "Mina böcker":
            target_locator = self.nav_mina_bocker
        else:
            raise ValueError(f"Unknown page name: {page_name}")

        # Only click the navigation button if it's not disabled (which
        # indicates we might already be on that page). Playwright's click()
        # will auto-wait for the element to be ready.
        if target_locator and not target_locator.is_disabled():
            target_locator.click()
