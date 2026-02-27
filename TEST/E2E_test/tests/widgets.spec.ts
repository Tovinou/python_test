import { test, expect } from '@playwright/test';

test.describe('Widget Management', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
  });

  test('kan skapa och ta bort flera widgets', async ({ page }) => {
    // Skapa två timers och en anteckning
    await page.getByText('Add timer', { exact: false }).click();
    await page.getByText('Add timer', { exact: false }).click();
    await page.getByText('Add note', { exact: false }).click();

    const timers = page.locator('.timer');
    const notes = page.locator('.note');
    
    await expect(timers).toHaveCount(2);
    await expect(notes).toHaveCount(1);

    // Ta bort en timer
    await page.locator('.timer').first().locator('.delete-button').click();
    await expect(timers).toHaveCount(1);

    // Ta bort anteckningen
    await page.locator('.note').locator('.delete-button').click();
    await expect(notes).toHaveCount(0);
  });

  test('kan hantera mixed widget layout', async ({ page }) => {
    // Skapa en blandad layout: timer -> note -> timer
    await page.getByText('Add timer', { exact: false }).click();
    await page.getByText('Add note', { exact: false }).click();
    await page.getByText('Add timer', { exact: false }).click();

    // Appen renderar timers först, sedan notes
    const timers = page.locator('.timer');
    const notes = page.locator('.note');
    
    await expect(timers).toHaveCount(2);
    await expect(notes).toHaveCount(1);
    
    // Verifiera att alla widgets är synliga
    await expect(timers.first()).toBeVisible();
    await expect(notes.first()).toBeVisible();
    await expect(timers.last()).toBeVisible();
  });
});