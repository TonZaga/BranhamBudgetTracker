"""
Branham Budget Tracker

created by: Anthony Branham
created on: 2/19/2021
last updated on: 2/25/2021

"""

import pandas as pd
import xlsxwriter
from openpyxl import load_workbook
import os.path
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


def create_workbook():
        if not os.path.exists("BudgetTracker.xlsx"):
            writer = pd.ExcelWriter("BudgetTracker.xlsx", engine="xlsxwriter")
            writer.save()
        else:
            pass

    
def set_categories():
            try:
                df1 = pd.DataFrame(            
                    index=["Mortgage/Rent", "Utilities", "Transportation", "Food", "Entertainment", "Debts", "Other"],
                    columns=["Planned", "Spent", "Remaining"])
                df1_verify = load_workbook("BudgetTracker.xlsx", read_only=True)
                if "Categories" in df1_verify.sheetnames:
                    pass
                else:
                    with pd.ExcelWriter("BudgetTracker.xlsx", mode="w") as writer:
                        df1.to_excel(writer, sheet_name="Categories")
            except PermissionError:
                print("Can't access because Excel file is open.  Please close the file and try again")
                print_mainmenu()

def create_inc_sheet():
        try:
            df2 = pd.DataFrame(            
                index=[],
                columns=["Income", "Planned", "Received"])
            df2_verify = load_workbook("BudgetTracker.xlsx", read_only=True)
            if "Incomes" in df2_verify.sheetnames:
                pass
            else:
                with pd.ExcelWriter("BudgetTracker.xlsx", mode="a", engine="openpyxl") as writer:
                    df2.to_excel(writer, sheet_name="Incomes")
        except PermissionError:
            print("Can't access because Excel file is open.  Please close the file and try again")
            print_mainmenu()

def create_exp_sheet():
        try:
            df3 = pd.DataFrame(            
                index=[],
                columns=["Income", "Planned", "Received"])
            df2_verify = load_workbook("BudgetTracker.xlsx", read_only=True)
            if "Incomes" in df2_verify.sheetnames:
                pass
            else:
                with pd.ExcelWriter("BudgetTracker.xlsx", mode="a", engine="openpyxl") as writer:
                    df2.to_excel(writer, sheet_name="Incomes")
        except PermissionError:
            print("Can't access because Excel file is open.  Please close the file and try again")
            print_mainmenu()


def print_mainmenu():
    main_option = ""
    while main_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("   MAIN MENU   ")
        print(30 * '-')
        print("1. Income menu")
        print("2. Expenses menu")
        print("3. Generate breakdown")
        print("q. Quit")
        print(30 * '-')
        option = input("Enter an option: ")
        if option.lower() == 'q':
            print("Exiting program...")
            exit()
        elif option == "1":
            main_option = income_menu()
        elif option == "2":
            main_option = expenses_menu()
        elif option == "3":
            print("Generating breakdown")
        else:
            print("Invalid option.  Please try again")


def income_menu():
    create_workbook()
    set_categories()
    create_inc_sheet() 
    inc_option = ""
    while inc_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("   INCOME MENU   ")
        print(30 * '-')
        print("1. Show Income(s)")
        print("2. Enter new income")
        print("3. Edit existing income")
        print("4. return to Main menu")
        print("q. Quit")
        print(30 * '-')
        inc_option = input("Enter an option: ")
        if inc_option.lower() == "q":
            print("Exiting program...")
        # elif inc_option = "1":

        # elif inc_option = "2":

        # elif inc_option = "3":

        elif inc_option == "4":
            print_mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            income_menu()


def expenses_menu():
    exp_option = ""
    while exp_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("   EXPENSES MENU   ")
        print(30 * '-')
        print("1. Show expense(s)")
        print("2. Enter new expense")
        print("3. Edit existing expense")
        print("4. return to Main menu")
        print("q. Quit")
        print(30 * '-')
        exp_option = input("Enter an option: ")
        if exp_option.lower() == "q":
            print("Exiting program...")
        # elif inc_option = "1":

        # elif inc_option = "2":

        # elif inc_option = "3":

        elif exp_option == "4":
            print_mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            expenses_menu()


    # """Get user menu option"""
    # choice = int(input('Enter an option: '))


    


#     """Configure navigation menu"""
#     income_list = []
#     expense_list = []

#     if choice == 1:
#             create_workbook()
#             set_categories()
#             create_inc_sheet()
#             # print_mainmenu()
#             choice
#     elif choice == 2:
#         create_inc_sheet()
#         # """Getting income inputs from user / creating or appending incomes.csv file"""
#         # num_of_incomes = int(input("How many incomes are you adding? "))
#         # if num_of_incomes <= 0:
#         #         print("You need to add an income.")
#         # total = 0
#         # for i in range(1, num_of_incomes + 1):
#         #         with open("incomes.csv", "a", newline="") as income_list:
#         #             income_amount = float(input("Add an income amount: "))
#         #             income_type = input("Type of income: ")
#         #             writer = csv.writer(income_list)
#         #             writer.writerow([income_amount, income_type])
#         #         # with open("incomes.csv", "r") as income_list:
#         #         #     reader = csv.reader(income_list, delimiter = '\n')
#         print_mainmenu()
#         choice
#     elif choice == 3:
#         """Getting expense inputs from user / creating or appending expenses.csv file"""
#         num_of_expenses = int(input("How many expenses are you adding? "))
#         if num_of_expenses <= 0:
#             print("You need to add an expense.")
#         total = 0

#         for i in range(1, num_of_expenses + 1):
#             with open("expenses.csv", "a", newline="") as expense_list:
#                 expense_amount = float(input("Add an expense amount: "))
#                 expense_type = input("Type of expense: ")
#                 writer = csv.writer(expense_list)
#                 writer.writerow([expense_amount, expense_type])
#         print_mainmenu()
#         choice
#     elif choice == 4:
#             if os.path.exists("incomes.csv"):
#                 with open("incomes.csv", "r") as income_list:
#                     print("Generating table... ")
#                     print_mainmenu()
#                     choice
#             else:
#                 print("Not enough incomes or expenses to calculate.\nPlease add amounts and try again")
#                 print_mainmenu()
#                 choice
#     elif choice == 5:
#             print ("Exiting program... ")
#     else:
#             print ("Invalid menu option. Try again...")
#             # categories()
#             # print_menu()

print_mainmenu()




## Archived code ##

# def cat_list():
#     """Read and write to the categories file"""
#     categories = []
#     def read_categories():
#             """Read categories.txt file to set default expense categories"""

#             with open("categories.txt", "r") as filename:
#                 categories = filename.read()
#                 print("Current expense categories are: \n{}".format(categories))
#                 filename.close()
#     read_categories()


#     def write_categories():        
#             """Loop through category until user is satisfied"""
#             prompt_new_cat = input(str(("Would you like to add a category? [y / n] "))).upper()
#             while prompt_new_cat == "Y":
#                 added = input("What is the name of the category you want to add? ")
#                 with open("categories.txt", "a") as filename:
#                     filename.write("\n" + added)
#                 prompt_new_cat = input("Would you like to add a category? [y / n] ").upper()
#     write_categories()

#     categories = open("categories.txt", "r")
#     categories = categories.read()
#     print("Current expense categories are: \n{}".format(categories))