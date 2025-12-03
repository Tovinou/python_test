Feature: Add New Book
  As a user, I want to add a new book to the catalog so that I can include books that are not already there.

  Scenario Outline: Add a new book with different inputs
    Given I am on the "Lägg till bok" page
    When I add a new book with title "<title>" and author "<author>"
    Then the book should be added to the catalog

    Examples:
      | title                 | author           |
      | The Hitchhiker's Guide | Douglas Adams   |
      | Dune                  | Frank Herbert    |

  Scenario: Attempt to add a book with missing information
    Given I am on the "Lägg till bok" page
    When I add a new book with title "<EMPTY>" and author "Some Author"
    Then the "Lägg till ny bok" button should be disabled
    And the book should not be added to the catalog