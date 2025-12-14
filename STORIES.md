# User Stories for Läslistan

This document outlines the user stories that guided the development of the automated test suite.

---

## 1. Navigation
**As a** user,
**I want to** navigate between the main sections of the website (Katalog, Lägg till bok, Mina böcker),
**so that I can** access the different functionalities provided by the site.

#### Scenarios Tested:
- Navigate from the default "Katalog" page to all other pages.

---

## 2. View Book Catalog
**As a** user,
**I want to** view a list of available books in the catalog,
**so that I can** see what books are available to choose from.

#### Scenarios Tested:
- Verify that the welcome header is visible.
- Verify that a list of books is displayed on the page.

---

## 3. Add New Book
**As a** user,
**I want to** add a new book to the catalog by providing a title and author,
**so that I can** include books that are not already in the system.

#### Scenarios Tested:
- Add a book with a valid title and author.
- Verify that the submit button is disabled if the title is missing.

---

## 4. Manage Favorite Books
**As a** user,
**I want to** mark books in the catalog as my favorites,
**so that I can** create a personalized reading list.

#### Scenarios Tested:
- Mark a book as a favorite.
- Unmark a book that is already a favorite (toggling).
- Toggle the favorite status multiple times.

---

## 5. View Favorite Books
**As a** user,
**I want to** view my list of favorite books on the "Mina böcker" page,
**so that I can** easily see all the books I have selected.

#### Scenarios Tested:
- View a list containing multiple favorite books.
- View the page when no books have been marked as favorites and verify the empty state message.
