prices = {
    "Espresso": {
        "Without": 0.90,
        "Normal": 1.00,
        "Extra": 1.20,
    },
    "Cappuccino": {
        "Without": 1.00,
        "Normal": 1.20,
        "Extra": 1.60,
    },
    "Tea": {
        "Without": 0.50,
        "Normal": 0.60,
        "Extra": 0.70,
    },
}

kind = input()  # "Espresso", "Cappuccino", or "Tea"
sugar = input()  # "Without", "Normal", or "Extra"
count = int(input())

price = prices[kind][sugar]

total_price = count * price

if sugar == "Without":
    total_price *= 0.65

if kind == "Espresso" and count >= 5:
    total_price *= 0.75

if total_price > 15.00:
    total_price *= 0.80

print(f"You bought {count} cups of {kind} for {total_price :.2f} lv.")
