# 1. Сумма цифр
#
# Напишите функцию print_digit_sum(), которая принимает одно целое число num и выводит на печать
# сумму его цифр.
def print_digit_sum(num):
    sum = 0
    for i in num:
        sum += int(i)
    print(f'Сумма цифр числа {num} равна {sum}')

num = input('Введите число: ')
while not num.isdigit():
    num = input('Ошибка! Введите число: ')
print_digit_sum(num)
