
from sys import argv

script_name, working_hours, rate, bonus = argv


print("Script name: ", script_name)
print("Working hours: ", working_hours)
print("Salary rate per hour: ", rate)
print("Bonus: ", bonus)
print("Total salary: ", ((int(working_hours) * int(rate)) + int(bonus)))
