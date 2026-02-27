import { Page, expect } from '@playwright/test';

export async function measureAction<T>(action: () => Promise<T>) {
  const t0 = Date.now();
  const result = await action();
  const ms = Date.now() - t0;
  return { result, ms };
}

export async function expectNoConsoleErrors(page: Page) {
  const errors: string[] = [];
  page.on('console', (msg) => {
    if (msg.type() === 'error') errors.push(msg.text());
  });
  await page.waitForLoadState('networkidle');
  expect(errors.length).toBe(0);
}

export async function retryOnStaleUI(fn: () => Promise<void>, retries = 2) {
  for (let i = 0; i <= retries; i++) {
    try {
      await fn();
      return;
    } catch (e) {
      if (i === retries) throw e;
    }
  }
}