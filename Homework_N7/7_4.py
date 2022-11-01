# 4. Данные об email-адресах студентов хранятся в словаре:
# {'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
# 'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
# 'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}
#
# Нужно дополнить код таким образом, чтобы он вывел все адреса
# в алфавитном порядке и в формате имя_пользователя@домен.
#
dict5 = {'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
         'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
         'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']
}
#вывод списком
list4 = []
for k, v in dict5.items():
    for i in v:
        a = i + '@' + k
        list4.append(a)
list.sort(list4)
print(list4)

#вывод отдельно
list.sort(list4)
for i in range(len(list4)):
    print(list4[i])
