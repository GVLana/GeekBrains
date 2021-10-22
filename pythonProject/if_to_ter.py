# слова -> СлОвО

word = 'слово'

result = []

for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i % 2 !=0 else letter.upper()
    result.append(letter)

result = ''.join(result)
print(result)

number = int(input('Введите число '))

try:
    result = 100/number
except ZeroDivisionError as e:
    print('Информация об исключении', e)
else:
    print('Все хорошо, шшибок не обнаруженно')
finally:
    print('Операция завершена')
