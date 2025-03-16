# : Събиране(+), Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%).

n1 = int(input())
n2 = int(input())
operator_string = input()  # "+", "-", "*", "/", or "%"

result = ''
if operator_string == '+':
    math_result = n1 + n2
    even_or_odd = ''
    if math_result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    result = f'{n1} {operator_string} {n2} = {math_result} - {even_or_odd}'
    # result = f'{n1} {operator_string} {n2} = {math_result} - {"even" if math_result % 2 == 0 else "odd"}'

elif operator_string == '-':
    math_result = n1 - n2
    even_or_odd = ''
    if math_result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    result = f'{n1} {operator_string} {n2} = {math_result} - {even_or_odd}'

elif operator_string == '*':
    math_result = n1 * n2
    even_or_odd = ''
    if math_result % 2 == 0:
        even_or_odd = 'even'
    else:
        even_or_odd = 'odd'

    result = f'{n1} {operator_string} {n2} = {math_result} - {even_or_odd}'

elif operator_string == '/':
    if n2 == 0:
        result = f'Cannot divide {n1} by zero'
    else:
        math_result = n1 / n2
        result = f'{n1} / {n2} = {math_result:.2f}'

elif operator_string == '%':
    if n2 == 0:
        result = f'Cannot divide {n1} by zero'
    else:
        math_result = n1 % n2
        result = f'{n1} % {n2} = {math_result}'

print(result)
