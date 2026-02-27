import { test, expect } from '@playwright/test';

test('diagnostic test - check what is actually on the page', async ({ page }) => {
  await page.goto('/', { waitUntil: 'networkidle' });
  
  // Ta en skärmbild
  await page.screenshot({ path: 'diagnostic-homepage.png', fullPage: true });
  
  // Logga page title
  console.log('Page title:', await page.title());
  
  // Logga page URL
  console.log('Current URL:', page.url());
  
  // Logga all synlig text på sidan
  const bodyText = await page.locator('body').textContent();
  console.log('Body text (first 500 chars):', bodyText?.substring(0, 500));
  
  // Logga alla knappar på sidan
  const buttons = await page.locator('button').all();
  console.log('Number of buttons found:', buttons.length);
  
  for (let i = 0; i < buttons.length; i++) {
    const buttonText = await buttons[i].textContent();
    console.log(`Button ${i}:`, buttonText);
  }
  
  // Kontrollera om det finns Vue-app related element
  const appElement = await page.locator('#app, [data-v-app], .app').first();
  if (await appElement.isVisible()) {
    console.log('Vue app element found');
  } else {
    console.log('No Vue app element found');
  }
});