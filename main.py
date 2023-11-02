# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
def read_balance():
    try:
        with open("bank.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("Balance:"):
                    balance_str = line.split()[1]  # Extract the numeric part of the balance string
                    # Remove the currency symbol ("R") and comma, then convert to float
                    balance_str = balance_str.replace("R", "").replace(",", "")
                    return float(balance_str)
    except FileNotFoundError:
        print("No existing balance file found. Starting with balance 0.0.")
    except Exception as e:
        print("Error occurred while reading balance:", str(e))
    return 0.0

# Read username and password from the file

# Rest of the functions and main loop
balance = read_balance()

# Function to update the user's transaction history
# Function to register a new user
def register_user():
    name = input("Enter your name: ")
    password = input("Create a password: ")

    # Generate a random account number
    account_number = str(random.randint(100000, 999999))

    # Save user information to the bank data file
    with open('bank.txt', "a") as file:
        file.write(f"{name},{password},{account_number},0.0\n")  # Initial balance is 0.0
    print("Registration successful. Your account number is:", account_number)

def save_balance(balance):
    try:
        with open("bank.txt", "r") as file:
            lines = file.readlines()

        with open("bank.txt", "w") as file:
            for line in lines:
                if line.startswith("Balance:"):
                    # Update the existing balance line with the new balance
                    updated_line = "Balance: R%.2f\n" % balance
                    file.write(updated_line)
                else:
                    # Write other lines back to the file
                    file.write(line)

    except Exception as e:
        print("Error occurred while updating balance:", str(e))


# Deposit function
def deposit(balance):
    while True:
        try:
            deposit_amount = float(input("How much do you want to deposit? "))
            if deposit_amount <= 0:
                print("Invalid deposit amount. Please enter a positive number.")
            else:
                balance += deposit_amount
                print("Your new balance is: R%.2f" % balance)
                save_balance(balance)  # Save the updated balance to the file

                # Write deposit transaction details to statement file
                with open("statement.txt", "a") as statement_file:
                    statement_file.write("Deposit: R%.2f\n" % deposit_amount)
                    statement_file.write("Available Balance: R%.2f\n" % balance)

                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return balance


# Withdraw function
def withdraw(balance):
    while True:
        try:
            withdraw_amount = float(input("How much do you want to withdraw? "))
            if withdraw_amount <= 0:
                print("Invalid withdrawal amount. Please enter a positive number.")
            elif withdraw_amount > balance:
                print("Insufficient funds. Your balance is: R%.2f" % balance)
            else:
                balance -= withdraw_amount
                print("Your new balance is: R%.2f" % balance)
                save_balance(balance)  # Save the updated balance to the file

                # Write withdrawal transaction details to statement file
                with open("statement.txt", "a") as statement_file:
                    statement_file.write("Withdrawal: R%.2f\n" % withdraw_amount)
                    statement_file.write("Available Balance: R%.2f\n" % balance)

                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    return balance


# Investment function
def calculate_interest():
    while True:
        try:
            initializer = float(input("How much do you want to invest? "))
            if initializer <= 0:
                print("Invalid input. Please enter a valid amount greater than 0.")
                continue  # Ask for input again if it's less than or equal to 0

            months = int(input("For how many months? "))
            percentage = float(input("What is the percentage of the investment? "))

            percent = percentage / 100
            interest = initializer * percent * months
            total_output = initializer + interest
            print("Your earned interest is: R%.2f" % interest)
            print("Total interest is: R%.2f" % total_output)
            break

        except ValueError:
            print("Invalid input. Please enter a valid number.")

import hashlib

def read_user_data(file_name):
    user_data = {}
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()

        for line in lines:
            username, hashed_password = line.strip().split(',')
            user_data[username] = hashed_password
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return user_data

def login():
    MAX_LOGIN_ATTEMPTS = 3
    file_name = 'bank.txt'
    user_data = read_user_data(file_name)

    attempts = 0
    while attempts < MAX_LOGIN_ATTEMPTS:
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")

        # Hash the input password for comparison
        hashed_password_input = hashlib.sha256(password_input.encode()).hexdigest()

        # Check if the username exists and the password matches the hashed password
        if username_input in user_data and user_data[username_input] == hashed_password_input:
            print("Login successful!")
            break
        else:
            print("Incorrect username or password. Please try again.")
            attempts += 1

    if attempts == MAX_LOGIN_ATTEMPTS:
        print("Too many login attempts. Your account is locked.")

while True:
    log = input("Sign In or Sign Up"). lower()
    if log == "sign in":
        login()
    elif log == "sign up":
        register_user()
    else:
        print("wrong input")
        break
    print(
        "How may we help you?\n '1' to deposit\n '2' to withdraw\n '3' to view balance\n '4' to invest\n '5' to view statement\n '6' to exit ")
    answer = input().lower()

    if answer == "1":
        balance = deposit(balance)
    elif answer == "2":
        balance = withdraw(balance)
    elif answer == "3":
        print("The balance is: R%.2f" % balance)
    elif answer == "4":
        calculate_interest()
    elif answer == "5":
        try:
            with open("statement.txt", "r") as statement_file:
                content = statement_file.read()
                print("Statement:\n", content)
        except FileNotFoundError:
            print("No statement file found.")
        except Exception as e:
            print("Error occurred while reading statement file:", str(e))
    elif answer == "6":
        print("Are you sure you want to exit? (yes/no)")
        confirm_exit = input().lower()
        if confirm_exit == "yes":
            print("Thank you for using our banking service. Goodbye!")
            break
    else:
        print("Invalid option. Please try again.")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
