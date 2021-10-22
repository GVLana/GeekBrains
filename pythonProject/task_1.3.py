
# вариант 1:
# nn = [n, n]
# nn = ''.join(nn)
#
# nnn = [n, n, n]
# nnn = ''.join(nnn)
#
# result = int(n) + int(nn) + int(nnn)
# print(result)

# вариант 2:
def check_input(num):
    if num.isdigit() is False:
        raise ValueError("You entered not a number.")
    else:
        return num


while True:
    try:
        n = input("Please, enter a number: ")
        result = check_input(n)
    except ValueError:
        print("You entered not a number.")
        continue
    else:
        n_2 = n * 2
        n_3 = n * 3

        total = int(n) + int(n_2) + int(n_3)
        print(total)
    break
