
my_list = [7, 5, 3, 3, 2]


def check_input(num):
    if num <= 0:
        raise ValueError("Your rating is not a natural number.")
    else:
        return num


while True:
    try:
        user_number = int(input("Please, enter your rating: "))
        result = check_input(user_number)
    except ValueError:
        print("Your rating is not a natural number. Try again. ")
        continue
    except TypeError:
        print("You enter not a number. ")
        continue
    else:
        for el in my_list:
            if my_list.count(el) > 1:



    break
