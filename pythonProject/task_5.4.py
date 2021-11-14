
translator = {
   "one": "один",
   "two": "два",
   "three": "три",
   "four": "четыре"
}


with open("text_5.4.txt") as my_f:
    num_list = my_f.readlines()
    print(num_list)
    to_print = []
    result = []
    for i in num_list:
        i = i.split(" ", 1)
        for k, v in translator.items():
            if i[0].lower() in k.lower():
                i[0] = v.capitalize()
                result.append(i[0] + ' ' + i[1])
    print(result)

with open("file_5.4.txt", "x+") as next_f:
    next_f.writelines(result)