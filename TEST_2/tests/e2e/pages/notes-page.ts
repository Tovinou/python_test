import { Page, Locator } from '@playwright/test';
import { BasePage } from './base-page';

export class NotesPage extends BasePage {
  readonly addNoteButton: Locator;
  readonly noteTextarea: Locator;

  constructor(page: Page) {
    super(page);
    this.addNoteButton = page.getByText('Add note', { exact: false });
    this.noteTextarea = page.locator('.note textarea');
  }

  async addNote() {
    await this.addNoteButton.click();
  }

  async fillNoteText(text: string) {
    await this.noteTextarea.fill(text);
  }

  async getNoteText() {
    return this.noteTextarea.inputValue();
  }
}