# 5. Пользователь вводит два числа c клавиатуры,
# необходимо вывести на экран все отрицательные
# числа, лежащие между ними.
# Например пользователь ввел -5 и 3, на экране вывелось -4, -3, -2, -1.
# (решить через while)
#
num1 = int(input('Введите первое число: '))
num2 = int(input('Введите второе число: '))
if 0 <= num1 <= num2 or 0 <= num2 <= num1:
    print('Отрицательных чисел нет')
elif abs(num1 - num2) <= 1:
    print('Чисел в заданном промежутке нет')
elif num2 < num1:
    num2 += 1
    while num2 < num1 and num2 < 0:
        print(num2, ', ', sep='', end='')
        num2 += 1
elif num1 < num2:
    num1 += 1
    while num1 < num2 and num1 < 0:
        print(num1, ', ', sep='', end='')
        num1 += 1
