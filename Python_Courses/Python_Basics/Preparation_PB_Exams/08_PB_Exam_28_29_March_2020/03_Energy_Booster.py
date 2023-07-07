prices = {
    "Watermelon": {
        "small": 56.00,
        "big": 28.70,
    },
    "Mango": {
        "small": 36.66,
        "big": 19.60,
    },
    "Pineapple": {
        "small": 42.10,
        "big": 24.80,
    },
    "Raspberry": {
        "small": 20.00,
        "big": 15.20,
    },
}

packages = {
    "small": 2,
    "big": 5,
}

fruit = input()  # "Watermelon", "Mango", "Pineapple", or "Raspberry"
size = input()  # "small" or "big"
count = int(input())

price = prices[fruit][size] * packages[size]
total_price = price * count

if total_price > 1_000:
    total_price *= (1 - 0.50)
elif total_price >= 400:
    total_price *= (1 - 0.15)

print(f"{total_price :.2f} lv.")
