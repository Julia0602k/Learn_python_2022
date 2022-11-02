# 3. В настольной игре Скрабл (Scrabble) каждая буква имеет
# определенную ценность.
# Напишите программу, которая вычисляет стоимость введенного
# пользователем слова. Будем считать, что на вход подается только
# одно слово, которое содержит только русские буквы.
# Решить через словарь.
dict3 = {
    1: ('А', 'В', 'Е', 'И', 'Н', 'О', 'Р', 'С', 'Т'),
    2: ('Д', 'К', 'Л', 'М', 'П', 'У'),
    3: ('Б', 'Г', 'Ё', 'Ь', 'Я'),
    4: ('Й', 'Ы'),
    5: ('Ж', 'З', 'Х', 'Ц', 'Ч'),
    8: ('Ш', 'Э', 'Ю'),
    10: ('Ф', 'Щ', 'Ъ')
}

# Вариант с доп списком
word3 = input('Введите слово из букв русского алфавита: ')
word3 = word3.upper()
list_alph = [] #Новый список из букв русского алфавита
for v in dict3.values():
    list_alph += v
count3 = 0
count4 = 0
for i in word3: #Проверка на содержание только букв русского алфавита
    if i not in list_alph:
        print('Ошибка! Введите слово из букв русского алфавита!')
        break
    elif i in list_alph:
        for k, v in dict3.items():
            if i in v:
                count3 += k
                count4 += 1
print('Стоимость введенного слова: ', count3) if count4 == len(word3) else None
