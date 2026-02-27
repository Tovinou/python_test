import { test, expect } from '@playwright/test';

test.describe('Teman', () => {
  test('ska ha läsbar primärknapp med definierade stilar', async ({ page }) => {
    await page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await page.waitForLoadState('domcontentloaded');
    const button = page.getByRole('button', { name: 'Ok nu kör vi' });
    await expect(button).toBeVisible();
    const styles = await button.evaluate((el) => {
      const s = getComputedStyle(el as HTMLElement);
      return { color: s.color, bg: s.backgroundColor, opacity: s.opacity };
    });
    expect(styles.color).toBeTruthy();
    expect(styles.bg).toBeTruthy();
    expect(styles.opacity).toBe('1');
  });
});