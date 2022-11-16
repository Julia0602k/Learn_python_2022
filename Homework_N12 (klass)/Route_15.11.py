            #Напишите программу, которая будет принимать на вход название двух городов
            #и запрашивать расстояние из одного города в другой, а также кол-во населенных пунктов на этом пути,
            #после чего программа должна запрашивать их названия, максимально допустимую в них скрость и их протяженность в км.
            #Всю эту информацию сохранять в файле.
            #Если маршрут был уже сохранен до этого, то программа должна пропускать этот шаг и сразу переходить к следующему.
def route_is(a = 1):
    if a == 0:
        with open('points.txt', 'r') as f:
            list1 = []
            for i in f.readlines():
                list1.append(i.strip('\n'))
            return list1
    global cities
    cities = input('''Введите информацию о маршруте в формате: Город Город Расстояние
Например: Минск Москва 718км 
Введите: ''')
    global choise_m
    choise_m = cities
    with open('points.txt', 'r+') as f:
        for i in f.readlines():
            if cities in i:
                return route_is(0)
        num = int(input('Введите количество населенных пунктов: '))
        time_points = 0
        long_points = 0
        for i in range(num):
            Newnp = input(f'''Введите информацию о населенном пункте №{i + 1} в формате: Н/П Расстояние Допустимая Скорость
Наример: д.Бубушкино 5км 60км/ч или д.Экимань 2км 40км/ч или гп.Лосвидо 12км 60км/ч
Введите: ''')
            long_points += int(Newnp.split(' ')[1].strip('км'))
            time_points += int(Newnp.split(' ')[1].strip('км')) / int(Newnp.split(' ')[2].strip('км/ч'))
        f.write(cities + '\n' + str(long_points) + '\n' + str(time_points) + '\n')
    return route_is(0)
            # После чего программа должна запрашивать время, за которое пользователь хочет добраться
            # из одного города в другой и выдавть среднюю скорость с которой пользователю нужно будет
            # проезжать участки, которые не относятся к населенным пунктам, чтобы успеть добраться за
            # отведенное время.
def speed_middle(choise_m, t):
    for i in route_is(0):
        if i == choise_m:
            n = route_is(0).index(i)
            speed_mid = (int(route_is(0)[n].split(' ')[2].strip('км')) - int(route_is(0)[n + 1])) / (t - float(route_is(0)[n + 2]))
            return speed_mid
def times(choise_m, v):
    for i in route_is(0):
        if i == choise_m:
            n = route_is(0).index(i)
            time = (int(route_is(0)[n].split(' ')[2].strip('км')) - int(route_is(0)[n + 1])) / v
            return time + float(route_is(0)[n + 2])
def car(a = 1):
    if a == 0:
        with open('car.txt', 'r') as f:
            list1 = []
            for i in f.readlines():
                list1 += i.strip('\n').split(' ')
        return list1
    global newCar
    newCar = input('''Введите информацию о новом авто: Марка/Расход на 100км/Объем бака
Например: Audi_Q7 12л 70л
Введите: ''')
    with open('car.txt', 'r+') as f:
        for i in f.readlines():
            if newCar in i:
                return car(0)
        f.write(newCar + '\n')
    return car(0)
def azs(a = 1):
    if a == 0:
        with open('azs.txt', 'r') as f:
            list1 = []
            for i in f.readlines():
                list1.append(i.strip('\n'))
            return list1
    choise_m = input(f'''К какому маршруту вы хотите добавить информацию об АЗС?
Ваши сохраненные маршруты: {str(route_is(0)[::3])[1:-1]}
Напишите свой выбор или "New", чтобы добавить новый: ''')
    if choise_m == 'New':
        route_is()
    with open('azs.txt', 'r+') as f:
        for i in f.readlines():
            if choise_m in i:
                return azs(0)
        num = int(input('Введите количество АЗС: '))
        f.write(cities +'\n')
        for i in range(num):
            new_AZS = input(f'''Введите информацию об АЗС №{i + 1} в формате: Удаленность от стартовой точки / Цена за 1л топлива
Например: 101км 2.46р
Введите: ''')
            f.write(str(i+1) + ' ' + new_AZS.split(' ')[0].strip('км') + ' ' + new_AZS.split(' ')[1].strip('р')+ ' ')
        f.write('\n')
    return azs(0)
            # Добавьте также возможность вводить пользователю среднюю скорость, с которой он хочет
            # проезжать участки, которые не относятся к населенным пунктам и в таком случае программа
            # должна выдавать время, за которое он сможет добраться с такой скорость из одного города в другой.

            # Добавте возможность сохранять данные о своем автомобиле (расход топлива на 100км и обем бака),
            # чтобы после этого программа смогла воспользоваться этими данными и выполнить следующий шаг.
            # Данные о своих авто также хранить в файлах.

            # **Добавтье возможность пользователю вводить сколько литров у него есть в баке, а также
            # информацию о заправках(название АЗС, например "№1", "№2" и т.д. и на каком километраже
            # они распалагаются, например весь маршрут будет 300км, а заправки №1 и №2 располагаются на
            # 101-ом км и 230-ом км, а также цену на топливо)
# После программа должна определять нужно ли пользователю дозаправлться в пути,
# на каких заправках это нужно сделать, чтобы кол-во остановок было минимальным в пути.
# Пользователь не может заправить больше, чем объем его бака, это нужно учитывать,
# а также нужно учитывать кол-во топлива в баке, которое останется с начала пути на момент приезда на запраку.

# # *** Сделайте так, чтобы программа определяла самые оптимальные точки для остановок на дозаправку,
# чтобы пользователь платил, как можно меньше за топливо. И программа дожна выдавать на экран
# на каких заправках, сколько и на какую сумму нужно будет дозаправить

def refuel():
    choise_m = input(f'''Ваши сохраненные маршруты: {str(route_is(0)[::3])[1:-1]}
Напишите свой выбор или "New", чтобы добавить новый: ''')
    if choise_m == 'New':
        route_is()
        choise_m = cities
    car_m = input(f'''Ваши сохраненные авто: {str(car(0)[::3])[1:-1]}
Напишите свой выбор или "New", чтобы добавить новое: ''')
    if car_m == 'New':
        car()
        car_m = newCar
    list_azs_all = []
    for i in azs(0):
        if i == choise_m:
            list_azs_all += azs(0)[azs(0).index(i) + 1].split(' ')
    rashod = ''
    volume = ''
    for i in car(0):
        if i == car_m:
            rashod = int(car(0)[car(0).index(i) + 1].strip('л'))
            volume = int(car(0)[car(0).index(i) + 2].strip('л'))
            print(rashod)
            print(volume)


    #Объем топлива в баке в начале поездки
    now_fuel_tank = int(input('Введите объем топлива в баке в начале поездки: '))
    #Расстояние (весь маршрут)
    all_way = choise_m.split(' ')[2].strip('км')
    #Количество топлива на весь путь:
    amount_fuel_all_way = int(all_way) * rashod / 100
    if now_fuel_tank >= amount_fuel_all_way:
        return f'Вам не нужны дозаправки! По окончании маршрута у вас останется {now_fuel_tank - amount_fuel_all_way}л'
    print('list_azs_all', list_azs_all)
    print('rashod =', rashod, 'volume =', volume)
    # Расстояние на полном баке (запас 5л)
    distance_all_fuel_tank = (volume - 5) * 100 / rashod
    # Заправки, до которых можно доехать на залитом топливе
    list2_can_drive = []
    n = ''
    for i in list_azs_all[1::3]:
        if int(i) <= ((now_fuel_tank - 5) * 100 / rashod):
            n = list_azs_all.index(i)
            list2_can_drive += list_azs_all[n - 1:n + 2]
    print('list_can_drive', list2_can_drive)
    # Определение минимальной цены на ближайших заправках
    list_for_minimal = []
    minimal = ''
    for i in list2_can_drive[2::3]:
        list_for_minimal.append(float(i))
        minimal = min(list_for_minimal)
    print('list_for_minimal', list_for_minimal)
    print('minimal =', minimal)
    #Список данных НУЖНОЙ заправки
    list3_1azs_for_me = []
    for i in list2_can_drive:
        if float(i) == minimal:
            n3 = list2_can_drive.index(i)
            list3_1azs_for_me += list2_can_drive[n3 - 2:n3 + 1]
    print('list3_1azs_for_me', list3_1azs_for_me)

    start = 1
    while start:
        list2_can_drive = []
        n5 = ''
        for i in list_azs_all:
            if i == list3_1azs_for_me[2]:
                n5 = list_azs_all.index(i)
        for i in list_azs_all[n5+2::3]:
            if int(i) - int(list3_1azs_for_me[1]) <= distance_all_fuel_tank:
                n6 = list_azs_all.index(i)
                list2_can_drive += list_azs_all[n6 - 1:n6 + 2]
        print('list_can_drive', list2_can_drive)
        list3_2azs_for_me = []
        list_for_minimal = []     #список с минимальными ценами
        minimal = ''
        for i in list2_can_drive[2::3]:
            list_for_minimal.append(float(i))
            minimal = min(list_for_minimal)
        print('list_for_minimal', list_for_minimal)
        print('minimal =', minimal)
        for i in list2_can_drive:
            if float(i) == minimal:
                n3 = list2_can_drive.index(i)
                list3_2azs_for_me += list2_can_drive[n3 - 2:n3 + 1]
        print('list3_2azs_for_me', list3_2azs_for_me)
        amount_fuel_on_azs = (int(list3_2azs_for_me[1]) - int(list3_1azs_for_me[1]))*rashod / 100
        print(f'''Нужно заправить автомобиль на заправке N{list3_1azs_for_me[0]}, на {list3_1azs_for_me[1]}км пути, цена топлива {list3_1azs_for_me[2]} рублей за 1 литр.
Заправить нужно {amount_fuel_on_azs} литров на сумму {amount_fuel_on_azs * float(list3_1azs_for_me[2])} рублей''')

    return 1



while True:
    choise = int(input('''Если хотите проложить новый маршрут, введите - 1            
Если хотите узнать среднюю скорость, необходимую чтобы проехать маршрут за отведенное время, введите - 2            
Если хотите узнать время, за которое вы сможете доехать с заданной скоростью, введите - 3
Если хотите ввести данные о новом авто, введите - 4
Если хотите добавить данные о расположении заправок на маршруте, введите - 5
Если хотите узнать, нужно ли вам будет дозаправляться и где это лучше сделать, введите - 6
Введите: '''))
    if choise == 1:
        route_is()

    elif choise == 2:
        choise_m = input(f'''Ваши сохраненные маршруты: {route_is(0)[::3]}
Напишите свой выбор или "New", чтобы добавить новый: ''')
        if choise_m not in route_is(0) or choise_m == 'New':
            route_is()
        t = int(input('''За сколько часов(ч) вы хотите добраться?
Введите: '''))
        print(f'''Чтобы проехать маршрут "{choise_m}" за {t}ч вам нужно ехать по трассе со скростью {int(speed_middle(choise_m, t))}-{int(speed_middle(choise_m, t)) + 1}км/ч''')

    elif choise == 3:
        choise_m = input(f'''Ваши сохраненные маршруты: {route_is(0)[::3]}
Напишите свой выбор или "New", чтобы добавить новый: ''')
        if choise_m not in route_is(0) or choise_m == 'New':
            route_is()
        v = int(input('''С какой скоростью вы хотите ехать?
Введите: '''))
        print(f'Вы сможете проехать маршрут "{choise_m}" со средней скоростью {v}км/ч по трасе за {int(times(choise_m, v))}ч {int(((times(choise_m, v) - int(times(choise_m, v))) * 1000) / 60) + 1}мин')
    elif choise == 4:
        print(car())
    elif choise == 5:
        print(azs())
    elif choise == 6:
        print(refuel())
