import { test, expect } from '@playwright/test';

test.describe('Antecknings Funktioner', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('/', { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
  });

  test('kan skapa en antecknings-widget', async ({ page }) => {
    await page.getByText('Add note', { exact: false }).click();
    
    const notes = page.locator('.note');
    await expect(notes).toHaveCount(1);
  });

  test('kan uppdatera anteckningstext', async ({ page }) => {
    await page.getByText('Add note', { exact: false }).click();

    const note = page.locator('.note').first();
    const textarea = note.locator('textarea');
    
    await textarea.fill('Kom ihåg kaffe');
    await expect(textarea).toHaveValue('Kom ihåg kaffe');
    
    // Testa att ändra text igen
    await textarea.fill('Möte kl 10:00');
    await expect(textarea).toHaveValue('Möte kl 10:00');
  });

  test('kan ta bort antecknings-widget', async ({ page }) => {
    await page.getByText('Add note', { exact: false }).click();
    
    const notesBefore = page.locator('.note');
    await expect(notesBefore).toHaveCount(1);
    
    // Anta att det finns en delete-knapp
    await page.locator('.note .delete-button').click();
    
    const notesAfter = page.locator('.note');
    await expect(notesAfter).toHaveCount(0);
  });

  test('kan byta mellan olika teman', async ({ page }) => {
    const themes = ['Light', 'Dark', 'Forest', 'Orange'];
    const body = page.locator('body');
    
    for (const theme of themes) {
      await page.getByText(theme, { exact: false }).click();
      await page.waitForTimeout(500);
      const bodyClass = await body.getAttribute('class');
      expect(bodyClass).toContain(theme.toLowerCase());
    }
  });
});