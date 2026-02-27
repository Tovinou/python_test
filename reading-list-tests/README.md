# Testprojekt för Läslistan

Detta projekt innehåller automatiserade tester för webbapplikationen "Läslistan". Testerna är skrivna i Python med ramverket `behave` (BDD) och `playwright` för webbläsarautomation.

## Vanliga kommandon

- Kör alla tester (snabbt, headless):
  ```bash
  behave
  ```
- Kör alla tester visuellt (headed, inga skipped):
  ```bash
  behave -D headless=false
  ```
- Snabb visuell demo av navigering (långsammare klick, fönstret öppet):
  ```bash
  behave -D headless=false -D slowmo=700 -D keep_open=true -f pretty -n "Navigera"
  ```
- Komplett favoritflöde (lägg till → favorit → ta bort), visuell demo:
  ```bash
  behave -D headless=false -D slowmo=700 -D keep_open=true -f pretty -n "Lägg till bok, favoritmarkera och ta bort från favoriter"
  ```
- Pytest för navigering:
  ```bash
  pytest -q
  ```

## Vad som testas

Testerna täcker följande funktionalitet baserat på definierade User Stories:

1. **Visa katalog**: Verifierar att startsidan visar en lista med böcker med titel, författare och favoritknapp.
2. **Hantera favoriter**:
   - Lägga till böcker som favoriter.
   - Ta bort böcker från favoriter.
   - Visa listan över favoritmarkerade böcker.
3. **Lägg till ny bok**:
   - Verifierar att det går att lägga till nya böcker i katalogen.
   - Kontrollerar att den nya boken visas korrekt efter sparande.

Testerna använder designmönstret **Page Object Model** för att göra koden modulär och återanvändbar.

## Installation och start

För att köra projektet lokalt, följ dessa steg:
  
Webbsidan som testas: https://tap-vt25-testverktyg.github.io/exam--reading-list/

### 1. Förutsättningar
- Python 3.8 eller senare installerat.

### 2. Installera beroenden

```bash
# Skapa en virtuell miljö (rekommenderas)
python -m venv venv
# Aktivera miljön
# Windows:
.\venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Installera paket
pip install -r requirements.txt

# Installera webbläsare för Playwright
playwright install chromium
```

### 3. Köra testerna

Kör alla tester med kommandot:

```bash
behave
```

För att se applikationen i en synlig webbläsare (headed):

```bash
behave -D headless=false
```

### Pytest

Projektet innehåller även en enkel pytest som verifierar navigering via klick och DOM:

```bash
pytest -q
```

Testen klickar på “Lägg till bok”, verifierar titel- och författarinput samt submit-knappen, klickar “Mina böcker” och kontrollerar att nav-knappen är disabled, och slutligen klickar “Katalog” och verifierar att minst en bok syns.

### Demo: Lägg till bok och visa alla vyer

Kör ett komplett flöde som lägger till bok, favoritmarkerar och visar den i “Mina böcker”:

```bash
behave -n "Lägg till bok och visa den som favorit" -D headless=false
```

Ta bort favoritmarkering i ett komplett flöde:

```bash
behave -n "Lägg till bok, favoritmarkera och ta bort från favoriter" -D headless=false
```

Navigeringsöversikt (klick + DOM-verifiering):

```bash
behave -n Navigering -D headless=false
```

...

Testerna körs i "headless" läge (utan synligt fönster) för att vara snabba. Alla tester ska ta under 5 sekunder att köra totalt.

### Visuell demo (slowMo och keep_open)

För att se stegen långsammare och behålla fönstret öppet efter körning:

```bash
# Navigering med långsamma klick och öppet fönster
behave -D headless=false -D slowmo=700 -D keep_open=true -f pretty -n "Navigera"

# Komplett favoritflöde (lägg till → favorit → ta bort) visuellt
behave -D headless=false -D slowmo=700 -D keep_open=true -f pretty -n "Lägg till bok, favoritmarkera och ta bort från favoriter"
```

### Konfiguration via Behave userdata

Följande flaggor kan styras vid körning:
- `headless` (default: true) — sätt till `false` för synlig webbläsare.
- `slowmo` (default: 0) — antal millisekunder att sakta ned varje steg.
- `keep_open` (default: false) — behåll fönstret öppet efter scenariot.

Exempel:

```bash
behave -D headless=false -D slowmo=500 -D keep_open=true
```

### Tips om -n/--name filter
- `-n` filtrerar på scenarionamn/substring. I filtrerade körningar markeras övriga scenarier som “skipped”.
- För att köra allt utan “skipped”, kör utan `-n`:
  
```bash
behave -D headless=false
```

### Scenario Outline och Examples

Scenario Outline låter dig återanvända samma steg med parametrar (t.ex. `<länktext>`, `<förväntad_vy>`). Varje rad i `Examples` ersätter parametrarna och kör scenariot en gång per rad.

Exempel från navigering:

```gherkin
Scenario Outline: Navigera till vy via huvudnavigation
  Given jag är på startsidan
  When jag klickar på navigation "<länktext>"
  Then ska vyn visa "<förväntad_vy>"

  Examples:
    | länktext      | förväntad_vy |
    | Lägg till bok | Lägg till bok |
    | Mina böcker   | Mina böcker   |
    | Katalog       | Katalog       |
```

Köra endast detta Scenario Outline visuellt:

```bash
behave -D headless=false -f pretty -n "Navigera"
```

Exempel från “Lägg till ny bok”:

```gherkin
Scenario Outline: Lägg till en ny bok
  Given jag är på startsidan
  When jag går till sidan för att lägga till bok
  And jag anger titeln "<title>"
  And jag anger författaren "<author>"
  And jag sparar boken
  Then ska boken "<title>" finnas i katalogen
  And boken "<title>" ska ha författaren "<author>"

  Examples:
    | title                 | author            |
    | Min nya bok           | Jag Själv         |
    | Python för nybörjare  | Guido van Rossum  |
```

## Projektstruktur

- `features/`: Innehåller feature-filer (Gherkin) och step-definitions.
- `features/steps/`: Python-kod som kopplar Gherkin-steg till handlingar.
- `pages/`: Page Objects som kapslar in logiken för webbsidans olika vyer.
- `STORIES.md`: Dokumentation av User Stories.
