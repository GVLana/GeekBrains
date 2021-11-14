import json
from itertools import groupby


with open("text_5.7.txt", "r") as my_func:
    firm_list = my_func.readlines()
    my_list = [(i, list(j)) for i, j in groupby(firm_list[0], key=lambda x: x[0].isdigit())]
    result = [[''.join(j) for i, j in groupby(item, key=lambda x: x[0].isdigit())] for item in firm_list]
    my_dict = {}
    avg_profit = {}
    total_info = []
    for el in result:
        r_list = []
        num_list = []
        for i in el:
            if i.isdigit():
                r_list.append(i)
        elem = ' '.join(el[0].split(' ')[:-1])
        my_dict[elem] = int(r_list[0]) - int(r_list[1])
        count_profit = 0
        for v in my_dict.values():
            if v >= 0:
                count_profit += 1
        avg_profit["average_profit"] = round(sum(v for v in my_dict.values() if v >= 0) / count_profit)
    total_info.append(my_dict)
    total_info.append(avg_profit)
    print(total_info)

with open("file_5.7.json","w") as write_f:
    json.dump(total_info, write_f)