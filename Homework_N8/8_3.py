# 3. Муж решил дарить своей жене каждый день цветы, но так чтобы в течении недели не повторяться. Он знает, что ей нравятся:
# розы, тюльпаны, ромашки, нарциссы, васильки, хлопок и амариллис.
#
# Напишите программу, которая будет принимать на вход с клавиатуры день недели и название цветка. В подсказке при вводе с клавиатуры
# должны выводиться цветы, которые муж еще не дарил на этой неделе.(Использовать множества)

# Если цветок был подарен, то на следующей день(следующая итерация) он не должен выдаваться в подсказке, но если пользователь введет
# название этого цветка, который он уже дарил на этой неделе, то ему на экран должна вывестись информация о том в какой день он дарил
# этот цветок(хранить эту инфу в словаре)

#            Подаренные цветы и полный список цветов, которые нравятся жене хранить во множествах.

# По истечении 7 дней(7 итераций) список цветов(который пишется в подсказке) из которых можно выбирать подарок должен сбрасываться.

# Также добавьте возможность добавлять и удалять цветы введеные с клавиатуры при желании пользователя.
dict1 = {}
set_day = {'пн', 'вт', 'ср', 'чт', 'пт', 'сб', 'вс'}
set_flower = {'розы', 'тюльпаны', 'ромашки', 'нарциссы', 'васильки', 'хлопок', 'амариллис'}
set_flower_given = set()
count = 0
while count < 8:
    day = input('Введите день недели (пн,вт,ср,чт,пт,сб,вс): ')
    if day not in set_day:
        print('Ошибка! Введите правильно день недели!')
        continue
    elif day in dict1.keys():
        print('Ошибка! Такой день недели уже был введен! Введите правильно день недели!')
        continue
    elif len(dict1.values()) == 0:
        print('На это неделе муж еще ничего не дарил')
    elif len(dict1.values()) > 0:
        print('На этой неделе еще можно подарить: ', set_flower - set_flower_given)
    flower = input('Введите название цветка (розы,тюльпаны,ромашки,нарциссы,васильки,хлопок,амариллис): ')
    while flower in set_flower:
        if
        print('Ошибка! Введите правильно название цветка!')
        continue
    elif flower in set_flower_given:
        for k, v in dict1.items():
            if v == flower:
                print('Ошибка! Такой цветок уже был на этой неделе (в ', k,')! Введите правильно название цветка!', sep='')
    else:
        set_flower_given.add(flower)
        dict1[day] = flower
        count += 1

#

