
# 3. Посчитать, сколько раз встречается определенная цифра
# в списке чисел. (Цифра – это от 0 до 9)
# Количество введенных чисел в список и искомая цифра задаются
# с клавиатуры. Числа для списка выбираются рандомно.

num1 = int(input('Введите количество чисел списка: '))
num2 = input('Введите искомую цифру (от 0 до 9): ')
if (num2 >= 0 or num2 <= 9) and num2.isdigit():
    import random
    list1 = []
    for i in range(num1):
        a = random.randint()
else:
    print('Ошибка! Введите искомую цифру правильно (от 0 до 9)!')
