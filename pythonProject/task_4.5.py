from functools import reduce
import random


my_list = [el for el in random.sample(range(100, 1001), 5) if el % 2 == 0]
result = reduce((lambda x, y: x * y), my_list)

print(f"Original list: {my_list}")
print(f"Multiplication of all elements: {result}")
