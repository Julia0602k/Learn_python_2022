# Представь, что мы пишем программу для банковских карточек.
# Человек может совершать покупки, пока у него на карте хватает на это денег.
# В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.

ost_na_karte = int(input('Введите количество денег на карте: '))
list1 = []
rashod = 0
while rashod <= ost_na_karte:
    rashod = int(input('Введите расходы: '))
    ost_na_karte -= rashod
    list1.append(rashod)
print('Были произведены следующие расходы:', list1)
print('На карте осталось: ', ost_na_karte)
