# Файл содержит числа и буквы. Каждый записан в
# отдельной строке. Нужно считать содержимое в список
# так, чтобы сначала шли числа по возрастанию, а потом
# слова по возрастанию их длинны
f = open('text.txt', 'w')
f.write('8\n3\na\nb')
f.close()
list1 = []
with open('text.txt', 'r') as f:
    # print(f.readlines(), end='')
    for i in f.readlines():
        list1.append(i.strip("\n"))
print(list1)
list1.sort()
print(list1)

# list1 = []
# with open('text.txt', 'r') as f:
#     for i in f.readlines():
#         list1.append(i.strip("\n"))
# print(list1)
# list1.sort()
# print(list1)

# for i in f:
# if i[-2:] == str('\n'):
#         list1.append(i[:-2])
#     else:
#         list1.append(i)

    # str1 = ''.join(list1)
    # print('1', str1)
    # str1.split(',')