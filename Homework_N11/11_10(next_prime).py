#
# 10. Next Prime 🌶️🌶️
# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное
# число num и возвращает первое простое число большее числа num.
#
# Примечание 1. Используйте функцию is_prime() из предыдущей задачи.
#
# Примечание 2. Следующий программный код:
#
# print(get_next_prime(6))
# print(get_next_prime(7))
# print(get_next_prime(14))
# должен выводить:
#
# 7
# 11
# 17
# def is_prime(num):
#     del1 = 2
#     while int(num) % del1 != 0:
#         del1 += 1
#     return int(num) == del1
# num = int(input('Введите целое натуральное число: '))
# print(is_prime(num))
