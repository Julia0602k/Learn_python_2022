num1 = int(input('Write a first number: '))
simbol = input('Write a simbol: ')
num2 = int(input('Write a second number: '))

# if simbol == '+':
#     print(num1 + num2)
# elif simbol == '-':
#     print(num1 - num2)
# elif simbol == '*':
#     print(num1 * num2)
# elif simbol == '/' and num2 != 0:
#     print(num1 / num2)
# elif num2 == 0:
#     print('Делить на 0 нельзя')
# else:
#     print('123')

if simbol == '+' or simbol == '-' or simbol == '*' or simbol == '/':
    if simbol == '+':
        print(num1 + num2)
    elif simbol == '-':
        print(num1 - num2)
    elif simbol == '*':
        print(num1 * num2)
    elif num2 != 0:
        print(num1 / num2)
    else:
        print("Can't divide by zero!")
else:
    print('Write a correct simbol!')
