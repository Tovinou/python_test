import { test, expect } from '@playwright/test';
import { waitForAppReady } from '../utils/helpers';

test.describe('Tillgänglighet', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await waitForAppReady(page);
  });

  test('ska ha semantiska element och tillgänglig knapp', async ({ page }) => {
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();
    const submit = page.getByRole('button', { name: 'Ok nu kör vi' });
    await expect(submit).toBeVisible();
    await expect(submit).toHaveAccessibleName('Ok nu kör vi');
    await expect(page.getByLabel('Namn')).toBeEditable();
    await expect(page.getByLabel('Födelseår')).toBeEditable();
    await expect(page.getByLabel('E-post')).toBeEditable();
    await expect(page.getByLabel('Lösenord')).toBeEditable();
  });
});