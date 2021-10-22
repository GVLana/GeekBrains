person = {'name':'Max', 'phones': [123, 345]}

# open file
with open('person.dat', 'wb') as f:
    # запишем объект в айл построчно
    name = person['name']
    # переведем в байты и запишем
    f.write('{}\n'.format(name).encode('utf-8'))
    phones = person['phones']
    for phone in phones:
        f.write('{}\n'.format(phone).encode('utf-8'))

print('объект записан')