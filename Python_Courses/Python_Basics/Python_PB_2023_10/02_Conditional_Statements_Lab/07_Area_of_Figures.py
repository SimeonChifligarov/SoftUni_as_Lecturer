import math

figure_type = input()

area = 0
if figure_type == "square":
    side = float(input())  # 5.0
    area = side * side
elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure_type == "circle":
    circle_radius = float(input())
    area = math.pi * circle_radius ** 2
elif figure_type == "triangle":
# else:
    side = float(input())
    height = float(input())
    area = side * height / 2

print(f"{area :.3f}")

# else:  # I am sure that all other cases are "triangle"
#     pass
