b1 = float(input())
b2 = float(input())
h = float(input())

# # This does not work in judge as an automated testing system
# b1 = float(input("Please insert the base 1 value here: "))
# b2 = float(input("Please insert the base 2 value here: "))
# h = float(input("Please insert the height value here: "))

trapezoid_area = (b1 + b2) * h / 2

print(f"{trapezoid_area :.2f}")
