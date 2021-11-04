
user_input = input("Enter a sentence: ")

# user_input = input("Enter a word: ")
# def cap_word(word):
#     return word.capitalize()
# print(cap_word(word))


def up_word(word):
    return word[0].upper() + word[1:]


# print(up_word(user_input))


def up_first_letter(my_string):
    return ' '.join(up_word(word) for word in my_string.split())


print(up_first_letter(user_input))
