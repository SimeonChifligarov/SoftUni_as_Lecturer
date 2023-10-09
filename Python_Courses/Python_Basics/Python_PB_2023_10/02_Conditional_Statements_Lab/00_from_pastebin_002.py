import math

shape = input()
side1 = float(input())

if shape == "square" or shape == "circle":
    if shape == "square":
        area_for_square = side1 * side1
        print(f"{area_for_square:.3f}")
    elif shape == "circle":
        area_for_circle = math.pi * side1 * side1
        print(f"{area_for_circle:.3f}")
elif shape == "rectangle" or shape == "triangle":
    side2 = float(input())
    if shape == "rectangle":
        area_for_rectangle = side1 * side2
        print(f"{area_for_rectangle:.3f}")
    elif shape == "triangle":
        area_for_triangle = side1 * side2 / 2
        print(f"{area_for_triangle:.3f}")
