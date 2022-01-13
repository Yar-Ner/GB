from itertools import count
from math import factorial


def factgen():
    for i in count(1):
        yield factorial(i)
gen = factgen()
n = 0
for elem in gen:
    if n < 6:
        print(elem)
        n += 1
    else:
        break
