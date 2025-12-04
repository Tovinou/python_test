Feature: View Favorite Books
  As a user, I want to view my list of favorite books on the "Mina böcker" page so I can easily see all the books I have selected.

  Scenario: View a list with favorite books
    Given I am on the "Katalog" page
    And I have marked "Kaffekokaren som visste för mycket" as a favorite
    And I have marked "Min katt är min chef" as a favorite
    When I navigate to the "Mina böcker" page
    Then I should see my favorite books
    And "Kaffekokaren som visste för mycket" should be in my list
    And "Min katt är min chef" should be in my list

  Scenario: View an empty list of favorites
    Given I am on the "Katalog" page
    And I have not marked any books as favorites
    When I navigate to the "Mina böcker" page
    Then the URL should contain "https://tap-vt25-testverktyg.github.io/exam--reading-list/my-books"
    Then I should see an empty list message