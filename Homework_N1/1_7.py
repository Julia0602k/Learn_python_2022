# 7. Напишите программу, которая проверяет, что для
# заданного четырехзначного числа выполняется
# следующее соотношение: сумма первой и последней цифр
# равна разности второй и третьей цифр.
#
# Программа должна вывести «ДА», если соотношение
# выполняется, и «НЕТ» — если не выполняется.

#Variant 1
# num4 = int(input('Введите четырехзначное число: '))
# # if len(num4) == 4:
# if num4 >= 1000 and num4 < 10000:
#     num4 = str(num4)
#     if (int(num4[0]) + int(num4[3])) == (int(num4[1]) - int(num4[2])):
#         print('ДА')
#     else:
#         print('НЕТ')
# else:
#     print('Ошибка! Введите четырехзначное число!')

#Variant 2
# num4 = int(input('Введите четырехзначное число: '))
# # if len(num4) == 4:
# if num4 >= 1000 and num4 < 10000 and (int(str(num4[0])) + int(str(num4[3]))) == (int(str(num4[1])) - int(str(num4[2]))):
#     print('ДА')
# elif num4 >= 1000 and num4 < 10000 and (int(str(num4[0])) + int(str(num4[3]))) != (int(str(num4[1])) - int(str(num4[2]))):
#     print('НЕТ')
# else:
#     print('Ошибка! Введите четырехзначное число!')

# #Variant 3 (не работает, тк нужна проверка на 4 число, а это доп if, а по заданию я должна сделать на 1 меньше
# num4 = input('Введите четырехзначное число: ')
# # if len(num4) == 4:
# answer1 = int(num4[0]) + int(num4[3])
# answer2 = int(num4[1]) - int(num4[2])
# if num4 >= 1000 and num4 < 10000 and answer1 == answer2:
#     print('ДА')
# elif num4 >= 1000 and num4 < 10000 and answer1 != answer2:
#     print('НЕТ')
# else:
#     print('Ошибка! Введите четырехзначное число!')

#Variant 4
num4 = input('Введите четырехзначное число: ')
if (int(num4[0]) + int(num4[3])) == (int(num4[1]) - int(num4[2])) and int(num4) >= 1000 and int(num4) < 10000:
    print('ДА')
elif (int(num4[0]) + int(num4[3])) != (int(num4[1]) - int(num4[2])) and int(num4) >= 1000 and int(num4) < 10000:
    print('НЕТ')
else:
    print('Ошибка! Введите четырехзначное число!')

