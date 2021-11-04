
def check_input(my_string):
    if len(my_string) == 1 and my_string[0].isdigit() is True:
        raise TypeError("Invalid entry. Use space. Needed at least two integers.")
    else:
        return my_string


total = 0
while True:
    try:
        user_input = input("Enter integer numbers and separate them with space: ")
        result = check_input(user_input)
    except TypeError:
        print("Invalid entry. Use space. Try again. Needed at least two integers.")
        continue
    if user_input[-1].isdigit() is True:
        sum_num = sum(list(map(int, user_input.replace(" ", ""))))
        total += sum_num
        print(total)
        continue
    else:
        print("Program has been stopped with your request.")
        user_input = user_input[:-1]
        sum_num = sum(list(map(int, user_input.replace(" ", ""))))
        total += sum_num
        print(total)
        break
