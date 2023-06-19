budget = float(input())
season = input()  # "Summer" or "Winter"

car_class = ""
car_type = ""
car_price = 0
if budget <= 100:  # does not have check for negative budget
    car_class = "Economy class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.35 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.65 * budget
elif budget <= 500:
    car_class = "Compact class"
    if season == "Summer":
        car_type = "Cabrio"
        car_price = 0.45 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.80 * budget
else:  # elif budget > 500:  # this way we exclude budget < 0
    car_class = "Luxury class"
    if season == "Summer":
        car_type = "Jeep"
        car_price = 0.90 * budget
    elif season == "Winter":
        car_type = "Jeep"
        car_price = 0.90 * budget

print(car_class)
print(f"{car_type} - {car_price :.2f}")
