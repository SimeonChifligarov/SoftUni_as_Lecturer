FUEL_PER_LITER_PRICE = 2.10
GUIDE_PRICE = 100

discounts = {
    "Saturday": 0.10,
    "Sunday": 0.20,
}

budget = float(input())
fuel_liters = float(input())
day = input()  # "Saturday" or "Sunday"

discount = discounts[day]

money_needed = (fuel_liters * FUEL_PER_LITER_PRICE + GUIDE_PRICE) * (1 - discount)

if budget >= money_needed:
    print(f"Safari time! Money left: {budget - money_needed :.2f} lv.")
else:
    print(f"Not enough money! Money needed: {money_needed - budget :.2f} lv.")
