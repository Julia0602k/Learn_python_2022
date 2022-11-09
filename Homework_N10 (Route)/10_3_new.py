# 3. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями

def type_tuple(a):
    b = 0
    s = []
    for i in a:
        if type(i) is str:
            for j in i:
                if j.isalpha():
                    b += 1
            s.append(str(b))
            b = 0
    print(f'Длина слов кортежа: {str(s)[1:-1]}')
    return b, s
def type_list(a):
    b = 0
    d = 0
    for i in str(a):
        if i.isalpha():
            b += 1
        elif i.isdigit():
            d += 1
    print(f'Количество букв списка {b}, количество цифр списка {d}')
    return b, d
def type_int(a):
    b = 0
    for i in str(a):
        if int(i) % 2:
            b += 1
    print(f'У числа {a} количество нечетных цифр: {b}')
    return b
def type_str(a):
    b = 0
    for i in str(a):
        if i.isalpha():
            b += 1
    print(f'Количество букв строки {b}')
    return b

# def is_alpha(a):
#     b = 0
#     for i in str(a):
#         if i.isalpha():
#             b += 1
#     return b

def what_is_type(abc):
    if type(abc) is tuple:
        type_tuple(abc)
    elif type(abc) is list:
        type_list(abc)
    elif type(abc) is int:
        type_int(abc)
    elif type(abc) is str:
        type_str(abc)

t = ('Hello world', 123, 'April')
h = ['Hello world', 123, 'April']
n = 123
w = 'Hello world'

what_is_type(h)      #Здесь нужно ввести букву из переменных выше
