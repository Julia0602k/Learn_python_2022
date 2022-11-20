# # Пример создания пустого класса:
# class Example:
#     pass
#
#
# # Пример создания экземпляра класса
# ex_1 = Example()
#
#
# # Тип переменной ex_1(Экземпляр класса):
# print(type(ex_1))


# # При создании экземпляра класса, всё тело класса сразу же начнет выполняться
# class Example_2:
#     print('Я экземпляр класса "Example_2"')
# ex_2 = Example_2()
#
#
# # Пример создания метода класса
# class Example_3:
#     print('Я экземпляр класса "Example_3"')
#
#     def print_info(self): # Функция = метод класса. Под "self" подрозумевается экземпляр класса
#         print('Я метод экземпляра класса "Example_3"')
# ex_3 = Example_3()
# ex_3.print_info()
# #
# #
# # Методы бывают пользовательские и встроенные
# class Metods:
#     def __init__(self): # Встроенный метод уже есть по умолчанию
#         pass
#     def print_info(self): # Пользовательский метод разработчик добавляет сам
#         pass
# print(dir(Metods))
# # Сначала отрабатывают те методы, которые стоят вначале "__Метод__", а потом уже пользовательские
#
#
# # Пример создания атрибута класса
# class Example_4:
#     a = 'Я атрибут класса'
#     age = 25 # Например атрибут класса - возраст. Обычная переменная
#              # Атрибута класса будут присвоены каждому экземпляру этого класса
# ex_4 = Example_4()
# new_ex_4 = Example_4()
# print(ex_4.a)
# print(new_ex_4.age)
#
#
# # Разница между атрибутами класса и атрибутами экземпляра класса
# class Example_5:
#     a = 'Я атрибут класса'
#
# ex_5 = Example_5()
# ex_5.b = 'Я атрибут экземпляра класса' # Это атрибут экземпляра класса
# ex_5.age = 25
# print(ex_5.b)
# # print(ex_5.age)
# #
# new_ex_5 = Example_5()
# print(new_ex_5.b) # Будет ошибка, т.к. атрибута одного экземпляра класса
#                   # никак не относятся к другим. Локальная переменная
#
#
# # Подробнее про метод __init__(self) и разница между статическими и динамическими атрибутами:
# class Car:
#     weight = 2000 # Это статический метод
#     def __init__(self, color, model): # Переопределяем метод __init__
#         self.color1 = color # Это динамический метод
#         self.model1 = model # Это динамический метод
#     def print_info(self,n1,n2,n3):
#         c = n1 + n2 + n3
#         print(c)
# car1 = Car('red', 'Ferrari')
# print(car1.color1, '|', car1.model1, '|', car1.weight)
# # print(Car.weight)
#
# car2 = Car('black', 'Tesla')
# print(car2.color1, '|', car2.model1, '|', car2.weight)
# #

# Методы экземпляра класса, методы класса, статические методы
# class Example_6:
#
#     @staticmethod
#     def print_info(): # теперь это статический метод, self не указывается
#         print('Информация')
#
# Example_6.print_info()

# class ClassMetods:
#     total_odject = 0
#     @classmethod
#     def __init__(cls):
#         cls.total_odject += 1
#     @classmethod
#     def get_count_info(cls):
#         print(f'Total Object are = {cls.total_odject}')
# class ClassMetods2(ClassMetods):
#     def print_info(self):
#         print('Информация')

# class1 = ClassMetods()
# # class2 = ClassMetods()
# # classs = ClassMetods()
# class3 = ClassMetods2()
# # ClassMetods.get_count_info()
# ClassMetods2.get_count_info()



# Уровни доступа атрибутов
# class Example_7:
#     a = 10
#     _b = 5
#     __c = 1
# #
# ex = Example_7()
# print(ex.a)
# print(ex._b)
# print(ex._Example_7__c)


# class Point:
#     def __init__(self, a='jj', b=0):
#         self.__x = a
#         self.__y = b
#
#     def set_coord(self, a=8, b=9):
#         if type(a) in (int, float) and type(b) in (int, float): # проверяем прежде чем перезаписывать
#             self.__x = a # так можно обратиться внутри к переменным типа Protected
#             self.__y = b
#         else:
#             raise ValueError("Координаты должны быть числами")
#
#     def get_coord(self):
#         return self.__x, self.__y
#
# pt = Point()
# # print(dir(pt))
# # print(pt.__x, pt.__y) # будет ошибка, так нельзя
# pt.set_coord(5,6)
# print(pt._Point__x, pt._Point__y)
# # print(pt.set_coord(111, 5))
# # print(pt.get_coord()) # так можно обратиться снаружи к переменным типа Protected
# pt.set_coord(10, 20) # так можно поменять значение этих переменных
# print(pt.get_coord()) # убеджаемся, что поменяли


# setter getter deleter
# class Phone:
#     # Инициализатор класса
#     def __init__(self):
#         self.is_on = False
#
#     # Включаем телефон
#     @property
#     def turn_on(self):
#         self.is_on = True
#         return self.is_on
#
#     @turn_on.setter
#     def turn_on(self,num1):
#         self.is_on = num1
#         print(self.is_on)
#     @turn_on.deleter
#     def turn_on(self):
#         del self.is_on
#         print('delete')
#
#
# my_phone = Phone()
# print(my_phone.turn_on)
# my_phone.turn_on = 1
# del my_phone.turn_on


class Phone:
    # Инициализатор класса
    def __init__(self):
        self.is_on = False

    # Включаем телефон
    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    # Если телефон включен, то делаем звонок
    def call(self):
        if self.is_on:
            print('Making call...')
        else:
            print('off')
# tel1 = Phone()
# tel1.turn_on()
# tel1.call()
# tel1.turn_off()
# tel1.call()
#
#
# class MobilePhone(Phone):
#     # Добавляем новое свойство батареи для класса потомка
#     def __init__(self):
#         super().__init__()
#         self.battery = 0
#     # Заряжаем телефон на велечину переданного значения
#     def charge(self, num):
#         self.battery = num
#         print(f'Charging battery up to ... {self.battery}%')
#     def call(self):
#         if self.is_on and self.battery > 0:
#             print('Making call...')
#         else:
#             print('off')
#
# mobile_phone_copy_1 = MobilePhone()
# print(dir(mobile_phone_copy_1))
#
# mobile_phone_copy_1.turn_on()
# mobile_phone_copy_1.call()
# mobile_phone_copy_1.charge(0)


# class Vehicle:
#     def vehicle_metod(self):
#         print('Это родительский метод класса Vehicle')
#
# class Car(Vehicle):
#     def car_metod(self):
#         print('Это дочерний метод класса Car')
#
# class Cycle(Vehicle):
#     def cycle_metod(self):
#         print('Это дочерний метод класса Cycle')
#
# class Double(Car, Cycle):
#     def __init__(self):
#         super().__init__()
#     def double_metod(self):
#         print('Это дочерний метод класса Double')
#
# car_a = Car()
# car_a.vehicle_metod()
# car_b = Cycle()
# car_b.vehicle_metod()
#
# double_a = Double()
# double_a.vehicle_metod()
# double_a.cycle_metod()
# double_a.car_metod()
# double_a.double_metod()
