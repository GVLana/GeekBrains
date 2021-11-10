import random

# my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

my_list = random.sample(range(0, 1000), 10)
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i - 1] < my_list[i]]

print(f"Original list is: {my_list}.")
print(f" New list is : {new_list}.")
