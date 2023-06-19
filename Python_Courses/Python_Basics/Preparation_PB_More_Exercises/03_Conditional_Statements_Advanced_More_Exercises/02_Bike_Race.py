OPERATIONS_COST_AS_PERCENT = 5 / 100

prices = {
    "juniors": {
        "trail": 5.50,
        "cross-country": 8.00,
        "downhill": 12.25,
        "road": 20.00,
    },
    "seniors": {
        "trail": 7.00,
        "cross-country": 9.50,
        "downhill": 13.75,
        "road": 21.50,
    },
}

juniors = int(input())
seniors = int(input())
track = input()  # "trail", "cross-country", "downhill", or "road"

juniors_price = prices["juniors"][track]
seniors_price = prices["seniors"][track]

discount = 0
if track == "cross-country" and juniors + seniors >= 50:
    discount = 0.25

juniors_price *= 1 - discount
seniors_price *= 1 - discount

total_income = juniors * juniors_price + seniors * seniors_price
total_profit = total_income * (1 - OPERATIONS_COST_AS_PERCENT)

print(f"{total_profit :.2f}")
