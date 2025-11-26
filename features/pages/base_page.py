from playwright.sync_api import Page, expect

class BasePage:
    """
    Base class for all page objects. Contains common elements and methods.
    """
    def __init__(self, page: Page):
        self.page = page
        # Define common navigation selectors
        self.nav_katalog = page.get_by_role("link", name="Katalog")
        self.nav_lagg_till_bok = page.get_by_role("link", name="Lägg till bok")
        self.nav_mina_bocker = page.get_by_role("link", name="Mina böcker")

    def navigate_to(self, page_name: str):
        """
        Navigate to a specific page using the navigation bar.
        """
        if page_name == "Katalog":
            self.nav_katalog.click()
        elif page_name == "Lägg till bok":
            self.nav_lagg_till_bok.click()
        elif page_name == "Mina böcker":
            self.nav_mina_bocker.click()
        else:
            raise ValueError(f"Unknown page name: {page_name}")