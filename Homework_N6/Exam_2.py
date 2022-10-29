
# 2. Напишите программу, которая генирирует случайное число
# от -1.000.000.000 до +1.000.000.000 и выводит на экран сколько раз
# в нем встречается та или иная цифра(цифра – это от 0 до 9),
# из которого оно состоит.

# Например если генируруется число 111333, то на экран должно вывести
# 'Число "111333" состоит из следущих цифр: 1, 3'
# 'Цифра "1" встречается 1 раз(-а)'
# 'Цифра "3" встречается 3 раз(-а)'
# Сколько будет уникальных цифр, столько должно быть и выводов на экран.

import random
num2 = str(random.randint(-1000000000, +1000000000))
print(num2)

#Вариант1 (не работает)
for i in range(0, 10):
    str(i)
    print('''Цифра "''', i, '''" встречается ''', num2.count('i'), ' раз(-а)', sep='')
print('\n')

#Вариант 2
list2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in list2:
    print('''Цифра "''', i, '''" встречается ''', str(num2).count(i), ' раз(-а)', sep='')
