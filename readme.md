# Branham Budget Tracker

## Description
```
**Run budget.py to start the application - app.py is a GUI work in-progress**

This is a budget tracker built in Python to help users keep track of their monthly income/expense.
App will create an XLSX file in the directory that the program is ran from that will display tables and a chart to help user visualize their
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

4. Visualize data in a graph, chart, or other visual representation of data
        - At any point (preferably after all data has been entered), a user can "generate breakdown" from the main menu.
        Openpyxl will create a pie chart on the Calc worksheet from data calculations made from other formulas within the workbook.

```
