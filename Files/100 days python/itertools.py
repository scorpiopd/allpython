#1

"""import itertools
import sys
import time

symbols=itertools.cycle("-\|/")
while True:
    sys.stdout.write('\r'+next(symbols))
    sys.stdout.flush()
    time.sleep(0.01)
    """


#2
"""from itertools import product
for letter in product("julian",repeat=2):
    print(letter)"""

from itertools import permutations,combinations
friends="mike bob julian".split()
print(list(combinations(friends,2)))
print(list(permutations(friends,2)))


