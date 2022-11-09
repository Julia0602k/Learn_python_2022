# Представь, что мы пишем программу для банковских карточек.
# Человек может совершать покупки, пока у него на карте хватает на это денег.
# В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.
dict1 = {}
count = 0
sum_card = input('Введите сумму денег на карте (в рублях): ')
while not sum_card.isdigit():
    sum_card = input('Ошибка! Введите сумму денег на карте (в рублях): ')
spend_money = input('Введите расходы (в рублях): ')
while not spend_money.isdigit():
    spend_money = input('Ошибка! Введите расходы (в рублях): ')
sum_card = int(sum_card)
spend_money = int(spend_money)
while spend_money <= sum_card:
    name_spend_money = input('Введите название покупки: ')
    sum_card -= spend_money
    count += 1
    if spend_money > 0:
        if dict1.get(name_spend_money) != None:
            dict1[name_spend_money] += spend_money
        else:
            dict1[name_spend_money] = spend_money
    if sum_card == 0:
        break
    spend_money = input('Введите расходы (в рублях): ')
    while not spend_money.isdigit():
        spend_money = input('Ошибка! Введите расходы (в рублях): ')
    spend_money = int(spend_money)
if spend_money > sum_card:
    print('Операция по оплате не прошла. Не хватает денежных средств на карте')
if len(dict1) == 0:
    print('Расходов не было')
else:
    print(f'Были сделано {count} покупки(-ок)')
    print('Были произведены следующие расходы:')
    for k, v in dict1.items():
        print(f'{k} - {v} рублей')
print(f'На карте осталось: {sum_card} рублей')
