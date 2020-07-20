#
# Example file for variables
#

# Declare a variable and initialize it
a = 8
print(a)

# # re-declaring the variable works

a = "abc"
print(a)
# # ERROR: variables of different types cannot be combined

print("this is a string " + str(123))


# Global vs. local variables in functions

def some():

    a="hello"
    print(a)


some()
print(a)
del f
print(f)
