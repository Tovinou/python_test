# Test Cases

## Form Loading
- ID: TC-FORM-LOAD-001
- Title: Page loads and core elements are visible
- Preconditions: User has network connectivity
- Steps:
  - Navigate to `https://tap-ht24-testverktyg.github.io/form-demo/`
  - Wait for `networkidle`
- Expected:
  - Heading "Registrera dig" is visible
  - Inputs for `Namn`, `Födelseår`, `E-post`, `Lösenord` are visible
  - Submit button `Ok nu kör vi` is visible

## Name Field Validation
- ID: TC-NAME-VAL-001
- Title: Empty name shows validation message
- Preconditions: Form is loaded
- Steps:
  - Leave `Namn` empty
  - Click submit
- Expected:
  - Validation message indicates name is required

- ID: TC-NAME-VAL-002
- Title: Too short name shows validation message
- Preconditions: Form is loaded
- Steps:
  - Enter `Namn` as `A`
- Expected:
  - Validation message indicates minimum 2 characters

## Birth Year Validation
- ID: TC-YEAR-VAL-001
- Title: Out of range year is invalid
- Preconditions: Form is loaded
- Steps:
  - Enter `Födelseår` as `1800`
  - Click submit
- Expected:
  - Validation message indicates invalid birth year

- ID: TC-YEAR-VAL-002
- Title: Too young user is rejected
- Preconditions: Form is loaded
- Steps:
  - Enter `Födelseår` as `2020`
- Expected:
  - Validation message indicates minimum age requirement

- ID: TC-YEAR-VAL-003
- Title: Non‑numeric year is invalid
- Preconditions: Form is loaded
- Steps:
  - Enter `Födelseår` as `abc`
- Expected:
  - Validation message indicates numeric input required

## Email Validation
- ID: TC-EMAIL-VAL-001
- Title: Invalid email formats are rejected
- Preconditions: Form is loaded
- Steps:
  - Enter `ogiltig-email` in `E-post`
  - Click submit
- Expected:
  - Validation message indicates invalid email address

- ID: TC-EMAIL-VAL-002
- Title: Missing domain is rejected
- Preconditions: Form is loaded
- Steps:
  - Enter `test@example` in `E-post`
- Expected:
  - Validation message indicates invalid email address

- ID: TC-EMAIL-VAL-003
- Title: Valid email passes validation
- Preconditions: Form is loaded
- Steps:
  - Enter `test@example.com` in `E-post`
- Expected:
  - No email validation error shown

## Password Validation
- ID: TC-PASS-VAL-001
- Title: Password too short is rejected
- Preconditions: Form is loaded
- Steps:
  - Enter `123` in `Lösenord`
  - Click submit
- Expected:
  - Validation message indicates minimum length

- ID: TC-PASS-VAL-002
- Title: Digits only are rejected
- Preconditions: Form is loaded
- Steps:
  - Enter `123456` in `Lösenord`
- Expected:
  - Validation message indicates letters and digits required

- ID: TC-PASS-VAL-003
- Title: Letters only are rejected
- Preconditions: Form is loaded
- Steps:
  - Enter `abcdef` in `Lösenord`
- Expected:
  - Validation message indicates letters and digits required

- ID: TC-PASS-VAL-004
- Title: Strong password passes validation
- Preconditions: Form is loaded
- Steps:
  - Enter `Secure123` in `Lösenord`
- Expected:
  - No password strength error shown

## Successful Registration
- ID: TC-FORM-SUBMIT-001
- Title: Valid form submits successfully
- Preconditions: Form is loaded, all fields filled with valid data
- Steps:
  - Fill `Namn` = `Maria Andersson`
  - Fill `Födelseår` = `1985`
  - Fill `E-post` = `maria.andersson@example.com`
  - Fill `Lösenord` = `Lösenord123`
  - Click submit
- Expected:
  - Confirmation text like `Registrering lyckades` or `Tack för din registrering` is visible

## Scalability
- ID: TC-SCALE-001
- Title: Multiple sequential submissions succeed
- Preconditions: Form is loaded
- Steps:
  - For each user in a list of two valid users
    - Fill all fields
    - Submit
    - Reload page
- Expected:
  - Each submission performs without UI errors

## Accessibility
- ID: TC-A11Y-001
- Title: Semantic elements and basic interactions
- Preconditions: Form is loaded
- Steps:
  - Verify heading is visible
  - Verify inputs are editable
  - Verify submit button is visible
- Expected:
  - Elements are present and accessible; submit button may be disabled until valid input is provided

## Performance
- ID: TC-PERF-001
- Title: Page load time under threshold
- Preconditions: User has network connectivity
- Steps:
  - Measure time from navigation to `networkidle`
- Expected:
  - Load time < 3 seconds

- ID: TC-PERF-002
- Title: Validation response under threshold
- Preconditions: Form is loaded
- Steps:
  - Trigger an email validation error
  - Measure time until error text is visible
- Expected:
  - Validation response < 1 second

## Notes Input
- ID: TC-NOTES-001
- Title: Free text field retains entered value
- Preconditions: Form is loaded
- Steps:
  - Enter text in `Namn`
- Expected:
  - Field value equals entered text