import os
import re
import time

from playwright.sync_api import sync_playwright

BASE = "https://fakestoreapi.com"
DOCS = f"{BASE}/docs"
PRODUCTS_URL = f"{BASE}/products"


class UIIntegrationTest:
    def setup(self):
        self.playwright = sync_playwright().start()
        slow_mo_ms = int(os.getenv("UI_SLOW_MO_MS", "0"))
        self.is_ci = os.environ.get("CI", "").lower() == "true"
        self.browser = self.playwright.chromium.launch(
            headless=self.is_ci,
            slow_mo=slow_mo_ms,
        )
        self.page = self.browser.new_page()
        self.page.set_viewport_size({"width": 1280, "height": 720})
        self.page.set_default_timeout(15000)

    def teardown(self):
        time.sleep(float(os.getenv("UI_KEEP_OPEN_SECONDS", "2")))
        self.browser.close()
        self.playwright.stop()

    def test_products_ui_integration(self):
        nav = self.page.goto(DOCS, wait_until="domcontentloaded")
        # When FakeStore blocks bots (e.g. GitHub Actions), /docs often returns
        # 403 too. Skip Swagger and hit /products like the API tests so CI fails
        # on the same GET /products expectation, not on /docs.
        swagger_ok = nav is None or nav.status < 400
        if swagger_ok:
            self.page.get_by_role(
                "menuitem", name=re.compile(r"Products", re.IGNORECASE)
            ).click()
            self.page.get_by_label("Get all products").first.click()
            assert self.page.locator("pre", has_text=PRODUCTS_URL).count() > 0

        res = self.page.request.get(PRODUCTS_URL)
        assert res.status == 200, f"GET /products expected 200, got {res.status}"

        products = res.json()
        assert len(products) == 20

        for p in products:
            assert "title" in p and "price" in p and "category" in p

        p1 = next((p for p in products if p.get("id") == 1), None)
        assert p1 is not None
        assert p1["id"] == 1
        assert "Fjallraven" in p1["title"]


if __name__ == "__main__":
    t = UIIntegrationTest()
    t.setup()
    try:
        t.test_products_ui_integration()
    finally:
        t.teardown()
