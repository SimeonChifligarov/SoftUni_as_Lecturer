import math

figure = input("Enter the type of figure please: ")  # "square", "rectangle", "circle", или "triangle"

if figure == "square":
    side_a = float(input('What is the side of the square?: '))
    area = side_a * side_a  # area = side_a ** 2
elif figure == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure == "circle":
    radius = float(input())
    area = math.pi * radius * radius  # math.pi * radius ** 2
elif figure == "triangle":
    side_a = float(input())
    h_a = float(input())
    area = side_a * h_a / 2
else:
    print('Not valid... Exiting the program')

print(f"{area :.3f}")
