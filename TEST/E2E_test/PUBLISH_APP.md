# Guide: Publicera Timer Vue App på GitHub Pages

## Steg 1: Klona repot
```bash
git clone https://github.com/Tovinou/test.git timer-vue-app
cd timer-vue-app
```

## Steg 2: Lägg till timer-vue-appen
Om du har appen lokalt:
```bash
# Kopiera alla filer från din timer-vue-app till detta repo
# T.ex. om appen finns i en annan mapp:
cp -r /path/to/timer-vue/* .
```

## Steg 3: Konfigurera för GitHub Pages

### För Vite-projekt:
1. Uppdatera `vite.config.js` eller `vite.config.ts`:
```typescript
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  base: process.env.NODE_ENV === 'production' ? '/test/' : '/',
})
```

**Viktigt:** Base path måste matcha repository-namnet. Om repot heter "test", använd `/test/`.

2. Skapa en GitHub Actions workflow (`.github/workflows/deploy.yml`):
```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20  # Vite 7 kräver Node.js 20.19+ eller 22.12+
      - run: npm ci
      - run: npm run build
      - uses: actions/upload-pages-artifact@v3
        with:
          path: ./dist

  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### Alternativ: Manuell deployment
1. Bygg appen:
```bash
npm run build
```

2. Pusha `dist`-mappen till `gh-pages` branch:
```bash
git subtree push --prefix dist origin gh-pages
```

Eller använd `gh-pages` paketet:
```bash
npm install --save-dev gh-pages
# Lägg till i package.json:
# "scripts": {
#   "deploy": "gh-pages -d dist"
# }
npm run deploy
```

## Steg 4: Aktivera GitHub Pages
1. Gå till repository settings på GitHub
2. Gå till "Pages" i vänstermenyn
3. Välj source: "GitHub Actions" (om du använder workflow) eller "gh-pages branch"
4. Spara

## Steg 5: Uppdatera Playwright config
När appen är publicerad, URL:en kommer att vara:
- `https://tovinou.github.io/test/` (om repo heter "test")

Uppdatera `playwright.config.ts`:
```typescript
use: {
  // Använd miljövariabel för lokal utveckling, annars GitHub Pages
  baseURL: process.env.TEST_URL || 'https://tovinou.github.io/test/',
  // ...
}
```

För lokal testning:
```bash
TEST_URL=http://localhost:5173 npm test
```

## Steg 6: Verifiera deployment
1. Kontrollera att GitHub Actions workflow kördes och lyckades
2. Gå till repository settings → Pages
3. Välj "GitHub Actions" som source
4. Vänta på att deployment slutförs (vanligtvis 1-2 minuter)
5. Öppna `https://tovinou.github.io/test/` i webbläsaren

## Steg 7: Testa
```bash
cd E2E_test
npm test
```

**Förväntat resultat:** 22 av 24 tester bör passa. Appen är nu deployad och fungerar!

## Alternativ: Kör appen lokalt för testning

Om du vill testa utan att publicera:

1. Starta appen lokalt:
```bash
# Om det är en Vite-app
npm run dev
# Appen körs på http://localhost:5173
```

2. Uppdatera `playwright.config.ts`:
```typescript
baseURL: 'http://localhost:5173',
```

3. Kör testerna:
```bash
npm test
```

