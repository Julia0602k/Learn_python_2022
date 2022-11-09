# 3. Если в функцию передаётся кортеж, то посчитать длину всех его слов.
# Если список, то посчитать кол-во букв и чисел в нём.
# Число – кол-во нечётных цифр.
# Строка – количество букв.
# Сделать проверку со всеми этими случаями
a = [1, 2, 3]
def type_is(a):
    b = 0
    c = 0
    if a is tuple:
        for i in str(a):
            if i.isalpha():
                b += 1
    elif a is list:
        for i in str(a):
            if i.isalpha():
                b += 1
            elif i.isdigit():
                c += 1
    elif a is int:
        for i in str(a):
            if int(i) % 2:
                b += 1
    elif a is str(a):
        for i in str(a):
            if i.isalpha():
                b += 1
    return b, с

print(type_is(a))