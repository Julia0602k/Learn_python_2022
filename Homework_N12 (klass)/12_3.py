# 3. Исправьте ошибки, правильный результат работы описан в конце
#class Class1:
    #
    # def __init__(self, value):
    #     self.__var = value
    #
    #
    # def read_set_del(self):
    #     print('Прочтено')
    #     return self.__var
    #
    #
    # def read_set_del(self, value):
    #     self.__var = value
    #     print('Изменено')
    #
    #
    # def read_set_del(self):
    #     del self.__var
    #     print('Удалено')
class Class1:
    def read_set_del(self):
        print('Прочтено')
    def read_set_del1(self):
        print('Изменено')
    def read_set_del2(self):
        print('Удалено')

c1 = Class1()
c1.read_set_del()
c1.read_set_del1()
c1.read_set_del2()
#
# # Если все ошибки исправлена, то на экран должно выводиться:
# # Прочтено
# # Изменено
# # Удалено

