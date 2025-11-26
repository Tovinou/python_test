Feature: Navigate Between Pages
  As a user, I want to navigate between the main sections of the website so that I can access different functionalities.

  Scenario Outline: Navigate to a page from the navigation bar
    Given I am on the "Katalog" page
    When I navigate to the "<page_name>" page
    Then the URL should contain "<url_fragment>"

    Examples:
      | page_name      | url_fragment |
      | Katalog        | /            |
      | Lägg till bok  | /add-book    |
      | Mina böcker    | /my-books    |