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

#Программа для генерации кортежей
import random
tuple1 = ()
tuple2 = ()
num1 = random.randint(3, 99) #рандомное количество элементов для tuple1
num2 = random.randint(3, 99) #рандомное количество элементов для tuple2
for i in range(num1):
    tuple1 += (random.randint(0, 1000),)
print(tuple1)
for i in range(num2):
    tuple2 += (random.randint(0, 1000),)
print(tuple2)
print(' Количество элементов кортежа tuple1: ', num1, '\n', 'Количество элементов кортежа tuple2: ', num2)

#Сравнение сумм элементов кортежей
print('Сумма элементов tuple1: ', sum(tuple1), '\nСумма элементов tuple1: ', sum(tuple2))
if sum(tuple1) > sum(tuple2):
    print('Сумма элементов кортежа tuple1 больше суммы элементов кортежа tuple2')
elif sum(tuple1) < sum(tuple2):
    print('Сумма элементов кортежа tuple2 больше суммы элементов кортежа tuple1')
else:
    print('Суммы элементов кортежей tuple1 и tuple2 равны')

# Индексы минимальных и максимальных элементов кортежей
print('Индекс максимального элемента кортежа tuple1: ', tuple1.index(max(tuple1)))
print('Индекс минимального элемента кортежа tuple1: ', tuple1.index(min(tuple1)))
print('Индекс максимального элемента кортежа tuple2: ', tuple2.index(max(tuple2)))
print('Индекс минимального элемента кортежа tuple2: ', tuple2.index(min(tuple2)))

# Cреднее из чисел каждого кортежа, а также его индекс
# print('Среднее число кортежа tuple1: ', end='')
# print(tuple1[num1 // 2 + 1]) if num1 % 2 else print(tuple1[num1 // 2])
# print('Индекс числа: ', end='')
# print(tuple1.index(tuple1[num1 // 2 + 1])) if num1 % 2 else print(tuple1.index(tuple1[num1 // 2]))



# print('Среднее число кортежа tuple1: ', end='')
# print(tuple1[num1 // 2 + 1]) if num1 % 2 else print(tuple1[num1 // 2])
# print('Индекс числа: ', end='')
# print(tuple1.index(tuple1[num1 // 2 + 1])) if num1 % 2 else print(tuple1.index(tuple1[num1 // 2]))
#
# print('Среднее число кортежа tuple2: ', end='')
# print(tuple2[num2 // 2 + 1]) if num1 % 2 else print(tuple2[num2 // 2])
# print('Индекс числа: ', end='')
# print(tuple2.index(tuple2[num2 // 2 + 1])) if num1 % 2 else print(tuple2.index(tuple2[num2 // 2]))
