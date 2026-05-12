# Selenium Test Project

This project contains Selenium UI tests for [Sauce Demo](https://www.saucedemo.com/) login, written with Python `unittest`.

## Prerequisites

- Windows + PowerShell
- Python 3.x installed (`py --version`)
- Google Chrome installed

## Setup

Create and use a virtual environment, then install dependencies:

```powershell
py -3 -m venv venv
.\venv\Scripts\python.exe -m pip install -U pip
.\venv\Scripts\python.exe -m pip install selenium
```

## Run

Run the test directly:

```powershell
.\venv\Scripts\python.exe .\tests\ui_test.py
```

Or run via `unittest` from the project root:

```powershell
.\venv\Scripts\python.exe -m unittest tests.ui_test -v
```

## What the tests cover

- **Successful login:** correct credentials, then assert inventory URL and visible product list.
- **Wrong username:** assert the login error banner (`[data-test='error']`) is visible with text.
- **Wrong password:** same error-banner checks.

Fields and the login button are briefly outlined in red before each action (useful when Chrome is visible). In CI, highlight pauses default to **0** so runs stay fast. Override with `UI_HIGHLIGHT_DELAY` (seconds), e.g. `0.5`. Optional: `UI_KEEP_OPEN_SECONDS` to pause before closing the browser.

## Project structure

- `tests/ui_test.py` — `SauceDemoLoginTests` (three test methods)
