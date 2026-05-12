# Selenium Test Project

This project contains a simple Selenium UI test written with Python `unittest`.

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

Or run via `unittest`:

```powershell
.\venv\Scripts\python.exe -m unittest -v .\tests\ui_test.py
```

## What The Test Does

- Opens https://www.saucedemo.com/ in Chrome
- Types into the username/password fields and clicks around the page
- Highlights elements in red before clicking/typing to make actions visible

The test is primarily a UI interaction demo; it does not currently include assertions about page state.

## Project Structure

- `tests/ui_test.py` contains the Selenium test case
