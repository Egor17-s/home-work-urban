my_dict = {'Egor': 1997, 'Nikita': 1998, 'Artem': 2000}
print(my_dict)
print(my_dict['Nikita'])
print(my_dict.get('Anton', 'Таких тут нет'))
my_dict.update({'Kris': 1994,
                'Roma': 1996})
print(my_dict)
my_dict.pop('Roma')
print(my_dict)

my_set = {1, 2, 3, 4, 1, 2, 4, 'Egor', 'Kto-to', True, 'Kto-to'}
print(my_set)
my_set.add('Tanya')
my_set.add(5)
my_set.discard(1)
print(my_set)