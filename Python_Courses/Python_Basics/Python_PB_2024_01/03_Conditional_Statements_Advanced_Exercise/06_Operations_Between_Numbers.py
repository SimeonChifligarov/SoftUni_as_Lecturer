number_1 = int(input())
number_2 = int(input())
math_operator = input()  # "+", "-", "*", "/", "%"


if math_operator == '+':
    result = number_1 + number_2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

    print(f'{number_1} {math_operator} {number_2} = {result} - {odd_or_even}')
elif math_operator == '-':
    result = number_1 - number_2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

    print(f'{number_1} {math_operator} {number_2} = {result} - {odd_or_even}')
elif math_operator == '*':
    result = number_1 * number_2
    if result % 2 == 0:
        odd_or_even = 'even'
    else:
        odd_or_even = 'odd'

    print(f'{number_1} {math_operator} {number_2} = {result} - {odd_or_even}')
elif math_operator == '/':
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        result = number_1 / number_2
        print(f'{number_1} / {number_2} = {result :.2f}')
elif math_operator == '%':  # eq. else: if correct input
    if number_2 == 0:
        print(f'Cannot divide {number_1} by zero')
    else:
        result = number_1 % number_2
        print(f'{number_1} % {number_2} = {result}')
