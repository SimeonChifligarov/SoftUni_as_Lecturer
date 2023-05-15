n1 = int(input())
n2 = int(input())
math_operator = input()

result = 0
even_or_odd = ""
if math_operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {result} - {even_or_odd}")
elif math_operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {result} - {even_or_odd}")
elif math_operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        even_or_odd = "even"
    else:
        even_or_odd = "odd"
    print(f"{n1} {math_operator} {n2} = {result} - {even_or_odd}")
elif math_operator == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result :.2f}")
elif math_operator == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
