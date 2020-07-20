"""Write a function called get_boundaries() that takes in two parameters, a number called target and a number called margin.

It should create two variables:

low_limit: target minus the margin
high_limit: margin added to target
2.
Return both low_limit and high_limit from the function, in that order.

3.
Call the function on the target 100 with a margin of 20. Save the returned values to variables called low and high."""


def get_boundaries(target, margin):
    low_limit = target - margin
    high_limit = target + margin
    return low_limit, high_limit


low, high = get_boundaries(100, 20)

# we added this print statement just to sanity-check our solution:
print("Low limit: " + str(low) + ", high limit: " + str(high))
