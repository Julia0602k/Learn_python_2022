# Список из 7 цифр
# Если четных цифр в нем больше чем нечетных, то
# найти сумму всех его цифр, если нечетных больше,
# то найти произведение 1 3 и 6 элемента

list = [1, 2, 3, 4, 5, 6, 8]
list_chet = []
list_nechet = []
for elem in list:
    if elem % 2 == 0:
        list_chet.append(elem)
    elif elem % 2:
        list_nechet.append(elem)
print(list_chet)
print(list_nechet)
sum = 0
if len(list_chet) > len(list_nechet):
    for elem in list:
        sum += elem
elif len(list_chet) < len(list_nechet):
    sum = list[0] * list[2] * list[5]
print(sum)
