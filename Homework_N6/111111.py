# 1. Создать множество
set11 = {1}
set1 = set([1, 2])
print(set1)

# 2. Создать неизменяемое множество

# print(frozenset([3, 4]))

# 3. Выполнить операцию объединения созданных
# множеств
print(set('fdgff')|frozenset([1, 2]))
# 4. Выполнить операцию пересечения созданных
# множеств
print(set([2, 3, 4, 'fgggfh2232']) & frozenset(['fgggfh2232', 2]))

# Напишите программу, которая проверит, есть ли в последовательности
# чисел списка дубликаты
list1 = [1, 2, 3, 4, 5, 2]
if len(list1) == len(set(list1)):
    print('Дубликатов нет')
else:
    print('Дубликаты есть')

# В саду сорвали цветы
#
# garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
#
# На лугу сорвали цветы
#
# meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
#
# Создайте множество цветов, произрастающих одновременно в саду и на лугу

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )
set1 = set(garden)&set(meadow)
print(set1)
