""" Bite 1. Sum n numbers ☆
Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument ...
"""


def sum_numbers(numbers):
    if numbers is None:
        numbers = range(1, 101)
    return sum(numbers)

numbers=int(input("enter number to sum"))
numbers=range(0,numbers)

print(sum_numbers(numbers))