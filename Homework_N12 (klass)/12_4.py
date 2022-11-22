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
class Human:
    year = 2022
    def __init__(self, gender, name, temper, work, capital, income, house, car, family, expence):
        self.gender = gender
        self.name = name
        # self.age = age
        self.temper = temper
        self.work = work
        self.capital = capital
        self.income = income
        # self.d_birth = d_birth
        # self.d_death = d_death
        self.house = house
        self.car = car
        self.family = family
        # self.d_wedding = d_wedding
        self.expence = expence
    # def person1(self):
    #     # Определение имени, пола, семейного положения, темперамента
    #     self.gender = random.choice('mw')
    #     if self.gender == 'm':
    #         self.name = random.choice(['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend','Lewis Pope'])
    #         self.family = random.choice(['Свободен', 'Женат'])
    #     elif self.gender == 'w':
    #         self.name = random.choice(['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice','Ruth Rice'])
    #         self.family = random.choice(['Свободна', 'Замужем'])
    #     self.temper = random.choice(['холерик', 'сангвиник', 'меланхолик', 'флегматик'])
    #     # Работа, доходы, имущество
    #     self.work = random.choice(['Рабочий', 'Безработный'])
    #     self.capital = random.randint(100, 10000)
    #     if self.work == 'Рабочий':
    #         self.income = random.randint(1000, 5000)
    #     else:
    #         self.income = random.randint(100, 300)
    #     self.expence = 0.3 * self.income
    #     self.house = random.choice(['Свой дом', 'Аренда'])
    #     self.car = (['Есть', 'Нет'])

####### Создать метод info() с информацией о каждом объекте класса Human
    def info(self):
        print(f'''Имя: {self.name}
пол: {self.gender}

характер: {self.temper}
место работы: {self.work}
капитал: {self.capital}
ежемесячный доход: {self.income}


наличие дома: {self.house}
наличие машины: {self.car}
семейное положение: {self.family}

ежемесячные расходы: {self.expence}''')



######Создать метод life() который ежегодно(1 итерация цикла) будет прибавлять 1 год объекту класса Human
# Добавить шанс 1/30, что жизнь может оборваться преждевременно, в таком случае изменить дату смерти
#     def life(self, year):
#         self.age += 1
#         year += 1
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



    # Создать метод house() который ежегодно с шансом 1/4 будет определять, появиться ли у обекта свой
    # дом, если его еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
    # цену дома при покупке. Цена дома генирируется рандомно каждый год от 20000$ до 50000$



    # Создать метод car() который ежегодно с шансом 1/3 будет определять, появиться ли у обекта своя
    # машина, если ее еще не было при условии, что у объекта будет нужная сумма и отнимать от капитала
    # цену машины при покупке. Цена машины генирируется рандомно каждый год от 5000$ до 100000$




    # Как только все объекты умрут, добавить возможность выбора о каком объекте вывести информацию
    # на экран. Информация должна быть сначала изначальной, потом на конец жизни, чтобы можно было
    # сравнить данные.


    # def date(self, day, month, year):
    #     dict1 = {28: (2,), 30: (4, 6, 9, 11), 31: (1, 3, 5, 7, 8, 10, 12)}
    #     start = 1
    #     while start:
    #         for k, v in dict1.items():
    #             if month in v:
    #                 if day in range(1, k + 1):
    #                     start = 0
    #                 elif day == 29 and month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
    #                     start = 0
    #                 if year == 2022 and month >= 11:
    #                     continue
    #                 elif year == 1923 and month < 11:
    #                     continue
    #     if day < 10:
    #         day = '0' + str(day)
    #     if month < 10:
    #         month = '0' + str(month)
    #     self.d_birth = str(day) + '.' + str(month) + '.' + str(year)
    #     return self.d_birth
##########################################################################################################################################




# Определение возраста, даты рождения, свадьбы, смерти
age = random.randint(18, 100)
# ????????.date(random.randint(1, 31), random.randint(1, 12), random.randint(1923, 2004))
# d_birth = (r
# d_death =
# d_wedding =
dict_human = {}
name = ''
family = ''
for i in range(random.randint(2, 5)):
    gender = random.choice('mw')
    if gender == 'm':
        name = random.choice(['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend','Lewis Pope'])
        family = random.choice(['Свободен', 'Женат'])
    elif gender == 'w':
        name = random.choice(['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice','Ruth Rice'])
        family = random.choice(['Свободна', 'Замужем'])
    temper = random.choice(['холерик', 'сангвиник', 'меланхолик', 'флегматик'])
    # Работа, доходы, имущество
    work = random.choice(['Рабочий', 'Безработный'])
    capital = random.randint(100, 10000)
    if work == 'Рабочий':
        income = random.randint(1000, 5000)
    else:
        income = random.randint(100, 300)
    expence = 0.3 * income
    house = random.choice(['Свой дом', 'Аренда'])
    car = random.choice(['Есть', 'Нет'])
    dict_human[i] = Human(gender, name, temper, work, capital, income,  house, car, family, expence)
# dict_human[i] = Human(gender, name, age, temper, work, capital, income, d_birth, d_death, house, car, family, d_wedding, expence)


# dict_human = {i: Human(gender, name, age, temper, work, capital, income, d_birth, d_death, house, car, family, d_wedding, expence) for i in range(random.randint(2, 5))}
print(dict_human)
for v in dict_human.values():
    v.info()
print(len(dict_human))

# if human1.work == 'Безработный':
#     human1.jobs = 'Рабочий'
# elif human1.work == 'Рабочий':
#     human1.jobs = 'Безработный'

# for k,v in dict_human.items():
#     if v.work == 'Рабочий':
#     #     if i.temper == 'холерик' and random.randint(1, 7) == 1:
#     #         i.jobs = 'Безработный'
#     #     elif i.temper == 'сангвиник' and random.randint(1, 10) == 1:
#     #         i.jobs = 'Безработный'
#     #     elif i.temper == 'меланхолик' and random.randint(1, 6) == 1:
#     #         i.jobs = 'Безработный'
    #     elif i.temper == 'флегматик'and random.randint(1, 20) == 1:
    #         i.jobs = 'Безработный'
    # elif work == 'Безработный':
    #     if i.temper == 'холерик'and random.randint(1, 2) == 1:
    #         i.jobs = 'Рабочий'
    #     elif i.temper == 'сангвиник' and random.randint(1, 3) == 1:
    #         i.jobs = 'Рабочий'
    #     elif i.temper == 'меланхолик' and random.randint(1, 7) == 1:
    #         i.jobs = 'Рабочий'
    #     elif i.temper == 'флегматик' and random.randint(1, 5) == 1:
    #         i.jobs = 'Рабочий'




