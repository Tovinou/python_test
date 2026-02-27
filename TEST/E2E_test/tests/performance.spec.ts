import { test, expect } from '@playwright/test';

test.describe('Performance Tests', () => {
  test('sidan laddas snabbt', async ({ page }) => {
    const startTime = Date.now();
    await page.goto('/', { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
    const loadTime = Date.now() - startTime;
    
    // Verifiera att sidan laddas inom 10 sekunder (mer realistiskt)
    expect(loadTime).toBeLessThan(10000);
    
    await expect(page.getByText('Add timer', { exact: false })).toBeVisible();
  });

  test('kan hantera många widgets utan prestandaproblem', async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
    
    // Skapa flera widgets
    for (let i = 0; i < 5; i++) {
      await page.getByText('Add timer', { exact: false }).click();
      await page.getByText('Add note', { exact: false }).click();
    }
    
    const timers = page.locator('.timer');
    const notes = page.locator('.note');
    
    await expect(timers).toHaveCount(5);
    await expect(notes).toHaveCount(5);
    
    // Testa att alla timers kan startas
    for (const timer of await timers.all()) {
      await timer.getByText('Start').click();
    }
    
    await page.waitForTimeout(1000);
    
    // Alla timers borde vara aktiva
    for (const timer of await timers.all()) {
      await expect(timer.getByText('Pause')).toBeVisible();
    }
  });

  test('tema-byte är omedelbar', async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
    
    // Mät tid för tema-byte
    const startTime = Date.now();
    await page.getByText('Dark', { exact: false }).click();
    const switchTime = Date.now() - startTime;
    
    // Temabyte borde ta mindre än 1 sekund
    expect(switchTime).toBeLessThan(1000);
    
    // Verifiera att temat applicerats
    const body = page.locator('body');
    const bodyClass = await body.getAttribute('class');
    expect(bodyClass).toContain('dark');
  });
});