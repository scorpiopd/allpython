"""Python Code Challenges: Control Flow
Python Code Challenges involving Control Flow

This article will help you review Python functions by providing some code challenges about control flow.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong, and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should see an option to get our solution code. However, truly investigate that solution — experiment and play with the solution code until you have a good grasp of how it is working. Good luck!

Function Syntax
As a refresher, function syntax looks like this:

def some_function(some_input1, some_input2):
  # … do something with the inputs …
  return output
For example, a function that returns the sum of the first and last elements of a given list might look like this:

def first_plus_last(lst):
  return lst[0] + lst[-1]
And this would produce output like:

>>> first_plus_last([1, 2, 3, 4])
5
>>> first_plus_last([8, 2, 5, -8])
0
>>> first_plus_last([-10, 2, 3, -4])
-14




Challenges
We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your control flow expertise.

1. Large Power
Create a function named large_power() that takes two parameters named base and exponent.

If base raised to the exponent is greater than 5000, return True, otherwise return False

1
# Write your large_power function here:
2
​
3
# Uncomment these function calls to test your large_power function:
4
#print(large_power(2, 13))
5
# should print True
6
#print(large_power(2, 12))
7
# should print False



 # Write your large_power function here:
def large_power(base, exponent):
  if base ** exponent > 5000:
    return True
  else:
    return False

# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False










2. Over Budget
Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent.

The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

1
# Write your over_budget function here:
2
​
3
# Uncomment these function calls to test your over_budget function:
4
#print(over_budget(100, 20, 30, 10, 40))
5
# should print False
6
#print(over_budget(80, 20, 30, 10, 30))
7
# should print True



# Write your over_budget function here:
def over_budget(budget, food_bill, electricity_bill, internet_bill, rent):
  if (budget < food_bill + electricity_bill + internet_bill + rent):
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True










3. Twice As Large
Create a function named twice_as_large() that has two parameters named num1 and num2.

Return True if num1 is more than double num2. Return False otherwise.

1
# Write your twice_as_large function here:
2
​
3
# Uncomment these function calls to test your twice_as_large function:
4
#print(twice_as_large(10, 5))
5
# should print False
6
#print(twice_as_large(11, 5))
7
# should print True



# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > 2 * num2:
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True












4. Divisible By Ten
Create a function called divisible_by_ten() that has one parameter named num.

The function should return True if num is divisible by 10, and False otherwise. Consider using modulo (%) to check for divisibility.

1
# Write your divisible_by_ten function here:
2
​
3
# Uncomment these function calls to test your divisible_by_ten function:
4
#print(divisible_by_ten(20))
5
# should print True
6
#print(divisible_by_ten(25))
7
# should print False






# Write your divisible_by_ten function here:
def divisible_by_ten(num):
  if (num % 10 == 0):
    return True
  else:
    return False
# Uncomment these function calls to test your divisible_by_ten function:
print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False









5. Not Equal
Create a function named not_sum_to_ten() that has two parameters named num1 and num2.

Return True if num1 and num2 do not sum to 10. Return False otherwise.

1
# Write your not_sum_to_ten function here:
2

3
# Uncomment these function calls to test your not_sum_to_ten function:
4
#print(not_sum_to_ten(9, -1))
5
# should print True
6
#print(not_sum_to_ten(9, 1))
7
# should print False
8
#print(not_sum_to_ten(5,5))
9
# should print False

"""


# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
    if (num1 + num2 != 10):
        return True
    else:
        return False


# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5, 5))
# should print False