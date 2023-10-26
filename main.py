# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
balance = 0


def deposit(balance):
    try:
        deposit_amount = float(input("How much do you want to deposit? "))
        if deposit_amount <= 0:
            print("Invalid deposit amount. Please enter a positive number.")
        else:
            balance += deposit_amount
            print("Your new balance is: R%.2f" % balance)
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
        print("Your earned interest is: R%.2f" % interest)
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def view_balance():
    print("The balance is: R%.2f" % balance)


while True:
    print(
        "How may we help you? (Type 'done' to exit, 'withdraw' to withdraw, 'deposit' to deposit, 'invest' to invest, 'balance' to view balance)")
    answer = input().lower()

    if answer == "done":
        print("Are you sure you want to exit? (yes/no)")
        confirm_exit = input().lower()
        if confirm_exit == "yes":
            print("Thank you for using our banking service. Goodbye!")
            break
        else:
            continue
    elif answer == "withdraw":
        balance = withdraw(balance)
    elif answer == "deposit":
        balance = deposit(balance)
    elif answer == "invest":
        calculate_interest()
    elif answer == "balance":
        view_balance()
    else:
        print("Invalid option. Please try again.")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
