# Представь, что мы пишем программу для банковских карточек.
# Человек может совершать покупки, пока у него на карте хватает на это денег.
# В начале программы вводим количество денег, а потом вводим расходы, пока они не превышают баланс на карте.
# Когда превысили, мы должны получить, сколько успели сделать покупок и сколько осталось денег на карте.
list1 = []
sum_card = input('Введите сумму денег на карте (в рублях): ')
while not sum_card.isdigit():
    sum_card = input('Ошибка! Введите сумму денег на карте (в рублях): ')
spend_money = input('Введите расходы (в рублях): ')
while not spend_money.isdigit():
    spend_money = input('Ошибка! Введите расходы (в рублях): ')
sum_card = int(sum_card)
spend_money = int(spend_money)
while spend_money <= sum_card:
    sum_card -= spend_money
    if spend_money > 0:
        list1.append(spend_money)
    if sum_card == 0:
            break
    spend_money = int(input('Введите расходы (в рублях): '))
if spend_money > sum_card:
    print('Операция по оплате не прошла. Не хватает денежных средств на карте')
if len(list1) == 0:
    print('Расходов не было')
else:
    print(f'Были произведены следующие расходы: {str(list1)[1:-1]} рублей')
print(f'На карте осталось: {sum_card} рублей')
