import { Page, Locator } from '@playwright/test';
import { BasePage } from './base-page';

export class TimerPage extends BasePage {
  readonly addTimerButton: Locator;
  readonly timerDisplay: Locator;

  constructor(page: Page) {
    super(page);
    this.addTimerButton = page.getByText('Add timer', { exact: false });
    this.timerDisplay = page.locator('.timer-display');
  }

  async addTimer() {
    await this.addTimerButton.click();
  }

  async getTimerCount() {
    return this.page.locator('.timer').count();
  }
}