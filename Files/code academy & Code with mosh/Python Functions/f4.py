"""The function calculate_age in script.py creates a variable called age that is the difference between the current year, and a birth year, both of which are inputs of the function. Add a line to return age.


Stuck? Get a hint
2.
Outside of the function, call calculate_age with values 2049 (current_year) and 1993 (birth_year) and save the value to a variable called my_age."""


def calculate_age(current_year, birth_year):
    age = current_year - birth_year
    return age


my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")