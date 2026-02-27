import { test, expect } from '@playwright/test';

test.describe('Diagnostik', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await page.waitForLoadState('networkidle');
  });

  test('ska ladda sidan utan konsolfel', async ({ page }) => {
    const errors: string[] = [];
    page.on('console', (msg) => {
      if (msg.type() === 'error') errors.push(msg.text());
    });

    await expect(page.getByText('Registrera dig')).toBeVisible();
    await expect(page.getByLabel('Namn')).toBeVisible();
    await expect(page.getByLabel('Födelseår')).toBeVisible();
    await expect(page.getByLabel('E-post')).toBeVisible();
    await expect(page.getByLabel('Lösenord')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Ok nu kör vi' })).toBeVisible();

    expect(errors.length).toBe(0);
  });
});