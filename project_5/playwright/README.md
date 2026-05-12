# Playwright (Python) Demo

This project runs a simple Playwright (Python) script that automates a login flow against https://www.saucedemo.com/.

## Prerequisites

- Python 3.10+ (Windows PowerShell examples below use the `py` launcher)
- Playwright installed for Python
- Playwright browsers installed (Chromium)

## Setup (Windows PowerShell)

From the project root:

```powershell
cd python_test\project_5\playwright
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install playwright
playwright install
```

## Run

```powershell
cd python_test\project_5\playwright
py .\tests\playwright_test.py
```

The script launches Chromium in headed mode (`headless=False`) and prints progress messages to the console.

## Project Layout

- `tests/playwright_test.py` — main script entrypoint

## Notes

- The script currently contains hardcoded credentials for the demo site. If you plan to publish this repository, replace them with environment variables (and keep `.env` out of git).
