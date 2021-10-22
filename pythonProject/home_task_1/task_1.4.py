
def check_input(num):
    if num < 0:
        raise RecursionError("You put a negative number.")
    else:
        return num


while True:
    list_numbers = []
    try:
        user_number = int(input("Please, enter a number: "))
        result = check_input(user_number)
    except RecursionError:
        print("You put a negative number.")
        continue
    except ValueError:
        print("You entered not a number.")
        continue
    else:
        while user_number >= 1:
            number = user_number % 10
            list_numbers.append(number)
            user_number = user_number // 10
            list_numbers = list_numbers[::-1]

            max_number = max(list_numbers)
            print(max_number)
            break
    break
