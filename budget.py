"""
Branham Budget Tracker

created by: Anthony Branham
created on: 2/19/2021
last updated on: 2/26/2021

"""
import datetime
from calendar import monthrange
from numpy.lib.npyio import load
import pandas as pd
from pandas.core.indexes.base import Index
import xlsxwriter
from openpyxl import load_workbook
import os.path
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
    print("\n\n\nWelcome to BBT, {}!\n".format(first_name))
get_name()


def month_remaining():
    """Get month and days remaining"""
    today = datetime.datetime.today()
    today_date = today.strftime("%B %d, %Y")
    print("Today is " + today_date)
    day_of = int(today.strftime("%d"))
    now = datetime.datetime.now()
    month_end = monthrange(now.year, now.month)[1]
    days_remaining = (month_end) - (day_of)
    print("There are {} days remaining in the month.\n".format(days_remaining))
month_remaining()


def create_workbook():
        if not os.path.exists("BudgetTracker.xlsx"):
            writer = pd.ExcelWriter("BudgetTracker.xlsx", engine="xlsxwriter")
            writer.save()
        else:
            pass

    
def set_categories():
            try:
                df1 = pd.DataFrame(            
                    index=["Housing", "Utilities", "Transportation", "Groceries", "Entertainment", "Debts", "Other"],
                    columns=["Planned", "Spent", "Remaining"])
                df1 = df1.fillna(0)
                df1_verify = load_workbook("BudgetTracker.xlsx", read_only=True)
                if "Categories" in df1_verify.sheetnames:
                    pass
                else:
                    with pd.ExcelWriter("BudgetTracker.xlsx", mode="w") as writer:
                        df1.to_excel(writer, sheet_name="Categories")
            except PermissionError:
                print("Can't access because Excel file is open.  Please close the file and try again")
                mainmenu()


def set_budget():
    df = pd.read_excel("BudgetTracker.xlsx", sheet_name="Categories", usecols=["Planned", "Remaining", "Spent"])
    df = df.fillna(0)
    user_cat = input("What category would you like to set a budget for? ").upper()
    budget_amount = float(input("Enter budget amount: "))
    if user_cat == "HOUSING":
        df.loc[0, 1] = budget_amount
    if user_cat == "UTILITIES":
        df.loc[1, "Planned"] = budget_amount
    if user_cat == "TRANSPORTATION":
        df.loc[2, "Planned"] = budget_amount
    if user_cat == "GROCERIES":
        df.loc[3, "Planned"] = budget_amount
    if user_cat == "ENTERTAINMENT":
        df.loc[4, "Planned"] = budget_amount
    if user_cat == "DEBTS":
        df.loc[5, "Planned"] = budget_amount
    if user_cat == "OTHER":
        df.loc[6, "Planned"] = budget_amount
    else:
        print("Invalid category selection")

    # df1 = pd.DataFrame(data=[add_cat])
    # df = pd.concat([df, df1], ignore_index=True)
    # print(df)
    # with pd.ExcelWriter("BudgetTracker.xlsx", mode="a", engine="openpyxl") as writer:
    #     add_cat.to_excel(writer, sheet_name="Categories")
    # new_cat = pd.concat(([add_cat, df1]), ignore_index=0)
    # with pd.ExcelWriter("BudgetTracker.xlsx", mode="a", engine="openpyxl") as writer:
    #     new_cat.to_excel(writer, sheet_name="Categories")


def create_inc_sheet():
        try:
            df2 = pd.DataFrame(            
                index=[],
                columns=["Date", "Income type", "Income Amount"])
            df2_verify = load_workbook("BudgetTracker.xlsx", read_only=True)
            if "Incomes" in df2_verify.sheetnames:
                pass
            else:
                with pd.ExcelWriter("BudgetTracker.xlsx", mode="a", engine="openpyxl") as writer:
                    df2.to_excel(writer, sheet_name="Incomes")
        except PermissionError:
            print("Can't access because Excel file is open.  Please close the file and try again")
            mainmenu()


def create_exp_sheet():
        try:
            df3 = pd.DataFrame(            
                index= [],
                columns=["Date", "Expense Type", "Expense Amount", "Merchant", "Notes"])
            df3_verify = load_workbook("BudgetTracker.xlsx", read_only=True)
            if "Expenses" in df3_verify.sheetnames:
                pass
            else:
                with pd.ExcelWriter("BudgetTracker.xlsx", mode="a", engine="openpyxl") as writer:
                    df3.to_excel(writer, sheet_name="Expenses")
        except PermissionError:
            print("Can't access because Excel file is open.  Please close the file and try again")
            mainmenu()


def mainmenu():
    main_option = ""
    while main_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("<<<<  MAIN MENU  >>>>")
        print(30 * '-')
        print("1. Category menu")
        print("2. Income menu")
        print("3. Expenses menu")
        print("4. Generate breakdown")
        print("q. Quit")
        print(30 * '-')
        option = input("Enter an option: ")
        if option.lower() == 'q':
            print("Exiting program...")
            exit()
        elif option == "1":
            main_option = category_menu()
        elif option == "2":
            main_option = income_menu()
        elif option == "3":
            main_option = expenses_menu()
        elif option == "4":
            print("Generating breakdown")
            # Add table for calculations between income/expense w/ exception #
        else:
            print("Invalid option.  Please try again")


def category_menu():
    create_workbook()
    set_categories() 
    cat_option = ""
    while cat_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("<<<<  CATEGORY MENU  >>>>")
        print(30 * '-')
        print("1. Show categories")
        print("2. Set budget amount")
        print("3. Edit existing budget")
        print("4. return to Main menu")
        print("q. Quit")
        print(30 * '-')
        cat_option = input("Enter an option: ")
        if cat_option.lower() == "q":
            print("Exiting program...")
        elif cat_option == "1":
            df_category = pd.read_excel("BudgetTracker.xlsx", sheet_name="Categories", index_col=0)
            if df_category.empty:
                print("*** No categories have been added yet ***\n")
                category_menu()
            else:
                print(df_category)
                category_menu()

        elif cat_option == "2":
            df_category = pd.read_excel("BudgetTracker.xlsx", sheet_name="Categories", index_col=0)
            if df_category.empty:
                print("*** No categories have been added yet ***\n")
                category_menu()
            else:
                print(df_category)
                set_budget()
                print("Budget has been set\n")
                category_menu()

        # elif cat_option == "3":
            # Edit an existing income (index #?)

        elif cat_option == "4":
            mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            category_menu()
            
            
def income_menu():
    create_inc_sheet() 
    inc_option = ""
    while inc_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("<<<<  INCOME MENU  >>>>")
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
        elif inc_option == "1":
            df_income = pd.read_excel("BudgetTracker.xlsx", sheet_name="Incomes")
            if df_income.empty:
                print("*** No incomes have been added yet ***\n")
                income_menu()
            else:
                print(df_income)

        # elif inc_option == "2":
            # Enter new income(s)
        # elif inc_option == "3":
            # Edit an existing income (index #?)

        elif inc_option == "4":
            mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            income_menu()


def expenses_menu():
    create_exp_sheet()
    exp_option = ""
    while exp_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("<<<<  EXPENSES MENU  >>>>")
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
        elif exp_option == "1":
            df_expense = pd.read_excel("BudgetTracker.xlsx", sheet_name="Expenses")
            if df_expense.empty:
                print("*** No expenses have been added yet ***\n")
                expenses_menu()
            else:
                print(df_expense)
                expenses_menu()

        # elif exp_option == "2":
            # Enter new expense(s)
        # elif exp_option == "3":
            # Editing existing expense (index #?)
        elif exp_option == "4":
            mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            expenses_menu()

mainmenu()