
def check_input(input_list):
    if ' ' not in input_list:
        raise TypeError("Invalid entry. Use space. Try again. ")
    else:
        return input_list


while True:
    try:
        my_string = input("Please, enter your words and separate them with space: ")
        result = check_input(my_string)
    except TypeError:
        print("Invalid entry. Use space. Try again. ")
        continue
    else:
        for ind, word in enumerate(my_string.split(), 1):
            print(f"{ind} - {word[:10]}")
    break
