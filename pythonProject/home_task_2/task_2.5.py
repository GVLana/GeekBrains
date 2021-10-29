
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
        count_r = rating.count(user_rating)
        for el in rating:
            if count_r > 0:
                ind = rating.index(user_rating)
                rating.insert(ind + count_r, user_rating)
                break
            else:
                if el < user_rating:
                    ind = rating.index(el)
                    rating.insert(ind, user_rating)
                    break
                elif rating[-1] > user_rating:
                    rating.append(user_rating)
        print(rating)
    break
