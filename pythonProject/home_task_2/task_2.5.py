
rating = [7, 5, 3, 3, 2]


def check_input(num):
    if num <= 0:
        raise ValueError("Your rating is not a natural number.")
    else:
        return num


while True:
    try:
        user_rating = int(input("Please, enter your rating: "))
        result = check_input(user_rating)
    except ValueError:
        print("Your rating is not a natural number. Try again. ")
        continue
    except TypeError:
        print("You enter not a number. ")
        continue
    else:
        # c = rating.count(user_rating)
        # for el in rating:
        #     if c > 0:
        #         i = rating.index(user_rating)
        #         rating.insert(i + c, user_rating)
        #         break
        #     else:
        #         if el < user_rating:
        #             i = rating.index(el)
        #             rating.insert(i, user_rating)
        #             break
        #         elif rating[-1] > user_rating:
        #             rating.append(user_rating)
        # print(rating)
        pass
    break
