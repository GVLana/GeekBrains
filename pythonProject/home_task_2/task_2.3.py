def check_input(num):
    if num <= 0 or num > 12:
        raise TypeError("You entered a number out of range form 1 to 12. Try again. ")
    else:
        return num


season_list = ["winter", "spring", "summer", "autumn"]


while True:
    try:
        month = int(input("Please, enter a number form 1 to 12: "))
        result = check_input(month)
    except ValueError:
        print("You entered not a number. Try again. ")
        continue
    except TypeError:
        print("You entered a number out of range form 1 to 12. Try again. ")
        continue
    else:
        if month == 12 or month == 1 or month == 2:
            print(f"It's {season_list[0]}.")
        elif month == 3 or month == 4 or month == 5:
            print(f"It's {season_list[1]}.")
        elif month == 6 or month == 7 or month == 8:
            print(f"It's {season_list[2]}.")
        elif month == 9 or month == 10 or month == 11:
            print(f"It's {season_list[3]}.")
    break


season_dict = {
    1: "winter",
    2: "winter",
    3: "spring",
    4: "Spring",
    5: "spring",
    6: "summer",
    7: "summer",
    8: "summer",
    9: "autumn",
    10: "autumn",
    11: "autumn",
    12: "winter"
}

while True:
    try:
        month = int(input("Please, enter a number form 1 to 12: "))
        result = check_input(month)
    except ValueError:
        print("You entered not a number. Try again. ")
        continue
    except TypeError:
        print("You entered a number out of range form 1 to 12. Try again. ")
        continue
    else:
        for key in season_dict:
            if key == month:
                print(f"It's {season_dict[key]}.")
    break
