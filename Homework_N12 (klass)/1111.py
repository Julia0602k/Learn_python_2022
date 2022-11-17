# # Создайте класс Example. В нём пропишите 3 (метода) функции. Две переменные
# # задайте статически, две динамически.
# # ❖ Первая функция: создайте переменную и выведите её
# # ❖ Вторая функция: верните сумму 2-ух глобальных переменных
# # ❖ Третья функция: верните результат возведения первой динамической
# # переменной во вторую динамическую переменную
# # ❖ Создайте объект класса.
# # ❖ Напечатайте обе функции
# # ❖ Напечатайте переменную a
#
# class Example:
#     a = 1
#     b = 2
#     def __init__(self, c, d, e):
#         self.c1 = c
#         self.d1 = d
#
#     def print1(self):
#         self.f = 5
#         print(self.f)
#     def info1(self, a, b):
#         return a + b
#
#     def result1(self):
#         return self.c1 ** self.d1
# abc = Example(2, 2, 3)
# print(abc.info1(1,2))
# print(abc.result1())
# print(Example.a)


# Тесты
# 1. Вызовите справочный метод default_info() для класса Human()
# 2. Создайте объект класса Human
# 3. Выведите справочную информацию о созданном объекте
# (вызовите метод info()).
# 4. Поправьте финансовое положение объекта - вызовите метод
# earn_money()
# 5. Посмотрите, как изменилось состояние объекта класса Human
class Human:

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.house = None

    @classmethod
    def default_info(cls):
        print(cls.__name__)
    def info(self):
        print(self.name, self.money, self.house)

    def earn_money(self, money):
        self.money += money

human1 = Human('Вася', 100)
human1.info()
human1.earn_money(500)
human1.info()
#


# Класс House
# 1. Создайте класс House
# 2. Создайте метод __init__() и определите внутри него два динамических свойства: _area и _price.
# 3. Свои начальные
# значения они получают из параметров метода __init__()
# 4. Создайте метод final_price(), который принимает в качестве параметра размер скидки и возвращает цену с учетом
# данной скидки.
# Класс SmallHouse
# 1. Создайте класс SmallHouse, унаследовав его функционал от класса House
# 2. Внутри класса SmallHouse переопределите метод __init__() так, чтобы он создавал объект с площадью 40м2
# Класс Human
# 1. Реализуйте приватный метод make_deal(), который будет отвечать за техническую реализацию покупки дома:
# уменьшать количество денег на счету и присваивать ссылку на только что купленный дом. В качестве аргументов
# данный метод принимает объект дома и его цену.
# 2. Реализуйте метод buy_house(), который будет проверять, что у человека достаточно денег для покупки, и
# совершать сделку. Если денег слишком мало - нужно вывести предупреждение в консоль. Параметры метода: ссылка
# на дом и размер скидки

class House:
    def __init__(self, area, price):
        self._area = area
        self._price = price
    def _make_deal(self, buyer):
        buyer.money -= self._price
        buyer.house = self
    def final_price(self, skidka):
        return self._price - self._price * skidka
    def buy_house(self, buyer, skidka):
        if buyer.money >= self.final_price(skidka):
            self._make_deal(buyer)
        else:
            print('Денег не достаточно!')

class SmallHouse(House):
    def __init__(self, price):
        super().__init__(40, price)
smallhouse = SmallHouse(1000)
smallhouse.buy_house(human1, 0.3)
if smallhouse.final_price(0.3) > human1.money:
    human1.earn_money(400)
    smallhouse.buy_house(human1, 0.3)
human1.info()


