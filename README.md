# Reading List Web Application Tests

This project contains automated end-to-end tests for the "Läslistan" web application. The tests are written using Python with the Behave framework and Playwright.

The primary goal of this project was to refactor a slow and unreliable test suite into one that is fast, stable, and uses modern best practices for browser automation. The test setup is now highly optimized for performance, allowing the entire suite to run in just a few seconds.

## What is Tested

The test suite covers the following functionalities:

1.  **Navigation**: Verifies navigation between the "Katalog", "Lägg till bok", and "Mina böcker" pages.
2.  **Viewing the Catalog**: Confirms that the book catalog loads and displays books.
3.  **Adding New Books**: Tests adding books with valid titles/authors and handling of invalid data (e.g., empty title).
4.  **Managing Favorites**: Covers marking and unmarking books as favorites.
5.  **Viewing Favorite Books**: Ensures the "Mina böcker" page displays the user's favorite books and shows an empty state message when no favorites are selected.

## Project Structure
```
reading-list-tests/
├── README.md
├── STORIES.md
├── requirements.txt
├── behave.ini
├── .gitignore
├── .github/
│   └── workflows/
│       └── test.yml
└── features/
    ├── environment.py
    ├── *.feature
    ├── steps/
    │   └── *_steps.py
    └── pages/
        ├── base_page.py
        ├── catalog_page.py
        ├── add_book_page.py
        └── my_books_page.py
```

## How to Run the Project

### Prerequisites

*   Python 3.8+
*   Git

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment:**
    *   On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install Playwright browsers:**
    ```bash
    playwright install
    ```

### Running the Tests

*   **To run all tests:**
    ```bash
    behave
    ```

*   **To run in headless mode (faster, no visible browser):**
    ```bash
    behave -D headless=true
    ```
    > **Note for Windows Users:** If you see encoding-related errors, you may need to enforce UTF-8. The following command is one way to do this for a single run:
    > `set PYTHONUTF8=1 && python -m behave`

*   **To run a specific feature:**
    ```bash
    behave features/navigation.feature
    ```

## Test Design

*   **Behavior-Driven Development (BDD):** Tests are written in Gherkin (`.feature` files) to describe application behavior from the user's perspective.
*   **Page Object Model (POM):** The `features/pages` directory separates UI interaction logic from the test steps, making the code cleaner and easier to maintain.
*   **Optimized Test Environment:** The test setup in `features/environment.py` is optimized for speed, launching the browser only once for the entire test suite.
