# 3. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями

def type_tuple(a):
    s = []
    print('Длина слов кортежа: ')
    for j in a:
        if type(j) is str:
            is_alpha(j)
    return s
def type_list(a):
    is_alpha(a)
    d = 0
    for i in str(a):
        if i.isdigit():
            d += 1
    print(f'{d} цифр(-ы)')
    return d
def type_int(a):
    b = 0
    for i in str(a):
        if int(i) % 2:
            b += 1
    print(f'У числа {a} количество нечетных цифр: {b}')
    return b
def is_alpha(a):
    b = 0
    for i in str(a):
        if i.isalpha():
            b += 1
    print(f'{b} букв')
    return b

def what_is_type(abc):
    if type(abc) is tuple:
        type_tuple(abc)
    elif type(abc) is list:
        type_list(abc)
    elif type(abc) is int:
        type_int(abc)
    elif type(abc) is str:
        is_alpha(abc)

t = ('Hello world', 123, 'April')
h = ['Hello world', 123, 'April']
n = 123
w = 'Hello world'

what_is_type(h)      #Здесь нужно ввести букву из переменных выше
