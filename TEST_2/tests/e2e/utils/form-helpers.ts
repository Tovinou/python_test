// form-helpers.ts
import { Page, Locator } from '@playwright/test';

export class FormPage {
  readonly page: Page;
  readonly nameInput: Locator;
  readonly birthYearInput: Locator;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;

  constructor(page: Page) {
    this.page = page;
    this.nameInput = page.getByLabel('Namn');
    this.birthYearInput = page.getByLabel('Födelseår');
    this.emailInput = page.getByLabel('E-post');
    this.passwordInput = page.getByLabel('Lösenord');
    this.submitButton = page.getByRole('button', { name: 'Ok nu kör vi' });
  }

  async goto() {
    await this.page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await this.page.waitForLoadState('networkidle');
  }

  async fillForm(name: string, birthYear: string, email: string, password: string) {
    await this.nameInput.fill(name);
    await this.birthYearInput.fill(birthYear);
    await this.emailInput.fill(email);
    await this.passwordInput.fill(password);
  }

  async submit() {
    await this.submitButton.click();
  }

  async getErrorMessage() {
    return this.page.locator('.error-message, [role="alert"]').textContent();
  }
}

// Testdata generator
export const generateTestData = {
  validUser() {
    return {
      name: 'Test User',
      birthYear: '1990',
      email: `test${Date.now()}@example.com`,
      password: 'Password123'
    };
  },

  invalidPasswords() {
    return [
      { password: '123', description: 'för kort' },
      { password: '123456', description: 'endast siffror' },
      { password: 'abcdef', description: 'endast bokstäver' },
      { password: 'abc', description: 'för kort och endast bokstäver' }
    ];
  }
};