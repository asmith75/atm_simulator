# atm_simulator

This Python program simulates the functionality of an ATM, allowing a user to deposit, withdraw, and check their balance. It reads the initial balance from a file and writes the final balance to another file. The program offers a simple menu for the user to interact with and manage their account.

## Features:
- **Deposit:** Allows the user to deposit money into their account.
- **Withdraw:** Allows the user to withdraw money from their account, provided there are sufficient funds.
- **Balance Inquiry:** Displays the current balance of the account.
- **File Handling:** Reads the initial balance from a file and writes the final balance to another file.
- **Error Handling:** Handles common errors like insufficient funds, invalid inputs, and missing files.

## Usage:

1. Run the script.
2. The program will:
   - Attempt to read the initial balance from `Projcet_read.txt` (or use a default balance of $5000 if the file is not found).
   - Display the ATM menu.
   - Allow the user to deposit or withdraw money, or check their balance.
3. Upon exiting, the program will write the final balance to `Smith_project.txt`.



