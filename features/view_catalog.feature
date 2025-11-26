Feature: View Book Catalog
  As a user, I want to view the book catalog so I can see available books.

  Scenario: View the catalog page
    Given I am on the "Katalog" page
    Then I should see a welcome header
    And I should see a list of books