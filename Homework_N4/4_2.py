# 2. Напиши программу, которая принимает на вход
# десятизначное число (например:1234567893)
# и находит в нём все четные числа.
num = input('Введите десятизначное число: ')
if num.isdigit() and len(num) == 10:
    for i in num:
        if int(i) % 2 == 0:
            print(i, ', ',sep='', end='')
else:
    print('Ошибка! Введите десятизначное число!')




    # for i in num:
    #     str = ''
    #     if int(i) % 2 == 0:
    #        str += i + ', '
    # print(str.removesuffix(', '))
