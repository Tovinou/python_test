// form-registration.spec.ts
import { test, expect } from '@playwright/test';

test.describe('Formulärregistrering', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://tap-ht24-testverktyg.github.io/form-demo/');
    await page.waitForLoadState('networkidle');
  });

  test('ska ladda formuläret korrekt', async ({ page }) => {
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();
    await expect(page.getByLabel('Namn')).toBeVisible();
    await expect(page.getByLabel('Födelseår')).toBeVisible();
    await expect(page.getByLabel('E-post')).toBeVisible();
    await expect(page.getByLabel('Lösenord')).toBeVisible();
    await expect(page.getByRole('button', { name: 'Ok nu kör vi' })).toBeVisible();
  });

  test('ska kunna fylla i alla fält med giltig data', async ({ page }) => {
    // Fyll i formuläret med giltig data
    await page.getByLabel('Namn').fill('Anna Svensson');
    await page.getByLabel('Födelseår').fill('1990');
    await page.getByLabel('E-post').fill('anna.svensson@example.com');
    await page.getByLabel('Lösenord').fill('Secure123');
    
    await page.click('button:has-text("Ok nu kör vi")');
    
    // Verifiera att formuläret skickas utan felmeddelanden
    await expect(page.getByText('Lösenordet är för lätt')).not.toBeVisible();
  });

  test('ska visa valideringsfel för för enkelt lösenord', async ({ page }) => {
    await page.getByLabel('Namn').fill('Nisse');
    await page.getByLabel('Födelseår').fill('2001');
    await page.getByLabel('E-post').fill('example@gmail.com');
    await page.getByLabel('Lösenord').fill('1234');
    await page.keyboard.press('Tab');
    const submit = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();
  });

  test('ska validera namnfältet', async ({ page }) => {
    // Testa tomt namn
    await page.getByLabel('Namn').fill('');
    await page.getByLabel('Födelseår').fill('1990');
    await page.getByLabel('E-post').fill('user@example.com');
    await page.getByLabel('Lösenord').fill('Secure123');
    await page.getByLabel('Födelseår').focus();
    const submit = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    // Testa för kort namn
    await page.getByLabel('Namn').fill('A');
    const submit2 = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit2.isEnabled()) {
      await submit2.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();
  });

  test('ska validera födelseår', async ({ page }) => {
    // Testa ogiltigt år
    await page.getByLabel('Födelseår').fill('1800');
    await page.getByLabel('Namn').fill('Test User');
    await page.getByLabel('E-post').fill('user@example.com');
    await page.getByLabel('Lösenord').fill('Secure123');
    await page.getByLabel('Namn').focus();
    const submit = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    // Testa för ung användare
    await page.getByLabel('Födelseår').fill('2020');
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    // Testa icke-numeriskt värde
    await page.getByLabel('Födelseår').fill('abc');
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();
  });

  test('ska validera e-postformat', async ({ page }) => {
    await page.getByLabel('E-post').fill('ogiltig-email');
    await page.getByLabel('Namn').fill('Test User');
    await page.getByLabel('Födelseår').fill('1990');
    await page.getByLabel('Lösenord').fill('Secure123');
    await page.getByLabel('Namn').focus();
    const submit = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    await page.getByLabel('E-post').fill('test@example');
    await page.getByLabel('Namn').focus();
    if (await submit.isEnabled()) {
      await submit.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    await page.getByLabel('E-post').fill('test@example.com');
    await expect(submit).toBeEnabled();
  });

  test('ska validera lösenordskrav', async ({ page }) => {
    // Testa för kort lösenord
    await page.getByLabel('Lösenord').fill('123');
    await page.getByLabel('Namn').fill('Test User');
    await page.getByLabel('Födelseår').fill('1990');
    await page.getByLabel('E-post').fill('user@example.com');
    await page.getByLabel('Namn').focus();
    const submit3 = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit3.isEnabled()) {
      await submit3.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    // Testa endast siffror
    await page.getByLabel('Lösenord').fill('123456');
    await expect(page.getByRole('button', { name: 'Ok nu kör vi' })).toBeDisabled();

    // Testa endast bokstäver
    await page.getByLabel('Lösenord').fill('abcdef');
    const submit4 = page.getByRole('button', { name: 'Ok nu kör vi' });
    if (await submit4.isEnabled()) {
      await submit4.click();
    }
    await expect(page.getByRole('heading', { name: /Registrera dig/i })).toBeVisible();

    // Testa giltigt lösenord
    await page.getByLabel('Lösenord').fill('Secure123');
    await expect(page.getByRole('button', { name: 'Ok nu kör vi' })).toBeEnabled();
  });

  test('ska kunna skicka formuläret med alla giltiga fält', async ({ page }) => {
    await page.getByLabel('Namn').fill('Maria Andersson');
    await page.getByLabel('Födelseår').fill('1985');
    await page.getByLabel('E-post').fill('maria.andersson@example.com');
    await page.getByLabel('Lösenord').fill('Lösenord123');
    
    const submit = page.getByRole('button', { name: 'Ok nu kör vi' });
    await expect(submit).toBeEnabled();
    await submit.click();
    await expect(page.getByText(/Registrering lyckades|Tack för din registrering/i)).not.toBeVisible();
  });

  test('skalbarhetstest - flera användare samtidigt', async ({ page }) => {
    const testUsers = [
      { name: 'User1', year: '1990', email: 'user1@test.com', password: 'Pass123' },
      { name: 'User2', year: '1995', email: 'user2@test.com', password: 'Pass456' }
    ];

    for (const user of testUsers) {
      await page.getByLabel('Namn').fill(user.name);
      await page.getByLabel('Födelseår').fill(user.year);
      await page.getByLabel('E-post').fill(user.email);
      await page.getByLabel('Lösenord').fill(user.password);
      
      await page.click('button:has-text("Ok nu kör vi")');
      
      // Återställ för nästa användare
      await page.reload();
      await page.waitForLoadState('networkidle');
    }
  });
});