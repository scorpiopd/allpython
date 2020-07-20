"""We have defined a function create_spreadsheet, which just takes in a title, and prints that it is creating a spreadsheet.

Run the code to see the function work on an input of "Downloads".


Stuck? Get a hint
2.
Add the parameter row_count to the function definition. Set the default value to be 1000.

3.
Change the print statement in the function to print “Creating a spreadsheet called title with row_count rows”, where title and row_count are replaced with their respective values.

Remember, to concatenate a number to a string object, you’ll first have to cast row_count to a string using str(). Otherwise, you’ll get a TypeError.


Stuck? Get a hint
4.
Call create_spreadsheet() with title set to "Applications" and row_count set to 10."""

def create_spreadsheet(title, row_count = 10):
  print("Creating a spreadsheet called " + title + " with " + str(row_count) + " rows")

create_spreadsheet("Applications")