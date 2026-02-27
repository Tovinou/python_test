# Testprojekt för Läslistan

Detta projekt innehåller automatiserade tester för webbapplikationen "Läslistan". Testerna är skrivna i Python med ramverket `behave` (BDD) och `playwright` för webbläsarautomation.

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

### 1. Förutsättningar
- Python 3.8 eller senare installerat.

### 2. Installera beroenden

```bash
# Skapa en virtuell miljö (rekommenderas)
python -m venv envn
# Aktivera miljön
# Windows:
.\envn\Scripts\activate
# Mac/Linux:
source envn/bin/activate

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

Testerna körs i "headless" läge (utan synligt fönster) för att vara snabba. Alla tester ska ta under 5 sekunder att köra totalt.

## Projektstruktur

- `features/`: Innehåller feature-filer (Gherkin) och step-definitions.
- `features/steps/`: Python-kod som kopplar Gherkin-steg till handlingar.
- `pages/`: Page Objects som kapslar in logiken för webbsidans olika vyer.
- `STORIES.md`: Dokumentation av User Stories.
