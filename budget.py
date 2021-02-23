"""
Branham Budget Tracker

created by: Anthony Branham
created on: 2/19/2021
last updated on: 2/19/2021

"""

from os import read
import pyfiglet


def print_banner():
    """Print Banner"""
    ascii_banner = pyfiglet.figlet_format("Branham Budget Tracker")
    print(ascii_banner)
print_banner()

def get_name():
    prompt_name = input("Please enter your first name: ")
    first_name = str(prompt_name)
    print("\n\n\nWelcome to BBT, {}!".format(first_name))
get_name()

def cat_list():
    categories = []
    def read_categories():
            """Read categories.txt file to set default expense categories"""

            with open("categories.txt", "r") as filename:
                categories = filename.read()
                print("Current expense categories are: \n{}".format(categories))
                filename.close()
    read_categories()


    def write_categories():        
            """Loop through category until user is satisfied"""
            prompt_new_cat = input(str(("Would you like to add a category? [y / n] "))).upper()
            while prompt_new_cat == "Y":
                added = input("What is the name of the category you want to add? ")
                with open("categories.txt", "a") as filename:
                    filename.write("\n" + added)
                prompt_new_cat = input("Would you like to add a category? [y / n] ").upper()
    write_categories()

    categories = open("categories.txt", "r")
    categories = categories.read()
    print("Current expense categories are: \n{}".format(categories))


def print_menu():
    print(30 * '-')
    print("   MAIN MENU   ")
    print(30 * '-')
    print("1. Enter income")
    print("2. Set categories")
    print("3. Enter expenses")
    print("4. Generate chart")
    print("5. Quit")
    print(30 * '-')

    """Get user menu option"""
    choice = int(input('Enter your choice [1-4] : '))


    """Configure navigation menu"""
    income_list = []
    expense_list = []
    remaining = []

    if choice == 1:
            num_of_incomes = int(input("How many incomes are you adding? "))
            if num_of_incomes <= 0:
                print("You need to add an income.")
            total = 0

            for i in range(1, num_of_incomes + 1):
                income = float(input("Add an income amount: "))
                total += income
                income_list.append(income)
                print("${} has been added to your total.  Your total income is now, ${}.".format(income, sum(income_list)))
            print_menu()
            choice
    elif choice == 2:
            cat_list()
            print_menu()
            choice
    elif choice == 3:
            num_of_expenses = int(input("How many expenses are you adding? "))
            if num_of_expenses <= 0:
                print("You need to add an expense.")
            total = 0

            for i in range(1, num_of_expenses + 1):
                expense = float(input("Add an expense amount: "))
                total += expense
                expense_list.append(expense)
                print("${} has been deducted from your total.  Your total deductions are, ${}.".format(expense, sum(expense_list)))
            print_menu()
            choice
    elif choice == 4:
            if sum(income_list) == 0:
                print("Not enough incomes or expenses to calculate.\nPlease add amounts and try again")
                print_menu()
                choice
            else:
                print("Generating chart... ")
                print_menu()
                choice
    elif choice == 5:
            print ("Exiting program... ")
    else:    ## default ##
            print ("Invalid number. Try again...")

print_menu()