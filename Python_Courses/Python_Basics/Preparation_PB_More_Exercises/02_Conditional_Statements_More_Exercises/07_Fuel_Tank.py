FUEL_LITERS_BOUNDARY = 25

valid_fuel_types = ["Diesel", "Gasoline", "Gas"]

fuel_type = input()  # "Diesel", "Gasoline" or "Gas"
fuel_liters = float(input())

if fuel_type not in valid_fuel_types:
    print("Invalid fuel!")
else:
    if fuel_liters >= FUEL_LITERS_BOUNDARY:
        print(f"You have enough {fuel_type.lower()}.")
    else:
        print(f"Fill your tank with {fuel_type.lower()}!")
