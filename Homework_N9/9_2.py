# 2. Добавьте на свой рабочий стол папку, в ней создайте 3 текстовых
# файла: test_1.txt, test_2.txt, test_3.txt.
# Затем переименуйте файлы на: rename_1.txt, rename_2.txt, rename_3.txt
# После этого удалите созданную папку.
# Все операции выполнять с помощью встроенных функций библиотеки os.
import os
os.chdir('..')
os.chdir('..')
os.chdir('..')
os.chdir('Рабочий стол')
if not os.path.isdir('new'):
    os.mkdir('new')
os.chdir('new')
print(os.getcwd())
test_1 = open('test_1.txt', 'w')
test_1.close()
test_2 = open('test_2.txt', 'w')
test_2.close()
test_3 = open('test_3.txt', 'w')
test_3.close()
os.rename('test_1.txt', 'rename_1.txt')
os.rename('test_2.txt', 'rename_2.txt')
os.rename('test_3.txt', 'rename_3.txt')
os.chdir('..')
print(os.getcwd())
# Не помню, как удалить папку с файлами через os, поэтому нашла такой способ
import shutil
shutil.rmtree('new')
