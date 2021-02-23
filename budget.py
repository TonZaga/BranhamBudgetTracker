"""
Branham Budget Tracker

created by: Anthony Branham
created on: 2/19/2021
last updated on: 2/23/2021

"""

import os.path
from os import read
import csv
import pyfiglet


def print_banner():
    """Print Banner"""
    ascii_banner = pyfiglet.figlet_format("Branham Budget Tracker")
    print(ascii_banner)
print_banner()

def get_name():
    """Get user's name and generate welcome message"""
    prompt_name = input("Please enter your first name: ")
    first_name = str(prompt_name).upper()
    print("\n\n\nWelcome to BBT, {}!".format(first_name))
get_name()

def cat_list():
    """Read and write to the categories file"""
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
    """Print out of navigation menu """
    print(30 * '-')
    print("   MAIN MENU   ")
    print(30 * '-')
    print("1. Set expense categories")
    print("2. Enter income(s)")
    print("3. Enter expense(s)")
    print("4. Generate table")
    print("5. Quit")
    print(30 * '-')

    """Get user menu option"""
    choice = int(input('Enter your choice [1-5]: '))


    """Configure navigation menu"""
    income_list = []
    expense_list = []

    if choice == 1:
            cat_list()
            print_menu()
            choice
    elif choice == 2:
        """Getting income inputs from user / creating or appending incomes.csv file"""
        num_of_incomes = int(input("How many incomes are you adding? "))
        if num_of_incomes <= 0:
                print("You need to add an income.")
        total = 0
        for i in range(1, num_of_incomes + 1):
                with open("incomes.csv", "a", newline="") as income_list:
                    income_amount = float(input("Add an income amount: "))
                    income_type = input("Type of income: ")
                    writer = csv.writer(income_list)
                    writer.writerow([income_amount, income_type])
                # with open("incomes.csv", "r") as income_list:
                #     reader = csv.reader(income_list, delimiter = '\n')
        print_menu()
        choice
    elif choice == 3:
        """Getting expense inputs from user / creating or appending expenses.csv file"""
        num_of_expenses = int(input("How many expenses are you adding? "))
        if num_of_expenses <= 0:
            print("You need to add an expense.")
        total = 0

        for i in range(1, num_of_expenses + 1):
            with open("expenses.csv", "a", newline="") as expense_list:
                expense_amount = float(input("Add an expense amount: "))
                expense_type = input("Type of expense: ")
                writer = csv.writer(expense_list)
                writer.writerow([expense_amount, expense_type])
        print_menu()
        choice
    elif choice == 4:
            if os.path.exists("incomes.csv"):
                with open("incomes.csv", "r") as income_list:
                    print("Generating table... ")
                    print_menu()
                    choice
            else:
                print("Not enough incomes or expenses to calculate.\nPlease add amounts and try again")
                print_menu()
                choice
    elif choice == 5:
            print ("Exiting program... ")
    else:    ## default ##
            print ("Invalid number. Try again...")

print_menu()