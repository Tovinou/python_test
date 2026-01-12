Feature: Lägg till ny bok
  Som en användare
  Vill jag kunna lägga till saknade böcker i katalogen
  Så att listan blir mer komplett

  Scenario Outline: Lägg till en ny bok
    Given jag är på startsidan
    When jag går till sidan för att lägga till bok
    And jag anger titeln "<title>"
    And jag anger författaren "<author>"
    And jag sparar boken
    Then ska boken "<title>" finnas i katalogen
    And boken "<title>" ska ha författaren "<author>"

    Examples:
      | title                 | author          |
      | Min nya bok           | Jag Själv       |
      | Python för nybörjare  | Guido van Rossum|
