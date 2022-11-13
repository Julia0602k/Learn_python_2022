# 6. Палиндром 🌶️
# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и
# возвращает значение True если указанный текст является палиндромом и False в противном случае.
#
# Примечание 1. Палиндром – это строка, которая читается одинаково в обоих направлениях
#
# Примечание 2. При проверке считайте большие и маленькие буквы одинаковыми, а также игнорируйте
# пробелы, а также символы , . ! ? -.
#
# Примечание 3. Следующий программный код:
#
# print(is_palindrome(‘А роза упала на лапу Азора.’))
# print(is_palindrome(‘Gabler Ruby - burrel bag!’))
# print(is_palindrome(‘BEEGEEK’))
# должен выводить:
#
# True
# True
# False
def is_palindrome(text):
    for i in list(text.lower()):
        if i not in [' ', ',', '.', '!', '?', '-']:
            list_new.append(i)
    list_new2 = list.copy(list_new)
    list_new2.reverse()
    print(list_new, list_new2)
    return list_new == list_new2

text = input('Введите текст: ')
list_new = []
print(is_palindrome(text))
