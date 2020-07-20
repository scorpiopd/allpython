import random
print(random.choice(["pears","banana","apple"]))
print(random.shuffle(["pears","banana","goat","why "]))

import random as hey
print(hey.choice(["heelo","hello",'why']))

# to specifically include something from a module

from random import choice,randint

print(choice(["hello","goat","why bro "]))
print(randint(1,100))