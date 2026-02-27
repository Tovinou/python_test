import { test, expect } from '@playwright/test';
import { FormPage } from '../pages/form-page';

test.describe('Formulärregistrering', () => {
  let formPage: FormPage;

  test.beforeEach(async ({ page }) => {
    formPage = new FormPage(page);
    await formPage.goto();
  });

  test('ska ladda formuläret korrekt', async () => {
    await expect(formPage.nameInput).toBeVisible();
    await expect(formPage.birthYearInput).toBeVisible();
    await expect(formPage.emailInput).toBeVisible();
    await expect(formPage.passwordInput).toBeVisible();
    await expect(formPage.submitButton).toBeVisible();
  });

  // ... resten av testerna
});
