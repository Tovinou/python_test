"""
Utility functions for page objects including debugging and retry logic.
"""
import os
from typing import Callable, Any, Optional
from playwright.sync_api import Page, Locator, TimeoutError as PlaywrightTimeoutError


def debug_page_state(page: Page, selector: Optional[str] = None, context: str = ""):
    """
    Debug function to capture page state when elements aren't found.
    Saves HTML and screenshot for debugging.
    """
    debug_dir = "debug_output"
    os.makedirs(debug_dir, exist_ok=True)
    
    try:
        # Get page URL and title
        url = page.url
        title = page.title()
        
        # Get page HTML (first 5000 chars)
        html = page.content()[:5000]
        
        # Take screenshot
        screenshot_path = f"{debug_dir}/screenshot_{context}.png"
        page.screenshot(path=screenshot_path, full_page=True)
        
        # Save HTML snippet
        html_path = f"{debug_dir}/page_html_{context}.txt"
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(f"URL: {url}\n")
            f.write(f"Title: {title}\n")
            f.write(f"Selector: {selector}\n")
            f.write("\n" + "="*80 + "\n")
            f.write("HTML (first 5000 chars):\n")
            f.write(html)
        
        # Try to find all elements with data-testid
        if selector:
            test_ids = page.locator("[data-testid]").all()
            test_id_path = f"{debug_dir}/testids_{context}.txt"
            with open(test_id_path, "w", encoding="utf-8") as f:
                f.write(f"Found {len(test_ids)} elements with data-testid:\n")
                for i, elem in enumerate(test_ids[:20]):  # Limit to first 20
                    try:
                        test_id = elem.get_attribute("data-testid")
                        text = elem.inner_text()[:100] if elem.is_visible() else "[hidden]"
                        f.write(f"{i+1}. data-testid='{test_id}' - text: {text}\n")
                    except:
                        pass
        
        print(f"\n[DEBUG] Page state saved to {debug_dir}/ for context: {context}")
        print(f"[DEBUG] URL: {url}, Title: {title}")
    except Exception as e:
        print(f"[DEBUG] Error capturing page state: {e}")


def retry_with_fallback(
    page: Page,
    primary_selector: str,
    fallback_selectors: list[str],
    action: Callable[[Locator], Any],
    timeout: int = 60000,
    context: str = ""
) -> Any:
    """
    Try to find an element using primary selector, fallback to alternatives if it fails.
    
    Args:
        page: Playwright page object
        primary_selector: Primary CSS selector to try first
        fallback_selectors: List of alternative selectors to try
        action: Function to execute with the found locator
        timeout: Timeout in milliseconds
        context: Context string for debugging
    """
    all_selectors = [primary_selector] + fallback_selectors
    
    for i, selector in enumerate(all_selectors):
        try:
            locator = page.locator(selector)
            locator.wait_for(state="visible", timeout=timeout if i == 0 else timeout // 2)
            return action(locator)
        except PlaywrightTimeoutError:
            if i == len(all_selectors) - 1:
                # Last attempt failed, debug and raise
                debug_page_state(page, selector, f"{context}_failed")
                raise
            continue
        except Exception as e:
            if i == len(all_selectors) - 1:
                debug_page_state(page, selector, f"{context}_error")
                raise
            continue
    
    # Should never reach here, but just in case
    debug_page_state(page, primary_selector, f"{context}_unknown")
    raise PlaywrightTimeoutError(f"All selectors failed: {all_selectors}")


def wait_for_element_with_retry(
    page: Page,
    selector: str,
    timeout: int = 60000,
    retries: int = 3,
    context: str = ""
) -> Locator:
    """
    Wait for an element with retry logic.
    
    Args:
        page: Playwright page object
        selector: CSS selector
        timeout: Timeout per attempt in milliseconds
        retries: Number of retry attempts
        context: Context string for debugging
    """
    last_error = None
    
    for attempt in range(retries):
        try:
            locator = page.locator(selector)
            # Use first() to avoid strict mode violation when multiple elements exist
            locator.first.wait_for(state="visible", timeout=timeout)
            return locator
        except PlaywrightTimeoutError as e:
            last_error = e
            if attempt < retries - 1:
                # Wait a bit before retrying
                page.wait_for_timeout(2000)
                continue
            else:
                # Final attempt failed, debug and raise
                debug_page_state(page, selector, f"{context}_final_failure")
                raise
    
    # Should never reach here
    debug_page_state(page, selector, f"{context}_unknown_error")
    raise last_error or PlaywrightTimeoutError(f"Element not found: {selector}")

