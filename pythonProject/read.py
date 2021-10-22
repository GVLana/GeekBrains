f = open('first.txt', 'r')

# print(f.read())

# for line in f:
#  print(line)

for line in f:
    print(line.replace('\n', ''))

f.close()

with open('first.txt', 'r') as f:
    for line in f:
     print(line.replace('\n', ''))

print('end')

