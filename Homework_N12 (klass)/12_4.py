# ***4. Напишите программу, которая будет рандомно генирировать от 2 до 5 объектов класса Human.
# У каждого объекта этого класса рандомным образом должны определяться следующие свойства:
# 1) Пол: Мужчина или Женщина
# 2) Рандомное имя в зависимости от пола:
# М(Lionel McCoy, Charles Cross, John Pitz, Jeffry Young, Johnathan Randall, Edward Townsend, Lewis Pope)
# Ж(Aubrey Gilmore, Avice Reynolds, Theresa Bradford, Shonda Douglas, Karen Sanders, Ruby Rice, Ruth Rice)
# Можно дополнить своими вариантами
# 3) Возраст: от 18 до 100 лет
# 4) Характер: холерик или сангвиник или меланхолик или флегматик
# 5) Место работы: Рабочий или Безработный
# 6) Рандомный капитал от 100$ до 10000$
# 7) Рандомный ежемесячный доход от 1000$ до 5000$, при наличии работы. Если работы нет, то от 100$ до 300$.
# 8) Рандомная дата рождения в формате xx.xx.xxxx(тип Protected)
# 9) Рандомная дата смерти в формате xx.xx.xxxx(тип Protected)
# 10) Наличие дома: Свой дом или Аренда
# 11) Наличие машины: Есть или нет
# 12) Семейное положение: Свободен или Женат/Замужем в зависимости от пола
# 13) Дата свадьбы, если статус Женат/Замужем присвоен сразу, то рандомная дата
# в формате xx.xx.xxxx(тип Protected) в диапазоне от даты рождения +18 лет до текущего возраста
# Если изначально статус свободен, то значение None
# 14) Ежемесячные расходы 30% от ежемесячного дохода
import copy
import random


def date_is(year1, year2):
    year = random.randint(year1, year2)
    dict1 = {28: (2,), 30: (4, 6, 9, 11), 31: (1, 3, 5, 7, 8, 10, 12)}
    start = 1
    day = ''
    month = ''
    while start:
        day = random.randint(1, 31)
        month = random.randint(1, 12)
        for k, v in dict1.items():
            if month in v:
                if day in range(1, k + 1):
                    start = 0
                elif day == 29 and month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
                    start = 0
    if day < 10:
        day = '0' + str(day)
    if month < 10:
        month = '0' + str(month)
    str_date = str(day) + '.' + str(month) + '.' + str(year)
    return str_date


class Human:
    def __init__(self):
        self.gender = random.choice(['Мужчина', 'Женщина'])
        if self.gender == 'Мужчина':
            self.name = random.choice(
                ['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend',
                 'Lewis Pope'])
            self.family = random.choice(['Свободен', 'Женат'])
        elif self.gender == 'Женщина':
            self.name = random.choice(
                ['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice',
                 'Ruth Rice'])
            self.family = random.choice(['Свободна', 'Замужем'])
        self.temper = random.choice(['холерик', 'сангвиник', 'меланхолик', 'флегматик'])
        self.work = random.choice(['Рабочий', 'Безработный'])
        self.capital = round(random.randint(100, 10000), -2)
        if self.work == 'Рабочий':
            self.income = round(random.randint(1000, 5000), -2)
        else:
            self.income = round(random.randint(100, 300), -2)
        self.expense = int(round(0.3 * self.income))
        self.house = random.choice(['Свой дом', 'Аренда'])
        self.car = random.choice(['Есть', 'Нет'])
        self.__d_birth = date_is(1923, 2004)
        # self.__d_death = date_is(2023, (int(self.__d_birth[-4:]) + 100))
        self.__d_death = 'неизвестна'
        self.__d_wedding = ''
        self.age = 2023 - int(self.__d_birth[-4:])
        if self.family == 'Женат' or self.family == 'Замужем':
            self.__d_wedding = date_is((int(self.__d_birth[-4:]) + 18), 2022)
        elif self.family == 'Свободен' or self.family == 'Свободна':
            self.__d_wedding = None
        self.count_jobs = 0
        if self.work == 'Рабочий':
            self.count_jobs = 1
        self.children = random.randint(0,2)

    #  Создать метод info() с информацией о каждом объекте класса Human
    def info(self):
        print(
            f'''Имя: {self.name}\nпол: {self.gender}\nвозраст: {self.age}\nхарактер: {self.temper}\nместо работы: {self.work}
капитал: {self.capital}\nежемесячный доход: {self.income}\nдата рождения: {self.__d_birth}\nдата смерти: {self.__d_death}
наличие дома: {self.house}\nналичие машины: {self.car}\nсемейное положение: {self.family}\nдата свадьбы: {self.__d_wedding}
ежемесячные расходы: {self.expense}\nколичество работ: {self.count_jobs}\nколичество детей: {self.children}''')

    def info_name(self):
        return self.name

    #  Создать метод life() который ежегодно(1 итерация цикла) будет прибавлять 1 год объекту класса Human
    # Добавить шанс 1/30, что жизнь может оборваться преждевременно, в таком случае изменить дату смерти
    def life(self, year_now):
        self.age += 1
        if random.randint(1, 30) == 1:
            self.__d_death = date_is(2022, 2100)[:6] + str(year_now)
    ### Метод для даты смерти человека:
    def date_death(self, year_now):
        death_this_year = ''
        dict_date_death = {100: (0, 20), 90: (21, 30), 80: (31, 40), 70: (41, 50), 50: (51, 60), 30: (61, 70),
                           10: (71, 80), 5: (81, 90), 3: (91, 150)}
        for k, v in dict_date_death.items():
            if v[0] <= self.age <= v[1] and random.randint(1, k) == 1:
                self.__d_death = date_is(year_now, year_now)

    #  Создать метод jobs() который ежегодно(1 итерация цикла) будет определять появится ли работа у того,
    # у кого ее не было, или уволят ли того, у кого работа была и перезавписывать это свойство объекта.
    # Если характер "холерик", то шансы устроиться на работу 1/2, шансы быть уволеным 1/7
    # Если характер "сангвиник", то шансы устроиться на работу 1/3, шансы быть уволеным 1/10
    # Если характер "меланхолик", то шансы устроиться на работу 1/7, шансы быть уволеным 1/6
    # Если характер "флегматик", то шансы устроиться на работу 1/5, шансы быть уволеным 1/20
    # Добавить счётчик, который посчитает кол-во работ за всю жизнь.
    def jobs(self):
        dict_job1_temper = {'холерик': (7, 2), 'сангвиник': (10, 3), 'меланхолик': (6, 7), 'флегматик': (20, 5)}
        for k, v in dict_job1_temper.items():
            if k == self.temper:
                if self.work == 'Рабочий' and random.randint(1, v[0]) == 1:
                    self.work = 'Безработный'
                    self.income = round(random.randint(100, 300), -2)
                elif self.work == 'Безработный' and random.randint(1, v[1]) == 1:
                    self.work = 'Рабочий'
                    self.income = round(random.randint(1000, 5000), -2)
                    self.count_jobs += 1

    #   Создать метод wedding() который ежегодно(1 итерация цикла) будет определять появиться ли вторая
    # половинка, если ее не было. От 18 до 30 лет шансы 1/4, от 31 до 45 шансы 1/7,
    # от 46 до 65 шансы 1/12, от 66+ шансы 1/20
    # Метод должен перезаписывать дату свадьбы
    def wedding(self, year_now):
        dict_wedding = {4: (18, 30), 7: (31, 45), 12: (46, 65), 20: (66, 100)}
        for k, v in dict_wedding.items():
            if self.family == 'Свободен' and v[0] <= self.age <= v[1] and random.randint(1, k) == 1:
                self.family = 'Женат'
                self.__d_wedding = date_is(2022, 2100)[:6] + str(year_now)
            elif self.family == 'Свободна' and v[0] <= self.age <= v[1] and random.randint(1, k) == 1:
                self.family = 'Замужем'
                self.__d_wedding = date_is(2022, 2100)[:6] + str(year_now)
    def birth_child(self):
        dict_birth_child = {10:(18,30), 20:(31,40), 50:(41,50)}
        for k,v in dict_birth_child.items():
            if (self.family == 'Женат' or self.family == 'Замужем') and random.randint(1, k) == 1 and v[0] <= self.age <= v[1]:
                self.children += 1
            elif (self.family == 'Свободен' or self.family == 'Свободна') and random.randint(1, k*5) == 1 and v[0] <= self.age <= v[1]:
                self.children += 1
    def divorce_or_death_of_h_w(self):
        if self.family == 'Женат' and random.randint(1, 20) == 1:
            self.family = 'Свободен'
            self.__d_wedding = None
        elif self.family == 'Замужем' and random.randint(1, 20) == 1:
            self.family = 'Свободна'
    #  Создать метод salary() который ежегодно будет увеличивать капитал объекта согласно его доходу.
    # Добавить шанс 1/4 что доход может измениться в рандом диапазоне от 1000$ До 5000$.
    def salary(self):
        self.capital += self.income * 12
        if self.work == 'Рабочий' and random.randint(1, 4) == 1:
            self.income = round(random.randint(1000, 5000), -2)

    #   Создать метод expenses() который ежегодно будет отнимать расходы от капитала
    # При наличии арендного жилья расходы должны увеличиваться на 15%, при собственном жилье только на 7%
    # При наличии авто расходы должны увеличиваться на 13%
    def expenses(self):
        self.expense = 0.3 * self.income
        if self.house == 'Аренда':
            a = 1.15 * self.expense
            self.capital -= (self.expense * 1.15) * 12
        elif self.house == 'Свой дом':
            self.capital -= (self.expense * 1.07) * 12
        if self.car == 'Есть':
            self.capital -= (self.expense * 1.13) * 12
        if self.children > 0:
            self.capital -= (self.expense * (1 + 0.1*self.children)) * 12
        self.capital = int(round(self.capital, -1))
        self.expense = int(self.expense)

    #  Создать метод house() который ежегодно с шансом 1/4 будет определять, появиться ли у обекта свой
    # дом, если его еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
    # цену дома при покупке. Цена дома генирируется рандомно каждый год от 20000$ до 50000$
    def houses(self):
        price_of_house = round(random.randint(20000, 50000), -2)
        if self.house == 'Аренда' and self.capital >= price_of_house and random.randint(1, 4) == 1:
            self.house = 'Свой дом'
            self.capital -= price_of_house

    #  Создать метод car() который ежегодно с шансом 1/3 будет определять, появиться ли у обекта своя
    # машина, если ее еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
    # цену машины при покупке. Цена машины генирируется рандомно каждый год от 5000$ до 100000$
    def cars(self):
        price_of_car = round(random.randint(5000, 100000), -2)
        if self.car == 'Нет' and self.capital >= price_of_car and random.randint(1, 3) == 1:
            self.car = 'Есть'
            self.capital -= price_of_car

# class Children(Human):
#     def __init__(self):
#         super().__init__()
# ex = Children()
# print(1111111)
# ex.info()

dict_human1 = {}
for i in range(random.randint(2, 5)):
    dict_human1[i] = Human()
# Как только все объекты умрут, добавить возможность выбора о каком объекте вывести информацию
# на экран. Информация должна быть сначала изначальной, потом на конец жизни, чтобы можно было
# сравнить данные.
year_now = 2022
dict_human_live = copy.deepcopy(dict_human1)
list_human = []
for k in dict_human1.keys():
    list_human.append(k)
dict_human_death = {}
while len(dict_human1) != len(dict_human_death):
    year_now += 1
    for k, v in dict_human1.items():
        if k in list_human:
            v.life(year_now)
            v.date_death(year_now)
            if v._Human__d_death[-4:] == str(year_now):
                dict_human_death[k] = v
                list_human.remove(k)
                continue
            v.jobs()
            v.wedding(year_now)
            v.birth_child()
            v.divorce_or_death_of_h_w()
            v.salary()
            v.expenses()
            v.houses()
            v.cars()
# Выдача информации в конце программы
while True:
    print(f'Информацию о каком человеке вы хотите получить? Список имен:')
    for k, v in dict_human1.items():
        print(k, '-', v.info_name(), end='; ')
    human_number = input('\nвведите цифру: ')
    print('Данные в 2022 году:')
    for k, v in dict_human_live.items():
        if k == int(human_number):
            v.info()
    print('Данные в конце жизни: ')
    for k, v in dict_human_death.items():
        if k == int(human_number):
            v.info()
