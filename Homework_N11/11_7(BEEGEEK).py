# 7. BEEGEEK
# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
# строковое значение пароля password и возвращает значение True если пароль является действительным
# паролем BEEGEEK банка и False в противном случае.
# Примечание. Следующий программный код:
# print(is_valid_password(‘1221:101:22’))
# print(is_valid_password(‘565:30:50’))
# print(is_valid_password(‘112:7:9’))
# print(is_valid_password(‘1221:101:22:22’))
# должен выводить:
# True
# False
# False
# False
def is_valid_password(password):
    if password.count(':') == 2:
        a = password.split(':')[0]
        b = password.split(':')[1]
        c = password.split(':')[2]
        if is_digit(a,b,c) and is_palindrome(a) and is_prime(b) and is_even(c):
            return True
    return False
def is_digit(*args):
    count = 0
    for i in args:
        if not i.isdigit():
            count += 1
    return count == 0
def is_palindrome(num):
    list_new = []
    for i in list(num.lower()):
        if i not in [' ', ',', '.', '!', '?', '-']:
            list_new.append(i)
    list_new2 = list.copy(list_new)
    list.reverse(list_new2)
    return list_new == list_new2
def is_prime(num):
    del1 = 2
    while int(num) % del1 != 0:
        del1 += 1
    return int(num) == del1
def is_even(num):
    return int(num) % 2 == 0
password = input('''Введите пароль в формате a:b:c
число a должно быть палиндромом,
число b должно быть простым,
число c должно быть четным.
Введите пароль: ''')
print(is_valid_password(password))
while not is_valid_password(password):
    password = input('Ошибка! Введите пароль в формате a:b:c правильно: ')
