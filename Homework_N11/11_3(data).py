# 3. Правильная дата
#
# Написать функцию "date", принимающую 3 аргумента — день, месяц, год.
# Вернуть True, если такая дата есть в нашем календаре, иначе — False.

def date(d, m, y):
    for k, v in dict1.items():
        if (y % 4 == 0 and y % 100 != 0 or y % 400 == 0) and m in v and d == 29:
            print(True)
            break
        elif d in range(1, k + 1) and m in v:
            print(True)
        else:
            print(False)
d = int(input('введите число: '))
m = int(input('введите номер месяца: '))
y = int(input('введите год: '))
dict1 = {28: (2,), 30: (4, 6, 9, 11), 31: (1, 3, 5, 7, 8, 10, 12)}
date(d, m, y)
