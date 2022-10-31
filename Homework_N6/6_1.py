# # 1. Создайте кортеж с одним элементом
tuple1 = (1,)
print('Задача 1\n', tuple1, type(tuple1))

# 2. Создайте кортеж из 10 случайно сгенирированных чисел
# от -100 до 100.
# Найдите индексы максимального и минимального элемента.
# Решить 3-мя способами.
# #Способ 1
import random
list2 = []
for i in range(10):
    list2.append(random.randint(-100, 100))
tuple2 = tuple(list2)
print('111', tuple2)
print('\n Задача 2 \n', tuple2)
print('Индекс максимального элемента кортежа: ', tuple2.index(max(tuple2)))
print('Индекс минимального элемента кортежа: ', tuple2.index(min(tuple2)))

#Способ 2
list22 = list.copy(list2)
list222 = list.copy(list2)
list.sort(list22)
print('Индекс максимального элемента: ', list2.index(list22[-1]))
print('Индекс минимального элемента: ', list2.index(list22[0]))

#Способ 3
max1 = list222[0]
for i in list222:
    if max1 < i:
        max1 = i
print('Индекс максимального элемента: ', list222.index(max1))
min1 = list222[0]
for i in list222:
    if min1 > i:
        min1 = i
print('Индекс минимального элемента: ', list222.index(min1))

#     if list2.index(i) == 9 and i > a:
#         a = i
#     elif i < list2[list2.index(i) + 1]:
#         a = list2[list2.index(i) + 1]
#     else:
#         a = i
# # for i in list2:
#     if i > list2[list2.index(i) + 1]:
# #         b = list2[list2.index(i) + 1]
# #     else:
# #         b = i

# print('Индекс минимального элемента: ', b)


# # 3. Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму.
# # Решить 2-мя способами(через цикл и через встроенную функцию сложения)
tuple3 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
sum1 = 0
for i in tuple3:
    sum1 += i
print('\nЗадача 3\n Сумма элементов кортежа N3: ', sum1, ',', sum(tuple3))

# 4. Выведите статистику частности букв в кортеже
# long_word = ( 'т', 'т', 'а', 'и', 'и', 'а', 'и',
#  'и', 'и', 'т', 'т', 'а', 'и', 'и',
#  'и', 'и', 'и', 'т', 'и')
# Например: 'Буква "и" встречается 11 раз' (и так с каждой)
# Решить 2-мя способами через цикл и через метод.

print('\nЗадача N4')
long_word = ('т', 'т', 'а', 'и', 'и', 'а', 'и', 'и', 'и', 'т', 'т', 'а', 'и', 'и', 'и', 'и', 'и', 'т', 'и')


my_list = list(long_word)
list4 = []
for i in my_list:
    if i not in list4:
        print('Количество', i, '=', my_list.count(i))
        list4.append(i)


        # my_list.remove(str(i))
        # print(my_list)
