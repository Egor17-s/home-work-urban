immutable_var = 1, 2, 3, 4, " КОРТЕЖ", True
print(immutable_var)
#immutable_var[0] = 11
#print(immutable_var)  ответ на 2 вопрос TypeError: 'tuple' object does not support item assignment
mutable_list = ["Фрукты", "Овощи", "Проудкты", "Ферма",]
print(mutable_list)
mutable_list[0] = "Чипсы"
mutable_list[1] = "Молоко"
mutable_list[2] = "Жидкость"
mutable_list[3] = "Грядка"
print(mutable_list)

