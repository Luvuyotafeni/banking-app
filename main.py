# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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

def save_balance(balance):
    with open("bank.txt", "w") as file:
        file.write("Balance: R%.2f\n" % balance)

# Initialize balance by reading from the file
balance = read_balance()

def deposit(balance):
    try:
        deposit_amount = float(input("How much do you want to deposit? "))
        if deposit_amount <= 0:
            print("Invalid deposit amount. Please enter a positive number.")
        else:
            balance += deposit_amount
            print("Your new balance is: R%.2f" % balance)
            save_balance(balance)  # Save the updated balance to the file
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def withdraw(balance):
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
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    return balance

def calculate_interest():
    try:
        initializer = float(input("How much do you want to invest? "))
        months = int(input("For how many months? "))
        percentage = float(input("What is the percentage of the investment? "))
        percent = percentage / 100
        interest = initializer * percent * months
        total_output = initializer + interest
        print("Your earned interest is: R%.2f" % interest)
        print("total interest is: R%.2f" % total_output)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def view_balance():
    print("The balance is: R%.2f" % balance)

while True:
    print("How may we help you? (Type 'done' to exit, 'withdraw' to withdraw, 'deposit' to deposit, 'invest' to invest, 'balance' to view balance)")
    answer = input().lower()

    # Open the statement file in append mode
    with open("statement.txt", "a") as statement_file:
        # Process deposit and withdrawal actions and write to the file
        if answer == "withdraw":
            try:
                withdraw_amount = float(input("How much do you want to withdraw? "))
                if withdraw_amount <= 0:
                    print("Invalid withdrawal amount. Please enter a positive number.")
                elif withdraw_amount > balance:
                    print("Insufficient funds. Your balance is: R%.2f" % balance)
                else:
                    balance -= withdraw_amount
                    print("Your new balance is: R%.2f" % balance)
                    statement_file.write("Withdrawal: R%.2f\n" % withdraw_amount)
                    statement_file.write("Available Balance: R%.2f\n" % balance)  # Write available balance to the file
                    save_balance(balance)  # Save the updated balance to the file
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif answer == "deposit":
            try:
                deposit_amount = float(input("How much do you want to deposit? "))
                if deposit_amount <= 0:
                    print("Invalid deposit amount. Please enter a positive number.")
                else:
                    balance += deposit_amount
                    print("Your new balance is: R%.2f" % balance)
                    statement_file.write("Deposit: R%.2f\n" % deposit_amount)
                    statement_file.write("Available Balance: R%.2f\n" % balance)  # Write available balance to the file
                    save_balance(balance)  # Save the updated balance to the file
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif answer == "invest":
            calculate_interest()
        elif answer == "statement":
            try:
                with open("statement.txt", "r") as statement_file:
                    content = statement_file.read()
                    print("Statement:\n", content)
            except FileNotFoundError:
                print("No statement file found.")
            except Exception as e:
                print("Error occurred while reading statement file:", str(e))
        elif answer == "balance":
            print("The balance is: R%.2f" % balance)
        elif answer == "done":
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
