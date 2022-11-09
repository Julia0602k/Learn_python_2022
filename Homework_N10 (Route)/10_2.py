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
while int(start):
    num1 = float(input('Введите первое число: '))
    sign = input('Введите + - * / ')
    while not sign in ['+', '-', '*', '/']:
        sign = input('''Ошибка! Введите + - * / ''')
    num2 = float(input('Введите второе число: '))
    if sign == '+':
        print(plus1(num1, num2))
    elif sign == '-':
        print(minus1(num1, num2))
    elif sign == '*':
        print(ymn1(num1, num2))
    elif sign == '/':
        if num2 == 0:
            print('Ошибка! делить на "0" нельзя!')
        else:
            print(del1(num1, num2))
    start = input('''Если вы хотите выйти, введите 0.\n Если хотите продолжить вычисления, введите 1\n Сделайте выбор: ''')
    while not start.isdigit():
        start = input('Ошибка! Введите цифру! Если вы хотите выйти, введите 0.\n Если хотите продолжить вычисления, введите 1')



