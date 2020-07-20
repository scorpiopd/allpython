"""Outside of the function calculate_age(), try to print current_year. Does it work?

2.
What about age? Outside of calculate_age(), try to print age. Does it work?

3.
No! Even though we return age at the end of the function, the variable age still only exists within the context of the function.

Remove both print statements.

4.
Let’s try something different. Remove the parameter current_year so that it is no longer a parameter of calculate_age().

5.
It’s the year 2048.

Define current_year as a variable BEFORE defining the function and give it the value 2048. Now, every time calculate_age() is called, it should only take birth_year.

6.
Try to print current_year one last time. Does it work finally?

7.
Hooray! Now we have current_year globally defined. Great work!

Let’s make sure our function still works: print the value of calculate_age() with 1970 as the argument.

"""


current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age

print(current_year)

print(calculate_age(1970))