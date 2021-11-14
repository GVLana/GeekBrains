
with open("text_5.2.txt") as my_f:
    my_line = my_f.readlines()
    num_line = len(my_line)
    print(f"Number of lines is: {num_line}")
    word = 0
    for el in my_line:
        word += el.count(" ") + 1
    print(f"Number of words is: {word}")
