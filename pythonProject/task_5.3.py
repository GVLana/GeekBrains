from functools import reduce

with open("text_5.3.txt") as my_f:
    staff = my_f.readlines()
    avg_salary = 0
    print("Employees with the salary less than 20 000 are: ")
    for i in staff:
        x = i.split(" - ")
        if int(x[1]) < 20000:
            print(x[0])
        avg_salary += int(x[1])
        total = avg_salary / len(staff)
    print(f"The average salary is: {round(total)}")
