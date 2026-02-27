import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: '../tests/e2e/specs',
  outputDir: '../test-results/results',
  
  use: {
    baseURL: 'https://tap-ht24-testverktyg.github.io/form-demo/',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
    video: 'retain-on-failure',
  },
  
  projects: [
    { name: 'chromium', use: { ...devices['Desktop Chrome'] } },
    { name: 'firefox', use: { ...devices['Desktop Firefox'] } },
    { name: 'webkit', use: { ...devices['Desktop Safari'] } },
    { name: 'mobile-chrome', use: { ...devices['Pixel 5'] } },
  ],
  
  reporter: [
    ['html', { outputFolder: '../test-results/html-report' }],
    ['json', { outputFile: '../test-results/test-results.json' }],
    ['junit', { outputFile: '../test-results/junit-report.xml' }],
    ['line']
  ],
});