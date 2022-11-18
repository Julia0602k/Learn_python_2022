#
# 3. Исправьте ошибки, правильный результат работы описан в конце
#
class Class1:

    def __init__(self, value):
        self.__var = value


    def read_set_del(self):
        print('Прочтено')
        return self.__var


    def read_set_del(self, value):
        self.__var = value
        print('Изменено')


    def read_set_del(self):
        del self.__var
        print('Удалено')

c1 = Class1(5)
c1.read_set_del = 35
c1.read_set_del
del c1.read_set_del
#
# # Если все ошибки исправлена, то на экран должно выводиться:
# # Прочтено
# # Изменено
# # Удалено

