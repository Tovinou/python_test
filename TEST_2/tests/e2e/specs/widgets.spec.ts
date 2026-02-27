import { test, expect } from '@playwright/test';
import { FormPage } from '../pages/form-page';

test.describe('Widgets', () => {
  test('ska interagera med alla fält och skicka', async ({ page }) => {
    const form = new FormPage(page);
    await form.goto();
    await form.fillForm('Widget Test', '1999', `widget${Date.now()}@example.com`, 'Pass1234');
    await form.submit();
    await expect(page.getByRole('button', { name: 'Ok nu kör vi' })).toBeVisible();
  });
});