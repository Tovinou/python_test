# FakeStore Integration Tests (API + UI)

This project runs automated integration tests against https://fakestoreapi.com:

- API tests: Pytest + Requests
- UI test: Playwright (Chromium, headed) + a small API call via `page.request`

## Requirements

- Python 3.12+ (tested with Python 3.12.8)

## Project Layout

- `tests/api/` – API tests
- `tests/ui/test_fakestore_ui.py` – UI integration test
- `scripts/run_tests.py` – runner that executes both API + UI and writes logs
- `scripts/logger.py` – logging configuration used by the runner
- `run_tests.log` – output log file created when running the runner

## Setup (Windows)

Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

Install Playwright browsers (needed for the UI test):

```powershell
python -m playwright install
```

## Run

Run API + UI together (recommended):

```powershell
python scripts\run_tests.py
```

Run only API tests:

```powershell
python -m pytest -v tests/api
```

Run only the UI test:

```powershell
python tests\ui\test_fakestore_ui.py
```

## Logs

- `scripts/run_tests.py` writes the labeled sections:
  - `API Integration Tests (pytest)`
  - `UI Integration Test (Playwright)`
- Those messages are written to both the console and `run_tests.log`.

## UI Test (watch mode)

To slow down the browser actions and keep the browser open longer:

```powershell
$env:UI_SLOW_MO_MS="300"
$env:UI_KEEP_OPEN_SECONDS="15"
python scripts\run_tests.py
```

## CI Note

FakeStoreAPI often returns `403 Forbidden` from GitHub Actions (bot traffic). Tests assert **HTTP 200** for `/products` (and related checks), so the workflow **fails** in CI when the API responds with 403, which matches the course requirement.
