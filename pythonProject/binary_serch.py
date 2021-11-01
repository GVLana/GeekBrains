
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
        low = 0
        high = len(rating) - 1
        mid = (low + high) // 2
        for el in rating:
            while low <= high:
                mid = (low + high) // 2
                if user_rating == rating[mid]:
                    rating.insert(mid, user_rating)
                    break
                else:
                    if user_rating < rating[mid]:
                        low = mid + 1
                    else:
                        high = mid - 1

            break
        print(rating)
    break
