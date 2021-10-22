import math

fruit_1 = ['apple', 'orange', 'pear', 'watermelon']
fruit_2 = ['orange', 'melon', 'rasberry', 'apple']

fruits = [fruit for fruit in fruit_1 if fruit in fruit_2]
print(fruits)

numbers = [1, 2, 15, -8, 9, -7, -6, 5, 4, 3]

new_numbers = [number for number in numbers if number % 3 == 0 and number > 0 and number % 4 != 0]
print(new_numbers)

old_list = [1, 2, 15, -8, 9, -7, -6, 5, 4, 3]
def sqrt_list(input_list):
    new_list = [math.sqrt(number) if number > 0 else number for number in input_list]
    return new_list

result = sqrt_list(old_list)
print(result)

def get_number(number):
    if number == 13:
        raise ValueError ('Несчастливое число ')
    else:
        return number **2

number = int(input('Введите число от 1 до 100: '))

try:
    result = get_number(number)
except ValueError:
    print('Несчастлиое число')
else:
    print(result)




