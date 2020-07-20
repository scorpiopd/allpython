import random
from collections import deque
import timeit

lst = list(range(1000000))
deq = deque(range(1000000))


def insert_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)



print(timeit.timeit())
