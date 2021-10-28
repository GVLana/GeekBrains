
def check_input(input_list):
    if ' ' not in input_list:
        raise TypeError("Invalid entry. Use space. Try again. ")
    else:
        return input_list.strip()


while True:
    try:
        my_list = input("Create a list by putting elements in the line, separate them with space: ")
        result = check_input(my_list)
    except TypeError:
        print("Invalid entry. Use space. Try again. ")
        continue
    else:
        new_list = my_list.split()
        for i in range(0, len(new_list)-1, 2):
            new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        print(new_list)
    break
