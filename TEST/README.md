# Timer App E2E Tests

E2E-tester för Timer & Notes Vue App skrivna med Playwright.

## App Status

**Appen är deployad och tillgänglig på:** `https://tovinou.github.io/test/`

## Projektstruktur

```
TEST/
  ├── .github/
  │   └── workflows/
  │       └── deploy.yml             # Deploy app
  │
  ├── public/
  │   └── vite.svg
  ├── src
  ├── timer-vue-temp
  └── E2E_test/
      ├── .github/
      │   └── workflows/
      │       └── e2e-tests.yml      # Test app
      ├── test-results/
      ├── node_modules/
      ├── tests/
      │   ├── timer.spec.ts          # Timer-specifika tester
      │   ├── notes.spec.ts          # Antecknings-specifika tester  
      │   ├── widgets.spec.ts        # Widget-hanterings tester
      │   ├── themes.spec.ts         # Tema-relaterade tester
      │   ├── accessibility.spec.ts  # Tillgänglighet och användbarhet
      │   ├── performance.spec.ts    # Prestandatester
      │   ├── anteckning.spec.ts     # Anteckningstester
      │   ├── helpers.ts             # Hjälpfunktioner
      │   └── diagnostic.spec.ts     # Diagnostiska tester
      ├── playwright.config.ts       # Playwright konfiguration
      ├── package.json
      ├── package-lock.json
      ├── tsconfig.json
      ├── README.md
      ├── TEST-DOCUMENTATION.md
      ├── PUBLISH_APP.md
      └── diagnostic-homepage.png
```

## Installation

```bash
cd E2E_test
npm install
npx playwright install
```

## Kör testerna

```bash
# Kör alla tester
npm test

# Kör testerna mot lokal server
TEST_URL=http://localhost:5173 npm test

# Kör specifik testfil
npx playwright test timer.spec.ts

# Kör tester i headed mode (synlig webbläsare)
npx playwright test --headed

# Kör tester med interaktiv UI
npx playwright test --ui
```

## Testresultat

**Status:** ✅ 22 av 24 tester passerar

- Timer-funktionalitet: ✅ Alla tester passerar
- Antecknings-funktionalitet: ✅ Alla tester passerar
- Tema-funktionalitet: ✅ Alla tester passerar
- Widget-hantering: ✅ Alla tester passerar
- Accessibility: ✅ Alla tester passerar
- Performance: ✅ Alla tester passerar

## Testscenarier

### Timer-funktionalitet
- Skapa och ta bort timer-widgets
- Starta, pausa och återställa timers
- Ändra tidsinställningar
- Hantera flera widgets samtidigt

### Anteckningsfunktionalitet
- Skapa och ta bort antecknings-widgets
- Redigera anteckningstext i realtid

### Tema-funktionalitet
- Byt temafärg (Light, Dark, Forest, Orange)
- Tema persists efter page reload

## Konfiguration

Testerna är konfigurerade att använda den deployade versionen som standard. För lokal utveckling kan du använda miljövariabeln `TEST_URL`:

```bash
TEST_URL=http://localhost:5173 npm test
```

Eller redigera `playwright.config.ts`:
```typescript
use: {
  baseURL: process.env.TEST_URL || 'https://tovinou.github.io/test/',
  // ...
}
```

## Ytterligare kommandon

```bash
# Kör tester från specifikt projekt (t.ex. endast Chrome)
npx playwright test --project=chromium

# Kör tester i debug-läge
npx playwright test --debug

# Generera och visa testrapport
npx playwright show-report

# Kör tester med tag
npx playwright test --grep "theme"

# Kör tester i parallell
npx playwright test --workers=4
```

## Felsökning

Om tester misslyckas:

1. Kontrollera att appen är tillgänglig på `https://tovinou.github.io/test/`
2. För lokal testning, starta appen: `npm run dev` (i timer-vue-app mappen)
3. Använd Playwrights UI-läge för att inspektera element:
   ```bash
   npx playwright test --ui
   ```
4. Använd `page.pause()` för att pausa execution och inspektera:
   ```typescript
   await page.pause();
   ```

## App Repository

- **App-kod:** https://github.com/Tovinou/test.git
- **Live app:** https://tovinou.github.io/test/

## Support

För frågor om dessa tester eller Playwright:

- [Playwright Documentation](https://playwright.dev/)
- [Timer App Repository](https://github.com/Tovinou/test.git)
