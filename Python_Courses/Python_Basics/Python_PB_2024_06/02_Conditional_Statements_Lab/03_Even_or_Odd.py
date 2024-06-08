# Ако е четно отпечатайте "even", ако е нечетно "odd".

number = int(input())  # int('4') == 4

if number % 2 == 0:  # number is even  # 4 % 2 == 0
    print('even')
else:
    print('odd')
