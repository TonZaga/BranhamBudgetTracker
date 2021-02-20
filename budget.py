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


class Categories:
    def get_categories():
        """Read categories.txt file to set expense categories"""
        categories = []

        with open("categories.txt", "r") as txt_file:
            list = txt_file.read().splitlines()
        print("Current expense categories are: {}".format(list))
    
    get_categories()

    # def add_categories():
    #     """Prompt user to add a category or 'quit' to use current list"""
