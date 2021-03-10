"""
Branham Budget Tracker

created by: Anthony Branham
created on: 2/19/2021
last updated on: 3/10/2021

"""
import datetime
import openpyxl
import os.path
import pyfiglet
from calendar import monthrange


def print_banner():
    # Print Banner
    ascii_banner = pyfiglet.figlet_format("Branham Budget Tracker")
    print(ascii_banner)
print_banner()


def get_name():
    # Get user's name and generate welcome message
    prompt_name = input("Please enter your first name: ")
    first_name = str(prompt_name).upper()
    print("\n\n\nWelcome to BBT, {}!\n".format(first_name))
get_name()


def month_remaining():
    # Get month and days remaining
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
    # Check for file and create if not found
        if not os.path.exists("BudgetTracker.xlsx"):
            wb = openpyxl.Workbook()
            sheet = wb.active
            sheet.title = "Budget"
            # Create income sheet
            ws1 = wb.create_sheet("Sheet_A")
            ws1.title = "Income"
            ws1.sheet_properties.tabColor = "00FF00"
            # Create expenses sheet
            ws2 = wb.create_sheet("Sheet_B")
            ws2.title = "Expenses"
            ws2.sheet_properties.tabColor = "FF0000"
            wb.save(filename="BudgetTracker.xlsx")
        else:
            pass
create_workbook()


def set_categories():
    wb = openpyxl.load_workbook(filename="BudgetTracker.xlsx")
    Budget = wb["Budget"]
    if Budget["A1"].value is None:
    # Create headers
        Budget["A1"] = "CATEGORY"
        Budget["B1"] = "PLANNED"
        Budget["C1"] = "SPENT"
        Budget["D1"] = "REMAINING"
    # Create first column
        Budget["A2"] = "Housing"
        Budget["A3"] = "Utilities"
        Budget["A4"] = "Transportation"
        Budget["A5"] = "Groceries"
        Budget["A6"] = "Entertainment"
        Budget["A7"] = "Debts"
        Budget["A8"] = "Other"
    else:
        pass
    wb.save("BudgetTracker.xlsx")

def create_income_sheet():
    wb = openpyxl.load_workbook(filename="BudgetTracker.xlsx")
    Income = wb["Income"]
    if Income["A1"].value is None:
    # Create headers
        Income["A1"] = "SOURCE"
        Income["B1"] = "AMOUNT"
    else:
        pass
    wb.save("BudgetTracker.xlsx")

def create_expense_sheet():
    wb = openpyxl.load_workbook(filename="BudgetTracker.xlsx")
    Expenses = wb["Expenses"]
    if Expenses["A1"].value is None:
    # Create headers
        Expenses["A1"] = "DATE"
        Expenses["B1"] = "AMOUNT"
        Expenses["C1"] = "MERCHANT"
        Expenses["D1"] = "CATEGORY"
    else:
        pass
    wb.save("BudgetTracker.xlsx")


def set_budget():
    # Prompt user to select a category and set budget amount
    wb = openpyxl.load_workbook(filename="BudgetTracker.xlsx")
    Budget = wb["Budget"]
    user_cat = input("What category would you like to set a budget for? ").upper()
    budget_amount = float(input("Enter budget amount: "))
    if user_cat == "HOUSING":
        Budget["B2"] = budget_amount
        print("Budget for HOUSING has been set to ${}.".format(budget_amount))
    elif user_cat == "UTILITIES":
        Budget["B3"] = budget_amount
        print("Budget for UTILITIES has been set to ${}.".format(budget_amount))
    elif user_cat == "TRANSPORTATION":
        Budget["B4"] = budget_amount
        print("Budget for TRANSPORTATION has been set to ${}.".format(budget_amount))
    elif user_cat == "GROCERIES":
        Budget["B5"] = budget_amount
        print("Budget for GROCERIES has been set to ${}.".format(budget_amount))
    elif user_cat == "ENTERTAINMENT":
        Budget["B6"] = budget_amount
        print("Budget for ENTERTAINMENT has been set to ${}.".format(budget_amount))
    elif user_cat == "DEBTS":
        Budget["B7"] = budget_amount
        print("Budget for DEBTS has been set to ${}.".format(budget_amount))
    elif user_cat == "OTHER":
        Budget["B8"] = budget_amount
        print("Budget for OTHER has been set to ${}.".format(budget_amount))
    else:
        print("Invalid category selection")
    wb.save("BudgetTracker.xlsx")


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
        # elif option == "4":
        #     print("Generating breakdown")
        #     # Add table for calculations between income/expense w/ exception #
        else:
            print("Invalid option.  Please try again")


def category_menu():
    set_categories() 
    cat_option = ""
    while cat_option == "":
        """Print out of navigation menu """
        print(30 * '-')
        print("<<<<  CATEGORY MENU  >>>>")
        print(30 * '-')
        print("1. Show categories")
        print("2. Set budget amount")
        print("3. Return to Main Menu")
        print("q. Quit")
        print(30 * '-')
        cat_option = input("Enter an option: ")
        if cat_option.lower() == "q":
            print("Exiting program...")
        elif cat_option == "1":
            wb = openpyxl.load_workbook("BudgetTracker.xlsx")
            Budget = wb["Budget"]
            print("\nCategories and their budgets are:\n")
            for row_cells in Budget.iter_rows(min_row=2, max_col=2):
                for cell in row_cells:
                    if cell.value == None:
                        print("Not set")
                    else:
                        print(cell.value) 
            category_menu()
        elif cat_option == "2":
            wb = openpyxl.load_workbook("BudgetTracker.xlsx")
            Budget = wb["Budget"]
            print("\nCategories and their budgets are:\n")
            for row_cells in Budget.iter_rows(min_row=2, max_col=2):
                for cell in row_cells:
                    if cell.value == None:
                        print("Not set")
                    else:
                        print(cell.value)
            set_budget()
            category_menu()
        elif cat_option == "3":
            mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            category_menu()
            
            
def income_menu():
    create_income_sheet()
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
            wb = openpyxl.load_workbook("BudgetTracker.xlsx")
            Income = wb["Income"]
            if Income["A2"].value is None:
                print("*** No incomes have been added yet ***\n")
                income_menu()
            else:
                print("\nCurrent Income(s) are:\n")
                for row_cells in Income.iter_rows(min_row=2, max_col=2):
                    for cell in row_cells:
                        print(cell.value)
                income_menu()
        elif inc_option == "2":
            wb = openpyxl.load_workbook(filename="BudgetTracker.xlsx")
            Income = wb["Income"]
            src_income = input("What is the source of this income? ")
            income_amount = float(input("Enter income amount: "))
            Income.append([src_income, income_amount])
            wb.save("BudgetTracker.xlsx")
            print("\nCurrent income(s) are:\n")
            for row_cells in Income.iter_rows(min_row=2, max_col=2):
                for cell in row_cells:
                    print(cell.value)
            income_menu()
        # elif inc_option == "3":
        #     Edit an existing income (index #?)
        elif inc_option == "4":
            mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            income_menu()


def expenses_menu():
    create_expense_sheet()
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
            wb = openpyxl.load_workbook("BudgetTracker.xlsx")
            Expenses = wb["Expenses"]
            if Expenses["A2"].value is None:
                print("*** No expenses have been added yet ***\n")
                expenses_menu()
            else:
                for row_cells in Expenses.iter_rows(min_row=2, max_col=4):
                    for cell in row_cells:
                        print(cell.value)
                expenses_menu()
        elif exp_option == "2":
            wb = openpyxl.load_workbook(filename="BudgetTracker.xlsx")
            Expenses = wb["Expenses"]
            expense_date = datetime.datetime.strptime(input("What is the date of this expense? (MM/DD/YYYY format) "), "%m/%d/%Y")
            print(expense_date.strftime("%m/%d/%Y"))
            expense_amount = float(input("Enter expense amount: "))
            merch_expense = input("What is the merchant of this expense? ")
            expense_cat = input("What is the category for this expense? ")
            Expenses.append([expense_date.strftime("%m/%d/%Y"), expense_amount, merch_expense, expense_cat])
            wb.save("BudgetTracker.xlsx")
            for row_cells in Expenses.iter_rows(min_row=2, max_col=4):
                    for cell in row_cells:
                        print(cell.value)
#             # Enter new expense(s)
#         # elif exp_option == "3":
#             # Editing existing expense (index #?)
        elif exp_option == "4":
            mainmenu()
        else:
            print("Invalid menu option.  Please try again")
            expenses_menu()

mainmenu()