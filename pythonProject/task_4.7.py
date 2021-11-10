import random
from functools import reduce

n = random.randint(1, 15)
print(n)

def generator():
    for el in range(1, n + 1):
        yield el


g = generator()
print(g)

for el in g:
    print(reduce((lambda x, y: x * y), g))
