import pickle

person = {'name':'Max', 'phones': [123, 345]}

# открываем файл
with open('person.dat', 'wb') as f:
    # сразу пишем объект целиком с помощью pickle
    pickle.dump(person, f)

print('Объект записан')