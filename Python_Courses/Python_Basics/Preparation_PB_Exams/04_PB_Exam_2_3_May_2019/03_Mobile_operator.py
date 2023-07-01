prices = {
    "Small": {
        "one": 9.98,
        "two": 8.58,
    },
    "Middle": {
        "one": 18.99,
        "two": 17.09,
    },
    "Large": {
        "one": 25.98,
        "two": 23.59,
    },
    "ExtraLarge": {
        "one": 35.99,
        "two": 31.79,
    },
}

contract_duration = input()  # "one" or "two"
contract_type = input()  # "Small",  "Middle", "Large", or "ExtraLarge"
extra_internet = input()  # "yes" or "no"
months = int(input())

price = prices[contract_type][contract_duration]

if extra_internet == "yes":
    if price <= 10:
        price += 5.50
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

if contract_duration == "two":
    price *= (1 - 0.0375)

total_price = price * months

print(f"{total_price :.2f} lv.")
