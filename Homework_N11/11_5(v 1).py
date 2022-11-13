# 5. Ровно в одном
# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова
# word1 и word2 и возвращает значение True если слова имеют одинаковую длину и отличаются ровно
# в 1 символе и False в противном случае.
#
# Примечание. Следующий программный код:
#
# print(is_one_away(‘bike’, ‘hike’))
# print(is_one_away(‘water’, ‘wafer’))
# print(is_one_away(‘abcd’, ‘abpo’))
# print(is_one_away(‘abcd’, ‘abcde’))
# должен выводить:
#
# True
# True
# False
# False
def is_one_away(word1, word2):
    count = 0
    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
    if len(word1) - count == 1 and len(word1) == len(word2):
        return True
    else:
        return False

word1 = input('Введите первое слово: ')
word2 = input('Введите второе слово: ')
print(is_one_away(word1, word2))
