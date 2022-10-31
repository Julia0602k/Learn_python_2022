# # 1. Создайте кортеж с одним элементом
# tuple1 = (1,)
# print('Задача 1\n', tuple1, type(tuple1))

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
list.sort(list22)
print('Вариант 2:', list22)
print('Индекс максимального элемента: ', list2.index(list22[-1]))
print('Индекс минимального элемента: ', list2.index(list22[0]))

#Способ 3
# for i in list2:
#     if i < list2[list2.index(i) + 1]:
#
#


# # 3. Создайте кортеж с цифрами от 0 до 9 и посчитайте сумму.
# # Решить 2-мя способами(через цикл и через встроенную функцию сложения)
# tuple3 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# sum1 = 0
# for i in tuple3:
#     sum1 += i
# print('\nЗадача 3\n Сумма элементов кортежа N3: ', sum1, ',', sum(tuple3))

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






# print("\nЗадача 4 \nКортеж N4 (2 способ):")
# # for i in set(long_word):
# #     print(i, ' - ', long_word.count(i))

# print("\nЗадача 4 \nКортеж N4 (1 способ): \nбуква 'т':", long_word.count('т'))
# print("буква 'а':", long_word.count('а'))
# print("буква 'и':", long_word.count('и'))




# t = 0
# a = 0
# u = 0
#     if i == 'т':
#         t += 1
#     elif i == 'а':
#         a += 1
#     elif i == 'и':
#         u += 1
# print("Кортеж N4 (2 способ): \nбуква 'т':", t, "\nбуква 'а':", a, "\nбуква 'и':", u)
