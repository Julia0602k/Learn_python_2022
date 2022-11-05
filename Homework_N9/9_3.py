# 3. В текстовом файле посчитать количество строк, а также для каждой
# отдельной строки определить количество в ней символов.
# Помним, что '\n' не должны учитываться как отдельные строки.
list1 = []
with open('text3.txt', 'w') as f:
    f.write('Декабрь\nЯнварь\nФевраль\nМарт\nАпрель\nМай')
with open('text3.txt', 'r') as f:
    # count = 0
    for i in f.readlines():
        list1.append(i.rstrip('\n'))
print(list1)
print('Количество строк в файле:', len(list1), '\nКоличество символов строк: ', end='')
for i in list1:
    print(i, ' - ', len(list1[list1.index(i)]), ', ', sep='',end='')
