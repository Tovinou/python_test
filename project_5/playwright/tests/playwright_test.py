# -*- coding: utf-8 -*-
import os
import re
import sys
import time

from playwright.sync_api import expect, sync_playwright

from run_logger import BASE_URL, LOCATORS, RunLogger


class UntitledPlaywrightTest:
    def __init__(self):
        self.playwright = None
        self.browser = None
        self.page = None
        self.rlog = RunLogger()

    def setup(self):
        self.playwright = sync_playwright().start()
        is_ci = os.environ.get("CI", "").lower() == "true"
        self.rlog.start_playwright(is_ci)
        self.browser = self.playwright.chromium.launch(headless=is_ci)
        self.page = self.browser.new_page()
        self.page.set_viewport_size({"width": 1280, "height": 720})
        self.page.set_default_timeout(30000)

    def teardown(self):
        keep_open_seconds = float(os.getenv("UI_KEEP_OPEN_SECONDS", "2"))
        self.rlog.closing_browser(keep_open_seconds)
        time.sleep(keep_open_seconds)
        self.browser.close()
        self.playwright.stop()
        self.rlog.done()

    def _open_login_page(self) -> None:
        self.rlog.step_open_login_page(BASE_URL)
        self.page.goto(BASE_URL, wait_until="domcontentloaded")
        self.rlog.step_page_loaded_dom()

    def test_login_succeeds(self):
        """G: Successful login and inventory (home) page."""
        self.rlog.banner_test_g()
        self._open_login_page()

        self.rlog.step_attempt_valid_credentials()
        self.rlog.log_locator("username")
        self.page.fill(LOCATORS["username"]["css"], "standard_user")
        self.rlog.value_standard_user_entered()

        self.rlog.log_locator("password")
        self.page.fill(LOCATORS["password"]["css"], "secret_sauce")
        self.rlog.value_secret_sauce_entered()

        self.rlog.log_locator("login_button")
        self.rlog.step_click_log_in()
        self.page.click(LOCATORS["login_button"]["css"])

        self.rlog.verify_user_logged_in_header()
        self.rlog.verify_url_should_contain_inventory()
        expect(self.page).to_have_url(re.compile(r"inventory"))
        self.rlog.check_url_ok()

        self.rlog.log_locator("inventory_list")
        self.rlog.verify_product_list_should_show()
        expect(self.page.locator(LOCATORS["inventory_list"]["css"])).to_be_visible()
        self.rlog.check_inventory_list_visible()
        self.rlog.result_g_passed()

    def test_wrong_username_shows_error(self):
        """VG: Wrong username shows an error message."""
        self.rlog.banner_test_vg_wrong_username()
        self._open_login_page()

        self.rlog.step_attempt_wrong_username()
        self.rlog.log_locator("username")
        self.page.fill(LOCATORS["username"]["css"], "not_a_real_sauce_user")
        self.rlog.value_invalid_username()

        self.rlog.log_locator("password")
        self.page.fill(LOCATORS["password"]["css"], "secret_sauce")
        self.rlog.value_valid_password()

        self.rlog.log_locator("login_button")
        self.page.click(LOCATORS["login_button"]["css"])

        self.rlog.step_verify_error_on_page()
        self.rlog.log_locator("error_message")
        err = self.page.locator(LOCATORS["error_message"]["css"])
        expect(err).to_be_visible()
        self.rlog.check_error_box_visible()
        expect(err).to_contain_text("Username and password do not match")
        self.rlog.check_error_text_username_password_mismatch()
        self.rlog.result_vg_wrong_username_passed()

    def test_wrong_password_shows_error(self):
        """VG: Wrong password shows an error message."""
        self.rlog.banner_test_vg_wrong_password()
        self._open_login_page()

        self.rlog.step_attempt_wrong_password()
        self.rlog.log_locator("username")
        self.page.fill(LOCATORS["username"]["css"], "standard_user")
        self.rlog.value_valid_username()

        self.rlog.log_locator("password")
        self.page.fill(LOCATORS["password"]["css"], "wrong_password")
        self.rlog.value_invalid_password()

        self.rlog.log_locator("login_button")
        self.page.click(LOCATORS["login_button"]["css"])

        self.rlog.step_verify_error_on_page()
        self.rlog.log_locator("error_message")
        err = self.page.locator(LOCATORS["error_message"]["css"])
        expect(err).to_be_visible()
        self.rlog.check_error_box_visible()
        expect(err).to_contain_text("Username and password do not match")
        self.rlog.check_error_text_username_password_mismatch()
        self.rlog.result_vg_wrong_password_passed()

    def test_untitled_test_case(self):
        """Backward compatibility: same as successful login test."""
        self.test_login_succeeds()


if __name__ == "__main__":
    rlog = RunLogger()
    rlog.suite_intro()
    test = UntitledPlaywrightTest()
    test.setup()
    exit_code = 0
    try:
        test.test_login_succeeds()
        test.test_wrong_username_shows_error()
        test.test_wrong_password_shows_error()
        rlog.suite_all_passed()
    except Exception:
        exit_code = 1
        rlog.suite_failed_banner()
        raise
    finally:
        test.teardown()
    sys.exit(exit_code)
