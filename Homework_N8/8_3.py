        # 3. Муж решил дарить своей жене каждый день цветы, но так чтобы в течении недели не повторяться. Он знает, что ей нравятся:
        # розы, тюльпаны, ромашки, нарциссы, васильки, хлопок и амариллис.
        #
        # Напишите программу, которая будет принимать на вход с клавиатуры день недели и название цветка. В подсказке при вводе с клавиатуры
        # должны выводиться цветы, которые муж еще не дарил на этой неделе.(Использовать множества)

            # Если цветок был подарен, то на следующей день(следующая итерация) он не должен выдаваться в подсказке, но если пользователь введет
            # название этого цветка, который он уже дарил на этой неделе, то ему на экран должна вывестись информация о том в какой день он дарил
            # этот цветок(хранить эту инфу в словаре)

                        # Подаренные цветы и полный список цветов, которые нравятся жене хранить во множествах.

                    # По истечении 7 дней(7 итераций) список цветов(который пишется в подсказке) из которых можно выбирать подарок должен сбрасываться.

# Также добавьте возможность добавлять и удалять цветы введеные с клавиатуры при желании пользователя.

# print(dict1)
set_flower = {'розы', 'тюльпаны', 'ромашки', 'нарциссы', 'васильки', 'хлопок', 'амариллис'}
set_flower_given = set()
set2 = set_flower - set_flower_given
start = True
while start:
    set_day = set()
    dict1 = dict.fromkeys(['пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'])
    print(dict1)
    count = 0
    while not count == 7:
        day = input('Введите день недели (пн,вт,ср,чт,пт,сб,вс): ')
        if day not in dict1.keys():
            print('Ошибка! Введите правильно день недели!')
            continue
        elif day in set_day:
            print('Ошибка! Такой день недели уже был введен! Введите правильно день недели!')
            continue
        elif day not in set_day:
            set_day.add(day)
        print('На этой неделе можно подарить: ', set2)
        flower = input('Введите название цветка: ')
        while flower not in set_flower:
            print('Ошибка! Введите правильно название цветка!', set2)
            flower = input('Введите название цветка: ')
            continue
        while flower in set_flower_given:
            for k, v in dict1.items():
                if v == flower:
                    print('Ошибка! Такой цветок уже был на этой неделе (в ', k,')! Выберите из: ', set2, sep='')
                    flower = input('Введите название цветка: ')
                    continue
        dict1[day] = flower
        set_flower_given.add(flower)
        print(dict1)
        # print(set_flower_given)
        # # #  Возможность измениния названия цветка
        # num1 = input('''Если вы:
        # хотите изменить название цветка для только что введенного дня недели - введите цифру 1;
        # хотите удалить название цветка и ввести новое из предыдущих дней введите цифру 2;
        # не хотите ничего изменять - нажмите Enter
        # # ''')
        # # if num1 == '1':
        #     set_flower_given.discard(flower)
        #     print('Введите новое название цветка из', set2, 'для только что введенного дня недели')
        #     flower = input('Новое название цветка: ')
        #     while flower in set2:
        #         print('Ошибка! Введите правильно название цветка! ', set2)
        #         flower = input('Введите название цветка: ', )
        #         continue
        #     dict1[day] = flower
        #     set_flower_given.add(flower)
        # elif num1 == '2':
        #     print('Введите название цветка из списка ', set_flower_given, 'для удаления')
        #     flower_del = input('название цветка:')
        #     set_flower_given.discard(flower_del)
        #     for k, v in dict1.items():
        #         if v == flower_del:
        #             dict1[k] = None
        #             print(dict1)
        #             print('Для дня недели', k)
        #             flower_new = input('введите новое название цветка: ')
        #             while flower_new not in set_flower:
        #                 print('Ошибка! Введите правильно название цветка из ', set2)
        #                 flower_new = input('Введите название цветка: ')
        #                 continue
        #             while flower_new in set_flower_given:
        #                 for k, v in dict1.items():
        #                     if v == flower_new:
        #                         print('Ошибка! Такой цветок уже был на этой неделе (в', k, ')! Выберите из:', set2, sep='')
        #                         flower_new = input('Введите название цветка: ')
        #                         dict1[k] = flower_new
        #                         continue
        #             set_flower_given.add(flower_new)
        print(dict1)
        print(set_flower_given)
        count += 1
    print('Цветы по дням недели:', dict1)
    print('Список подаренных цветов:', set_flower_given)
    print('Началась новая неделя!')
    set_flower_given.clear()
    set_day.clear()
    print(set_flower_given, set_day)
