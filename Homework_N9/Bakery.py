        # Клиент приходит в кондитерскую. Он хочет приобрести один или несколько видов продукции, а также узнать её состав.
        # Реализуйте кондитерскую.У вас есть словарь, где ключ – название продукции (торт, пирожное, маффин и т.д.).
        # Значение – список, который содержит состав, цену (за 100гр) и кол-во (в граммах).
# Предложите выбор:
# 1. Если человек хочет посмотреть описание: название – описание
# 2. Если человек хочет посмотреть цену: название – цена.
# 3. Если человек хочет посмотреть количество: название – количество.
# 4. Всю информацию.
# 5. Приступить к покупке:
# С клавиатуры вводите название торта и его кол-во. n – выход из программы. Посчитать
# цену выбранных товаров и сколько товаров осталось в изначальном списке
        # 6. До свидания
dict1 = {'торт': ['сахар, мука, молоко', 3.5, 2000],
         'пирожное': ['миндаль, мука, молоко', 4.6, 500],
         'маффин': ['изюм, мука, кефир', 5.7, 1750],
         'печенье': ['какао, мука, имбирь', 2.3, 1700]}
list1 = str(dict1.keys()).lstrip('dict_keys([').rstrip('])')
num1 = 0
v_korzine = {}
while num1 != 'n':
    num1 = input('''Если вы хотите:
    посмотреть описание товара, введите 1,
    посмотреть цену товара, введите 2,
    посмотреть количество товара в граммах, введите 3,
    посмотреть всю информацию о товаре, введите 4,
    приступить к покупке, введите 5,
    выйти, введите n
    Сделайте свой выбор: ''')
    if num1 == 'n':
        break
    elif num1 in ['1', '2', '3', '4', '5']:
        product = input(f"Введите название товара из списка {list1}: ")
        while product not in dict1.keys():
            product = input(f'Вы ошиблись! Введите название товара из списка {list1} или введите цифру 0 для выхода в главное меню: ')
            if product == '0':
                break
        for k, v in dict1.items():
            if k == product:
                if num1 == '1':
                    print(f'В состав товара "{k}" входит: {v[0]}', end='.\n')
                elif num1 == '2':
                    print(f'Цена товара "{k}": {v[1]} руб.', end='.\n')
                elif num1 == '3':
                    print(f'Количество товара "{k}" в граммах: {v[2]}', end='.\n')
                elif num1 == '4':
                    print(f'В состав товара "{k}" входит: {v[0]}', end='.\n')
                    print(f'Цена товара "{k}": {v[1]} руб.', end='.\n')
                    print(f'Количество товара "{k}" в граммах: {v[2]}', end='.\n')
                elif num1 == '5':
                    choise = 1
                    sum_total = 0
                    while choise == 1:
                        for k, v in dict1.items():
                            if k == product:
                                kol = int(input(f'Введите количество товара в граммах (в наличии {v[2]} грамм) или для возврата в главное меню введите 0: '))
                                if kol == '0':
                                    break
                                elif kol <= int(v[2]):
                                    sum1 = float(v[1]) * kol / 100
                                    sum_total += sum1
                                    print(f'В корзине товар "{k}", масса: {kol}, сумма за данное количество товара: {sum1}')
                                    print(f'В наличии товара "{k}", осталось: {int(v[2]) - kol}')
                                    v_korzine[k] = kol
                                    dict1[k] = [int(v[2]) - kol]
                                    print('У вас в корзине (товар: масса в граммах):', v_korzine)
                                elif kol > int(v[2]):
                                    print(f'Ошибка! В наличии есть только {v[2]} грамм(-ов)')
                                    break
                        choise = input('''Если вы
                хотите продолжить покупки введите цифру 1,
                хотите вернуться в главное меню введите цифру 0.
                Сделайте свой выбор: ''')
                        if choise == '1':
                            product = input(f'Введите новое название товара для покупки из списка {list1}: ')
                        else:
                            print(f'Ваши покупки: {v_korzine}\nСумма покупок составляет {sum_total}')
                            print(f'Количество оставшихся товаров: {dict1}')
    else:
        print('Ошибка! Сделайте свой выбор еще раз!')




print('До свидания!')




