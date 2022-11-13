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
def get_next_prime(num):
    while not is_prime(num):
        num += 1
    return num
def is_prime(num):
    if num >= 2:
        del1 = 2
        while num % del1 != 0:
            del1 += 1
        return num == del1
    return False
num = int(input('Введите натуральное число: '))
num += 1
print(get_next_prime(num))
