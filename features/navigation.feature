Feature: Navigate Between Pages
  As a user, I want to navigate between the main sections of the website.

  Scenario: Navigate to the catalog page
    Given I am on the start page
    When I navigate to the "Katalog" page
    Then I should be on the "Katalog" page

  Scenario: Navigate to the add book page
    Given I am on the start page
    When I navigate to the "Lägg till bok" page
    Then I should be on the "Lägg till bok" page

  Scenario: Navigate to the my books page
    Given I am on the start page
    When I navigate to the "Mina böcker" page
    Then I should be on the "Mina böcker" page
