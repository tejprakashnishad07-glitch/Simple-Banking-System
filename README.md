# Simple Banking System

## Project Description
Simple Banking System is a Python-based mini project that allows users to perform basic banking operations using a menu-driven console application.

## Programming Language
- Python 3

## Concepts Used
- Functions
- Loops
- Conditional Statements
- File Handling
- Dictionaries

## Features
1. Create a new bank account
2. Deposit money
3. Withdraw money
4. Transfer money between accounts
5. Check account balance
6. Save account details in bank.txt

## Project Requirements
- Account numbers start from 1001.
- Minimum account balance is Rs.500.
- Account details are stored in bank.txt.
- Invalid inputs and insufficient balance are handled.

## How to Run
1. Install Python 3.
2. Download the project.
3. Open the project folder.
4. Run the following command:

```bash
python banking_system.py
```

5. Select an option from the menu.

## Sample Output
```text
===== SIMPLE BANKING SYSTEM =====
1. Create Account
2. Deposit Money
3. Withdraw Money
4. Transfer Money
5. Balance Enquiry
6. Exit

Enter your choice: 1
Enter customer name: Anil
Enter opening deposit: 2000

Account created successfully!
Account Number: 1001
Balance: Rs. 2000.00
```

## Test Cases

| Test Case | Expected Result |
|---|---|
| Create account with Rs.2000 | Account 1001 created |
| Withdraw Rs.1500 from Rs.2000 | Balance Rs.500 |
| Transfer to invalid account 9999 | Transfer cancelled |
| Transfer Rs.1000 from 1002 to 1001 | Balances Rs.2000 and Rs.3000 |

## Conclusion
This project demonstrates basic banking operations using Python functions, loops, conditions, and file handling. It helps beginners understand how to build a simple menu-driven application.

## Project Type
BCA Mini Project – Python Programming
