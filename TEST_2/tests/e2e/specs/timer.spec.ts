import { test, expect } from '@playwright/test';

test.describe('Prestanda-timer', () => {
  test('ska ladda inom 3 sekunder och validera inom 1 sekund', async ({ page }) => {
    const t0 = Date.now();
    await page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await page.waitForLoadState('networkidle');
    const loadMs = Date.now() - t0;
    expect(loadMs).toBeLessThan(3000);

    await page.getByLabel('E-post').fill('ogiltig-email');
    await page.getByLabel('Namn').focus();
    const v0 = Date.now();
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible({ timeout: 1000 });
    const validateMs = Date.now() - v0;
    expect(validateMs).toBeLessThan(1000);
  });
});