# Reading List Web Application Tests

This project contains automated end-to-end tests for the "Läslistan" web application. The tests are written using Python with the Behave framework (BDD) and Playwright for browser automation.

## What has been tested

The test suite covers the following functionalities of the Läslistan application:

1.  **Navigation**: Verifies that users can correctly navigate between the "Katalog", "Lägg till bok", and "Mina böcker" pages using the main navigation bar.
2.  **Viewing the Catalog**: Confirms that the book catalog loads correctly and displays a list of available books.
3.  **Adding New Books**: Tests the functionality of adding new books to the catalog. This includes:
    *   Successfully adding a book with a valid title and author.
    *   Attempting to add a book with missing information (e.g., an empty title).
4.  **Managing Favorites**: Covers the process of marking books as favorites and unmarking them.
    *   Marking a book as a favorite.
    *   Unmarking a book to remove it from favorites.
5.  **Viewing Favorite Books**: Ensures that the "Mina böcker" page correctly displays the user's list of favorite books.
    *   Viewing a populated list of favorite books.
    *   Viewing the page when no favorites have been selected (empty state).

## Project Structure
reading-list-tests/
├── README.md
├── STORIES.md
├── requirements.txt
├── behave.ini
├── .gitignore
├── .github/
│ └── workflows/
│ └── test.yml
└── features/
│ ├── environment.py
│ ├── view_catalog.feature
│ ├── add_book.feature
│ ├── mark_favorites.feature
│ ├── view_favorites.feature
│ ├── navigation.feature
│ ├── steps/
│ │ ├── catalog_steps.py
│ │ ├── add_book_steps.py
│ │ ├── favorites_steps.py
│ │ ├── view_favorites_steps.py
│ │ └── navigation_steps.py
│ └── pages/
│ ├── base_page.py
│ ├── catalog_page.py
│ ├── add_book_page.py
│ └── my_books_page.py


## How to start the project

Follow these steps to set up the project and run the tests on your local machine.

### Prerequisites

*   Python 3.8 or higher
*   Git

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/Tovinou/python_test.git
    cd python_test
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

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Install the necessary Playwright browsers:**
    ```bash
    playwright install
    ```

### Running the Tests

*   **To run the tests in headed mode (with a browser window visible):**
    ```bash
    behave
    ```
    > **Note for Windows users:** If you encounter encoding-related errors, you may need to run the tests using the following command to enforce UTF-8 encoding:
    > ```cmd
    > set PYTHONUTF8=1&& python -m behave
    > ```

*   **To run the tests in headless mode (in the background, faster):**
    ```bash
    behave -D headless=true
    ```
    > **Note for Windows users:** Similarly, for headless mode, use:
    > ```cmd
    > set PYTHONUTF8=1&& python -m behave -D headless=true
    > ```

*   **To run a specific feature file:**
    ```bash
    behave features/view_favorites.feature
    ```

## Test Design

*   **Behavior-Driven Development (BDD):** Tests are written in Gherkin syntax (`.feature` files) to describe behavior in a human-readable format.
*   **Page Object Model (POM):** The `features/pages` directory implements the POM design pattern. This separates the test logic (in `steps` files) from the UI interaction logic (in `pages` files), making the code cleaner and more maintainable.
*   **Scenario Outlines:** Used for testing the same scenario with multiple data sets, such as adding different books.
*   **Robust Selectors:** Tests primarily use `data-testid` attributes for locating elements, which are less likely to change than CSS classes or XPath.