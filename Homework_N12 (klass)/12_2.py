# 2. Два метода в классе, один принимает в себя либо строку, либо число.
#
# Если передают строку, то смотрим:
# если произведение гласных и согласных букв меньше или равно
# длине слова, выводить все гласные, иначе согласные;
# Если передают число то находим, произведение суммы чётных цифр на длину числа.
#
# Длину строки и числа искать во втором методе
#
class Str_or_int:
    def str_or_int(self, abc):
        if abc.isdigit():
            count1 = self.calculation(abc)
            for i in abc:
                if int(i) % 2 == 0:
                    count1 *= int(i)
            print(count1)
        elif not abc.isdigit():
            abc = abc.lower()
            str_gl = ''
            str_sogl = ''
            count_gl = 0
            count_sogl = 0
            for i in abc:
                if i.isalpha():
                    if i in ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
                        str_gl += i
                        count_gl += 1
                    else:
                        str_sogl += i
                        count_sogl += 1
            if count_gl * count_sogl <= self.calculation(abc):
                print(str_gl)
            else:
                print(str_sogl)

    def calculation(self, abc):
        return len(abc)

house = Str_or_int()
house.str_or_int(input('Введите строку или число: '))
