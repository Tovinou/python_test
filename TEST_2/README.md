Form Registration Test Suite
Automated Playwright/TypeScript tests that validate a registration form’s functionality, accessibility, and performance.

Overview
The tests cover form fields, validations, accessibility, performance, and basic widget interactions. The suite targets `https://tap-ht24-testverktyg.github.io/form-demo/` and is ready for CI execution.

Tech Stack
- Test framework: Playwright
- Language: TypeScript
- Reporters: HTML, JSON, JUnit
- Execution: Headless/Headed, multi‑browser

Project Structure
```
TEST_2/
├── .github/workflows/
│   ├── playwright-tests.yml
│   ├── deploy.yml
│   └── database-test.yml
├── config/
│   ├── playwright.config.ts
│   └── tsconfig.json
├── docs/
│   ├── test-strategy.md
│   ├── test-cases.md
│   └── bug-reports.md
├── reports/
│   └── test-summary.md
├── tests/
│   ├── e2e/
│   │   ├── pages/
│   │   │   ├── base-page.ts
│   │   │   ├── form-page.ts
│   │   │   ├── timer-page.ts
│   │   │   └── notes-page.ts
│   │   ├── specs/
│   │   │   ├── form-registration.spec.ts
│   │   │   ├── form-performance.spec.ts
│   │   │   ├── diagnostic.spec.ts
│   │   │   ├── accessibility.spec.ts
│   │   │   ├── themes.spec.ts
│   │   │   ├── timer.spec.ts
│   │   │   ├── notes.spec.ts
│   │   │   └── widgets.spec.ts
│   │   └── utils/
│   │       ├── helpers.ts
│   │       ├── form-helpers.ts
│   │       ├── test-data.ts
│   │       └── test-utils.ts
│   ├── units/
│   │   └── README.md
│   └── integration/
│       └── README.md
├── package.json
├── package-lock.json
├── eslint.config.cjs
├── README.md
├── .gitignore
├── .env.example
└── docker-compose.yml
```

Install
```
npm install
npx playwright install
```

Run Tests
- `npm run test` – run all tests using the central config
- `npm run test:e2e` – run e2e specs
- `npm run test:form` – run form‑focused specs
- `npm run test:ui` – headed mode
- `npm run test:debug` – debug mode

Reports
- `npm run test:ci` – generate HTML/line reports
- `npm run test:report` – open the HTML report under `test-results/html-report`

Code Quality
- `npm run lint`
- `npm run lint:fix`
- ESLint v9 flat config: `eslint.config.cjs`

Configuration
- Base URL and reporters via `config/playwright.config.ts`
- TypeScript paths and options via `config/tsconfig.json`

Environment Variables
Create a `.env` (optional) based on `.env.example`:
```
BASE_URL=https://tap-ht24-testverktyg.github.io/form-demo/
CI=false
```

Test Scenarios
- Form load: elements and submit button visible
- Validation: name, birth year, email, password
- Successful registration: valid data + submission
- Performance: page load < 3s, validation response < 1s
- Accessibility: semantic roles and interactions
- Widgets: basic interactions with fields/button

CI
GitHub Actions workflows run unit/e2e/performance, install Playwright browsers with `--with-deps`, and publish reports. Security tests run on `pull_request` events and can be enabled via `workflow_dispatch`.

Troubleshooting
- Missing browser dependencies on Linux runners
  - Symptom: `browserType.launch` with “Host system is missing dependencies to run browsers”
  - Fix: run `npx playwright install --with-deps` before tests in CI
- Reporter/output directory clash
  - Symptom: “HTML reporter output folder clashes with the tests output folder”
  - Fix: set `outputDir` to `test-results/results` and HTML reporter `outputFolder` to `test-results/html-report` in `config/playwright.config.ts`
- Wrong working directory in workflows
  - Symptom: “No such file or directory” for `/usr/bin/bash` or missing project path
  - Fix: run workflows from repo root; avoid non‑existent `working-directory`; ensure artifact/publish paths match current structure
- Missing unit script in CI
  - Symptom: `npm error Missing script: "test:unit"`
  - Fix: add a placeholder `test:unit` or modify workflow to skip unit tests
- Disabled submit button and click timeouts
  - Symptom: click action retries on disabled submit
  - Fix: use label‑based selectors (`getByLabel`), trigger validation via focus/blur, and avoid asserting enabled until fields are valid
- Slow page/resource in CI
  - Symptom: `toBeVisible` timeouts
  - Fix: add resilient waits or increase timeouts for critical selectors; verify network access to the base URL

CI Quick Checklist
- Checkout and setup Node
- `npm ci`
- `npx playwright install --with-deps`
- `npx playwright test -c config/playwright.config.ts`
- Upload `test-results` / publish HTML report

License
MIT
