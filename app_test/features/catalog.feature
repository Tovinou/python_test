Feature: Visa katalog
  Som en bokintresserad användare
  Vill jag se en lista över tillgängliga böcker
  Så att jag kan få inspiration till min läsning

  Scenario: Visa lista över böcker
    Given jag är på startsidan
    Then ska jag se en lista med böcker
    And varje bok ska visa titel och författare
    And det ska finnas en knapp för att favoritmarkera
