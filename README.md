# Reading List Web Application Tests

Detta projekt innehåller automatiserade end-to-end-tester för webbsidan "Läslistan". Testerna är skrivna i Python med Behave-ramverket och Playwright.

## Vad som har testats

Testpaketet täcker följande funktionalitet:

1. **Navigation**: Verifierar navigation mellan sidorna "Katalog", "Lägg till bok" och "Mina böcker".
2. **Visa katalog**: Bekräftar att bokkatalogen laddas och visar böcker.
3. **Lägga till nya böcker**: Testar att lägga till böcker med giltiga titlar/författare och hantering av ogiltiga data (t.ex. tom titel).
4. **Hantera favoriter**: Täcker att markera och avmarkera böcker som favoriter, inklusive att växla favoritstatus flera gånger.
5. **Visa favoritböcker**: Säkerställer att sidan "Mina böcker" visar användarens favoritböcker och visar ett tomt tillstånd när inga favoriter är valda.

## Hur man startar projektet

### Förutsättningar

*   Python 3.8 eller senare
*   Git

### Installationsinstruktioner

1.  **Klona repositoryt:**
    ```bash
    git clone <repository-url>
    cd reading-list-tests
    ```

2.  **Skapa och aktivera ett virtuellt miljö:**
    *   På macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   På Windows:
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

3.  **Installera beroenden:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Installera Playwright-webbläsare:**
    ```bash
    playwright install chromium
    ```

### Köra testerna

*   **För att köra alla tester:**
    ```bash
    behave
    ```

*   **För att köra i headless-läge (snabbare, ingen synlig webbläsare):**
    ```bash
    behave -D headless=true
    ```

*   **För att köra en specifik feature:**
    ```bash
    behave features/navigation.feature
    ```

## Testdesign

*   **Behavior-Driven Development (BDD):** Tester är skrivna i Gherkin (`.feature`-filer) för att beskriva applikationens beteende från användarens perspektiv.
*   **Page Object Model (POM):** Katalogen `features/pages` separerar UI-interaktionslogik från teststegen, vilket gör koden renare och lättare att underhålla.
*   **Optimerad testmiljö:** Testuppsättningen i `features/environment.py` är optimerad för hastighet och startar webbläsaren endast en gång för hela testpaketet.
