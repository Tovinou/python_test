Feature: View Favorite Books
  As a user, I want to view my list of favorite books on the "Mina böcker" page.

  Scenario: View a list with favorite books
    Given I have marked "Kaffekokaren som visste för mycket" as a favorite
    And I have marked "Min katt är min chef" as a favorite
    When I navigate to the "Mina böcker" page
    Then I should see my favorite books
    And "Kaffekokaren som visste för mycket" should be in my list of favorites
    And "Min katt är min chef" should be in my list of favorites

  Scenario: View an empty list of favorites
    Given I have not marked any books as favorites
    When I navigate to the "Mina böcker" page
    Then I should see an empty favorites list message