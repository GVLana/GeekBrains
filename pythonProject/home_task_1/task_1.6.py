# a - кол-во километров в первый день
# b - ограничение в километрах

# print(f"{day} day: {a} km.")
# while b > a:
#     a = round(a * (1 + increase), 2)
#     day += 1
#     print(f"{day} day: {a} km.")
#     if b <= a:
#         print(f"On {day} day the sportsmen will achieve the goal - not less then {b} km. ")
#         break

def check_input(num):
    if num < 0:
        raise RecursionError("You entered a negative number.")
    else:
        return num


while True:
    increase = 0.1
    day = 1
    try:
        a = int(input("Please, enter a number of kilometers for the first day: "))
        result = check_input(a)
    except RecursionError:
        print("You entered a negative number.")
        continue
    except ValueError:
        print("You entered not a number.")
        continue
    else:
        while True:
            try:
                b = int(input("Please, enter your goal in kilometres: "))
                result = check_input(b)
            except RecursionError:
                print("You entered a negative number.")
                continue
            except ValueError:
                print("You entered not a number.")
                continue
            else:
                while b > a:
                    a = round(a * (1 + increase), 2)
                    result = check_input(a)
                    day += 1
                    if b <= a:
                        print(day)

                break
    break
