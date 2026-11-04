# PS Number: 9
# Project Title: Simple Banking System
# Student Name: Tej Prakash Nishad
# Email: tej.prakash.nishad@rungta.org
# Section: BCA 1B
import json
import os

FILE = "bank.txt"
MIN_BALANCE = 500


def load_data():
    if os.path.exists(FILE):
        try:
            with open(FILE, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, OSError):
            print("Error reading bank.txt")
    return {}


def save_data():
    with open(FILE, "w") as f:
        json.dump(accounts, f, indent=4)


def get_amount(message):
    while True:
        try:
            amount = float(input(message))
            if amount <= 0 or amount == float("inf") or amount != amount:
                print("Enter a valid positive amount.")
            elif round(amount, 2) != amount:
                print("Enter at most 2 decimal places.")
            else:
                return round(amount, 2)
        except ValueError:
            print("Invalid input! Enter a number.")


def create_account():
    name = input("Enter customer name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    amount = get_amount("Enter opening deposit: ")

    if amount < MIN_BALANCE:
        print("Minimum opening deposit is Rs.500")
        return

    acc_no = str(max([int(x) for x in accounts] + [1000]) + 1)

    accounts[acc_no] = {
        "name": name,
        "balance": amount
    }

    save_data()

    print("\nAccount created successfully!")
    print("Account Number:", acc_no)
    print("Balance: Rs.", format(amount, ".2f"))


def deposit():
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = get_amount("Enter deposit amount: ")

    accounts[acc_no]["balance"] = round(
        accounts[acc_no]["balance"] + amount, 2
    )

    save_data()

    print("Deposit successful!")
    print("Balance: Rs.", accounts[acc_no]["balance"])


def withdraw():
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    amount = get_amount("Enter withdrawal amount: ")

    balance = accounts[acc_no]["balance"]

    if round(balance - amount, 2) < MIN_BALANCE:
        print("Withdrawal failed!")
        print("Minimum Rs.500 balance must remain.")
        return

    accounts[acc_no]["balance"] = round(balance - amount, 2)

    save_data()

    print("Withdrawal successful!")
    print("Balance: Rs.", accounts[acc_no]["balance"])


def transfer():
    sender = input("Enter sender account number: ")
    receiver = input("Enter receiver account number: ")

    if sender not in accounts:
        print("Sender account not found!")
        return

    if receiver not in accounts:
        print("Account", receiver, "not found.")
        print("Transfer cancelled.")
        return

    if sender == receiver:
        print("Cannot transfer to the same account.")
        return

    amount = get_amount("Enter transfer amount: ")

    if round(accounts[sender]["balance"] - amount, 2) < MIN_BALANCE:
        print("Insufficient balance!")
        print("Minimum Rs.500 must remain.")
        return

    accounts[sender]["balance"] = round(
        accounts[sender]["balance"] - amount, 2
    )

    accounts[receiver]["balance"] = round(
        accounts[receiver]["balance"] + amount, 2
    )

    save_data()

    print("\nTransfer successful!")
    print(sender, "balance:", accounts[sender]["balance"])
    print(receiver, "balance:", accounts[receiver]["balance"])


def balance_enquiry():
    acc_no = input("Enter account number: ")

    if acc_no not in accounts:
        print("Account not found!")
        return

    print("\nAccount Number:", acc_no)
    print("Customer Name:", accounts[acc_no]["name"])
    print("Balance: Rs.", accounts[acc_no]["balance"])


accounts = load_data()

while True:
    print("\n===== SIMPLE BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. Balance Enquiry")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        create_account()

    elif choice == "2":
        deposit()

    elif choice == "3":
        withdraw()

    elif choice == "4":
        transfer()

    elif choice == "5":
        balance_enquiry()

    elif choice == "6":
        print("Thank you for using Simple Banking System!")
        break

    else:
        print("Invalid choice! Please select 1 to 6.")
