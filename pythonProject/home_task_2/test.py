
user_rating = int(input("Enter a number: "))

rating = [7, 5, 3, 3, 2]

low = rating[0]
high = rating[-1]

mid = len(rating) // 2

c = rating.count(user_rating)

if rating[0] < user_rating:
    rating.insert(0, user_rating)
elif rating[-1] > user_rating:
    rating.append(user_rating)
else:
    for el in rating:
        while low <= high:
            mid = (low + high) // 2
            if c > 0:
                i = rating.index(user_rating)
                rating.insert(i + c, user_rating)
                break
            else:
                if el < user_rating:
                    i = rating.index(el)
                    rating.insert(i, user_rating)

            if user_rating > mid:
                low = mid + 1
            else:
                high = mid - 1
        print(rating)

