number1 = int(input('Input number 1 '))
number2 = int(input('Input number 2 '))
operator = input('Input operator ')
if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(number1 / number2)
elif operator == '//':
    print(number1 // number2)
elif operator == '%':
    print(number1 % number2)
elif operator == '**':
    print(number1 ** number2)
else:
    print('error wrong operator')
