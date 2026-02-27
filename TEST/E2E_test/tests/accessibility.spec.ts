import { test, expect } from '@playwright/test';
import { waitForAppReady, getAddTimerButton, getAddNoteButton } from './helpers';

test.describe('Accessibility and Usability', () => {
  test('sidan laddas med korrekt titel', async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    
    await waitForAppReady(page);
    
    // Kontrollera page title
    const title = await page.title();
    expect(title).toBeTruthy();
    
    // Använd helper-funktioner istället för direkt text matching
    const addTimerButton = getAddTimerButton(page);
    const addNoteButton = getAddNoteButton(page);
    
    await expect(addTimerButton).toBeVisible({ timeout: 10000 });
    await expect(addNoteButton).toBeVisible({ timeout: 10000 });
    
    // Check for theme selector text med mer flexibel approach
    const themeText = page.getByText(/select theme|theme|tema/i).first();
    await expect(themeText).toBeVisible({ timeout: 10000 });
  });

  test('keyboard navigation fungerar', async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await waitForAppReady(page);
    
    // Fokusera på body först
    await page.locator('body').click();
    
    // Navigera med tab
    await page.keyboard.press('Tab');
    
    // Fokus bör vara på första interaktiva elementet
    const focusedElement = page.locator('*:focus');
    await expect(focusedElement).toBeVisible();
  });

  test('sidan är responsiv', async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await waitForAppReady(page);
    
    // Testa mobile view
    await page.setViewportSize({ width: 375, height: 667 });
    await page.waitForTimeout(1000);
    
    // Verifiera att element fortfarande är synliga
    const addTimerButton = getAddTimerButton(page);
    const addNoteButton = getAddNoteButton(page);
    
    await expect(addTimerButton).toBeVisible({ timeout: 10000 });
    await expect(addNoteButton).toBeVisible({ timeout: 10000 });
  });

  test('error handling vid ogiltig timer-input', async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await waitForAppReady(page);
    
    // Skapa först en timer
    await getAddTimerButton(page).click();
    await page.waitForTimeout(1000);
    
    const timer = page.locator('.timer').first();
    await expect(timer).toBeVisible();
    
    const display = timer.locator('.timer-display, [data-testid="timer-display"]').first();
    await expect(display).toBeVisible();
    
    // Försök ange ogiltig tid
    await display.click();
    await page.keyboard.press('Control+A');
    await page.keyboard.type('99:99');
    await page.keyboard.press('Enter');
    
    await page.waitForTimeout(1000);
    
    // Verifiera att appen inte kraschar
    const currentTime = await display.textContent();
    expect(currentTime).toBeTruthy();
  });
});