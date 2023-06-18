fuels = {
    "Diesel": {"price": 2.33, "discount": 0.12},
    "Gasoline": {"price": 2.22, "discount": 0.18},
    "Gas": {"price": 0.93, "discount": 0.08},
}


fuel_type = input()  # "Gas", "Gasoline", or "Diesel"
fuel_amount = float(input())
discount_card = input()  # "Yes" or "No"

fuel_price = fuels[fuel_type]["price"]
fuel_discount = fuels[fuel_type]["discount"] if discount_card == "Yes" else 0

final_fuel_price = fuel_price - fuel_discount
total_price = final_fuel_price * fuel_amount

extra_discount = 0
if fuel_amount > 25:
    extra_discount = 10 / 100
elif fuel_amount >= 20:
    extra_discount = 8 / 100

final_total_price = total_price * (1 - extra_discount)

print(f"{final_total_price :.2f} lv.")
