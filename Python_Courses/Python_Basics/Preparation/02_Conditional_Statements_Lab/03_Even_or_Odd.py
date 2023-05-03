EVEN_MESSAGE = "even"
ODD_MESSAGE = "odd"

number = int(input())

is_even = number % 2 == 0

print(EVEN_MESSAGE) if is_even else print(ODD_MESSAGE)
