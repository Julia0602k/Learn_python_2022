
# 4. Посчитать, сколько пар букв верхнего и нижнего регистра
# находится в веденном с клавиатуры слове.
# (Например: HjkLM - 1 пара нижнего(это jk), 1 пара верхнего(это LM))
# а также отдельно вывести на экран сколько всего букв в слове,
# отдельно сколько гласных и согласных.

word4 = input('Введите слово: ')
if word4.isalpha():
    count_low = 0
    count_up = 0
    for i in range(0, len(word4)-1):
        if word4[i].islower() and word4[i + 1].islower():
            count_low += 1
        elif word4[i].isupper() and word4[i + 1].isupper():
            count_up += 1
    print('В слове', word4, 'содержится', count_low, 'пар (-а) нижнего регистра')
    print('В слове', word4, 'содержится', count_up, 'пар (-а) верхнего регистра')
    print('В слове', len(word4), 'букв')
    #Подсчет гласных и согласных
    count_gl = 0
    count_sogl = 0
    word44 = word4.lower()
    for i in word44:
        if i in ['a', 'e', 'i', 'o', 'u', 'y']:
            count_gl += 1
        else:
            count_sogl += 1
    print('В слове', word4, 'содержится', count_gl, 'гласных букв')
    print('В слове', word4, 'содержится', count_sogl, 'согласных букв')
else:
    print('Ошибка! Введите слово, состоящее из букв!')

