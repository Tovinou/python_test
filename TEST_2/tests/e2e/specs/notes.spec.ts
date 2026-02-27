import { test, expect } from '@playwright/test';

test.describe('Anteckningar', () => {
  test('ska kunna fylla i textfält och behålla värdet', async ({ page }) => {
    await page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await page.getByLabel('Namn').fill('Min anteckning');
    await expect(page.getByLabel('Namn')).toHaveValue('Min anteckning');
  });
});