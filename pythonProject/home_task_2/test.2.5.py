
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
        for i, el in enumerate(rating):
            if user_rating >= el:
                rating.insert(i, user_rating)
                break
            elif len(rating) == i + 1:
                rating.append(user_rating)
                break
        print(rating)
    break