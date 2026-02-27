import { Page, Locator } from '@playwright/test';

export async function waitForAppReady(page: Page) {
  // Vänta på att sidan är helt laddad
  await page.waitForLoadState('networkidle');
  await page.waitForLoadState('domcontentloaded');
  
  // Vänta på att Vue-appen är redo - försök med olika selektorer
  try {
    // Försök första vägen - vänta på knappar
    await page.waitForSelector('button:has-text("Add timer"), button:has-text("Add note")', { 
      timeout: 15000,
      state: 'visible'
    });
  } catch {
    // Fallback - vänta på body eller andra element
    await page.waitForSelector('body', { timeout: 10000 });
  }
  
  // Ytterligare kort väntan för att vara säker
  await page.waitForTimeout(1000);
}

export function getAddTimerButton(page: Page): Locator {
  return page.locator('button').filter({ hasText: /Add timer/i });
}

export function getAddNoteButton(page: Page): Locator {
  return page.locator('button').filter({ hasText: /Add note/i });
}

export function getThemeButton(page: Page, themeName: string): Locator {
  return page.locator('button').filter({ hasText: new RegExp(themeName, 'i') });
}

// Ny funktion för att kontrollera om appen är redo
export async function isAppReady(page: Page): Promise<boolean> {
  try {
    await waitForAppReady(page);
    return true;
  } catch {
    return false;
  }
}