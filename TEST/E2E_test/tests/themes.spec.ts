import { test, expect } from '@playwright/test';

test.describe('Theme Functionality', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
  });

  test('kan cykla genom alla teman', async ({ page }) => {
    const themes = [
      { name: 'Light', class: 'light' },
      { name: 'Dark', class: 'dark' },
      { name: 'Forest', class: 'forest' },
      { name: 'Orange', class: 'orange' }
    ];

    for (const theme of themes) {
      await page.getByText(theme.name, { exact: false }).click();
      await page.waitForTimeout(500);
      
      const body = page.locator('body');
      const bodyClass = await body.getAttribute('class');
      
      expect(bodyClass).toContain(theme.class);
      
      // Verifiera att widgets fortfarande fungerar efter tema-byte
      await page.getByText('Add timer', { exact: false }).click();
      const timer = page.locator('.timer').first();
      await expect(timer).toBeVisible();
      
      // Rensa för nästa iteration
      await page.locator('.timer .delete-button').click();
    }
  });

  test('tema persists efter page reload', async ({ page }) => {
    await page.getByText('Dark', { exact: false }).click();
    
    // Verifiera att temat är satt
    const bodyBefore = page.locator('body');
    const classBefore = await bodyBefore.getAttribute('class');
    expect(classBefore).toContain('dark');

    // Ladda om sidan
    await page.reload();
    
    // Verifiera att temat fortfarande är satt
    const bodyAfter = page.locator('body');
    const classAfter = await bodyAfter.getAttribute('class');
    expect(classAfter).toContain('dark');
  });

  test('widgets behåller funktionalitet vid tema-byte', async ({ page }) => {
    // Skapa widgets först
    await page.getByText('Add timer', { exact: false }).click();
    await page.getByText('Add note', { exact: false }).click();

    // Byt tema
    await page.getByText('Forest', { exact: false }).click();

    // Testa att timern fortfarande fungerar
    const timer = page.locator('.timer').first();
    await timer.getByText('Start').click();
    await page.waitForTimeout(1000);
    await timer.getByText('Pause').click();
    
    const display = timer.locator('.timer-display');
    const pausedTime = await display.textContent();
    await expect(pausedTime).not.toBe('15:00');

    // Testa att anteckningen fortfarande fungerar
    const note = page.locator('.note').first();
    const textarea = note.locator('textarea');
    await textarea.fill('Test efter tema-byte');
    await expect(textarea).toHaveValue('Test efter tema-byte');
  });
});