# 11. Правильная скобочная последовательность 🌶️
# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую
# строку text, состоящую из символов ( и ) и возвращает значение True если поступившая на вход
# строка является правильной скобочной последовательностью и False в противном случае.
#
# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только
# из символов ( и ), где каждой открывающей скобке найдется парная закрывающая скобка.
# Примечание 2. Следующий программный код:
# print(is_correct_bracket(‘()(()())’))
# print(is_correct_bracket(‘)(())(‘))
# должен выводить:
# True
# False

def is_correct_bracket(text):
    count1 = 0
    count2 = 0
    count3 = 0
    while count2 - count1 == count3 - count2:
        start = 1
        while start:
            for i in text[count1:]:
                if i == '(':
                    count2 += 1
                else:
                    break
        start = 1
        count3 = count2
        print(111, count1, count2, count3)
        while start:
            for i in text[count2:]:
                if i == ')':
                    count3 += 1
                else:
                    break
        count1 = count3
        print(222, count1, count2, count3)
    return True

text = input('''Введите строку, состоящую из символов "(" и ")" : ''')
print(is_correct_bracket(text))
