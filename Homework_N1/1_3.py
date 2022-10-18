# Преобразовать строку "Hello" в байтовую.
# Преобразовать байтовую строку b'\xd1\x84' в обычную.

str1 = 'Hello'
str2 = b'\xd1\x84'
print(str1.encode())
print(str2.decode())
