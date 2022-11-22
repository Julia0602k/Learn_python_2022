# import random
# class Human:
#     # gender = random.choice('mw')
#     def __init__(self, gender, name, family):
#         self.gender = gender
#         self.name = name
#         self.family = family
#     # @classmethod
#     def info(self):
#         print(f'''Имя: {self.name}
# пол: {self.gender}
# семейное положение: {self.family}''')
#     # @property
#     # def person1(self):
#     #     return self.gender
#     # @person1.setter
#     # def person1(self, gender):
#     #     # Определение имени, пола, семейного положения, темперамента
#     #     self.gender = random.choice('mw')
# dict_human = {}
# name = ''
# family = ''
# for i in range(random.randint(2, 5)):
#     gender = random.choice('mw')
#     if gender == 'm':
#         name = random.choice(
#             ['Lionel McCoy', 'Charles Cross', 'John Pitz', 'Jeffry Young', 'Johnathan Randall', 'Edward Townsend',
#              'Lewis Pope'])
#         family = random.choice(['Свободен', 'Женат'])
#     elif gender == 'w':
#         name = random.choice(
#             ['Aubrey Gilmore', 'Avice Reynolds', 'Theresa Bradford', 'Shonda Douglas', 'Karen Sanders', 'Ruby Rice',
#              'Ruth Rice'])
#         family = random.choice(['Свободна', 'Замужем'])
#     dict_human[i] = Human(gender, name, family)
#
#
# # gender = random.choice('mw')
# # human1 = Human(random.choice('mw'))
# # human2 = Human(gender)
# # human1.info()
# # human2.info()
#
# # dict_human = {i: Human(gender) for i in range(random.randint(2, 5))}
# # # for k, v in dict_human:
# #
# print(dict_human)
# # Human.info()
# for v in dict_human.values():
#     v.info()
#
# # print(len(dict_human))
str = '11.22.3333'
print(str[6:])