# 7. BEEGEEK
# BEEGEEK наконец открыл свой банк в котором используются специальные банкоматы с необычным паролем.
#
# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа.
# Поскольку основатель BEEGEEK фанатеет от математики, то он решил:
#
# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.
# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента
# строковое значение пароля password и возвращает значение True если пароль является действительным
# паролем BEEGEEK банка и False в противном случае.
#
# Примечание. Следующий программный код:
#
# print(is_valid_password(‘1221:101:22’))
# print(is_valid_password(‘565:30:50’))
# print(is_valid_password(‘112:7:9’))
# print(is_valid_password(‘1221:101:22:22’))
#
# должен выводить:
#
# True
# False
# False
# False
# def is_valid_password(password):
#     if :
#         return True
#     else:
#         return False

# def is_palindrome(text):
#     list_new = []
#     for i in list(text.lower()):
#         if i not in [' ', ',', '.', '!', '?', '-']:
#             list_new.append(i)
#     list_new2 = list.copy(list_new)
#     list.reverse(list_new2)
#     if list_new == list_new2:
#         return True
#     else:
#         return False
def is_prime(num):
    del1 = 2
    while int(num) % del1 != 0:
        del1 += 1
    return num == del1





# print('Введите пароль в формате a:b:c')
# a = input('Введите a (число должно быть палиндромом): ')
# while True:
#     if not is_palindrome(a) or not a.isdigit():
#         a = input('Ошибка! Введите a: ')
b = input('Введите b (число должно быть простым): ')
while True:
    if not is_prime(b) or not b.isdigit():
        print(is_prime(b))
        b = input('Ошибка! Введите b: ')

# c = input('Введите c: (должно быть четным): ')

# print(is_valid_password(password))
# password = a + b + c
