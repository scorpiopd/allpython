#
# Example file for working with functions
#

# define a basic function
#def function1():
 #   print("i am a function")
#function1()
# function that takes arguments
def func2(arg1 , arg2):
    print(arg1,arg2)


# function that returns a value
def cube(x):
    return x*x*x


# function with default value for an argument


#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result




#function1()
#print(function1())
#print(function1)
#func2(10,20)
#print(func2(10,20))
#print(func2)
print(cube(3))
#print (multi_add(10 , 2 ,4 ,1))