# 1. Напишите программу, которая принимает аргумент в виде списка
# и возвращает словарь, в котором каждый элемент списка является
# и ключом и значением. Предполагается, что элементы списка будут
# соответствовать правилам задания ключей в словарях.


#Превращает список в словарь
str1 = input("Введите список, например ['a', 'b', 1]: ")
print(str1)
list1 = ((str1.removeprefix('[')).removesuffix(']')).split(', ')
print(list1, type(list1))
for i in list1:
    if i in [' ', '[', ']', ',', ', ', '''"''']:
            # i == '[' or i == ',' or i == ' ' or i == ']' or i == "'":
        list1.remove(str(i))
dict1 = {a: a for a in list1}
print(dict1)


#Еще вариант
# list111 = list(input("Введите список, например ['a', 'b', 1]: "))
# print(list111)
# for i in list111:
#     if i in [' ', '[', ']', ',', ', ', "'", '''"''']:
#         list111.remove(str(i))
# dict1 = {a: a for a in list111}
# print(dict1)

# #Превращает строку в словарь (строка преобразуется в список, а потом в словарь)
# list11 = list(input('Введите список: '))
# print(list11)
# dict1 = {a: a for a in list11}
# print(dict1)
#
# #Вариант
# list2 = [1, 2.0, 'abc']
# dict2 = {a: a for a in list2}
# print(dict2)
