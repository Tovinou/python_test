# -*- coding: utf-8 -*-
"""All user-facing log lines and locators for the Sauce Demo Playwright run."""

from __future__ import annotations

from logger import get_logger

BASE_URL = "https://www.saucedemo.com/"
ERROR_LOCATOR = '[data-test="error"]'

# CSS used by Playwright; XPath mirrors typical Selenium style (for console output).
LOCATORS: dict[str, dict[str, str]] = {
    "username": {
        "css": "#user-name",
        "xpath": "//input[@id='user-name']",
    },
    "password": {
        "css": "#password",
        "xpath": "//input[@id='password']",
    },
    "login_button": {
        "css": "#login-button",
        "xpath": "//input[@id='login-button']",
    },
    "inventory_list": {
        "css": ".inventory_list",
        "xpath": "//div[contains(@class,'inventory_list')]",
    },
    "error_message": {
        "css": ERROR_LOCATOR,
        "xpath": "//*[@data-test='error']",
    },
}


class RunLogger:
    """Central place for every log line emitted during a test run."""

    _BANNER_WIDTH = 60

    def __init__(self) -> None:
        self._emit = get_logger().info

    def blank(self) -> None:
        self._emit("")

    def banner(self, title: str) -> None:
        line = "=" * self._BANNER_WIDTH
        self._emit(line)
        self._emit(title)
        self._emit(line)

    def suite_intro(self) -> None:
        self.blank()
        self._emit("Sauce Demo - Playwright: running G + two VG tests (three scenarios).")
        self.blank()

    def suite_all_passed(self) -> None:
        self._emit("=" * self._BANNER_WIDTH)
        self._emit("ALL TESTS COMPLETED WITH NO FAILURES.")
        self._emit("=" * self._BANNER_WIDTH)

    def suite_failed_banner(self) -> None:
        self.blank()
        self._emit("=" * self._BANNER_WIDTH)
        self._emit("FAILED - see traceback below.")
        self._emit("=" * self._BANNER_WIDTH)

    def start_playwright(self, headless: bool) -> None:
        self.blank()
        self._emit(">>> Starting Playwright (Chromium)...")
        self._emit(f"    headless={headless}  (set CI=true for headless mode)")
        self.blank()

    def closing_browser(self, keep_open_seconds: float) -> None:
        self.blank()
        self._emit(
            f">>> Closing browser in {keep_open_seconds:.0f} s (UI_KEEP_OPEN_SECONDS)..."
        )

    def done(self) -> None:
        self._emit(">>> Done.")
        self.blank()

    def log_locator(self, name: str) -> None:
        info = LOCATORS[name]
        self._emit(f"    Element [{name}]  CSS: {info['css']}")
        self._emit(f"                    XPath: {info['xpath']}")

    # --- Login page ---
    def step_open_login_page(self, url: str) -> None:
        self._emit(f"  [Step] Opening login page: {url}")

    def step_page_loaded_dom(self) -> None:
        self._emit("  [Step] Page loaded (domcontentloaded).")

    # --- G: successful login ---
    def banner_test_g(self) -> None:
        self.banner("TEST G: Successful login -> verify inventory (home) page")

    def step_attempt_valid_credentials(self) -> None:
        self._emit("  [Step] Attempting login with valid credentials...")

    def value_standard_user_entered(self) -> None:
        self._emit('         Value: "standard_user" entered.')

    def value_secret_sauce_entered(self) -> None:
        self._emit('         Value: "secret_sauce" entered.')

    def step_click_log_in(self) -> None:
        self._emit("  [Step] Clicking Log in...")

    def verify_user_logged_in_header(self) -> None:
        self._emit("  [Step] Verifying user is logged in:")

    def verify_url_should_contain_inventory(self) -> None:
        self._emit("         - URL should contain 'inventory'")

    def check_url_ok(self) -> None:
        self._emit("         [OK] URL OK.")

    def verify_product_list_should_show(self) -> None:
        self._emit("         - Product list (.inventory_list) should be visible")

    def check_inventory_list_visible(self) -> None:
        self._emit("         [OK] Inventory list visible.")

    def result_g_passed(self) -> None:
        self._emit("  [Result] G-level test passed.")
        self.blank()

    # --- VG: wrong username ---
    def banner_test_vg_wrong_username(self) -> None:
        self.banner("TEST VG: Wrong username -> error message should appear")

    def step_attempt_wrong_username(self) -> None:
        self._emit("  [Step] Attempting login with WRONG username (correct password)...")

    def value_invalid_username(self) -> None:
        self._emit('         Value: "not_a_real_sauce_user" (invalid).')

    def value_valid_password(self) -> None:
        self._emit('         Value: "secret_sauce" (valid).')

    def step_verify_error_on_page(self) -> None:
        self._emit("  [Step] Verifying error message on page...")

    def check_error_box_visible(self) -> None:
        self._emit("         [OK] Error box visible.")

    def check_error_text_username_password_mismatch(self) -> None:
        self._emit('         [OK] Text contains "Username and password do not match".')

    def result_vg_wrong_username_passed(self) -> None:
        self._emit("  [Result] VG test (wrong username) passed.")
        self.blank()

    # --- VG: wrong password ---
    def banner_test_vg_wrong_password(self) -> None:
        self.banner("TEST VG: Wrong password -> error message should appear")

    def step_attempt_wrong_password(self) -> None:
        self._emit("  [Step] Attempting login with valid username but WRONG password...")

    def value_valid_username(self) -> None:
        self._emit('         Value: "standard_user" (valid).')

    def value_invalid_password(self) -> None:
        self._emit('         Value: "wrong_password" (invalid).')

    def result_vg_wrong_password_passed(self) -> None:
        self._emit("  [Result] VG test (wrong password) passed.")
        self.blank()
