/// <reference types="node" />
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  fullyParallel: true,
  timeout: 60000, // Increase timeout to 60 seconds
  use: {
    // Appen är publicerad på GitHub Pages
    // URL: https://tovinou.github.io/test/
    // För lokal utveckling: 'http://localhost:5173'
    // Använd miljövariabel TEST_URL för att välja, annars använd GitHub Pages
    baseURL: process.env.TEST_URL || 'https://tovinou.github.io/test/',
    trace: 'on-first-retry',
    screenshot: 'only-on-failure',
  },
  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
  // Retry failed tests
  retries: process.env.CI ? 2 : 0,
});