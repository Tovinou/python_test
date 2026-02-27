# Test Strategy

## Objectives
- Validate core form functionality, accessibility, and performance against `https://tap-ht24-testverktyg.github.io/form-demo/`.
- Provide stable, maintainable tests using Page Object Models and shared utils.

## Scope
- End‑to‑End tests under `tests/e2e/specs` using Playwright/TypeScript.
- Future unit and integration tests placeholders under `tests/units` and `tests/integration`.

## Approach
- Page Objects: `BasePage`, `FormPage`, `TimerPage`, `NotesPage` encapsulate selectors and actions.
- Utilities: `helpers.ts` for robust `waitForAppReady`, `test-utils.ts` for timing, console error checks, retry helpers.
- Data‑driven: Dynamic emails and structured test data in `test-data.ts`.
- Configuration: Central `config/playwright.config.ts` controls baseURL, reporters, projects.
- Assertions: Prefer role‑based locators and generic error containers; avoid brittle text matches.

## Environments
- OS: Windows (local), Ubuntu (CI)
- Node.js: 18.x/20.x
- Playwright: 1.56.1
- Browsers: chromium, firefox, webkit, mobile‑chrome

## Test Types
- Functional: field presence, input, submission
- Validation: name, birth year, email, password
- Accessibility: basic roles and interactive elements (button visible; enabled only with valid input)
- Performance: page load < 3s; validation response < 1s
- Smoke/Diagnostic: console error absence, critical UI elements

## Pass/Fail Criteria
- Functional and validation tests pass on chromium before expanding to other browsers.
- No console errors during page load for smoke tests.
- Performance thresholds respected under normal network conditions.

## Flakiness Mitigation
- Use `waitForLoadState('networkidle')` and `waitForAppReady` before interactions.
- Avoid strict string matching; use regex and role‑based queries.
- Implement retries for transient UI states via `retryOnStaleUI`.

## Reporting
- Reporters: HTML, JSON, JUnit.
- Artifacts: screenshots, videos, error contexts under `test-results/`.
- CI uploads artifacts and summarizes outcomes.

## CI/CD
- Workflows: `playwright-tests.yml` orchestrates unit/e2e/performance matrices and uploads artifacts.
- Database workflow available for integration scenarios (`database-test.yml`).

## Execution
- `npm run test` uses central config.
- `npm run test:e2e` runs E2E specs.
- `npm run test:ui` for headed debugging.
- `npm run test:report` to open HTML report.

## Traceability
- Test cases documented in `docs/test-cases.md` map to specs in `tests/e2e/specs/`.
- Example: Accessibility expectation at tests/e2e/specs/accessibility.spec.ts:12.

## Maintenance
- ESLint v9 flat config in `eslint.config.cjs`; `npm run lint` and `npm run lint:fix` enforce quality.
- Keep Page Objects in sync with UI; prefer semantic locators to reduce churn.