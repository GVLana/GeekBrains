
def check_input(str_list):
    if sum(map(int, num_list)) is False:
        raise ValueError("You put not a number or use wrong separator.")


try:
    with open("text_5.5.txt", "x+") as my_func:
        user_input = input("Enter several numbers. Use spaces. ")
        my_func.write(user_input)
        num_list = user_input.split()
        # print(num_list)
        result = sum(map(int, num_list))
        print(result)
except ValueError:
    print("You put not a number or use wrong separator.")
