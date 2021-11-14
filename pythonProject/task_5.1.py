
with open("text_5-1.txt", "x") as my_f:
    while True:
        user_input = input("Enter your sentence: ")
        my_f.writelines(user_input + "\n")
        if not user_input:
            break
