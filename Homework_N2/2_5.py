# 5. Напишите программу, которая выводит наименьшее из четырёх чисел.
# Использовать только if, elif, else, and, not, or.
# Если получилось, то можно попробовать через функцию min()
# Я про нее еще не рассказывал, но если знаешь ее, то реши.

num1 = int(input('Введите число N1: '))
num2 = int(input('Введите число N2: '))
num3 = int(input('Введите число N3: '))
num4 = int(input('Введите число N4: '))

if num1 < num2 and num1 < num3 and num1 < num4:
    print('Наименьшее число N1: ', num1)
elif num2 < num3 and num2 < num4:
    print('Наименьшее число N2: ', num2)
elif num3 < num4:
    print('Наименьшее число N3: ', num3)
else:
    print('Наименьшее число N4: ', num4)

# Второй вариант

print('Наименьшее число: ', min(num1, num2, num3, num4))
