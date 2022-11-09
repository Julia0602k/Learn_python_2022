# 3. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями

t = ('Hello world', 123, 'April')
h = ['Hello world', 123, 'April']
n = 123
w = 'Hello world'
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
    return b, s
def type_list(a):
    b = 0
    d = 0
    for i in str(a):
        if i.isalpha():
            b += 1
        elif i.isdigit():
            d += 1
    return b, d
def type_int(a):
    b = 0
    for i in str(a):
        if int(i) % 2:
            b += 1
    return b
def type_str(a):
    b = 0
    for i in str(a):
        if i.isalpha():
            b += 1
    return b




#Вариант, где все в функции
# def type_is(a):
#     b = 0
#     s = 0
#     d = []
#     if type(a) is tuple:
#         for i in a:
#             if type(i) is str:
#                 for j in i:
#                     if j.isalpha():
#                         b += 1
#                 d.append(str(b))
#                 b = 0
#     elif type(a) is list:
#         for i in str(a):
#             if i.isalpha():
#                 b += 1
#             elif i.isdigit():
#                 s += 1
#     elif type(a) is int:
#         for i in str(a):
#             if int(i) % 2:
#                 b += 1
#     elif type(a) is str:
#         for i in str(a):
#             if i.isalpha():
#                 b += 1
#     return b, s, d
#
# print(type_is(s))

