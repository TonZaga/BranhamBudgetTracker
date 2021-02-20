"""
Branham Budget Tracker

created by: Anthony Branham
created on: 2/19/2021
last updated on: 2/19/2021

"""

import pyfiglet


def print_banner():
    """Print Banner"""
    ascii_banner = pyfiglet.figlet_format("Branham Budget Tracker")
    print(ascii_banner)
print_banner()


def enter_basic_information():
    """Enter user's information"""
    first_name = input("Please enter your first name: ")
    monthly_income = input("Please enter your total monthly income? ")
    info_confirmation = ("{}, your total monthly income is {}.".format(first_name, monthly_income))
    print(info_confirmation)
enter_basic_information()


def get_categories():
        """Read categories.txt file to set default expense categories"""
        categories = []

        with open("categories.txt", "r") as filename:
            category_list = filename.read()
            print("Current expense categories are: \n{}".format(category_list))
        prompt_new_cat = input("Would you like to add a category? [y / n] ").upper()
        
        """Loop through category until user is satisfied"""
        while prompt_new_cat == "Y":
                added = input("What is the name of the category you want to add? ")
                with open("categories.txt", "a") as filename:
                    new_category_list = filename.write("\n" + added)
                    prompt_new_cat = input("Would you like to add a category? [y / n] ").upper()
        print("Current expense categories are: \n{}".format(category_list))
get_categories()