Feature: Hantera favoriter
  Som en användare vill jag kunna spara och hantera mina favoritböcker.

  Background:
    Given jag är på startsidan

  Scenario: Lägg till favorit
    When jag klickar på hjärtat för boken "Kaffekokaren som visste för mycket"
    Then ska boken "Kaffekokaren som visste för mycket" finnas under "Mina böcker"

  Scenario: Ta bort favorit
    Given jag har lagt till boken "Kaffekokaren som visste för mycket" som favorit
    When jag tar bort favoriten "Kaffekokaren som visste för mycket"
    Then ska boken "Kaffekokaren som visste för mycket" inte finnas under "Mina böcker"

  Scenario: Växla favoritmarkering flera gånger (toggle)
    Given boken "Kaffekokaren som visste för mycket" är inte favorit
    When jag klickar på hjärtat för boken "Kaffekokaren som visste för mycket"
    And jag klickar på hjärtat för boken "Kaffekokaren som visste för mycket"
    And jag klickar på hjärtat för boken "Kaffekokaren som visste för mycket"
    Then ska boken "Kaffekokaren som visste för mycket" finnas under "Mina böcker"

  Scenario: Visa favoriter
    Given jag har lagt till boken "Min katt är min chef" som favorit
    When jag går till "Mina böcker"
    Then ska jag se boken "Min katt är min chef" i listan

  Scenario: Visa tom vy utan favoriter
    Given jag är på startsidan
    When jag går till "Mina böcker"
    Then ska favoritlistan vara tom

  Scenario: Lägg till bok och visa den som favorit
    Given jag är på startsidan
    When jag går till sidan för att lägga till bok
    And jag anger titeln "E2E Testbok"
    And jag anger författaren "E2E Testförfattare"
    And jag sparar boken
    Then ska boken "E2E Testbok" finnas i katalogen
    And boken "E2E Testbok" ska ha författaren "E2E Testförfattare"
    When jag klickar på hjärtat för boken "E2E Testbok"
    When jag går till "Mina böcker"
    Then ska jag se boken "E2E Testbok" i listan

  Scenario: Lägg till bok, favoritmarkera och ta bort från favoriter
    Given jag är på startsidan
    When jag går till sidan för att lägga till bok
    And jag anger titeln "E2E Remove Testbok"
    And jag anger författaren "E2E Remove Testförfattare"
    And jag sparar boken
    Then ska boken "E2E Remove Testbok" finnas i katalogen
    And boken "E2E Remove Testbok" ska ha författaren "E2E Remove Testförfattare"
    When jag klickar på hjärtat för boken "E2E Remove Testbok"
    When jag går till "Mina böcker"
    Then ska jag se boken "E2E Remove Testbok" i listan
    When jag tar bort favoriten "E2E Remove Testbok"
    When jag går till "Mina böcker"
    Then ska boken "E2E Remove Testbok" inte finnas under "Mina böcker"
