# Представь, что мы пишем программу для банковских карточек.
# Человек может совершать покупки, пока у него на карте хватает на это денег.
# В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.

#Вариант 1 (с проверками на содержание только цифр во введенных суммах):
list1 = []
ost_na_karte = input('Введите сумму денег на карте (в рублях): ')
while not ost_na_karte.isdigit():
    ost_na_karte = input('Ошибка! Введите сумму денег на карте (в рублях): ')
rashod = input('Введите расходы (в рублях): ')
while not rashod.isdigit():
    rashod = input('Ошибка! Введите расходы (в рублях): ')
ost_na_karte = int(ost_na_karte)
rashod = int(rashod)
while rashod <= ost_na_karte:
    ost_na_karte -= rashod
    if rashod > 0:
        list1.append(rashod)
    if ost_na_karte == 0:
            break
    rashod = int(input('Введите расходы (в рублях): '))
if rashod > ost_na_karte:
    print('Операция по оплате не прошла. Не хватает денежных средств на карте')
if len(list1) == 0:
    print('Расходов не было')
else:
    print(f'Были произведены следующие расходы: {str(list1)[1:-1]} рублей')
print(f'На карте осталось: {ost_na_karte} рублей')



#Вариант 2 (без проверок на содержание только цифр во введенных суммах):
# ost_na_karte = int(input('Введите количество денег на карте (в рублях): '))
# list1 = []
# rashod = int(input('Введите расходы (в рублях): '))
# while rashod <= ost_na_karte:
#     ost_na_karte -= rashod
#     if rashod > 0:
#         list1.append(rashod)
#         if ost_na_karte == 0:
#             break
#     rashod = int(input('Введите расходы (в рублях): '))
# if rashod > ost_na_karte:
#     print('Операция по оплате не прошла. Не хватает денежных средств на карте')
# if len(list1) == 0:
#     print('Расходов не было')
# else:
#     print(f'Были произведены следующие расходы: {str(list1)[1:-1]} рублей')
# print(f'На карте осталось: {ost_na_karte} рублей\n')

