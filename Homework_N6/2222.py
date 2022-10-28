# Дан словарь с числовыми значениями. Необходимо
# их все перемножить и вывести на экран

dict1 = {a: a for a in range(1, 10)}
print(dict1)
count1 = 1
for a, b in dict1.items():
    count1 *= a * b
print(count1)

# Значениями словаря могут быть и списки.
# Создайте словарь с ключами BMW, Tesla и
# списками из 3х моделей в качестве значений.
# Выведите первое и последнее значения каждого из
# ключей

dict2 = dict([('bmw', ['x3', 'x5', 'x6']), ('tesla', ['model s', 'model x', 'model a'])])
print(dict2)
print(dict2['bmw'][0::2], dict2['tesla'][0::2])
for a, b in dict2.items():
    print(a, b[0])
    print(a, b[-1])

