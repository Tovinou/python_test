# Python Test Repository

This repository contains a collection of test automation projects and a sample application, demonstrating various testing frameworks and strategies.

## 📂 Project Structure

The repository is organized into four main projects:

### 1. `reading-list-tests`
- **Focus**: Acceptance testing for the Reading List application.
- **Tech Stack**: Python, Behave (BDD), Playwright.
- **Key Features**:
  - Gherkin feature files for BDD.
  - Page Object Model (POM) architecture.
  - Automated tests for adding books, catalog navigation, and favorites.

### 2. `TEST_3`
- **Focus**: Comprehensive testing for multiple applications.
- **Tech Stack**: Python, Behave, Pytest, Playwright.
- **Contents**:
  - `laslistan-tests`: BDD tests for the Reading List app (similar to `reading-list-tests` but with different implementation details).
  - `tests/test_agile_helper.py`: Pytest/Playwright tests for the Agile Helper application.

### 3. `TEST_2`
- **Focus**: End-to-End (E2E) testing for a Form Registration application.
- **Tech Stack**: TypeScript, Playwright.
- **Key Features**:
  - Extensive E2E test suite covering form validation, accessibility, and performance.
  - Detailed test reporting and artifacts.

### 4. `TEST`
- **Focus**: A Vue.js-based Timer Application with integrated tests.
- **Tech Stack**: Vue.js, TypeScript, Vite, Playwright.
- **Contents**:
  - Source code for the Timer App.
  - E2E tests located in `E2E_test/` folder.
  - configured to run against a local development server during CI.

## 🚀 CI/CD Pipelines

Each project has its own dedicated GitHub Actions workflow to ensure independent testing and rapid feedback. Workflows are triggered only when files in the specific project directory are changed.

| Project | Workflow File | Trigger Path |
|---------|---------------|--------------|
| `reading-list-tests` | `ci.yml` | `reading-list-tests/**` |
| `TEST_3` | `test_3_ci.yml` | `TEST_3/**` |
| `TEST_2` | `test_2_ci.yml` | `TEST_2/**` |
| `TEST` | `test_ci.yml` | `TEST/**` |

## 🛠️ Getting Started

To run the tests locally, navigate to the respective project directory and follow the instructions below:

### Python Projects (`reading-list-tests`, `TEST_3`)
1. Create and activate a virtual environment.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run tests:
   - For Behave: `behave`
   - For Pytest: `pytest`

### Node.js Projects (`TEST`, `TEST_2`)
1. Install dependencies:
   ```bash
   npm install
   ```
2. Install Playwright browsers:
   ```bash
   npx playwright install
   ```
3. Run tests:
   ```bash
   npx playwright test
   ```

## 📝 License
[MIT](LICENSE)
