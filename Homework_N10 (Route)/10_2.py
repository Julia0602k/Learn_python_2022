# 2. Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
def plus1(a, b):
    return (a + b)
def minus1(a, b):
    return (a - b)
def ymn1(a, b):
    return (a * b)
def del1(a, b):
    return (a / b)
start = 1
while start:
    num1 = input('Введите первое число: ')
    while not num1.isdigit():
        num1 = input('Ошибка! Введите первое число: ')
    num2 = input('Введите второе число: ')
    while not num2.isdigit():
        num2 = input('Ошибка! Введите второе число: ')
    sign = input('Введите операцию + - * / ')
    while not sign in ['+', '-', '*', '/']:
        sign = input('''Ошибка! Введите операцию + - * / ''')
    num1 = float(num1)
    num2 = float(num2)
    if sign == '+':
        plus1(num1, num2)
    elif sign == '-':
        minus1(num1, num2)
    elif sign == '*':
        ymn1(num1, num2)
    elif sign == '/':
        if num2 == 0:
            print('Ошибка! делить на "0" нельзя!')
        else:
            del1(num1, num2)
    start = input('''Если вы хотите выйти, введите 0.\n Если хотите продолжить вычисления, введите 1''')
    while not start.isdigit():
        start = input('Ошибка! Введите цифру! Если вы хотите выйти, введите 0.\n Если хотите продолжить вычисления, введите 1')

