# 3. Исправьте ошибки, правильный результат работы описан в конце
#
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

