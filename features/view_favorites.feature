Feature: View Favorite Books
  As a user, I want to view my list of favorite books on the "Mina böcker" page so I can easily see all the books I have selected.

  Scenario: View a list with favorite books
    Given I am on the "Katalog" page
    And I have marked "Bertil Flimmer" as a favorite
    And I have marked "Hur man tappar bort sin TV - fjärr 10 gånger om dagen" as a favorite
    When I navigate to the "Mina böcker" page
    Then I should see my favorite books
    And "Bertil Flimmer" should be in my list
    And "Hur man tappar bort sin TV - fjärr 10 gånger om dagen" should be in my list

  Scenario: View an empty list of favorites
    Given I am on the "Katalog" page
    And I have not marked any books as favorites
    When I navigate to the "Mina böcker" page
    Then the URL should contain "https://tap-vt25-testverktyg.github.io/exam--reading-list/my-books"
    Then I should see an empty list message