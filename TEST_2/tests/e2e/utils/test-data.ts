export const TEST_USERS = {
  valid: { name: 'Test User', year: '1990', email: `test${Date.now()}@example.com`, password: 'Secure123' },
  invalid: {
    shortName: { name: 'A', year: '1990', email: 'a@example.com', password: 'Secure123' },
    oldYear: { name: 'User', year: '1800', email: 'u@example.com', password: 'Secure123' },
    youngYear: { name: 'User', year: '2020', email: 'u@example.com', password: 'Secure123' },
    badEmail: { name: 'User', year: '1990', email: 'bademail', password: 'Secure123' },
    weakPasswords: ['123', '123456', 'abcdef']
  }
};