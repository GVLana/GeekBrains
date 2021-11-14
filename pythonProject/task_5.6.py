from itertools import groupby

with open("text_5.6.txt", "r") as my_func:
    all_classes = {}
    class_list = my_func.readlines()
    my_list = [(i, list(j)) for i, j in groupby(class_list[0], key=lambda x: x[0].isdigit())]
    result = [[''.join(j) for i, j in groupby(item, key=lambda x: x[0].isdigit())] for item in class_list]
    print(result)
    for el in result:
        r_list = []
        for i in el:
            if i.isdigit():
                r_list.append(i)
                elem = ':'.join(el[0].split(':')[:-1])
                all_classes[elem] = sum(map(int, r_list))

    print(all_classes)
