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
    year = 2022
    def __init__(self, gender, name, age, temper, work, capital, income, d_birth, d_death, house, car, family, d_wedding, expence):
        self.gender = gender
        self.name = name
        self.age = age
        self.temper = temper
        self.work = work
        self.capital = capital
        self.income = income
        self.__d_birth = d_birth
        self.__d_death = d_death
        self.house = house
        self.car = car
        self.family = family
        self.__d_wedding = d_wedding
        self.expence = expence

####### Создать метод info() с информацией о каждом объекте класса Human
    def info(self):
        print(f'''Имя: {self.name}
пол: {self.gender}
возраст: {self.age}
характер: {self.temper}
место работы: {self.work}
капитал: {self.capital}
ежемесячный доход: {self.income}
дата рождения: {self.__d_birth}
дата смерти: {self.__d_death}
наличие дома: {self.house}
наличие машины: {self.car}
семейное положение: {self.family}
дата свадьбы: {self.__d_wedding}
ежемесячные расходы: {self.expence}\n''')



######Создать метод life() который ежегодно(1 итерация цикла) будет прибавлять 1 год объекту класса Human
# Добавить шанс 1/30, что жизнь может оборваться преждевременно, в таком случае изменить дату смерти
#     def life(self, year):
#         self.age += 1
#         num_d = random.randint(1,30)
#         if num_d == 1:
#             # del

#########Создать метод jobs() который ежегодно(1 итерация цикла) будет определять появится ли работа у того,
    # у кого ее не было, или уволят ли того, у кого работа была и перезавписывать это свойство объекта.
    # Если характер "холерик", то шансы устроиться на работу 1/2, шансы быть уволеным 1/7
    # Если характер "сангвиник", то шансы устроиться на работу 1/3, шансы быть уволеным 1/10
    # Если характер "меланхолик", то шансы устроиться на работу 1/7, шансы быть уволеным 1/6
    # Если характер "флегматик", то шансы устроиться на работу 1/5, шансы быть уволеным 1/20
    # Добавить счётчик, который посчитает кол-во работ за всю жизнь.
    @property
    def jobs(self):
        return self.work
    @jobs.setter
    def jobs(self, w):
        self.work = w



################ Создать метод wedding() который ежегодно(1 итерация цикла) будет определять появиться ли вторая
    # половинка, если ее не было. От 18 до 30 лет шансы 1/4, от 31 до 45 шансы 1/7,
    # от 46 до 65 шансы 1/12, от 66+ шансы 1/20
    # Метод должен перезаписывать дату свадьбы
    # @property
    # def wedding(self):
    #     return self.family
    # # @wedding.setter
    # # def wedding(self, ):
    # #     year += 1



    # Создать метод salary() который ежегодно будет увеличивать капитал объекта согласно его доходу.
    # Добавить шанс 1/4 что доход может измениться в рандом диапазоне от 1000$ До 5000$.

    # def salary(self):
    #     self.capital += income
    #     if random.randint(1, 4) == 1:
    #         self.income = random.randint(1000, 5000)



    # Создать метод expenses() который ежегодно будет отнимать расходы от капитала
    # При наличии арендного жилья расходы должны увеличиваться на 15%, при собственном жилье только на 7%
    # При наличии авто расходы должны увеличиваться на 13%
    # def expenses(self):
    #


    # Создать метод house() который ежегодно с шансом 1/4 будет определять, появиться ли у обекта свой
    # дом, если его еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
    # цену дома при покупке. Цена дома генирируется рандомно каждый год от 20000$ до 50000$
    # def house(self):


    # Создать метод car() который ежегодно с шансом 1/3 будет определять, появиться ли у обекта своя
    # машина, если ее еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
    # цену машины при покупке. Цена машины генирируется рандомно каждый год от 5000$ до 100000$
    # def car(self):

    # Как только все объекты умрут, добавить возможность выбора о каком объекте вывести информацию
    # на экран. Информация должна быть сначала изначальной, потом на конец жизни, чтобы можно было
    # сравнить данные.
##########################################################################################################################################

dict_human1 = {}
name = ''
family = ''
for i in range(random.randint(2, 5)):
    #Имя, пол, семейное положение, характер
    gender = random.choice(['Мужчина', 'Женщина'])
    if gender == 'Мужчина':
        name = random.choice(['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend','Lewis Pope'])
        family = random.choice(['Свободен', 'Женат'])
    elif gender == 'Женщина':
        name = random.choice(['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice','Ruth Rice'])
        family = random.choice(['Свободна', 'Замужем'])
    temper = random.choice(['холерик', 'сангвиник', 'меланхолик', 'флегматик'])
    # Работа, доходы, имущество
    work = random.choice(['Рабочий', 'Безработный'])
    capital = round(random.randint(100, 10000), -2)
    if work == 'Рабочий':
        income = round(random.randint(1000, 5000), -2)
    else:
        income = round(random.randint(100, 300), -2)
    expence = int(round(0.3 * income))
    house = random.choice(['Свой дом', 'Аренда'])
    car = random.choice(['Есть', 'Нет'])
    # Даты жизни, свадьбы, возраст
    d_birth = date_is(1923, 2004)
    d_death = date_is(2023, (int(d_birth[-4:]) + 100))
    d_wedding = ''
    if family == 'Женат' or family == 'Замужем':
        d_wedding = date_is((int(d_birth[-4:]) + 18), 2022)
    elif family == 'Свободен' or family == 'Свободна':
        d_wedding = None
    age = 2023 - int(d_birth[-4:])
    dict_human1[i] = Human(gender, name, age, temper, work, capital, income, d_birth, d_death, house, car, family, d_wedding, expence)

print(dict_human1)
for v in dict_human1.values():
    v.info()
print(len(dict_human1))

# count = len(dict_human1)
# while count:    #значение счетчика становится меньше, когда кто-то умирает. Как только count == 0 - цикл остановится и выведется информация о людях

###########Выдача информации в конце программы
# for v in dict_human1.values():
#     v.info()
# for v in dict_human2.values():
#     v.info()

dict_job1_temper = {'холерик': (7, 2), 'сангвиник': (10, 3), 'меланхолик': (6, 7), 'флегматик': (20, 5)}
for v in dict_human1.values():
    for key, value in dict_job1_temper.items():
        if key == v.temper:
            if v.work == 'Рабочий' and random.randint(1, value[0]) == 1:
                v.jobs = 'Безработный'
            elif v.work == 'Безработный' and random.randint(1, value[1]) == 1:
                v.jobs = 'Рабочий'




