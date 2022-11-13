# 9. Is a Number Prime? 🌶️
# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и
# возвращает значение True если число является простым и False в противном случае.
#
# Примечание. Следующий программный код:
#
# print(is_prime(1))
# print(is_prime(10))
# print(is_prime(17))
# должен выводить:
# False
# False
# True

def is_prime(num):
    if num >= 2:
        del1 = 2
        while num % del1 != 0:
            del1 += 1
        return num == del1
    return False
num = int(input('Введите натуральное число: '))
print(is_prime(num))
