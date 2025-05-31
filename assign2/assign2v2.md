# Assignment 2: PyQt6 Password Manager

**To be done individually or in teams of two students :**

- If done individually, you only need to do _Part 1_
- If done in a team of students, you need to do both parts.

**Due date**: June 1 before midnight

## Part 1: Password Generator

- **Password Options:**
    - Users can select the password length (between 8 and 64 characters) using a slider and increment/decrement buttons.
    - Users can choose which character types to include in the password (lowercase, uppercase, digits, symbols) using
      checkboxes.
    - The application must ensure that at least one character type is selected.

- **Password Generation:**
    - When the user clicks "Generate," a new password is created based on the selected options.
    - If the "validate" option is enabled (optional extension), the password must contain at least one character from
      each selected type.

- **Password Display:**
    - The generated password is shown in a large, selectable label.
    - Users can toggle between showing the actual password and hiding it (displaying asterisks instead) with a "Show"
      checkbox.

- **Copy Functionality:**
    - A "Copy" button copies the current password to the clipboard.

- **User Interface:**
    - The main window should be resizable and visually organized.
    - Use layouts (vertical and horizontal) to arrange widgets as in the example.

---

## Part 2: Secure Password Vault

Extend your application to manage a collection of encrypted email/password pairs.

**New Requirements:**

- **Encrypted Storage:**
    - Automatically load/save email-password pairs from/to a hard-coded filename (e.g., `vault.enc`) on startup/exit
    - Use a predefined encryption/decryption interface (details provided separately)

- **Password List Interface:**
    - Display saved credentials in a scrollable list widget showing emails with masked passwords (`******* `)
    - Support double-click/context menu to reveal the full password temporarily
    - Allow sorting entries by email alphabetically

- **Entry Management:**
    - **Add New:** Button to open a dialog with:
        - Email input field
        - Password field (with the "Generate" button launching Part 1's window)
    - **Edit:** Modify existing entries' email or password
    - **Delete:** Remove entries with the confirmation dialog

- **UI Integration:**
    - The main window must show the credential list and management controls
    - Part 1's password generator becomes a reusable dialog/popup

---

## Deliverables

- A git repository on GitHub shared with user **profdenis**, containing :
    - `main.py`: Your PyQt6 application code.
    - `genpass.py`: A module containing password generation logic (you may adapt the provided example).
    - A short README describing how to run your application.
- Each file should start with a comment (or comments) containing the name, student number, and the GitHub username of
  each student

---

## Grading Criteria

- **Functionality:** All required features work as described.
- **Code Structure:** Code is organized, modular, and uses PyQt6 best practices.
- **Usability:** The interface is clear and easy to use.
- **Documentation:** README and code comments are clear and helpful.
- **Data Integrity:** No data loss between sessions
- **UI Consistency:** Logical flow between the main list and password generator
- **Error Handling:** Graceful recovery for missing/corrupted vault files

---

## Bonus (Optional)

- Add search/filter functionality for emails
- Implement password strength indicators in the list
- Add categories/tags for credentials

---

## Constraints

- Use PyQt6 widgets only (no external UI libraries)
- Encryption implementation details will be provided separately  

