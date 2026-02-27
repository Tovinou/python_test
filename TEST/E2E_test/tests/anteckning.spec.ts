import { test, expect } from '@playwright/test';

test("ändra anteckningstext", async ({ page }) => {
    await page.goto("/", { waitUntil: 'networkidle' });
    await page.waitForLoadState('networkidle');
    await page.waitForTimeout(3000);
    await page.getByText('Add note', { exact: false }).click();
  
    const note = page.locator(".note textarea");
    await note.fill("Kom ihåg kaffe");
    await expect(note).toHaveValue("Kom ihåg kaffe");
  });
  