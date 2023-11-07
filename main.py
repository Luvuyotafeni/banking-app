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
file_path = 'bank.txt'  # Replace 'bank.txt' with the path to your credentials file
try:
    with open(file_path, 'r') as file:
        # Read the first line from the file
        first_line = file.readline()

        # Check if the first line is not empty
        if first_line:
            # Split the first line into username and password
            username, password = first_line.strip().split(maxsplit=1)
        else:
            print("The file is empty.")
            exit()
except FileNotFoundError:
    print("Error: Credentials file not found.")
    exit()

# Ask for username and password
while True:
    required_user = input("Enter username: ")
    required_password = input("Enter password: ")

    # Verify username and password
    if required_user == username and required_password == password:
        print("Welcome to the program")
        break
    else:
        print("Wrong username or password. Please try again.")

# Rest of the functions and main loop
balance = read_balance()


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
            months = int(input("For how many months? "))
            percentage = float(input("What is the percentage of the investment? "))
            percent = percentage / 100
            interest = initializer * percent * months
            total_output = initializer + interest
            print("Your earned interest is: R%.2f" % interest)
            print("total interest is: R%.2f" % total_output)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")


while True:
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
