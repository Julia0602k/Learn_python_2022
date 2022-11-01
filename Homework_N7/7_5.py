# 5. Напишите программу, которая будет генирировать словарь
# в котором ключами будут числа от 1 до 5,
# а значениями будут элементы списка:

list5 = ['orange', 'apple', 'mango', 'banana', 'fruits']
dict5 = {(a + 1): list5[a] for a in range(5)}
print(dict5)

#Вариант2:
dict55 = {a: list5[a - 1] for a in range(1, 6)}
print(dict55)
