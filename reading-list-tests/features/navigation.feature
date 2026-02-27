Feature: Navigering
  Som användare vill jag kunna navigera mellan sidans vyer.

  Scenario Outline: Navigera till vy via huvudnavigation
    Given jag är på startsidan
    When jag klickar på navigation "<länktext>"
    Then ska vyn visa "<förväntad_vy>"

    Examples:
      | länktext     | förväntad_vy |
      | Lägg till bok | Lägg till bok |
      | Mina böcker   | Mina böcker   |
      | Katalog       | Katalog       |
