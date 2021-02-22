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


def enter_basic_information():
    """Enter user's information"""
    first_name = input("Please enter your first name: ")
    monthly_income = input("Please enter your total monthly income? ")
    info_confirmation = ("{}, your total monthly income is {}.".format(first_name, monthly_income))
    print(info_confirmation)
enter_basic_information()


def cat_list():

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
cat_list()