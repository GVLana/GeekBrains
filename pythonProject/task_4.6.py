import itertools


for el in itertools.count(3):
    if el % 3 == 0:
        print(el)
    if el > 25:
        break


c = 0
for el in itertools.cycle("Hello"):
    print(el)
    if c > 10:
        break
    c += 1
