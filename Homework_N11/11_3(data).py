# 3. Правильная дата
#
# Написать функцию "date", принимающую 3 аргумента — день, месяц, год.
# Вернуть True, если такая дата есть в нашем календаре, иначе — False.
def date(day, month, year):
    for k, v in dict1.items():
        if month in v:
            if day in range(1, k + 1):
                print(True)
            elif day == 29 and month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                print(True)
            else:
                print(False)
day = int(input('введите число: '))
month = int(input('введите номер месяца: '))
year = int(input('введите год: '))

dict1 = {28: (2,), 30: (4, 6, 9, 11), 31: (1, 3, 5, 7, 8, 10, 12)}
date(day, month, year)
