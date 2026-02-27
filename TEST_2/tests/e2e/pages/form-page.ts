import { Page, Locator } from '@playwright/test';
import { BasePage } from './base-page';

export class FormPage extends BasePage {
  readonly nameInput: Locator;
  readonly birthYearInput: Locator;
  readonly emailInput: Locator;
  readonly passwordInput: Locator;
  readonly submitButton: Locator;

  constructor(page: Page) {
    super(page);
    this.nameInput = page.getByLabel('Namn');
    this.birthYearInput = page.getByLabel('Födelseår');
    this.emailInput = page.getByLabel('E-post');
    this.passwordInput = page.getByLabel('Lösenord');
    this.submitButton = page.getByRole('button', { name: 'Ok nu kör vi' });
  }

  async goto() {
    await this.page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await this.waitForReady();
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