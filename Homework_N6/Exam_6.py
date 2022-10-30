# 6. Напишите программу, которая сгенирирует 2 кортежа, состоящих из
# нечетного рандомного кол-ва элементов от 3 до 99 каждый,
# все числа также генирируются рандомно от 0 до 1000 и не повторяются
# дважды в одном и том же кортеже.
# Переменные для кортежей назвать "tuple1" и "tuple2".
#
# Выведите на экран сообщение с указанием того, в каком кортеже
# сумма его элементов оказалась больше, чем у другого.
#
# Вывести на экран индексы минимальных и максимальных элементов
# этих кортежей.
#
# Вывести на экран среднее из чисел кождого кортежа, а также его индекс.

# #Программа для генерации кортежей
import random
tuple1 = ()
tuple2 = ()
num1 = random.randint(3, 99) #рандомное количество элементов для tuple1
while num1 % 2 == 0:
    num1 = random.randint(3, 99) #рандомное количество элементов для tuple1
    # print(num1)
print('Количество элементов кортежа tuple1: ', num1)
num2 = random.randint(3, 99) #рандомное количество элементов для tuple2
while num2 % 2 == 0:
    num2 = random.randint(3, 99) #рандомное количество элементов для tuple1
    # print(num2)
print('Количество элементов кортежа tuple2: ', num2)

# Генерация 1 кортежа
while len(tuple1) < num1:
    a = random.randint(0, 1000)
    if a not in tuple1:
        tuple1 += (a,)
    else:
        continue
print('Кортеж tuple1', tuple1)
# Генерация 2 кортежа
while len(tuple2) < num2:
    a = random.randint(0, 1000)
    if a not in tuple2:
        tuple2 += (a,)
    else:
        continue
print('Кортеж tuple2', tuple2)

# #Сравнение сумм элементов кортежей
print('Сумма элементов tuple1: ', sum(tuple1), '\nСумма элементов tuple2: ', sum(tuple2))
if sum(tuple1) > sum(tuple2):
    print('Сумма элементов кортежа tuple1 больше суммы элементов кортежа tuple2')
elif sum(tuple1) < sum(tuple2):
    print('Сумма элементов кортежа tuple2 больше суммы элементов кортежа tuple1')
else:
    print('Суммы элементов кортежей tuple1 и tuple2 равны')

# # Индексы минимальных и максимальных элементов кортежей
print('Индекс максимального элемента кортежа tuple1: ', tuple1.index(max(tuple1)))
print('Индекс минимального элемента кортежа tuple1: ', tuple1.index(min(tuple1)))
print('Индекс максимального элемента кортежа tuple2: ', tuple2.index(max(tuple2)))
print('Индекс минимального элемента кортежа tuple2: ', tuple2.index(min(tuple2)))

# Cреднее из чисел каждого кортежа, а также его индекс
# Среднее число для кортежа tuple1:
list1 = list(tuple1)
print(list1)
# list11 = list1.copy()
# list11 = list1
# print(list11)
while len(list1) > 1:
    list1.remove(max(list1))
    list1.remove(min(list1))
print('Среднее число кортежа tuple1: ', list1[0])
print('Индекс числа: ', tuple1.index(list1[0]))

# # Среднее число для кортежа tuple2:
# list2 = list(tuple2)
# print(list2)
# list22 = list2.copy()
# # list11 = list1
# print(list11)
# while len(list11) > 1:
#     list11.remove(max(list11))
#     list11.remove(min(list11))
# print('Среднее число кортежа tuple1: ', str(list11))
# print('Индекс числа: ', list1.index(list11[0]))



