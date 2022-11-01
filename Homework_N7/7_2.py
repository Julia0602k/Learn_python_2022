# 2. Есть словарь песен группы Depeche Mode
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут.
# Создайте новый словарь тех песен, название которых
# состоит из одного слова.
#

songsdict = {
'World in My Eyes': 4.76,
'Sweetest Perfection': 5.43,
'Personal Jesus': 4.56,
'Halo': 4.30,
'Waiting for the Night': 6.07,
'Enjoy the Silence': 4.6,
'Policy of Truth': 4.88,
'Blue Dress': 4.18,
'Clean': 5.68,
}
# Общее время звучания
print('Общее время звучания песен: ', sum(dict.values(songsdict)))

#Список песен, время звучаниях которых больше 5 минут
list5 = []
for key, value in dict.items(songsdict):
    if value <= 5.0:
        list5.append(key)
print('Список песен, время звучаниях которых больше 5 минут: ', list5)

## Создайте новый словарь тех песен, название которых состоит из одного слова
dict1 = {}
for key, value in dict.items(songsdict):
    if ' ' not in key:
        dict1[key] = value
print(dict1)


