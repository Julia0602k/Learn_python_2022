# 3. Даны три различных целых числа. Напишите программу,
# которая выводит на экран среднее по величине число.
#
# Средним называется число, которое будет вторым,
# если три числа отсортировать в порядке возрастания.

num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
num3 = int(input('Введите третье число: '))

if num2 < num1 < num3 or num3 < num1 < num2:
    print('Среднее число:', num1)
elif num1 < num2 < num3 or num3 < num2 < num1:
    print('Среднее число:', num2)
else:
    print('Среднее число:', num3)


