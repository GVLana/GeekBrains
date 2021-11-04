
def my_division(x, y):
    return round(x / y, 1)


def check_input(num):
    if num == 0:
        raise ZeroDivisionError("Division by 0 is not possible. Second number cannot be equal zero.")
    else:
        return num


num_1 = int(input("Enter first number: "))


while True:
    try:
        num_2 = int(input("Enter second number: "))
        result = check_input(num_2)
    except ZeroDivisionError:
        print("Division by 0 is not possible. Second number cannot be equal zero. Try again")
        continue
    else:
        print(my_division(num_1, num_2))
    break


