Feature: Mark and Unmark Favorite Books
  As a user, I want to manage my favorite books so I can create a personalized reading list.

  Background:
    Given I am on the "Katalog" page

  Scenario: Mark a book as a favorite
    When I mark "Bertil Flimmer" as a favorite
    Then "Bertil Flimmer" should be marked as a favorite

  Scenario: Unmark a book as a favorite
    Given "Bertil Flimmer" is marked as a favorite
    When I mark "Bertil Flimmer" as a favorite again
    Then "Bertil Flimmer" should not be marked as a favorite

  Scenario: Toggle favorite multiple times
    When I mark "Bertil Flimmer" as a favorite
    Then "Bertil Flimmer" should be marked as a favorite
    When I mark "Bertil Flimmer" as a favorite again
    Then "Bertil Flimmer" should not be marked as a favorite
    When I mark "Bertil Flimmer" as a favorite again
    Then "Bertil Flimmer" should be marked as a favorite
    When I mark "Bertil Flimmer" as a favorite again
    Then "Bertil Flimmer" should not be marked as a favorite