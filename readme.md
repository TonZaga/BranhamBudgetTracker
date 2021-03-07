# Branham Budget Tracker

## Description
```
This is a budget tracker built in Python to help users keep track of their monthly income/expense.
App will allow the user to export to CSV as well as create charts/graphs to help visualize their
spending behavior and patterns.

```


## Features list
```
The features that were used for this project are:

1. Read data from an external file, such as text, JSON, CSV, etc and use that data in your application
        - Users are able to enter/edit their inputs for income(s), expenses within the app.  The inputs are then written to a .xlsx file to calculate budget information.  The data can be printed to console through the navigation menu options or accessed through excel by opening "/BudgetTracker.xlsx" once the file has been created.

2. Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program.
        - Added a text navigation menu that users can repeatedly add incomes, expenses, generate breakdowns, or have the option to quit the program altogether

3. Calculate and display data based on an external factor
        - Upon entering a name at startup, we get today's date and notify the user how many days are left in the month.

```