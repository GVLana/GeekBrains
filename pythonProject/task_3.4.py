
def check_input_1(num):
    if num <= 0:
        raise ValueError("First number should be positive and not equal zero.")
    else:
        return num


def check_input_2(num):
    if num > 0:
        raise ValueError("Second number should be negative.")
    elif num == 0:
        raise ZeroDivisionError("Second number can not be equal zero.")
    else:
        return num


# def my_func(x, y):
#     return round(x ** y, 2)


def my_func_2(x, y):
    c = 1
    for i in range(-1, y - 1, -1):
        c *= x
        i -= 1
    return round(1 / c, 3)


while True:
    try:
        num_1 = int(input("Enter a positive integer: "))
        result_1 = check_input_1(num_1)
    except ValueError:
        print("First number should be positive and not equal zero. Try again.")
        continue
    while True:
        try:
            num_2 = int(input("Enter a negative integer: "))
            result_2 = check_input_2(num_2)
        except ValueError:
            print("Second number should be negative.")
            continue
        except ZeroDivisionError:
            print("Second number cannot be equal zero. Try again.")
            continue
        else:
            print(my_func_2(num_1, num_2))
            break
    break
