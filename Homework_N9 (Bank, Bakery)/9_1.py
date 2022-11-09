# 1. Ввести в файл 'input.txt' 2 числа в одну строку через пробел.
# Вывести в файл 'output.txt' их разность.
with open('input.txt', 'w') as f:
    f.write('8 9')
with open('input.txt') as f:
    str1 = f.readline()
    # print('Строка из файла: ', str1, '; Разность: ', answer1)
with open('output.txt', 'w') as f:
    f.write(str(int(str1[0]) - int(str1[-1])))
