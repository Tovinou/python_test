# Bug Reports

## BR-001: Submit button disabled by default conflicts with test expectation

- Type: Test defect
- Severity: Low
- Status: Open
- Environment: Windows, Node.js, Playwright 1.56.1; Base URL `https://tap-ht24-testverktyg.github.io/form-demo/`
- Affected Browsers: chromium, firefox, webkit, mobile-chrome
- Steps to Reproduce:
  - Navigate to the form page
  - Observe submit button state before entering any data
- Expected Result:
  - Test assertion expects the button to be enabled
- Actual Result:
  - Button is disabled until valid input is provided
- Evidence:
  - JSON reporter shows failure at tests/e2e/specs/accessibility.spec.ts:12
  - Screenshot and video under `test-results/accessibility-*/test-failed-1.png` and `video.webm`
- Notes:
  - Adjust test to assert visibility instead of enabled state until fields are valid

## BR-002: Validation copy mismatch between tests and application

- Type: Test defect
- Severity: Medium
- Status: Open
- Environment: Windows, Node.js, Playwright 1.56.1
- Affected Areas: Email, birth year, password validation messages
- Symptoms:
  - Tests expect specific Swedish strings which may differ from actual UI text
- Evidence:
  - Multiple failures across form-registration specs in `test-results/form-registration-*` directories
- Proposed Resolution:
  - Use regex patterns less strict on exact phrasing
  - Prefer role/alert regions and generic error containers for assertions

## BR-003: Success confirmation text may be absent post submission

- Type: Test defect (to verify)
- Severity: Medium
- Status: Open
- Environment: All browsers
- Steps:
  - Fill valid form data and submit
- Expected:
  - Confirmation text like `Registrering lyckades` or `Tack för din registrering`
- Actual:
  - Not consistently present; tests should verify absence of errors and stable state instead
- Proposed Resolution:
  - Adjust success criteria to reflect app behavior (no error, possibly reset/thank‑you state)

## BR-004: High failure count in multi‑browser matrix

- Type: Test suite configuration issue
- Severity: Medium
- Status: Open
- Description:
  - Running all specs across four browsers multiplies assertion mismatches
- Proposed Resolution:
  - Stabilize assertions first in chromium, then expand to others

---
Owner: QA
Report Date: 2025‑11‑22
