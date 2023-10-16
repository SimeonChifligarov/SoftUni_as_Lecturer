num1 = int(input())
num2 = int(input())
math_operator = input()

if math_operator == "+":
    result = num1 + num2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{num1} + {num2} = {result} - {even_or_odd}")
elif math_operator == "-":
    result = num1 - num2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{num1} - {num2} = {result} - {even_or_odd}")
elif math_operator == "*":
    result = num1 * num2
    even_or_odd = ""
    if result % 2 == 0:
        even_or_odd = "even"  # True ; False
    else:
        even_or_odd = "odd"
    print(f"{num1} * {num2} = {result} - {even_or_odd}")
elif math_operator == "/":
    if num2 == 0:
        print(f" Cannot divide {num1} by zero")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {result :.2f}")
elif math_operator == "%":
    if num2 == 0:
        print(f" Cannot divide {num1} by zero")
    else:
        result = num1 % num2
        print(f"{num1} % {num2} = {result}")
