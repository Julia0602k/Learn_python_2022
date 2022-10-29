# Создайте кортеж из случайных 10 чисел.
# Найдите индексы максимального и
# минимального элемента

# a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# print(a.index(max(a)))
# print(a.index(min(a)))

# Создайте словарь person, в котором будут
# присутствовать ключи name, age, city.
# Выведите значение возраста из словаря
# person
person = dict.fromkeys(['name', 'age', 'city'])
person['age'] = 20
print(person['age'])

# dict.values(['name'])

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

