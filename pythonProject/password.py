password = input('Введите пароль: ')

print('Войти' if password == 'secret' else 'Вход запрещен')

numbers = [1, 2, 3, 5, -2, -6]

result = []

for number in numbers:
    if number > 0:
        result.append(number)

print(result)

result = filter(lambda number: number > 0, numbers)
print(list(result))

result = [number for number in numbers if number > 0]
print(result)

pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

result = {}
for pair in pairs:
    key = pair[0]
    val = pair[1]
    result[key] = val

print(result)


result = {pair[0]:pair[1] for pair in pairs}
print(result)
