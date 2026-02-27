# TEST_4 - Test Automation Project

This project contains automated tests for both UI (Selenium) and API (Requests).

## Project Structure

- **selenium_tests/**: Contains UI tests using Selenium WebDriver for [Sauce Demo](https://www.saucedemo.com/).
- **integration_tests/**: Contains API tests using `requests` for [Fake Store API](https://fakestoreapi.com/).
- **.github/workflows/**: CI/CD configuration for running tests automatically on push.
- **REPORT.md**: Assignment report and answers to questions.

## Prerequisites

- Python 3.x
- Google Chrome (for Selenium tests)

## Installation

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running Tests

Run all tests with pytest:
```bash
pytest
```

Run specific test categories:
```bash
# Run only Selenium tests
pytest selenium_tests/

# Run only API tests
pytest integration_tests/
```
