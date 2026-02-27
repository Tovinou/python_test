Timer App E2E Tests with Playwright
E2E-tester för Timer Vue App skrivna med Playwright. Dessa tester validerar kärnfunktionaliteten för en timer-app med widget-baserat gränssnitt.

## ✅ App Status

**Appen är deployad och tillgänglig på:** `https://tovinou.github.io/test/`

Testerna är konfigurerade att använda den deployade versionen som standard. För lokal utveckling kan du använda miljövariabeln `TEST_URL`:

```bash
# Kör testerna mot lokal server
TEST_URL=http://localhost:5173 npm test

# Eller redigera playwright.config.ts direkt
```

För att ändra baseURL, redigera `playwright.config.ts`:
```typescript
use: {
  baseURL: process.env.TEST_URL || 'https://tovinou.github.io/test/',
  // ...
}
```

Testscenarier
Timer-funktionalitet
- Skapa och ta bort timer-widgets

- Starta, pausa och återställa timers

- Ändra tidsinställningar

- Hantera flera widgets samtidigt

Anteckningsfunktionalitet
- Skapa och ta bort antecknings-widgets

- Redigera anteckningstext i realtid

Anpassning
- Byt temafärg (Light, Dark, Forest, Orange)

Projektstruktur
text
tests/
├── timer.spec.ts          # Timer-specifika tester
├── notes.spec.ts          # Antecknings-specifika tester  
├── widgets.spec.ts        # Widget-hanterings tester
├── themes.spec.ts         # Tema-relaterade tester
├── accessibility.spec.ts  # Tillgänglighet och användbarhet
└── performance.spec.ts    # Prestandatester

Installation och körning

Förutsättningar
- Node.js (version 16 eller senare)

- npm

Steg-för-steg installation
bash
# Initiera npm-projekt
npm init -y

# Installera Playwright som dev dependency
npm install -D @playwright/test

# Installera Playwright browsers (Chromium, Firefox, WebKit)
npx playwright install

# Kör alla tester
npx playwright test

# Kör testerna med interaktiv UI
npx playwright test --ui

# Kör tester för specifikt fil
npx playwright test timer.spec.ts

# Kör tester i headed mode (synlig webbläsare)
npx playwright test --headed

# Generera och visa testrapport
npx playwright show-report
Ytterligare användbara kommandon
bash
# Kör tester från specifikt projekt (t.ex. endast Chrome)
npx playwright test --project=chromium

# Kör tester i debug-läge
npx playwright test --debug

# Skapa Playwright konfigurationsfil (redan gjord i detta projekt)
npx playwright init

# Öppna Playwright trace viewer
npx playwright show-trace trace.zip

# Kör alla tester
npx playwright test

# Kör specifik testfil
npx playwright test widgets.spec.ts

# Kör tester med tag
npx playwright test --grep "theme"

# Kör tester i parallell
npx playwright test --workers=4

Anpassningsområden
Dessa tester använder CSS-selektorerna som visas i appens nuvarande implementation. Om appens HTML-struktur ändras kan följande selektorer behöva uppdateras:

Viktiga CSS-selektorer som kan behöva anpassas:
.timer - Container för timer-widgets

.timer-display - Element som visar timer-tiden

.note - Container för antecknings-widgets

.delete-button - Knapp för att ta bort widgets (kan heta något annat i appen)

Ytterligare anpassningspunkter:
Widget-ordning - Appen renderar timers först, sedan notes. Drag-and-drop är inte implementerat.

Tema-klasser - Klassnamnen för teman (forest, dark, etc.) kan variera

Knapp-text - Texter som "Start", "Pause", "Reset" kan vara lokaliserade

Input-fält - Selektorerna för text-redigering kan behöva uppdateras

Så här anpassar du selektorerna:
Inspecta appens DOM-struktur i webbläsarens devtools

Identifiera rätt CSS-klasser och attribut

Uppdatera selektorerna i testfilerna:

typescript
// Exempel: Uppdatera timer-display selektor
const display = page.locator('.timer-display'); // ← Uppdatera denna

// Alternativt använda role eller text
const display = page.getByRole('timer');
Testrapporter
Efter testkörning genereras en detaljerad rapport:

bash
# Generera HTML-rapport
npx playwright show-report
Rapporten inkluderar:

Testresultat (pass/fail)

Screenshots vid failure

Execution traces

Test-timeline

Felsökning
Om tester misslyckas på grund av selektor-problem:

Använd Playwrights UI-läge för att inspektera element:

bash
npx playwright test --ui
Använd page.pause() för att pausa execution och inspektera:

typescript
await page.pause();
Kontrollera att baseURL är korrekt i playwright.config.ts

Bidrag
För att lägga till nya tester:

Skapa ny .spec.ts fil i tests/ mappen

Använd befintliga tester som mall

Kör testerna lokalt för att verifiera

Se till att alla tester passerar innan merge

## Testresultat

**Status:** ✅ 22 av 24 tester passerar

- Timer-funktionalitet: ✅ Alla tester passerar
- Antecknings-funktionalitet: ✅ Alla tester passerar
- Tema-funktionalitet: ✅ Alla tester passerar
- Widget-hantering: ✅ Alla tester passerar
- Accessibility: ✅ Alla tester passerar
- Performance: ✅ Alla tester passerar

## App Repository

- **App-kod:** https://github.com/Tovinou/test.git
- **Live app:** https://tovinou.github.io/test/

## Support

För frågor om dessa tester eller Playwright:

- [Playwright Documentation](https://playwright.dev/)
- [Timer App Repository](https://github.com/Tovinou/test.git)