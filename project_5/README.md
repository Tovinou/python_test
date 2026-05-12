# Project 5

This repository contains three independent Python testing examples. Each folder has its own setup/run instructions:

- [Integration_test/](python_test/project_5/Integration_test/README.md): FakeStoreAPI API + UI (Playwright) integration tests

[login_test]
		- [playwright/](python_test/project_5/playwright/README.md): Playwright (Python) demo script
		- [Selenium_test/](python_test/project_5/Selenium_test/README.md): Selenium (Python) UI test demo

## CI

GitHub Actions runs the full suite (Integration_test + Playwright + Selenium) using:

- [.github/workflows/project_5-tests.yml](python_test/project_5/.github/workflows/project_5-tests.yml)
