# class Home:
#     b = 3 #атрибут класса
#     a = 7
#     def new1(self, a):
#         print(a)
# v = Home()
# m = 5
# family_home = Home()  #экземпляр класса
# # print(type(family_home))
# family_home.a = 2 #атрибут экземпляра класса
# print(family_home.b)
# c = Home()       #экземпляр класса
# c.new1(family_home.a)

class Human:
    def __init__(self, age, num1, num2):
        self.age1 = age
        self.num11 = num1
        self.num22 = num2
    f = 25
human1 = Human(20, 2, 2)
print(type(human1))
human1.wear = 'платье'
print(human1.age1, type(human1.num11), human1.num22, human1.wear)
human2 = Human(25, 2, 2)
print(type(human1.f), human2.f)


# class Example_2:
#     print('Я экземпляр класса "Example_2"')
# ex_2 = Example_2()
# ex_2

# class Example_3:
#     print('Я экземпляр класса "Example_3"')
#     def print_info(self): # Функция = метод класса. Под "self" подрозумевается экземпляр класса
#         print('Я метод экземпляра класса "Example_3"')
# ex_3 = Example_3()
# ex_3.print_info()
