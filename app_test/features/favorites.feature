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
